import time
from cxio.element import Element
from cxio.aspect_element import AspectElement
from cxio.cx_constants import CxConstants
from cxio.aspect_element import AspectElement
from cxio.cx_reader import CxReader
from cxio.cx_writer import CxWriter
from cxio.cx_constants import CxConstants
from cxio.cx_util import CxUtil
from cxio.element_maker import ElementMaker


class NdexCXHelper:
    def __init__(self, output_stream):
        self.out = output_stream
        self.contexts = {}
        self.citation_id_counter = 0
        self.support_id_counter = 0
        self.edge_id_counter = 0
        self.node_id_counter = 0
        self.update_time = -1
        self.cx_writer = CxWriter(output_stream)
        self.aspect_names = ["@context", "citations", "edgeAttributes",
                             "edgeCitations", "edgeSupports", "edges",
                             "networkAttributes", "nodeAttributes", "nodeCitations",
                             "nodeSupports", "nodes", "provenanceHistory", "supports"]

    def start(self):
        self.update_time = int(round(time.time() * 1000))
        self.cx_writer.start()

    def end(self):
        self.cx_writer.end()

    def add_cx_context(self, prefix, uri):
        self.contexts[prefix] = uri


    def emit_post_metadata(self):
        aspect_meta_data = [
            {"name": "nodes",
             "idCounter": self.node_id_counter},
            {"name": "edges",
             "idCounter": self.edge_id_counter},
            {"name": "supports",
             "idCounter": self.support_id_counter},
            {"name": "citations",
             "idCounter": self.citation_id_counter},
        ]
        self.emit({'metaData': aspect_meta_data})

    def emit_cx_fragment(self, aspect_name, body):
        self.emit({aspect_name: [body]})

    def emit_cx_context(self):
        self.emit_cx_fragment('@context', self.contexts)

    def emit_cx_citation(self, citation_type, title, contributors, identifier, description):
        self.citation_id_counter += 1
        self.emit_cx_fragment(
            'citations', {
                '@id': self.citation_id_counter,
                'dc:title': title,
                'dc:contributor': contributors,
                'dc:identifier': identifier,
                'dc:type': citation_type,
                'dc:description': description,
                'attributes': []
            })
        return self.citation_id_counter

    def emit_cx_support(self, cx_citation_id, text):
        self.support_id_counter += 1
        self.emit_cx_fragment(
            'supports', {
                '@id': self.support_id_counter,
                'citation': cx_citation_id,
                'text': text,
                'attributes': []
            })
        return self.support_id_counter

    def emit_cx_edge(self, source_id, target_id, interaction):
        self.edge_id_counter += 1
        self.cx_writer.write_single_aspect_fragment(
            ElementMaker.create_edges_aspect_element(self.edge_id_counter, source_id,
                                                     target_id, interaction))
        return self.edge_id_counter

    def emit_cx_edge_attribute(self, edge_id, name, value):
        self.cx_writer.write_single_aspect_fragment(
            ElementMaker.create_edges_attribute_aspect_element(edge_id, name, value))

    def emit_cx_node(self, node_name):
        self.node_id_counter += 1
        self.cx_writer.write_single_aspect_fragment(
            ElementMaker.create_nodes_aspect_element(self.node_id_counter, node_name))
        return self.node_id_counter

    def emit_cx_node_attribute(self, node_id, name, value, att_type=None):
        self.cx_writer.write_single_aspect_fragment(
            ElementMaker.create_nodes_attribute_aspect_element(node_id, name, value, att_type))

    def emit_cx_function_term(self, function_term):
        self.emit_cx_fragment('functionTerms', function_term)

    def emit_cx_node_citation(self, node_id, citation_id):
        self.emit_cx_fragment(
            'nodeCitations',
            {
                "citations": [citation_id],
                "po": [node_id]
            }
        )

    def emit_cx_edge_citation(self, edge_id, citation_id):
        self.emit_cx_fragment(
            'edgeCitations', {
                "citations": [citation_id],
                "po": [edge_id]
            }
        )

    def emit_cx_node_support(self, node_id, support_id):
        self.emit_cx_fragment(
            'nodeSupports',
            {
                "supports": [support_id],
                "po": [node_id]
            }
        )

    def emit_cx_edge_support(self, edge_id, support_id):
        self.emit_cx_fragment(
            'edgeSupports',
            {
                "supports": [support_id],
                "po": [edge_id]
            }
        )