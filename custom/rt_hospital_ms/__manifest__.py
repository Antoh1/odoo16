# -*- coding: utf-8 -*-
{
    'name': "rt_hospital_ms",

    'summary': """
        Hospital and Medical Management Information System""",

    'description': """
        Hospital Management System
    """,

    'author': "Ropetech Solutions",
    'website': "https://www.ropetech.co.ke",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'account', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/patient_prescription_sequence.xml',
        'data/patient_seq.xml',
        'data/diagnosis_seq.xml',
        'data/building_seq.xml',
        'data/test_seq.xml',
        'data/lab_sequence.xml',
        'data/ir_sequence_data.xml',
        'data/dental_data.xml',
        'data/ultrasound_data.xml',
        'views/bed.xml',
        'views/wards.xml',
        'views/staff.xml',
        'views/room.xml',
        'views/payment.xml',
        # 'wizard/create_prescription_invoice_wizard.xml',
        # 'wizard/create_prescription_shipment_wizard.xml',
        'wizard/medical_appointments_invoice_wizard.xml',
        # 'wizard/medical_lab_test_create_wizard.xml',
        # 'wizard/medical_lab_test_invoice_wizard.xml',
        'views/patient_view.xml',
        'views/medical_service.xml',
        'views/ultra_sound_view.xml',
        'views/medical_insurance.xml',
        'views/medical_appointment.xml',
        'views/medical_pathology.xml',
        'views/medical_pathology_group.xml',
        'views/insurance_company.xml',
        'views/prescription.xml',
        'views/medical_patient_treatment.xml',
        'views/blood.xml',
        'views/doctor.xml',
        'views/facilities.xml',
        'views/building.xml',
        'views/degree.xml',
        'views/hospital.xml',
        'views/lab.xml',
        'views/vaccine.xml',
        'views/pharmacy.xml',
        'views/vaccination.xml',
        'views/inpatient.xml',
        'views/diagnosis.xml',
        'views/medicine.xml',
        'views/lab_test.xml',
        'views/lab_test_type.xml',
        'views/hospital_labs.xml',
        'wizard/room_assign.xml',
        'report/patient_prescription_report.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
