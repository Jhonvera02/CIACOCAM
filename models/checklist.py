# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ChecklistPlantilla(models.Model):
    _name = 'ciacocam.checklist.plantilla'
    _description = 'Plantillas de Checklist'

    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')
    linea_ids = fields.One2many('ciacocam.checklist.linea', 'plantilla_id', string='Ítems')
    active = fields.Boolean(default=True)


class ChecklistLinea(models.Model):
    _name = 'ciacocam.checklist.linea'
    _description = 'Líneas de Checklist'
    _order = 'secuencia, id'

    name = fields.Char(string='Punto a Verificar', required=True)
    secuencia = fields.Integer(string='Secuencia', default=10)
    plantilla_id = fields.Many2one('ciacocam.checklist.plantilla', string='Plantilla', ondelete='cascade')
