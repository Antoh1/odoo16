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


class Blood(models.Model):
    _name = 'hospital.blood'
    _description = 'Blood Group'
    _rec_name = 'blood_type'

    # blood_grp = fields.Char(string="Blood Group", required="True")
    blood_type = fields.Selection([('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], string="Blood Group")
    rh = fields.Selection([('-+', '+'), ('--', '-')], string="Rhesus")
    # _sql_constraints = [('unique_blood', 'unique (blood_grp)',
    #                      'Blood group already present!')]


class GeneticRisks(models.Model):
    _name = 'genetic.risks'
    _description = ' Genetic Risks'
    _rec_name = 'risks'

    risks = fields.Char(string="Genetic Risks", required="True")

