
import datetime
from odoo import models, fields, api
from datetime import datetime


class MaintenanceRequestInh(models.Model):
    _inherit = 'maintenance.request'

    part_ids = fields.One2many('helpdesk.parts.line', 'request_id')
    ticket_ids = fields.Many2many('helpdesk.ticket.type')
    location_src_id = fields.Many2one('stock.location', required=True)

    # @api.onchange('equipment_id')
    # def onchange_location_dest_id(self):
    #     print("rrtrtr")
    #     location = self.env['stock.location'].search([('name', '=', self.equipment_id.location_id.name)])
    #     self.location_dest_id = location.id

    location_dest_id = fields.Many2one('stock.location', required=True)

    cctv_installed = fields.Many2many('product.product', 'name', 'uom_id',related='equipment_id.cctv_installed')
    ptz_camera = fields.Many2one('product.product', related='equipment_id.ptz_camera')
    contractor_name = fields.Many2one('res.partner', related='equipment_id.contractor_name')
    site_contactor = fields.Many2one('contact.name', related='equipment_id.site_contactor')
    no_of_ptz = fields.Many2many('product.product', 'type', 'barcode',related='equipment_id.no_of_ptz')
    cctv_camera = fields.Many2one('product.product', related='equipment_id.cctv_camera')
    ptz_contactor_name = fields.Many2one('res.partner', related='equipment_id.ptz_contactor_name')
    ptz_site_name = fields.Many2one('contact.name', related='equipment_id.ptz_site_name')
    no_of_fibre = fields.Many2many('product.product', 'default_code', 'categ_id',related='equipment_id.no_of_fibre')
    fibre_info = fields.Many2one('product.product', related='equipment_id.fibre_info')
    fibre_contractor_name = fields.Many2one('res.partner', related='equipment_id.fibre_contractor_name')
    fibre_site_name = fields.Many2one('contact.name', related='equipment_id.fibre_site_name')
    ip_address = fields.Char('IP Address', related='equipment_id.ip_address')

    is_pole = fields.Boolean('Pole & Pole Foundation', related='equipment_id.is_pole')
    is_outdoor = fields.Boolean('Outdoor Closures', related='equipment_id.is_outdoor')
    is_battery = fields.Boolean('Battery Closures', related='equipment_id.is_battery')
    is_civil = fields.Boolean('Civil & Fiber Network', related='equipment_id.is_civil')
    is_optical = fields.Boolean('Optical Testing: Fiber Optical Length Measurement', related='equipment_id.is_optical')
    is_attenuation = fields.Boolean('Optical Testing: Attenuation Test', related='equipment_id.is_attenuation')
    is_camera = fields.Boolean('Cameras', related='equipment_id.is_camera')
    is_site = fields.Boolean('Site Power', related='equipment_id.is_site')
    is_wireless = fields.Boolean('Wireless System', related='equipment_id.is_wireless')

    pole_lines = fields.One2many('pole.line', 'site_id', related='equipment_id.pole_lines')
    outdoor_lines = fields.One2many('outdoor.line', 'site_id', related='equipment_id.outdoor_lines')
    battery_lines = fields.One2many('battery.line', 'site_id', related='equipment_id.battery_lines')
    civil_lines = fields.One2many('civil.line', 'site_id', related='equipment_id.civil_lines')
    fibre_lines = fields.One2many('fibre.line', 'site_id', related='equipment_id.fibre_lines')
    attenuation_lines = fields.One2many('attenuation.line', 'site_id', related='equipment_id.attenuation_lines')
    camera_lines = fields.One2many('camera.line', 'site_id', related='equipment_id.camera_lines')
    site_lines = fields.One2many('site.line', 'site_id', related='equipment_id.site_lines')
    wireless_lines = fields.One2many('wireless.line', 'site_id', related='equipment_id.wireless_lines')

    pole_pic = fields.Many2many('ir.attachment', 'res_model', related='equipment_id.pole_pic')
    outdoor_pic = fields.Many2many('ir.attachment', 'file_size', related='equipment_id.outdoor_pic')
    battery_pic = fields.Many2many('ir.attachment', 'url', related='equipment_id.battery_pic')
    civil_pic = fields.Many2many('ir.attachment', 'name', related='equipment_id.civil_pic')
    fibre_pic = fields.Many2many('ir.attachment', 'original_id', related='equipment_id.fibre_pic')
    attenuation_pic = fields.Many2many('ir.attachment', 'res_id', related='equipment_id.attenuation_pic')
    camera_pic = fields.Many2many('ir.attachment', 'res_name', related='equipment_id.camera_pic')
    site_pic = fields.Many2many('ir.attachment', 'public', related='equipment_id.site_pic')
    wireless_pic = fields.Many2many('ir.attachment', 'type', related='equipment_id.wireless_pic')

    pole_comment = fields.Text('Comments', related='equipment_id.pole_comment')
    outdoor_comment = fields.Text('Comments', related='equipment_id.outdoor_comment')
    battery_comment = fields.Text('Comments', related='equipment_id.battery_comment')
    civil_comment = fields.Text('Comments', related='equipment_id.civil_comment')
    fibre_comment = fields.Text('Comments', related='equipment_id.fibre_comment')
    attenuation_comment = fields.Text('Comments', related='equipment_id.attenuation_comment')
    camera_comment = fields.Text('Comments', related='equipment_id.camera_comment')
    site_comment = fields.Text('Comments', related='equipment_id.site_comment')
    wireless_comment = fields.Text('Comments', related='equipment_id.wireless_comment')

    is_pole_client_approved = fields.Boolean('Pole Client Approved', tracking=True)
    is_pole_contractor_approved = fields.Boolean('Pole Contractor Approved', tracking=True)

    is_outdoor_client_approved = fields.Boolean('Outdoor Client Approved', tracking=True)
    is_outdoor_contractor_approved = fields.Boolean('Outdoor Contractor Approved', tracking=True)

    is_battery_client_approved = fields.Boolean('Battery Client Approved', tracking=True)
    is_battery_contractor_approved = fields.Boolean('Battery Contractor Approved', tracking=True)

    is_civil_client_approved = fields.Boolean('Civil Client Approved', tracking=True)
    is_civil_contractor_approved = fields.Boolean('Civil Contractor Approved', tracking=True)

    is_fibre_client_approved = fields.Boolean('Fibre Client Approved', tracking=True)
    is_fibre_contractor_approved = fields.Boolean('Fibre Contractor Approved', tracking=True)

    is_attenuation_client_approved = fields.Boolean('Attenuation Client Approved', tracking=True)
    is_attenuation_contractor_approved = fields.Boolean('Attenuation Contractor Approved', tracking=True)

    is_camera_client_approved = fields.Boolean('Camera Client Approved', tracking=True)
    is_camera_contractor_approved = fields.Boolean('Camera Contractor Approved', tracking=True)

    is_site_client_approved = fields.Boolean('Site Client Approved', tracking=True)
    is_site_contractor_approved = fields.Boolean('Site Contractor Approved', tracking=True)

    is_wireless_client_approved = fields.Boolean('Wireless Client Approved', tracking=True)
    is_wireless_contractor_approved = fields.Boolean('Wireless Contractor Approved', tracking=True)

    pole_name = fields.Char('Name')
    outdoor_name = fields.Char('Name')
    battery_name = fields.Char('Name')
    civil_name = fields.Char('Name')
    fibre_name = fields.Char('Name')
    attenuation_name = fields.Char('Name')
    camera_name = fields.Char('Name')
    site_name = fields.Char('Name')
    wireless_name = fields.Char('Name')

    pole_sig = fields.Char('Signature')
    outdoor_sig = fields.Char('Signature')
    battery_sig = fields.Char('Signature')
    civil_sig = fields.Char('Signature')
    fibre_sig = fields.Char('Signature')
    attenuation_sig = fields.Char('Signature')
    camera_sig = fields.Char('Signature')
    site_sig = fields.Char('Signature')
    wireless_sig = fields.Char('Signature')

    @api.onchange('equipment_id')
    def onchange_equipment_id(self):
        line_list = []
        for rec in self.part_ids:
            rec.unlink()
        for line in self.equipment_id.transfer_id.move_ids_without_package:
            lines = {
                'type': 'add',
                'product_id': line.product_id.id,
                'name': line.product_id.name,
                'uom_id': line.product_id.uom_id.id,
                'qty': line.quantity_done,
                'request_id': self.id,
                'is_added': True,
            }
            line_list.append(lines)
        stock_move = self.env['helpdesk.parts.line'].create(line_list)
        location = self.env['stock.location'].search([('name', '=', self.equipment_id.location_id.name)])
        location_src = self.env['stock.location'].search([('name', '=', 'Stock')])
        self.location_src_id = location_src.id
        self.location_dest_id = location.id

    def action_pole_contractor_approve(self):
        self.is_pole_contractor_approved = True

    def action_pole_client_approve(self):
        self.is_pole_client_approved = True

    def action_outdoor_contractor_approve(self):
        self.is_outdoor_contractor_approved = True

    def action_outdoor_client_approve(self):
        self.is_outdoor_client_approved = True

    def action_battery_contractor_approve(self):
        self.is_battery_contractor_approved = True

    def action_battery_client_approve(self):
        self.is_battery_client_approved = True

    def action_civil_contractor_approve(self):
        self.is_civil_contractor_approved = True

    def action_civil_client_approve(self):
        self.is_civil_client_approved = True

    def action_fibre_contractor_approve(self):
        self.is_fibre_contractor_approved = True

    def action_fibre_client_approve(self):
        self.is_fibre_client_approved = True

    def action_attenuation_contractor_approve(self):
        self.is_attenuation_contractor_approved = True

    def action_attenuation_client_approve(self):
        self.is_attenuation_client_approved = True

    def action_camera_contractor_approve(self):
        self.is_camera_contractor_approved = True

    def action_camera_client_approve(self):
        self.is_camera_client_approved = True

    def action_site_contractor_approve(self):
        self.is_site_contractor_approved = True

    def action_site_client_approve(self):
        self.is_site_client_approved = True

    def action_wireless_contractor_approve(self):
        self.is_wireless_contractor_approved = True

    def action_wireless_client_approve(self):
        self.is_wireless_client_approved = True

    def action_validate(self):
        for rec in self.part_ids:
            if not rec.is_picking_created:
                if rec.type == 'add' and not rec.is_added:
                    outgoing_pick = self.env['stock.picking.type'].search([('code', '=', 'outgoing')], limit=1)
                    vals = {
                        'location_id': self.location_src_id.id,
                        'location_dest_id': self.location_dest_id.id,
                        # 'partner_id': self.partner_id.id,
                        'picking_type_id': outgoing_pick.id,
                        'scheduled_date': datetime.now(),
                        'move_type': 'direct',
                    }
                    picking = self.env['stock.picking'].create(vals)
                    lines = {
                        'picking_id': picking.id,
                        'product_id': rec.product_id.id,
                        'name': rec.product_id.name,
                        'product_uom': rec.product_id.uom_id.id,
                        'location_id': self.location_src_id.id,
                        'location_dest_id': self.location_dest_id.id,
                        'product_uom_qty': rec.qty,
                    }
                    stock_move = self.env['stock.move'].create(lines)
                    picking.action_confirm()
                    rec.delivered_id = picking.id
                    rec.is_picking_created = True
                if rec.type == 'remove':
                    incoming_pick = self.env['stock.picking.type'].search([('code', '=', 'incoming')], limit=1)
                    vals = {
                        'location_id': self.location_src_id.id,
                        'location_dest_id': self.location_dest_id.id,
                        # 'partner_id': self.partner_id.id,
                        'picking_type_id': incoming_pick.id,
                        'scheduled_date': datetime.now(),
                        'move_type': 'direct',
                    }
                    picking = self.env['stock.picking'].create(vals)
                    lines = {
                        'picking_id': picking.id,
                        'product_id': rec.product_id.id,
                        'name': rec.product_id.name,
                        'product_uom': rec.product_id.uom_id.id,
                        'location_id': self.location_src_id.id,
                        'location_dest_id': self.location_dest_id.id,
                        'product_uom_qty': rec.qty,
                    }
                    stock_move = self.env['stock.move'].create(lines)
                    picking.action_confirm()
                    rec.received_id = picking.id
                    rec.is_picking_created = True