# -*- coding: utf-8 -*-
# Part of Ropetech. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
# from datetime import datetime, date
from datetime import datetime, timedelta, date
from odoo.exceptions import UserError

class medical_appointment(models.Model):
    _name = "medical.appointment"
    _description = "Medical Appointment"
    _inherit = 'mail.thread'
    _order = 'appointment_date desc'

    @api.model
    def create(self, vals):
        if vals.get('name', _('APT')) == _('APT'):
            vals['name'] = self.env['ir.sequence'].next_by_code('medical.appointment') or _('APT')
            msg_body = 'Appointment created'
            for msg in self:
                msg.message_post(body=msg_body)
        result = super(medical_appointment, self).create(vals)
        return result

    name = fields.Char(string="Appointment ID", readonly=True , copy=True)
    is_invoiced = fields.Boolean(copy=False, default=False)
    # institution_partner_id = fields.Many2one('res.partner', domain=[('is_company', '=', True)], string="Health Center")
    inpatient_registration_id = fields.Many2one('hospital.inpatient', string="Inpatient Registration")
    patient_status = fields.Selection([
        ('ambulatory', 'Ambulatory'),
        ('outpatient', 'Outpatient'),
        ('inpatient', 'Inpatient'),
    ], 'Patient status', sort=False, default='outpatient')
    patient_id = fields.Many2one('res.partner', 'Patient', domain="[('patient_seq', '!=', 'New')]", required=True)
    # patient_id = fields.Many2one('res.partner', 'Patient', required=True)
    urgency_level = fields.Selection([
        ('a', 'Normal'),
        ('b', 'Urgent'),
        ('c', 'Medical Emergency'),
    ], 'Urgency Level', sort=False, default="b")
    appointment_date = fields.Datetime('Appointment Date', required=True, default=fields.Datetime.now)
    appointment_end = fields.Datetime('Appointment End', required=True)
    doctor_id = fields.Many2one('hr.employee', 'Physician', required=True, domain="[('is_doctor','=','doctor')]")
    no_invoice = fields.Boolean(string='Invoice exempt', default=True)
    validity_status = fields.Selection([('invoice', 'Invoice'), ('tobe', 'To be Invoiced')],
                                       'Status', sort=False, readonly=True, default='tobe')
    invoice_status = fields.Selection([('invoice', 'Invoiced'), ('tobe', 'To be Invoiced')],
                                        'Status', sort=False, readonly=True, default='tobe')
    appointment_validity_date = fields.Datetime('Validity Date')
    consultations_id = fields.Many2one('product.product', 'Consultation Service', domain="[('type','=','service')]")
    consultation_fee = fields.Float(related='consultations_id.lst_price')
    consult_qty = fields.Integer(string="Quantity", default=1)
    comments = fields.Text(string="Info")
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirm'),
                              ('cancel', 'Cancel'), ('done', 'Done')], string="State", default='draft')
    app_state = fields.Selection([('draft', 'Draft'), ('approved', 'Waiting'),
                                  ('progress', 'In Progress'), ('suspend', 'Pending'), ('done', 'Completed')],
                                 string='Status', default='draft')
    invoice_to_insurer = fields.Boolean('Invoice to Insurance')
    # medical_patient_psc_ids = fields.Many2many('medical.patient.psc',string='Pediatrics Symptoms Checklist')
    # medical_prescription_order_ids = fields.One2many('medical.prescription.order','appointment_id',string='Prescription')
    prescription_ids = fields.One2many('hospital.prescription', 'appointment_id', string='Prescriptions')
    evaluation_ids = fields.One2many('hospital.evaluation', 'appointment_id', string='Evaluations')
    treatment_ids = fields.One2many('medical.patient.disease', 'appointment_id', string='Treatments')
    hos_lab_ids = fields.One2many('hospital.laboratory', 'appointment_id',
                                  string="Lab Tests")
    hospital_vaccine_id = fields.One2many('hospital.vaccination', 'appointment_id',
                                  string="Vaccine")
    insurer_id = fields.Many2one('medical.insurance', 'Insurer')
    service_type = fields.Selection([('dental', 'Dental'),
                                     ('ultra', 'Ultra Sound')], string="Service Type")
    dental_id = fields.Many2one('dental.service', 'Dental Service Category')
    dental_service_id = fields.Many2one('dental.sub.service', 'Dental Service')
    ultrasound_id = fields.Many2one('ultrasound.category', 'Ultra Sound Category')
    ultrasound_service_id = fields.Many2one('ultrasound.service', 'Ultra Sound Service')
    dental_charge = fields.Float(related='dental_service_id.price')
    ultrasound_charge = fields.Float(related='ultrasound_service_id.price')
    duration = fields.Integer('Duration')
    inv_count = fields.Integer(string='Invoices', compute='compute_invoice_count')

    def compute_invoice_count(self):
        for record in self:
            inv_count = self.env['account.move'].search_count([('ref', '=', record.name)])
            record.inv_count = inv_count

    def _valid_field_parameter(self, field, name):
        return name == 'sort' or super()._valid_field_parameter(field, name)

    @api.onchange('patient_id')
    def onchange_name(self):
        ins_obj = self.env['medical.insurance']
        ins_record = ins_obj.search([('patient_id', '=', self.patient_id.id)])
        if len(ins_record) >= 1:
            self.insurer_id = ins_record[0].id
        else:
            self.insurer_id = False

    # @api.onchange('inpatient_registration_id')
    # def onchange_patient(self):
    # 	if not self.inpatient_registration_id:
    # 		self.patient_id = ""
    # 	inpatient_obj = self.env['hospital.inpatient'].browse(self.inpatient_registration_id.id)
    # 	self.patient_id = inpatient_obj.id

    def status_approve(self):
        self.write({'app_state': 'approved'})

    def status_in_progress(self):
        self.write({'app_state': 'progress'})

    def status_done(self):
        self.write({'app_state': 'done'})

    def status_suspend(self):
        self.write({'app_state': 'suspend'})

    def confirm(self):
        self.write({'state': 'confirmed'})

    def done(self):
        self.write({'state': 'done'})

    def cancel(self):
        self.write({'state': 'cancel'})

    # def print_prescription(self):
    # 	return self.env.ref('rt_hospital_ms.report_print_prescription').report_action(self)

    # def view_patient_invoice(self):
    # 	self.write({'state': 'cancel'})

    # def create_invoice(self):
    #     lab_req_obj = self.env['medical.appointment']
    #     account_invoice_obj = self.env['account.invoice']
    #     account_invoice_line_obj = self.env['account.invoice.line']
    #
    #     lab_req = lab_req_obj
    #     if lab_req.is_invoiced == True:
    #         raise UserError(_(' Invoice Already Exist'))
    #     if lab_req.no_invoice == False:
    #         res = account_invoice_obj.create({'partner_id': lab_req.patient_id.id,
    #                                           'date_invoice': date.today(),
    #                                           'account_id': lab_req.patient_id.property_account_receivable_id.id,
    #                                           })
    #
    #         res1 = account_invoice_line_obj.create({'product_id': lab_req.consultations_id.id,
    #                                                 'product_uom': lab_req.consultations_id.uom_id.id,
    #                                                 'name': lab_req.consultations_id.name,
    #                                                 'product_uom_qty': 1,
    #                                                 'price_unit': lab_req.consultations_id.lst_price,
    #                                                 'account_id': lab_req.patient_id.property_account_receivable_id.id,
    #                                                 'invoice_id': res.id})
    #
    #         if res:
    #             lab_req.write({'is_invoiced': True})
    #             imd = self.env['ir.model.data']
    #             action = self.env.ref('account.action_invoice_tree1')
    #             list_view_id = imd.sudo()._xmlid_to_res_id('account.view_order_form')
    #             result = {
    #                 'name': action.name,
    #                 'help': action.help,
    #                 'type': action.type,
    #                 'views': [ [list_view_id,'form' ]],
    #                 'target': action.target,
    #                 'context': action.context,
    #                 'res_model': action.res_model,
    #                 'res_id':res.id,
    #             }
    #             if res:
    #                 result['domain'] = "[('id','=',%s)]" % res.id
    #     else:
    #         raise UserError(_(' The Appointment is invoice exempt'))
    #     return result

    # @api.onchange('inv_count')
    # def invoice_count(self):
    #     invoices = self.env['account.move'].filtered(lambda r: r.ref == self.name)
    #     self.inv_count = len(invoices)

    # def view_hospital_invoice(self):
    #     pass

    def hospital_create_invoices(self):
        self.invoice_status = 'invoice'
        appointment_obj = self.env['medical.appointment'].search([])
        inv_obj = self.env['account.move']
        # inv_line_obj = self.env['account.move.line']
        customer = self.patient_id
        if not customer.name:
            raise UserError(
                _(
                    'Please select Patient.'))

        invoice_line_ids = []
        company_id = self.env['res.users'].browse(1).company_id
        currency_value = company_id.currency_id.id
        self.ensure_one()
        journal_id = 1

        inv_data = {
            'ref': self.name,
            'partner_bank_id': customer.bank_ids[:1].id,
            'partner_id': customer.id,
            'currency_id': currency_value,
            'journal_id': int(journal_id),
            'invoice_origin': self.name,
            'company_id': company_id.id,
            'move_type': 'out_invoice',
            # 'invoice_line_ids': invoice_line_ids,
        }

        # for records in self.planned_works:
        #     if records.planned_work.id:
        #         income_account = records.planned_work.property_account_income_id.id
        #         inv_line_data = (0, 0, {
        #             'name': records.planned_work.name,
        #             'account_id': income_account,
        #             'price_unit': records.work_cost,
        #             'quantity': 1,
        #             'product_id': records.planned_work.id,
        #         })
        #         invoice_line_ids.append(inv_line_data)

        for record in self:
            if record.dental_charge > 1:
                inv_line_data = (0, 0, {
                    'name': record.dental_service_id.name,
                    'price_unit': record.dental_charge,
                    'quantity': 1,
                })
                invoice_line_ids.append(inv_line_data)

        for record in self:
            if record.ultrasound_charge > 1:
                inv_line_data = (0, 0, {
                    'name': record.ultrasound_service_id.name,
                    'price_unit': record.ultrasound_charge,
                    'quantity': 1,
                })
                invoice_line_ids.append(inv_line_data)

        for record in self:
            if record.consultations_id:
                income_account = record.consultations_id.property_account_income_id.id
                inv_line_data = (0, 0, {
                    'name': record.consultations_id.name,
                    'account_id': record.consultations_id.property_account_income_id.id,
                    'price_unit': record.consultations_id.lst_price,
                    'quantity': self.consult_qty,
                    'product_id': record.consultations_id.id,
                })
                invoice_line_ids.append(inv_line_data)

        for record in self:
            if record.treatment_ids != []:
                for rec in record.treatment_ids:
                    inv_line_data = (0, 0, {
                        'name': rec.pathology_id.name,
                        # 'account_id': record.consultations_id.property_account_income_id.id,
                        'price_unit': rec.treatment_charge,
                        'quantity': 1,
                        # 'product_id': record.consultations_id.id,
                    })
                    invoice_line_ids.append(inv_line_data)

        inv_data.update({
            'invoice_line_ids': invoice_line_ids
        })
        inv_id = inv_obj.create(inv_data)
        result = {
            'type': 'ir.actions.act_window',
            'name': _('Invoice'),
            'view_mode': 'form',
            'res_model': 'account.move',
            'target': 'current',
            'res_id': inv_id.id,
        }
        IMD = self.env['ir.model.data']
        form_view_id = IMD._xmlid_to_res_id('account.invoice_form')
        if len(inv_id) > 1:
            result['domain'] = "[('id','in',%s)]" % inv_id.ids
        elif len(inv_id) == 1:
            result['views'] = [(form_view_id, 'form')]
            result['res_id'] = inv_id.ids[0]
        else:
            result = {'type': 'ir.actions.act_window_close'}
        invoiced_records = self.env['medical.appointment']

        total = 0
        for rows in invoiced_records:
            invoiced_date = rows.date
            invoiced_date = invoiced_date[0:10]
            if invoiced_date == str(date.today()):
                total = total + rows.price_subtotal
        for line in self:
            product_id = self.env['product.product'].search(
                [('id', '=', line.consultations_id.id)])
            move_id = self.env['stock.picking']
            type_object = self.env['stock.picking.type']
            company_id = self.env.context.get('company_id') or self.env.user.company_id.id
            types = type_object.search([('code', '=', 'outgoing'), ('warehouse_id.company_id', '=', company_id)],
                                       limit=1)
            vals = {
                'partner_id': self.patient_id.id,
                'origin': self.name,
                'move_type': 'one',
                'picking_type_id': types.id,
                'location_id': types.default_location_src_id.id,
                'location_dest_id': self.patient_id.property_stock_customer.id,
                'move_lines': [(0, 0, {
                    'name': self.name,
                    'product_id': product_id.id,
                    'product_uom': product_id.uom_id.id,
                    'product_uom_qty': line.consult_qty,
                    'quantity_done': line.consult_qty,
                    'location_id': types.default_location_src_id.id,
                    'location_dest_id': self.patient_id.property_stock_customer.id,
                })],
            }
            move = move_id.create(vals)
            move.action_confirm()
            move.action_assign()
            move._action_done()

        return result

    def view_hospital_invoice(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Invoices',
            'view_mode': 'tree,form',
            'view_type': 'form',
            'res_model': 'account.move',
            'domain': [('ref', '=', self.name)],
            'context': "{'create': False}"
        }

