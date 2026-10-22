# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Incidencia(models.Model):
    _name = 'ciacocam.incidencia'
    _description = 'Incidencias'
    _order = 'fecha_reporte desc, id desc'

    name = fields.Char(string='Referencia', readonly=True, copy=False, default='Nuevo')
    fecha_reporte = fields.Datetime(string='Fecha de Reporte', default=fields.Datetime.now)
    reportado_por_id = fields.Many2one('res.users', string='Reportado por', default=lambda self: self.env.user)
    ubicacion_id = fields.Many2one('ciacocam.ubicacion', string='Ubicación', required=True)
    camara_id = fields.Many2one('ciacocam.camara', string='Cámara')
    dvr_id = fields.Many2one('ciacocam.dvr', string='DVR')
    inspeccion_id = fields.Many2one('ciacocam.inspeccion', string='Inspección Origen')
    tipo = fields.Selection([
        ('falla_equipo', 'Falla de Equipo'),
        ('vandalismo', 'Vandalismo'),
        ('cobertura', 'Problema de Cobertura'),
        ('conectividad', 'Conectividad'),
        ('otro', 'Otro')
    ], string='Tipo')
    prioridad = fields.Selection([
        ('0', 'Baja'),
        ('1', 'Media'),
        ('2', 'Alta'),
        ('3', 'Crítica')
    ], default='1', string='Prioridad')
    descripcion = fields.Text(string='Descripción', required=True)
    state = fields.Selection([
        ('abierta', 'Abierta'),
        ('en_proceso', 'En Proceso'),
        ('resuelta', 'Resuelta'),
        ('cerrada', 'Cerrada')
    ], default='abierta', string='Estado')
    fecha_resolucion = fields.Datetime(string='Fecha de Resolución')
    solucion = fields.Text(string='Solución')
    asignado_a_id = fields.Many2one('res.users', string='Asignado a')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'Nuevo') == 'Nuevo':
                vals['name'] = self.env['ir.sequence'].next_by_code('ciacocam.incidencia') or 'Nuevo'
        return super(Incidencia, self).create(vals_list)

    def action_en_proceso(self):
        for record in self:
            record.state = 'en_proceso'

    def action_resolver(self):
        for record in self:
            record.state = 'resuelta'
            if not record.fecha_resolucion:
                record.fecha_resolucion = fields.Datetime.now()

    def action_cerrar(self):
        for record in self:
            record.state = 'cerrada'

    def action_reabrir(self):
        for record in self:
            record.state = 'abierta'
            record.fecha_resolucion = False
