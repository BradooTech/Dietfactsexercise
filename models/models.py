# -*- coding: utf-8 -*-

from odoo import models, fields, api
from pygments.lexer import _inherit

class dietfacts(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    calories = fields.Integer('Calories')
    servingsize = fields.Float('Serving Size')
    lastupdated = fields.Date('Last Updated')
    
    
class dietfacts_res_users_meal(models.Model):
    _name = 'res.users.meal'
    name = fields.Char('Meal name')
    meal_date = fields.Datetime('Meal date')
    #item_ids = fields.One2Many()
    user_id = fields.Many2one('res.users','Meal user')
    notes = fields.Text('Meal notes')
    
    
    
    
    
    
    #dietitem = fields.Boolean('DietItem')
    
    
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
