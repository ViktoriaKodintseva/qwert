import xml.etree.ElementTree as ET

from programy.parser.template.nodes.base import TemplateNode
from programy.parser.template.nodes.tuple import TemplateTupleNode

from test.parser.template.graph_tests.graph_test_client import TemplateGraphTestClient

class TemplateGraphTupleTests(TemplateGraphTestClient):

     def test_tuple_simple(self):
        template = ET.fromstring("""
			<template>
			    <tuple></tuple>
			</template>
			""")

        ast = self.parser.parse_template_expression(template)
        self.assertIsNotNone(ast)

        self.assertIsInstance(ast, TemplateNode)
        self.assertIsNotNone(ast.children)
        self.assertIsNotNone(ast.children[0])
        self.assertIsInstance(ast.children[0], TemplateTupleNode)
        self.assertEqual(0, len(ast.children[0].children))