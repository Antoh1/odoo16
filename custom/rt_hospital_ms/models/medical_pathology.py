# -*- coding: utf-8 -*-
# Part of Ropetech. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _


class MedicalPathology(models.Model):
    _name = 'medical.pathology'
    _description = 'Medical Pathology'

    name = fields.Char(string="Disease Name", required=True)
    code = fields.Char(string="Code")
    disease_group = fields.Many2one('medical.pathology.group', string="Disease Category")
    chromosome = fields.Char(string="Affected Chromosome")
    gene = fields.Char(string="Gene")
    protein = fields.Char(string="Protein")
    info = fields.Text(string="Extra Info")
