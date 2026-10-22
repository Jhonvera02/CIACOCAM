# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Inspeccion(models.Model):
    _name = 'ciacocam.inspeccion'
    _description = 'Inspecciones'
    _order = 'fecha desc, id desc'

    name = fields.Char(string='Referencia', readonly=True, copy=False, default='Nuevo')
    fecha = fields.Datetime(string='Fecha', default=fields.Datetime.now)
    inspector_id = fields.Many2one('res.users', string='Inspector', default=lambda self: self.env.user)
    ubicacion_id = fields.Many2one('ciacocam.ubicacion', string='Ubicación', required=True)
    checklist_id = fields.Many2one('ciacocam.checklist.plantilla', string='Checklist')
    resultado_ids = fields.One2many('ciacocam.inspeccion.resultado', 'inspeccion_id', string='Resultados')
    state = fields.Selection([
        ('borrador', 'Borrador'),
        ('en_proceso', 'En Proceso'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada')
    ], default='borrador', string='Estado')
    observaciones = fields.Text(string='Observaciones')
    incidencia_ids = fields.One2many('ciacocam.incidencia', 'inspeccion_id', string='Incidencias')
    
    incidencia_count = fields.Integer(compute='_compute_incidencia_count', string='Cantidad de Incidencias')

    @api.depends('incidencia_ids')
    def _compute_incidencia_count(self):
        for record in self:
            record.incidencia_count = len(record.incidencia_ids)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'Nuevo') == 'Nuevo':
                vals['name'] = self.env['ir.sequence'].next_by_code('ciacocam.inspeccion') or 'Nuevo'
        return super(Inspeccion, self).create(vals_list)

    def action_iniciar(self):
        for record in self:
            record.state = 'en_proceso'

    def action_completar(self):
        for record in self:
            record.state = 'completada'

    def action_cancelar(self):
        for record in self:
            record.state = 'cancelada'

    def action_borrador(self):
        for record in self:
            record.state = 'borrador'

    def action_cargar_checklist(self):
        for record in self:
            if record.checklist_id:
                record.resultado_ids.unlink()
                lines = []
                for linea in record.checklist_id.linea_ids:
                    lines.append((0, 0, {
                        'linea_id': linea.id,
                        'cumple': False,
                    }))
                record.write({'resultado_ids': lines})


class InspeccionResultado(models.Model):
    _name = 'ciacocam.inspeccion.resultado'
    _description = 'Resultados de Inspección'

    inspeccion_id = fields.Many2one('ciacocam.inspeccion', string='Inspección', ondelete='cascade')
    linea_id = fields.Many2one('ciacocam.checklist.linea', string='Punto de Verificación')
    cumple = fields.Selection([
        ('si', 'Sí'),
        ('no', 'No'),
        ('na', 'N/A')
    ], string='¿Cumple?')
    observacion = fields.Text(string='Observación')
