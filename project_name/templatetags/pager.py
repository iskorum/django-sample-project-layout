# -*- coding: utf-8 -*-
from django import template
import re, json

register = template.Library()


@register.tag
def pager(parser, token):

	try:
		tag_name, arg = token.contents.split(None, 1)
	except ValueError:
		raise template.TemplateSyntaxError("%r tag requires exactly two argument" % token.contents.split()[0])

	try:
		m = re.search(r'(.*?) as (\w+)', arg)
		if not m: raise template.TemplateSyntaxError("%r tag had invalid arguments" % tag_name)
		object_name, var_name = m.groups()
	except:
		object_name, var_name = arg, None

	return PagerNode(object_name, var_name)


class PagerNode(template.Node):

	def __init__(self, object_name, var_name):

		self.template_file = 'utils/pagination.html'
		self.spacer = 0

		self.pager_var = 'sayfa'
		self.var_name = var_name
		self.object_name = object_name

	def render(self, context):
		try:
			pager = context[self.object_name]

			current_page = pager.number
			total_pages = pager.paginator.num_pages

			# ------------------------- page numbers -----------------------------
			pages = []
			if total_pages == 1: pass
			elif total_pages < 8: map(pages.append, range(1, total_pages+1))
			else:
				if current_page <= 4:
					map(pages.append, range(1, current_page+2))
					pages.append(self.spacer)
					map(pages.append, range(total_pages-1, total_pages+1))
				elif current_page >= total_pages-3:
					map(pages.append, range(1, 3))
					pages.append(self.spacer)
					map(pages.append, range(current_page-1, total_pages+1))
				else:
					map(pages.append, range(1, 3))
					pages.append(self.spacer)
					pages.append(current_page-1)
					pages.append(current_page)
					pages.append(current_page+1)
					pages.append(self.spacer)
					map(pages.append, range(total_pages-1, total_pages+1))
			# --------------------------------------------------------------------

			# ------------------------- get parameters ---------------------------
			data = context['request'].GET.copy()
			get_params = ""
			try: data.pop(self.pager_var)
			except: pass
			for key, value in data.iteritems(): get_params += "&{0}={1}".format(key, value)
			# --------------------------------------------------------------------

			p = {
				'total_pages': total_pages,
				'previous_page': current_page-1,
				'current_page': current_page,
				'next_page': current_page+1,
				'has_previous': pager.has_previous(),
				'has_next': pager.has_next(),
				'pages': pages,
				'pager_var': self.pager_var,
				'get_params': get_params
			}

			if self.var_name:
				context[self.var_name] = json.dumps(p)
				return ''
			else:
				t = template.loader.get_template(self.template_file)
				return t.render(template.Context({'pager': p}, autoescape=context.autoescape))

		except Exception, e:
			print e
