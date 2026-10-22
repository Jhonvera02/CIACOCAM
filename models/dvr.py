# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Dvr(models.Model):
    _name = 'ciacocam.dvr'
    _description = 'Grabadores DVR/NVR'

    name = fields.Char(string='Nombre', required=True)
    marca = fields.Char(string='Marca')
    modelo = fields.Char(string='Modelo')
    numero_serie = fields.Char(string='Número de Serie')
    ip_address = fields.Char(string='Dirección IP')
    puerto = fields.Integer(string='Puerto')
    capacidad_canales = fields.Integer(string='Canales Disponibles')
    capacidad_disco = fields.Char(string='Capacidad de Disco')
    ubicacion_id = fields.Many2one('ciacocam.ubicacion', string='Ubicación')
    camara_ids = fields.One2many('ciacocam.camara', 'dvr_id', string='Cámaras')
    state = fields.Selection([
        ('operativo', 'Operativo'),
        ('con_fallas', 'Con Fallas'),
        ('fuera_servicio', 'Fuera de Servicio')
    ], default='operativo', string='Estado')
    fecha_instalacion = fields.Date(string='Fecha de Instalación')
    notas = fields.Text(string='Notas')
    active = fields.Boolean(default=True)
    
    camara_count = fields.Integer(compute='_compute_camara_count', string='Cantidad de Cámaras')

    @api.depends('camara_ids')
    def _compute_camara_count(self):
        for record in self:
            record.camara_count = len(record.camara_ids)
