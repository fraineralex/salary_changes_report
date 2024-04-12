<div align="center">
  <h1>Salary Changes Report</h1>
  <h3>Odoo module that allows you to export a report of salary changes for employees to Excel.</h3>
</div>

<p align="center">
  <a href="https://github.com/fraineralex/salary_changes_report/fork" target="_blank">
    <img src="https://img.shields.io/github/forks/fraineralex/salary_changes_report?" alt="Badge showing the total of project forks"/>
  </a>

  <a href="https://github.com/fraineralex/salary_changes_report/stargazers" target="_blank">
    <img src="https://img.shields.io/github/stars/fraineralex/salary_changes_report?" alt="Badge showing the total of project stars"/>
  </a>

  <a href="https://github.com/fraineralex/salary_changes_report/commits/main" target="_blank">
    <img src="https://img.shields.io/github/commit-activity/m/fraineralex/salary_changes_report?" alt="Badge showing average commit frequency per month"/>
  </a>

  <a href="https://github.com/fraineralex/salary_changes_report/commits/main" target="_blank">
    <img src="https://img.shields.io/github/last-commit/fraineralex/salary_changes_report?" alt="Badge showing when the last commit was made"/>
  </a>

  <a href="https://github.com/fraineralex/salary_changes_report/issues" target="_blank">
    <img src="https://img.shields.io/github/issues/fraineralex/salary_changes_report?" alt="Badge showing the total of project issues"/>
  </a>

  <a href="https://github.com/fraineralex/salary_changes_report/pulls" target="_blank">
    <img src="https://img.shields.io/github/issues-pr/fraineralex/salary_changes_report?" alt="Badge showing the total of project pull-requests"/>
  </a>
</p>


<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0;
  <a href="#hammer_and_wrench-main-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#rocket-key-features">Key Features</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#handshake-contributions">Contributions</a>
</p>

## :dart: About ##

Salary Changes Report is an Odoo module that efficiently exports organized Excel reports of employee salary changes. This module seamlessly accesses and filters salary changes recorded in the `hr.contract` model via the `mail.tracking.value` model, streamlining resource management and ensuring compliance.

<img src="/static/description/wizard.png" alt="Screenshot of the modal wizard">

## :hammer_and_wrench: Main Technologies ##

<a href="https://python.org">
  <img width="50" title="Python" alt="Python Logo" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">
</a> &#xa0; &#xa0;

<a href="https://odoo.com">
  <img width="100" title="Odoo" alt="Odoo Logo" src="https://github.com/odoo/odoo/blob/17.0/addons/web/static/img/logo.png">
</a> &#xa0; &#xa0;

<a href="https://pypi.org/project/xlwt/">
  <img width="50" title="xlwt" alt="xlwt Logo" src="\static\description\xlwt.png">
</a> &#xa0; &#xa0;

<a href="https://odoo.com">
  <img width="50" title="hr.payroll" alt="hr.payroll Logo" src="\static\description\icon.png">
</a> &#xa0; &#xa0;

###

<details>
  <summary>See more</summary>

  ###

* Python
    - odoo
    - xlwt
    - xml
    - base64
    - io

</details>

## :rocket: Key Feautures

- **Efficient Reporting**: Easily generate organized Excel reports showcasing employee salary changes.
- **Integration**: Seamlessly accesses and filters salary changes recorded in the `hr.contract` model via the `mail.tracking.value` model.
- **Detailed Information**: Provides comprehensive details including contract name, employee name, identification number, current salary, previous salary, and effective date of the change.
- **User-Friendly**: Simplifies the process of tracking and managing salary adjustments for improved resource management.
- **Compliance Optimization**: Ensures compliance with regulatory requirements by efficiently documenting salary changes.

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com), [Python](https://python.org) and ([Odoo](https://odoo.com)) v14 or higher installed.

## :checkered_flag: Starting ##

```bash
# Clone this project
    $ git clone https://github.com/fraineralex/salary_changes_report
# Access
    $ cd salary_changes_report
# Install dependencies
    $ pip install xlwt
# Run the project
# The server will execute and you will see the modal wizard in hr payroll module -> reporting -> Reporte de Cambios Salariales
```

## :handshake: Contributions

Thank you for exploring my website! If you find the structure or features useful, feel free to use the template for your project. Contributions are welcome! if you have ideas, corrections, or improvements, open an issue or send a pull request. Your collaboration is valued and appreciated! 🚀


&#xa0;

