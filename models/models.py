# -*- coding: utf-8 -*-

from odoo import models, fields, api
from pygments.lexer import _inherit
from bzrlib.transport import readonly

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
    item_ids = fields.One2many('res.users.mealitem','meal_id')
    user_id = fields.Many2one('res.users','Meal user')
    notes = fields.Text('Meal notes')
    totalcalories = fields.Integer(string="Total Calories", store=True, compute="_calccalories")
    
    @api.one
    @api.depends('item_ids','item_ids.servings')
    def _calccalories(self):
        currentcalories = 0
        
        for item in self.item_ids:
            caloriestocalculate = item.item_id.calories
            servsize = item.servings
            currentcalories = currentcalories + (caloriestocalculate * servsize)
        
        self.totalcalories = currentcalories  
    
class dietfacts_res_users_mealitem(models.Model):
    _name = 'res.users.mealitem'
    meal_id = fields.Many2one('res.users.meal')
    item_id = fields.Many2one('product.template','Menu Item')
    servings = fields.Float('Servings')
    notes = fields.Text('Meal notes')
    calories = fields.Integer(related="item_id.calories", string="Calories per serving",
                               store=True, readonly=True)
    
    
    
    #dietitem = fields.Boolean('DietItem')
    
    
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
