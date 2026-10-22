# -*- coding: utf-8 -*-
{
    'name': 'CIACOCAM',
    'version': '19.0.1.0.0',
    'category': 'Services',
    'summary': 'Control Integral y Administración de Cámaras de Seguridad',
    'description': """
        CIACOCAM - Sistema de Control Integral y Administración de Cámaras
        ==================================================================
        Módulo para la gestión completa de sistemas de videovigilancia:
        * Gestión de DVRs/NVRs
        * Control de cámaras de seguridad
        * Inspecciones periódicas con checklists
        * Registro y seguimiento de incidencias
        * Órdenes de mantenimiento preventivo y correctivo
        * Historial completo de eventos
    """,
    'author': 'SIGI',
    'website': '',
    'depends': ['base'],
    'data': [
        # Security
        'security/security_groups.xml',
        'security/ir.model.access.csv',
        # Data
        'data/data.xml',
        # Views
        'views/menu.xml',
        'views/ubicacion_views.xml',
        'views/dvr_views.xml',
        'views/camara_views.xml',
        'views/checklist_views.xml',
        'views/inspeccion_views.xml',
        'views/incidencia_views.xml',
        'views/mantenimiento_views.xml',
        'views/historial_views.xml',
        'views/dashboard.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
