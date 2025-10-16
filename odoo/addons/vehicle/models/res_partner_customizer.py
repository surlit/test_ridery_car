# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
import requests 
_logger = logging.getLogger(__name__)

class ResPartnerCustomizer(models.Model):
    _inherit = 'res.partner'

    def search_vehicle(self):
        vehicles = self.env['vehicle.vehicle'].search([('res_id','=',self.id)])

        return vehicles
    
    def search_vehicle_user(self):        
                
        return{
            'name':'Vehiculos Asociados',
            'type':'ir.actions.act_window',
            'res_model':'vehicle.vehicle',
            'views':[
                (self.env.ref('vehicle.vehicle_modal_view_tree').id,'tree'),
                
                ],
            'view_mode':'tree',
            'domain':[('id','in',self.search_vehicle().ids)],
            'context':{'default_res_id':self.id},
            'target':'new',
            
        }        
    def send_vehicles_user(self):
        
        vehicles_ids = self.search_vehicle()
        
        list_vehicles = []
        
        for vehicle in vehicles_ids:
            list_vehicles.append({
                'text':{
                    'name':vehicle.name,
                    'res_id':str(vehicle.res_id.name),
                    'code':vehicle.sequence,
                    'brand':vehicle.brand,
                    'model':vehicle.model,
                    'year':vehicle.year,
                },
                'status':'Activo' if vehicle.status else 'Inactivo' 

            })
        
        url = "http://192.168.100.155:3000/api/vehicle"
            
        requests.post(
                url,
                json=list_vehicles,
                timeout=5
        )