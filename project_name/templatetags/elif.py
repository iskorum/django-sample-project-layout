from django.template import Library
from django.template import Node, VariableDoesNotExist
from django.template.defaulttags import TemplateIfParser

register = Library()


class IfBranch(object):
	def __init__(self, var, node_list):
		self.var = var
		self.node_list = node_list


class IfNode(Node):
	def __init__(self, branches):
		self.branches = branches

	def __repr__(self):
		return "<If node>"

	def __iter__(self):
		for n in self.branches:
			for node in n:
				yield node

	def render(self, context):
		for n in self.branches:
			var = n.var
			if var != True:
				try:
					var = var.eval(context)
				except VariableDoesNotExist:
					var = None
			if var:
				return n.node_list.render(context)
				break
		return ""


def do_if(parser, token):
	class Enders(list):
		def __contains__(self, val):
			return val.startswith('elif') or val in ('else', 'endif')

	enders = Enders()
	branches = []

	while True:
		contents = token.split_contents()
		bits = contents[1:]
		if contents[0] in ("if", "elif"):
			var = TemplateIfParser(parser, bits).parse()
			nodelist = parser.parse(enders)
			next_token = parser.next_token()
			branches.append(IfBranch(var, nodelist))
			token = next_token
		elif token.contents == 'else':
			nodelist = parser.parse(('endif',))
			parser.delete_first_token()
			branches.append(IfBranch(True, nodelist))
			break
		elif token.contents == 'endif':
			break

	return IfNode(branches)

do_if = register.tag("if", do_if)