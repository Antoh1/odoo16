# -*- coding: utf-8 -*-
#############################################################################
#
#    Ropetech Solutions.
#
#    Copyright (C) 2024 Ropetech Solutions(<https://www.ropetech.co.ke>)
#    Author: Ropetech Solutions(<https://www.ropetech.co.ke>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
from odoo import models, fields


class Vaccine(models.Model):
    _name = 'hospital.vaccine'
    _description = 'Vaccine'
    _rec_name = 'vaccine'

    vaccine = fields.Char('Vaccine', required=True, help="A vaccine is a biological preparation that provides active "
                                                         "acquired immunity to a particular infectious disease")
    brand = fields.Char('Brand')
    currency_id = fields.Many2one('res.currency', 'Currency',
                                  default=lambda self: self.env.user.company_id
                                  .currency_id.id,
                                  required=True)
    price = fields.Monetary(string='Price')


class Medicine(models.Model):
    _name = 'hospital.medicine'
    _description = 'Vaccine'
    _rec_name = 'medicine'

    medicine = fields.Char('Medicine', required=True)
    brand = fields.Char('Brand')
    currency_id = fields.Many2one('res.currency', 'Currency',
                                  default=lambda self: self.env.user.company_id
                                  .currency_id.id,
                                  required=True)
    price = fields.Monetary(string='Price')


class Vaccination(models.Model):
    _name = 'hospital.vaccination'
    _description = 'Vaccination'
    _rec_name = 'vaccine_id'

    patient_id = fields.Many2one('res.partner', 'Patient', required=True)
    appointment_id = fields.Many2one('medical.appointment', string="Appointment",
                                     domain="[('patient_id', '=', patient_id)]")
    vaccine_id = fields.Many2one('hospital.vaccine', 'Vaccine', required=True)
    dose = fields.Integer('Dose')
    vaccine_date = fields.Datetime(string="Date")
    pharmacist_id = fields.Many2one('hr.employee', string="Pharmacist's Name",
                                    domain=[('is_doctor', '=', 'pharmacist')])
    notes = fields.Text('notes')
    currency_id = fields.Many2one('res.currency', 'Currency',
                                  default=lambda self: self.env.user.company_id
                                  .currency_id.id,
                                  required=True)
    vaccination_charge = fields.Monetary('Vaccination Charges', help="Charge on the vaccination")




