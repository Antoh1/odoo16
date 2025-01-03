# -*- coding: utf-8 -*-
# Part of Ropetech. See LICENSE file for full copyright and licensing details.

from datetime import date,datetime
from odoo import api, fields, models, _


class MedicalPatientDisease(models.Model):
    _name = "medical.patient.disease"
    _description = 'Medical Patient Disease'
    _rec_name = 'patient_id'
    _order = 'diagnosis_date desc'

    pathology_id = fields.Many2one('medical.pathology', 'Disease', required=True)
    disease_severity = fields.Selection([('1_mi','Mild'),
                               ('2_mo','Moderate'),
                               ('3_sv','Severe')],'Severity')
    status = fields.Selection([('c','Chronic'),
                               ('s','Status quo'),
                               ('h','Healed'),
                               ('i','Improving'),
                               ('w','Worsening')],'Status of the disease')
    is_infectious = fields.Boolean('Infectious Disease')
    is_active = fields.Boolean('Active disease')
    short_comment = fields.Char('Remarks')
    diagnosis_date = fields.Date('Date of Diagnosis')
    healed_date = fields.Date('Healed')
    age = fields.Integer('Age when diagnosed')
    doctor_id = fields.Many2one('hr.employee', 'Physician', required=True, domain="[('is_doctor','=','doctor')]")
    is_allergic = fields.Boolean('Allergic Disease')
    allergy_type = fields.Selection([('da','Drag Allergy'),
                               ('fa','Food Allergy'),
                               ('ma','Misc Allergy'),
                               ('mc','Misc Contraindication')], 'Allergy type')
    pregnancy_warning = fields.Boolean('Pregnancy warning')
    week_of_pregnancy = fields.Integer('Contracted in pregnancy week #')
    is_on_treatment = fields.Boolean('Currently on Treatment')
    treatment_description = fields.Char('Treatment Description')
    date_start_treatment = fields.Date('Start of treatment')
    date_stop_treatment = fields.Date('End of treatment')
    patient_id = fields.Many2one('res.partner', 'Patient', domain="[('patient_seq', '!=', 'New')]", required=True)
    appointment_id = fields.Many2one('medical.appointment', string="Appointment", domain="[('patient_id', '=', patient_id)]")
    extra_info = fields.Text('info')
    currency_id = fields.Many2one('res.currency', 'Currency',
                                  default=lambda self: self.env.user.company_id
                                  .currency_id.id,
                                  required=True)
    treatment_charge = fields.Monetary('Treatment Charges', help="Charge on the treatment")

