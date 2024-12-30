# -*- coding: utf-8 -*-

from odoo import fields, models, api


class HospitalService (models.Model):
    _name = 'hospital.services'

    service_work = fields.Many2one('product.product', string='Hospital Service', domain=[('type', '=', 'service')])
    time_spent = fields.Float(string='Estimated Time')
    work_date = fields.Datetime(string='Date')  # Date of work planned:planned date
    responsible = fields.Many2one('res.users', string='Responsible')
    appointment_id = fields.Many2one('medical.appointment', string="Appointment id")
    work_cost = fields.Float(string="Service Cost")
    completed = fields.Boolean(string="Completed")
    duration = fields.Float(string='Duration')
    work_date2 = fields.Datetime(string='Date')  # Date of work completed/done:completed date

    @api.onchange('service_work')
    def get_price(self):
        self.work_cost = self.service_work.lst_price


class MedicineUsed (models.Model):
    _name = 'medicine.used'

    medicine = fields.Many2one('product.product', string='Medicine', domain=[('type', '=', 'service')])
    amount = fields.Integer(string='Quantity')
    price = fields.Float(string='Unit Price')
    appointment_id = fields.Many2one('medical.appointment', string="Appointment id")
    _defaults = {
                    'amount': 1, }

    @api.onchange('medicine')
    def get_price(self):
        self.price = self.medicine.lst_price


class DentalService(models.Model):
    _name = 'dental.service'
    _description = 'Main Dental Services'

    name = fields.Char(string='Dental Service', required=True)
    description = fields.Text(string='Description')


class DentalSubService(models.Model):
    _name = 'dental.sub.service'
    _description = 'Dental Service'

    name = fields.Char(string='Service', required=True)
    service_category = fields.Many2one('dental.service')
    description = fields.Text(string='Description')
    amount = fields.Integer(string='Quantity', default=1)
    price = fields.Float(string='Charges')


class UltraSoundCategory(models.Model):
    _name = 'ultrasound.category'
    _description = 'Ultra Sound Categories'

    name = fields.Char(string='Category Name', required=True)
    description = fields.Text(string='Description')


class UltraSoundService(models.Model):
    _name = 'ultrasound.service'
    _description = 'Ultra Sound Services'

    name = fields.Char(string='Ultra Sound Service', required=True)
    service_category = fields.Many2one('ultrasound.category')
    description = fields.Text(string='Description')
    amount = fields.Integer(string='Quantity', default=1)
    price = fields.Float(string='Charges')
