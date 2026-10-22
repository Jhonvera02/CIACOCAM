# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Mantenimiento(models.Model):
    _name = 'ciacocam.mantenimiento'
    _description = 'Órdenes de Mantenimiento'
    _order = 'fecha_programada desc, id desc'

    name = fields.Char(string='Referencia', readonly=True, copy=False, default='Nuevo')
    tipo = fields.Selection([
        ('preventivo', 'Preventivo'),
        ('correctivo', 'Correctivo')
    ], required=True, string='Tipo')
    fecha_programada = fields.Date(string='Fecha Programada')
    fecha_ejecucion = fields.Date(string='Fecha de Ejecución')
    tecnico_id = fields.Many2one('res.users', string='Técnico Responsable')
    ubicacion_id = fields.Many2one('ciacocam.ubicacion', string='Ubicación', required=True)
    camara_id = fields.Many2one('ciacocam.camara', string='Cámara')
    dvr_id = fields.Many2one('ciacocam.dvr', string='DVR')
    incidencia_id = fields.Many2one('ciacocam.incidencia', string='Incidencia Relacionada')
    descripcion = fields.Text(string='Trabajo a Realizar')
    resultado = fields.Text(string='Resultado')
    state = fields.Selection([
        ('programado', 'Programado'),
        ('en_proceso', 'En Proceso'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado')
    ], default='programado', string='Estado')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'Nuevo') == 'Nuevo':
                vals['name'] = self.env['ir.sequence'].next_by_code('ciacocam.mantenimiento') or 'Nuevo'
        return super(Mantenimiento, self).create(vals_list)

    def action_iniciar(self):
        for record in self:
            record.state = 'en_proceso'

    def action_completar(self):
        for record in self:
            record.state = 'completado'
            if not record.fecha_ejecucion:
                record.fecha_ejecucion = fields.Date.context_today(self)

    def action_cancelar(self):
        for record in self:
            record.state = 'cancelado'
