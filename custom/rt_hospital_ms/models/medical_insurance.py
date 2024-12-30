# -*- coding: utf-8 -*-
# Part of Ropetech. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_insurance(models.Model):
    _name = 'medical.insurance'
    _description = 'medical insurance'

    number = fields.Char('Number', required=True)
    # medical_insurance_partner_id = fields.Many2one('res.partner','Owner')
    patient_id = fields.Many2one('res.partner', 'Patient')
    type = fields.Selection([('state', 'State'), ('private', 'Private'),
                             ('company_insurance', 'Company Insured')], 'Insurance Type')
    insurance_company_id = fields.Many2one('insurance.company', string='Insurance Company')
    category = fields.Char('Category')
    notes = fields.Text('Extra Info')
    member_since = fields.Date('Member Since')
    member_exp = fields.Date('Expiration Date')
    medical_insurance_plan_id = fields.Many2one('medical.insurance.plan', 'Plan')

