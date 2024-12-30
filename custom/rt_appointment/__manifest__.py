# -*- coding: utf-8 -*-
{
    'name': "rt_appointment",

    'summary': """
        Hospital Appointment Management System""",

    'description': """
        Appointment
    """,

    'author': "Ropetech Solutions",
    'website': "https://www.ropetech.co.ke",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website_sale', 'rt_hospital_ms'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'reports/patient_card.xml',
        'reports/card_template.xml',
        'reports/patient_card_back.xml',
        'data/appointment_seq.xml',
        'data/mail_template.xml',
        'data/appointment_cancel_template.xml',
        'data/doctor_seq.xml',
        'views/doctor_appointment_views.xml',
        'views/doctor_slot_views.xml',
        'views/rt_appointment_views.xml',
        'views/hr_employee_views.xml',
        'views/patient_form_views.xml',
        'views/snippets_views.xml',
        'views/thanks_views.xml',
        'views/website_menu_views.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'rt_appointment/static/src/js/appointment.js',
        ]},
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
