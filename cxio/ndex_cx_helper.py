import time

from cxio.cx_writer import CxWriter
from cxio.element_maker import ElementMaker
from cxio.cx_constants import CxConstants


class NdexCXHelper:
    def __init__(self, output_stream):
        self.__contexts = {}
        self.__citation_id_counter = 0
        self.__support_id_counter = 0
        self.__edge_id_counter = 0
        self.__node_id_counter = 0
        self.__update_time = -1
        self.__cx_writer = CxWriter(output_stream)
        self.__aspect_names = ["@context", CxConstants.NODES, CxConstants.EDGES, CxConstants.NETWORK_ATTRIBUTES,
                               CxConstants.NODE_ATTRIBUTES, CxConstants.EDGE_ATTRIBUTES, CxConstants.CARTESIAN_LAYOUT,
                               "citations", "nodeCitations", "edgeCitations",
                               "nodeSupports", "edgeSupports", "provenanceHistory", "supports"]

    def get_cx_writer(self):
        return self.__cx_writer

    def start(self):
        self.__update_time = int(round(time.time() * 1000))
        self.__add_pre_metadata()
        self.__cx_writer.start()

    def end(self, success=True, error_msg=''):
        self.__add_post_metadata()
        self.__cx_writer.end(success, error_msg)

    def add_cx_context(self, prefix, uri):
        self.__contexts[prefix] = uri

    def emit_cx_context(self):
        self.__cx_writer.write_single_aspect_fragment(
            ElementMaker.create_ndex_context_element(self.__contexts))

    def emit_cx_node(self, node_name):
        self.__node_id_counter += 1
        self.__cx_writer.write_single_aspect_fragment(
            ElementMaker.create_nodes_aspect_element(self.__node_id_counter, node_name))
        return self.__node_id_counter

    def emit_cx_edge(self, source_id, target_id, interaction):
        self.__edge_id_counter += 1
        self.__cx_writer.write_single_aspect_fragment(
            ElementMaker.create_edges_aspect_element(self.__edge_id_counter, source_id,
                                                     target_id, interaction))
        return self.__edge_id_counter

    def emit_cx_node_attribute(self, node_id, name, value, data_type=None):
        self.__cx_writer.write_single_aspect_fragment(
            ElementMaker.create_node_attributes_aspect_element(None, node_id, name, value, data_type))

    def emit_cx_edge_attribute(self, edge_id, name, value, data_type=None):
        self.__cx_writer.write_single_aspect_fragment(
            ElementMaker.create_edge_attributes_aspect_element(None, edge_id, name, value, data_type))

    def emit_cx_network_attribute(self, sub_network_id, name, value, data_type=None):
        self.__cx_writer.write_single_aspect_fragment(
            ElementMaker.create_network_attributes_aspect_element(sub_network_id, name, value, data_type))

    def emit_cx_node_list_attribute(self, node_id, name, values, data_type):
        self.__cx_writer.write_single_aspect_fragment(
            ElementMaker.create_node_list_attributes_aspect_element(None, node_id, name, values, data_type))

    def emit_cx_edge_list_attribute(self, edge_id, name, values, data_type):
        self.__cx_writer.write_single_aspect_fragment(
            ElementMaker.create_edge_list_attributes_aspect_element(None, edge_id, name, values, data_type))

    def emit_cx_network_list_attribute(self, sub_network_id, name, values, data_type):
        self.__cx_writer.write_single_aspect_fragment(
            ElementMaker.create_network_list_attributes_aspect_element(sub_network_id, name, values, data_type))

    def emit_cx_cartesian_layout_element(self, node_id, view_id, x, y, z=None):
        self.__cx_writer.write_single_aspect_fragment(
            ElementMaker.create_cartesian_layout_element(node_id, view_id, x, y, z))

    def emit_cx_citation(self, citation_type, title, contributors, identifier, description):
        self.__citation_id_counter += 1
        self.__cx_writer.write_single_aspect_fragment(
            ElementMaker.create_ndex_citation_aspect_element(self.__citation_id_counter, citation_type, title,
                                                             contributors, identifier, description))
        return self.__citation_id_counter

    def emit_cx_support(self, cx_citation_id, text):
        self.__support_id_counter += 1
        self.__cx_writer.write_single_aspect_fragment(
            ElementMaker.create_ndex_support_aspect_element(self.__support_id_counter, cx_citation_id, text))
        return self.__support_id_counter

    def emit_cx_function_term(self, function_term):
        self.__cx_writer.write_single_aspect_fragment(
            ElementMaker.create_ndex_function_term_aspect_element(function_term))

    def emit_cx_node_citation(self, node_id, citation_id):
        self.__cx_writer.write_single_aspect_fragment(
            ElementMaker.create_ndex_node_citation_aspect_element(node_id, citation_id))

    def emit_cx_edge_citation(self, edge_id, citation_id):
        self.__cx_writer.write_single_aspect_fragment(
            ElementMaker.create_ndex_edge_citation_aspect_element(edge_id, citation_id))

    def emit_cx_node_support(self, node_id, support_id):
        self.__cx_writer.write_single_aspect_fragment(
            ElementMaker.create_ndex_node_support_aspect_element(node_id, support_id))

    def emit_cx_edge_support(self, edge_id, support_id):
        self.__cx_writer.write_single_aspect_fragment(
            ElementMaker.create_ndex_edge_support_aspect_element(edge_id, support_id))

    def __add_pre_metadata(self):
        pre_meta_data = []
        for aspect_name in self.__aspect_names:
            pre_meta_data.append(ElementMaker.create_pre_metadata_element(aspect_name, 1, '1.0', self.__update_time,
                                                                          [], 1))
        self.__cx_writer.add_pre_meta_data(pre_meta_data)

    def __add_post_metadata(self):
        post_meta_data = [
            ElementMaker.create_post_metadata_element('nodes', self.__node_id_counter),
            ElementMaker.create_post_metadata_element('edges', self.__edge_id_counter),
            ElementMaker.create_post_metadata_element('supports', self.__support_id_counter),
            ElementMaker.create_post_metadata_element('citations', self.__citation_id_counter)
        ]
        self.__cx_writer.add_post_meta_data(post_meta_data)