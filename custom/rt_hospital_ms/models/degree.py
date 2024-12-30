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


class Degree(models.Model):
    _name = 'hospital.degree'
    _description = 'Degree'
    _rec_name = 'degree'

    degree = fields.Char(string="Doctor's Degree", required="True")


class Specialization(models.Model):
    _name = 'hospital.specialization'
    _description = "Doctor's Specialization"
    _rec_name = 'specialization'

    specialization = fields.Char(string="Doctor's Specialization",
                                 required="True")


class Institution(models.Model):
    _name = 'hospital.institution'
    _description = "Doctor's Institution"
    _rec_name = 'institution'

    institution = fields.Char(string="Doctor's Institution", required="True")