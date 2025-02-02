{
    'name' : 'Hospital Management System',
    'version' : '15.0.1.1.2',
    'sequence' : 5,
    'category' : 'Tutorials',
    'summary' : 'odoo15 development tutorials',
    'author' : 'Rakib Hasan',
    'depends' : ['mail'],
    'data' : [

        # security
        'security/ir.model.access.csv',

        # data
        'data/patient_sequence.xml',
        'data/patient_reference.xml',
        'data/appointment_sequence.xml',
        # 'data/mail_template.xml',

        # wizards
        'wizards/create_appointment_view.xml',

        # views
        'views/menu.xml',
        'views/patient_view.xml',
        'views/appointment_view.xml',
        'views/doctor_view.xml',
        'views/female_patient.xml',

    ],
    'installable' : True,
    'application' : True
}