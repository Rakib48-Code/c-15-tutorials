from odoo import api, models, fields, _
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Record'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    image = fields.Binary(string='Image')
    name = fields.Char(string='Name', tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string='Gender')
    contact = fields.Char(string='Contact', tracking=True)
    note = fields.Text(string='Description')
    age_group = fields.Selection([
        ('major', 'Major'),
        ('minor', 'Minor'),
    ], string='Age Group', compute='_set_age_group')
    user_id = fields.Many2one('res.users', string='User')
    email_id = fields.Char(string='Email')
    appointment_count = fields.Integer(string='Appointment', compute='get_appointment_count')

    # sequence number
    sl_no = fields.Char(string='Patient ID', required=True, copy=False, readonly=True,
                        index=True, default=lambda self: _('New'))
    ref = fields.Char(string='Reference', required=True, copy=False, readonly=True,
                      index=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('sl_no', _('New')) == _('New'):
            vals['sl_no'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
        if vals.get('ref', _('New')) == _('New'):
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient.ref') or _('New')
        res = super(HospitalPatient, self).create(vals)
        return res

    @api.depends('age')
    def _set_age_group(self):
        for rec in self:
            if rec.age < 18:
                rec.age_group = 'minor'
            else:
                rec.age_group = 'major'

    @api.constrains('age')
    def check_age(self):
        for rec in self:
            if rec.age == 0:
                raise ValidationError(_('Give must be age value!'))

    def get_appointment_count(self):
        count = self.env['hospital.appointment'].search_count([('patient_id', '=', self.id)])
        self.appointment_count = count

    # smart button action
    def open_patient_appointment(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Appointments',
            'res_model': 'hospital.appointment',
            'domain': [('patient_id', '=', self.id)],
            'context': {'default_patient_id': self.id},
            'view_mode': 'tree,form',
            'target': 'current',
        }

        # send email with button action

    def action_send_email(self):
        print('Send Email')
        template_id = self.env.ref('om_hospital.patient_card_email_template').id
        self.env['mail.template'].browse(template_id).send_mail(self.id, force_send=True)
