# -*- coding: utf-8 -*-
# from odoo import http


# class RtProcurement(http.Controller):
#     @http.route('/rt_procurement/rt_procurement', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rt_procurement/rt_procurement/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rt_procurement.listing', {
#             'root': '/rt_procurement/rt_procurement',
#             'objects': http.request.env['rt_procurement.rt_procurement'].search([]),
#         })

#     @http.route('/rt_procurement/rt_procurement/objects/<model("rt_procurement.rt_procurement"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rt_procurement.object', {
#             'object': obj
#         })
