# -*- coding: utf-8 -*-

from odoo import models, fields, api


class vehicle(models.Model):
    _name = 'vehicle.vehicle'
    _description = 'Register Vehicle'

    year = fields.Char(string='Year', required=True)
    plate = fields.Char(string='Plate', required=True)
    model = fields.Char(string='Model', required=True)
    brand = fields.Char(string='Brand', required=True)
    res_id = fields.Many2one('res.partner',string='User', required=True)
