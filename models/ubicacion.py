# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Ubicacion(models.Model):
    _name = 'ciacocam.ubicacion'
    _description = 'Sedes/Sucursales'

    name = fields.Char(string='Nombre', required=True)
    direccion = fields.Text(string='Dirección')
    ciudad = fields.Char(string='Ciudad')
    responsable_id = fields.Many2one('res.users', string='Responsable')
    dvr_ids = fields.One2many('ciacocam.dvr', 'ubicacion_id', string='DVRs')
    camara_ids = fields.One2many('ciacocam.camara', 'ubicacion_id', string='Cámaras')
    notas = fields.Text(string='Notas')
    active = fields.Boolean(default=True)
    
    dvr_count = fields.Integer(compute='_compute_counts', string='Cantidad de DVRs')
    camara_count = fields.Integer(compute='_compute_counts', string='Cantidad de Cámaras')

    @api.depends('dvr_ids', 'camara_ids')
    def _compute_counts(self):
        for record in self:
            record.dvr_count = len(record.dvr_ids)
            record.camara_count = len(record.camara_ids)
