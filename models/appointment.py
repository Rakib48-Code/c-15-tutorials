from odoo import api, fields, models,_


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Appointment Record'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'patient_id'

    sl_app = fields.Char(string='Appointment ID', required=True, copy=False, readonly=True,
                        index=True, default=lambda self: _('New'))
    patient_id = fields.Many2one('hospital.patient', string='Patient')
    appointment_date = fields.Date(string='Appointment Date',  default=fields.Date.context_today)
    booking_date = fields.Date(string='Booking Time')
    age = fields.Integer(string='Age')
    note = fields.Text(string='Description')
    ref = fields.Char(string='Reference', related='patient_id.ref')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string='Gender')

    @api.model
    def create(self, vals):
        if vals.get('sl_app', _('New')) == _('New'):
            vals['sl_app'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or _('New')
        res = super(HospitalAppointment, self).create(vals)
        return res


    @api.onchange('patient_id')
    def set_gender(self):
        for rec in self:
            rec.gender = rec.patient_id.gender
            rec.age = rec.patient_id.age