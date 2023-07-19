from odoo import fields, models

class EstateProperties(models.Model):
    _name = "estate.property"
    _description = "Model for Real Estate Properties"


    name = fields.Char(string="Title", required=True)
    title = fields.Char(required=False)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    available_from = fields.Date()
    expected_price = fields.Float(required=True)
    selling_price = fields.Float()
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    state = fields.Selection([
        ('new', 'New'),
        ('offerReceived', 'Offer Received'),
        ('offerAccepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('cancel', 'Cancel'),
    ], required=True, default='new',)
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),
    ])
