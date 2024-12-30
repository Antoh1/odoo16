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
from odoo import models, fields, api


class ProductMedicine(models.Model):
    _inherit = 'product.template'
    brand = fields.Char('Brand')
    currency_id = fields.Many2one('res.currency', 'Currency',
                                  default=lambda self: self.env.user.company_id
                                  .currency_id.id,
                                  required=True)
    medicine_ok = fields.Boolean('Medicine')
    dental_service = fields.Boolean('Is Dental Service?')
    ultra_service = fields.Boolean('Is Ultra-Sound Service?')
    product_prices = fields.Monetary('Price', help="Price of the medicine")

    @api.onchange('medicine_ok')
    def onchange_product_type(self):
        self.type = 'consu'
        self.list_price = self.product_prices





