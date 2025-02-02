from odoo import api, fields, models


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor Record'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name')
    image = fields.Binary(string='Image')
    dob = fields.Date(string='Date of Birth')
    age = fields.Integer(string='Age', compute='_age_compute')
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female'),
    ], string='Gender')
    experience = fields.Integer(string='Experience')