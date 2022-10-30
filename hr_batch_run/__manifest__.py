# -*- coding: utf-8 -*-
{
    'name': "HR Payroll close Batch with loans & mail chatter  &  Accounting all in One Journal Entery ",

    'summary': """
        payroll batch & loans with one Draft journal entery accounting .  """,

    'description': """
        auto compute slips in batch and loans and close batch and create one  Draft journal entery in accounting .
    * add mail chatter to batch .
    * must be sure that you select partner in field(Address) in employee form (Private Information Tab) .
    * you can download hr_payroll_community & hr_payroll_account_community from here
    https://apps.odoo.com/apps/modules/13.0/hr_payroll_account_community/
    * to contact us info@nilco-tech.com  
    * you can download ohrms_loan & ohrms_loan_accounting from here
    * sure you add loan rule in contracts structure .
    * this module run without set invoicing access to payroll user manager .
    * if you want loan deduction account in journal entery to be valid remove (-) sign from loan rule in python code field
     debit account --> salary expense account , credit account --> loan account . 
    https://apps.odoo.com/apps/modules/13.0/ohrms_loan_accounting/
    """,

    'author': "Yusra Mohamed",
    'website': "http://www.nilco-tech.com",

    
    'category': 'Generic Modules/Human Resources',
    'version': '13.0.1',

    # any module necessary for this one to work correctly
    'depends': ['mail','ohrms_loan','hr_payroll_community','hr_payroll_account_community'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
      
    ],
    'currency': 'USD',
    'price': 107,
    
}
