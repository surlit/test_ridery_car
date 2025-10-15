# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests
import logging
_logger = logging.getLogger(__name__)

class vehicle(models.Model):
    _name = 'vehicle.vehicle'
    _description = 'Register Vehicle'

    name = fields.Char(string='Name', required=True)
    year = fields.Char(string='Year', required=True)
    plate = fields.Char(string='Plate', required=True,size=8)
    model = fields.Char(string='Model', required=True)
    brand = fields.Char(string='Brand', required=True)
    res_id = fields.Many2one('res.partner',string='User', required=True)

    def send_vehicle(self):
            
            data = {
                  'name':self.name,
                  'partner_id':self.res_id.name,
                  'brand':self.brand,
                  'model':self.model,
                  'plate':self.plate,
                  'year':self.year
            }
            url = "http://localhost:8069/"
            headers = ""
            
            requests.post(
                  url,
                  headers,
                  data,
                  timeout=5
            )

