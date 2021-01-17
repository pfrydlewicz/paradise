# -*- coding: utf-8 -*-
# Copyright (c) 2021, FCON and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator

class ProjectPortfolio(WebsiteGenerator):
	website = frappe._dict(
		template = "templates/generators/project_portfolio.html"
	)
	
	def validate(self):
		self.page_name = self.name.lower()

