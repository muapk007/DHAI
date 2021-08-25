from odoo import models, api


class MaintenanceLocationInh(models.Model):
    _inherit = 'maintenance.location'

    @api.model
    def create(self, vals_list):
        record = super(MaintenanceLocationInh, self).create(vals_list)
        wh = self.env['stock.location'].search([('name', '=', 'WH')])
        vals = {
            'name': record.name,
            'usage': 'internal',
            'location_id': wh.id,
        }
        rec = self.env['stock.location'].create(vals)
        return record
