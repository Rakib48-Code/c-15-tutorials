from odoo import api, fields, models

class CreateAppointmentWizard(models.TransientModel):
    _name = 'create.appointment.wiz'
    _description = 'Create Appointment Wizard'

    patient_name = fields.Many2one('hospital.patient',string='Name')
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string='Gender')
    appointment_date = fields.Date(string='Appointment Date')
    booking_date = fields.Date(string='Booking Time')


    # store wizard data
    def action_create(self):
        vals = {
            'patient_id' : self.patient_name.id,
            # 'age' : self.age,
            'appointment_date' : self.appointment_date,
            'booking_date' : self.booking_date,
            'gender' : self.gender,
        }
        self.env['hospital.appointment'].create(vals)