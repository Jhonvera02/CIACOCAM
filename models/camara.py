# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Camara(models.Model):
    _name = 'ciacocam.camara'
    _description = 'Cámaras de Seguridad'

    name = fields.Char(string='Nombre', required=True)
    marca = fields.Char(string='Marca')
    modelo = fields.Char(string='Modelo')
    numero_serie = fields.Char(string='Número de Serie')
    tipo = fields.Selection([
        ('domo', 'Domo'),
        ('bullet', 'Bullet'),
        ('ptz', 'PTZ'),
        ('fija', 'Fija'),
        ('otra', 'Otra')
    ], string='Tipo')
    resolucion = fields.Char(string='Resolución')
    ip_address = fields.Char(string='Dirección IP')
    dvr_id = fields.Many2one('ciacocam.dvr', string='DVR')
    canal = fields.Integer(string='Canal')
    ubicacion_id = fields.Many2one('ciacocam.ubicacion', string='Ubicación')
    zona = fields.Char(string='Zona/Área')
    state = fields.Selection([
        ('operativa', 'Operativa'),
        ('con_fallas', 'Con Fallas'),
        ('fuera_servicio', 'Fuera de Servicio')
    ], default='operativa', string='Estado')
    fecha_instalacion = fields.Date(string='Fecha de Instalación')
    notas = fields.Text(string='Notas')
    active = fields.Boolean(default=True)
