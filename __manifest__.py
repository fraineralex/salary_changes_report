{
    'name': 'Salary Changes Report',
    'version': '1.0.0',
    'category': 'Human Resources',
    'summary': 'Odoo module that allows you to export a report of salary changes for employees to Excel.',
    'description': 'Odoo module that allows you to export a report of salary changes for employees to Excel.',
    'depends': ['hr_payroll'],
    'author': 'Frainer Encarnación',
    'website': 'https://fraineralex.dev',
    'data': [
        'wizard/salary_changes_report_wizard_view.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3'
}
