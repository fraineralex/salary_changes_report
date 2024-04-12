from odoo import _, fields, models
from odoo.exceptions import UserError
import xlwt
import base64
import io

TITLE = 'Reporte de Cambios Salariales'

class SalaryChangesReportWizard(models.TransientModel):
    _name = 'salary.changes.report.wizard'
    _description = 'Reporte de Cambios Salariales'

    company_id = fields.Many2one('res.company',
                                 'Compañía',
                                 default=lambda self: self.env.company.id,
                                 required=True, readonly=True)

    structure_ids = fields.Many2many('hr.payroll.structure',
                                     string="Estructura Salarial", domain="[('x_company_id', '=?', company_id)]")

    date_from = fields.Date(string="Fecha desde")

    date_to = fields.Date(string="Fecha hasta")

    def generate_report(self):
        self.validate_date()

        employee_ids = self.env['hr.employee'].search([
            ('company_id', '=?', self.company_id.id),
            ('contract_id', '!=', False),
            ('contract_id.state', '=', 'open'),
            ('contract_id.wage', '>', '0'),
            ('contract_id.structure_type_id.default_struct_id',
             'in', self.structure_ids.ids)
        ])

        title = f'{TITLE} - {self.company_id.name}'

        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet(title)
        column_width = 256 * 30
        xlwt.add_palette_colour("silver", 0x21)
        workbook.set_colour_RGB(0x21, 211, 221, 227)
        header_style = xlwt.easyxf(
            'font: bold on, height 200; align: horiz center; pattern: pattern solid, fore_colour silver;')

        headers = ['Contrato', 'Empleado', 'Cédula',
                   'Salario Actual', 'Salario Anterior', 'Fecha Efectivo']

        for col_num, header in enumerate(headers):
            worksheet.write(0, col_num, header, header_style)
            worksheet.col(col_num).width = column_width

        row_num = 1

        for employee in sorted(employee_ids, key=lambda employee: employee.contract_id.name):
            historic_salary_ids = self.env['mail.tracking.value'].search([
                ('field_desc', 'in', ['Salario', 'Wage']),
                ('field_type', '=', 'monetary'),
                ('old_value_monetary', '!=', False),
                ('new_value_monetary', '!=', False),
                ('field', 'in', [7527, 6955]),
                ('mail_message_id.model', '=', 'hr.contract'),
                ('mail_message_id.res_id', 'in', employee.contract_ids.ids),
                ('create_date', '>=', self.date_from),
                ('create_date', '<=', self.date_to),
            ], order='create_date desc')

            for line in historic_salary_ids:
                if line.mail_message_id.res_id not in employee.contract_ids.ids:
                    continue

                worksheet.write(row_num, 0, employee.contract_id.name or '')
                worksheet.write(row_num, 1, employee.name or '')
                worksheet.write(
                    row_num, 2, employee.identification_id or '')
                formatted_wage = "{:,.2f}".format(line.new_value_monetary)
                worksheet.write(
                    row_num, 3, formatted_wage or '0.00')
                formatted_wage = "{:,.2f}".format(line.old_value_monetary)
                worksheet.write(
                    row_num, 4, formatted_wage or '0.00')
                worksheet.write(
                    row_num, 5, line.create_date.strftime('%d/%m/%Y') or '')

                row_num += 1

        workbook_data = io.BytesIO()
        workbook.save(workbook_data)
        workbook_data.seek(0)
        report_file = base64.b64encode(workbook_data.getvalue())
        filename = f'{title}.xls'
        attachement = self.env['ir.attachment'].create({
            'name': filename,
            'datas': report_file,
            'mimetype': 'application/vnd.ms-excel',
            'res_model': self._name,
            'res_id': self.id
        })

        return {
            'name': filename,
            'type': 'ir.actions.act_url',
            'url': f'/web/content/{attachement.id}?download=true',
            'target': 'self'
        }

    def validate_date(self):
        if not self.date_from:
            self.date_from = self.env.company.create_date.replace(
                month=1, day=1)

        if not self.date_to:
            today = fields.Date.today()
            self.date_to = today.replace(day=1, month=today.month + 1)

        if self.date_from > self.date_to:
            raise UserError(
                _('El campo "Fecha desde" debe ser menor o igual al campo "Fecha hasta"'))
