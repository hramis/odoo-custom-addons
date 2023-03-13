from odoo import models, fields, api
from odoo.exceptions import ValidationError

#Definimos modelo Biblioteca comic
class PrestamoComic(models.Model):

    _name = 'prestamo.comic'
    _description = 'Prestamos de Comics'

    _inherit = ['biblioteca.comic']

    nombre_socio = fields.Char()
    fecha_prestado = fields.Date(string='Fecha Prestado')
    fecha_devuelto = fields.Date(string='Fecha Devuelto')
