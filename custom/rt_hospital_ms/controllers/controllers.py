# -*- coding: utf-8 -*-
# from odoo import http


# class RtHospitalMs(http.Controller):
#     @http.route('/rt_hospital_ms/rt_hospital_ms', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rt_hospital_ms/rt_hospital_ms/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rt_hospital_ms.listing', {
#             'root': '/rt_hospital_ms/rt_hospital_ms',
#             'objects': http.request.env['rt_hospital_ms.rt_hospital_ms'].search([]),
#         })

#     @http.route('/rt_hospital_ms/rt_hospital_ms/objects/<model("rt_hospital_ms.rt_hospital_ms"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rt_hospital_ms.object', {
#             'object': obj
#         })
