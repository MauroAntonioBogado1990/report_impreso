# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ExeReporteFuneraria(models.Model):
    _inherit = 'account.move'