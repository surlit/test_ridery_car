# -*- coding: utf-8 -*-

from odoo import models, fields, api

class vehicles_logs(models.Model):
    _name = 'vehicles_logs.vehicles_logs'
    _description = 'Register logs of the vehicles '

    status = fields.Char(string='Status')
    text = fields.Char(string='Text')

