# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Historial(models.Model):
    _name = 'ciacocam.historial'
    _description = 'Historial de Eventos'
    _order = 'fecha desc'

    name = fields.Char(string='Descripción', required=True)
    fecha = fields.Datetime(string='Fecha', default=fields.Datetime.now)
    tipo_evento = fields.Selection([
        ('instalacion', 'Instalación'),
        ('desinstalacion', 'Desinstalación'),
        ('falla', 'Falla'),
        ('reparacion', 'Reparación'),
        ('inspeccion', 'Inspección'),
        ('cambio_estado', 'Cambio de Estado'),
        ('otro', 'Otro')
    ], string='Tipo de Evento')
    usuario_id = fields.Many2one('res.users', string='Registrado por', default=lambda self: self.env.user)
    ubicacion_id = fields.Many2one('ciacocam.ubicacion', string='Ubicación')
    camara_id = fields.Many2one('ciacocam.camara', string='Cámara')
    dvr_id = fields.Many2one('ciacocam.dvr', string='DVR')
    detalle = fields.Text(string='Detalle')
