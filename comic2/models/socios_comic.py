# -*- coding: utf-8 -*-
from datetime import timedelta
from odoo import models, fields, api


class socios(models.Model):
    _name = 'biblioteca.socios'

    _description = 'Socio de Biblioteca'
    _inherit = ['biblioteca.comic']
    nombre = fields.Char()
    apellidos = fields.Char()
    identificador = fields.Integer()
