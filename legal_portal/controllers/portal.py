# -*- coding: utf-8 -*-

from odoo import http
from odoo.addons.web.controllers.main import Home
from odoo.http import request


class Home(Home):

    @http.route()
    def index(self, s_action=None, db=None, **kw):
        # sobre escribimos el comportamiento de portal mandando a /web
        # TODO deberiamos hacer algo mas elegante que re-escribir el metodo
        return http.local_redirect('/web', query=request.params, keep_hash=True)

    def _login_redirect(self, uid, redirect=None):
        # sobre escribimos el comportamiento de portal mandando a /web
        # TODO deberiamos hacer algo mas elegante que re-escribir el metodo
        return redirect if redirect else '/web'
