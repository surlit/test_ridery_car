# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests
import logging
import json 
_logger = logging.getLogger(__name__)

class vehicle(models.Model):
    _name = 'vehicle.vehicle'
    _description = 'Register Vehicle'
   
    name = fields.Char(string='Name', required=True)
    res_id = fields.Many2one('res.partner',string='User', required=True)
    brand = fields.Char(string='Brand', required=True)
    model = fields.Char(string='Model', required=True)
    plate = fields.Char(string='Plate', required=True,size=8)
    year = fields.Char(string='Year', required=True)
    status = fields.Boolean(string='Activo')
    image = fields.Image(stirng='Image',max_width=512, max_height=512)
    sequence = fields.Char(string="Code", readonly=True, copy=False,default='')
    
    @api.model_create_multi
    def create(self, vals_list):
      for vals in vals_list:
            
            vals['sequence'] = self.env['ir.sequence'].next_by_code('vehicle.vehicle') or '/'
      return super().create(vals_list)
    
    def send_vehicle(self):
            
            
            data = [
                        {
                        'text':{
                              'name':self.name,
                              'res_id':str(self.res_id.name),
                              'code':self.sequence,
                              'brand':self.brand,
                              'model':self.model,
                              'plate':self.plate,
                              'year':self.year
                              },
                        'status':'Activo' if self.status  else 'Inactivo' 
                        }
                  ]  
            
            url = "http://192.168.100.155:3000/api/vehicle"
            
            requests.post(
                  url,
                  json=data,
                  timeout=5
            )

            

