# -*- coding: utf-8 -*-
# Copyright (c) 2021, FCON and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator
from frappe.website.doctype.website_slideshow.website_slideshow import \
	get_slideshow

class PortfolioProject(WebsiteGenerator):
	website = frappe._dict(
		template = "templates/generators/portfolio_project.html"
	)
	
	def validate(self):
		pass

	def make_route(self):
		route = "/portfolio-projects/" + self.name.lower()

		
	def get_context(self, context):
		if self.slideshow:
			context.update(get_slideshow(self))

		return context
