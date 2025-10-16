// server.js
require('dotenv').config();
const express = require('express');
const fs = require('fs');
const path = require('path');
const app = express();
const PORT = 3000;
const xmlrpc = require('xmlrpc')
const odoo_url = process.env.odoo_url
const odoo_port = process.env.odoo_port
const db = process.env.db_odoo
const username = process.env.username_admin 
const password = process.env.password_admin


// Middleware para parsear JSON
app.use(express.json());

// Endpoint para recibir datos de vehículos
app.post('/api/vehicle', (req, res) => {
    const datas = req.body;

    console.log(' Datos recibidos...');
    
    
    const clientCommon = xmlrpc.createClient({
        host: odoo_url,
        port: odoo_port,
        path: '/xmlrpc/2/common'
    });

    clientCommon.methodCall('authenticate',[db,username,password,{}],(err,uid) =>{
        if(err){
            

            console.log('error al auntentificar');  
            res.status(400).json({
                status: 'error',
                message: 'Ha ocurrido un error al aunteticar',
                timestamp: new Date().toISOString()   
            });
            
            
        }
        
        
        datas.map((vehicle)=>{
            console.log('vehicle');
            console.log(vehicle);            
            create_logs(uid,vehicle,res)
        })
    })
    
    
    const response = {
        status: 'success',
        message: 'Vehículos recibido correctamente',
        timestamp: new Date().toISOString()
    };
    
    res.status(200).json(response);
});
function create_logs(uid,data,res){
    const models = xmlrpc.createClient({
        host: odoo_url,
        port: odoo_port,
        path: '/xmlrpc/2/object' 
    });
        
     models.methodCall('execute_kw', [
        db,          
        uid,                
        password,          
        'vehicles_logs.vehicles_logs',    
        'create',    
        [data], 
        {}  
        ], (err, result) => {
        if(err){
            res.status
        }
    });
}

// Iniciar servidor
app.listen(PORT, () => {
    console.log(`🚀 API de los logs de vehículos corriendo en http://localhost:${PORT}`);
        
});