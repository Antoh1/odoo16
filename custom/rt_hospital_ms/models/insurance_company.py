# -*- coding: utf-8 -*-
# Part of Ropetech. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _


class InsuranceCompany(models.Model):
    _name = 'insurance.company'
    _description = 'Insurance Company'

    name = fields.Char('Insurance Company Name', required=True)
    contact = fields.Char('Contact Number')
    location = fields.Char('Address')
    note = fields.Text('Other Details')
    # medical_insurance_partner_id = fields.Many2one('res.partner','Owner')

