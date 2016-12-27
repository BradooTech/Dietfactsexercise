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
    meal_nutrient_ids = fields.One2many('product.template.nutrient', 'product_id')
    
class dietfacts_res_users_meal(models.Model):
    _name = 'res.users.meal'
    name = fields.Char('Meal name')
    meal_date = fields.Datetime('Meal date')
    item_ids = fields.One2many('res.users.mealitem', 'meal_id')
    user_id = fields.Many2one('res.users', 'Meal user')
    notes = fields.Text('Meal notes')
    totalcalories = fields.Integer(string="Total Calories", store=True, compute="_calccalories")
    totalitems = fields.Integer(string="Meal items", compute="_calccalories", store=True) 
    
    @api.multi
    @api.depends('item_ids', 'item_ids.servings')
    def _calccalories(self):
        currentcalories = 0
        currentitem = 0
        
        for item in self.item_ids:
            caloriestocalculate = item.item_id.calories
            servsize = item.servings
            currentcalories = currentcalories + (caloriestocalculate * servsize)
            currentitem += 1
            
        self.totalcalories = currentcalories  
        self.totalitems = currentitem
            
        
    
class dietfacts_res_users_mealitem(models.Model):
    _name = 'res.users.mealitem'
    meal_id = fields.Many2one('res.users.meal')
    item_id = fields.Many2one('product.template', 'Menu Item')
    servings = fields.Float('Servings')
    notes = fields.Text('Meal notes')
    calories = fields.Integer(related="item_id.calories", string="Calories per serving",
                               store=True, readonly=True)
    
    
    dailyvalue = fields.Float('Daily value')

class dietfacts_product_nutrient(models.Model):
    _name = 'product.nutrient'
    name = fields.Char('Nutrient name')
    uom_id = fields.Many2one('product.uom', 'Unity of Measure')
    description = fields.Text('Description')
    # meal_item_id = fields.Many2one('product.template','Meal')
    

class dietfacts_product_template_nutrient(models.Model):
    _name = 'product.template.nutrient'
    nutrient_id = fields.Many2one('product.nutrient', string='Nutrient')
    product_id = fields.Many2one('product.template', string='Diet Item')
    value = fields.Float('Value')
    dailypercentage = fields.Float('Daily Percentage')
    unityofmeasure = fields.Char(related="nutrient_id.uom_id.name", string="Unity of measure",
                                readonly=True)
    # dietitem = fields.Boolean('DietItem')
    
    
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
