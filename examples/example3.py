import io
from cxio.cx_reader import CxReader
from cxio.cx_constants import CxConstants
from cxio.ndex_cx_helper import NdexCXHelper


# -------
# WRITING
# -------

# Writing to a string pretending to be a file/stream
fo = io.StringIO("")

# Creating a NdexCXHelper
w = NdexCXHelper(fo)

w.add_cx_context("uni", "uniprot.org")
w.add_cx_context("ncbi", "ncbi.org")

w.start()

w.emit_cx_context()

w.emit_cx_node("node 1")
w.emit_cx_node("node 2")
w.emit_cx_node("node 3")

w.emit_cx_edge(1, 2, "1->2")
w.emit_cx_edge(2, 3, "2->3")
w.emit_cx_edge(1, 3, "1->3")

w.emit_cx_node("node 4")
w.emit_cx_edge(3, 4, "3->4")


w.emit_cx_cartesian_layout_element(1, None, 20, 30)

w.emit_cx_cartesian_layout_element(2, None, -20, -30)

w.emit_cx_node_attribute(1, "node attribute 1", "value 1", CxConstants.DATA_TYPE_STRING)

w.emit_cx_node_attribute(2, "node attribute 2", "1293827302", CxConstants.DATA_TYPE_LONG)

w.emit_cx_edge_attribute(1, "edge attribute 1", "value 1", CxConstants.DATA_TYPE_STRING)

w.emit_cx_network_attribute(1, "size", "12", CxConstants.DATA_TYPE_INTEGER)

w.emit_cx_network_attribute(1, "expressions", ["12", "13"], CxConstants.DATA_TYPE_LIST_OF_INTEGER)

w.emit_cx_hidden_attribute(1, "algorithm", "circular")

w.emit_cx_sub_networks(1200, [1, 2], [3, 4])

w.emit_cx_groups(22, 1200, 'group 1', [1], [3, 4], [2])

w.emit_cx_table_column(1200, 'nodes', 'weight', CxConstants.DATA_TYPE_DOUBLE)

w.emit_cx_network_relations(1200, 22, CxConstants.RELATIONSHIP_TYPE_VIEW, 'subnetwork one')

w.emit_cx_views(2000, 1200)

properties = {"NODE_BORDER_PAINT": "#CCCCCC",
              "NODE_BORDER_STROKE": "SOLID",
              "NODE_BORDER_TRANSPARENCY": "255"}
dependencies = {"nodeCustomGraphicsSizeSync": "true",
                "nodeSizeLocked": "false"}
mappings = {"NODE_LABEL": {
    "type": "PASSTHROUGH",
    "definition": "COL=name,T=string"}}

w.emit_cx_visual_properties(CxConstants.VP_PROPERTIES_OF_NODES_DEFAULT, 1, 2000, properties, dependencies, mappings)

w.emit_cx_node_citation(1, 11)
w.emit_cx_node_citation(2, 22)

w.emit_cx_edge_citation(2, 1100)

w.emit_cx_node_citation(3, 33)

w.emit_cx_node_support(1, 111)

w.emit_cx_edge_support(2, 222)

w.emit_cx_support(1, "bcl2 review")

w.emit_cx_citation("review", "bcl2 review", "John Reed", "123", "about bcl2")
w.emit_cx_citation("original", "bcl2 and bax", "John Reed", "400", "new")

w.emit_cx_function_term("function 1")
w.emit_cx_function_term("function 2")

w.emit_cx_cartesian_layout_element(3, None, -200, -300)

w.end()

# Printing out element counts written so far
for name, count in w.get_cx_writer().get_aspect_element_counts().items():
    print(name + ': ' + str(count))

print()
print()

# Printing to console
json_str = fo.getvalue()
print(json_str)

print()
print()

# -------
# READING
# -------
fi = io.StringIO(json_str)

cx_reader = CxReader(fi)

# Getting and printing pre meta data
print('pre meta data: ')
for e in cx_reader.get_pre_meta_data():
    print(e)

print()
print()

cx2 = cx_reader.parse_as_dictionary()
# Note: In real-world application, this would be used instead:
# for e in cx_reader.aspect_elements():
# do something with e

for e in cx2[CxConstants.NODES]:
    print(e)

for e in cx2[CxConstants.EDGES]:
    print(e)

for e in cx2[CxConstants.CARTESIAN_LAYOUT]:
    print(e)

for e in cx2[CxConstants.NODE_ATTRIBUTES]:
    print(e)

for e in cx2[CxConstants.EDGE_ATTRIBUTES]:
    print(e)

for e in cx2[CxConstants.NETWORK_ATTRIBUTES]:
    print(e)

for e in cx2[CxConstants.HIDDEN_ATTRIBUTES]:
    print(e)

for e in cx2[CxConstants.SUB_NETWORKS]:
    print(e)

for e in cx2[CxConstants.GROUPS]:
    print(e)

for e in cx2[CxConstants.NETWORK_RELATIONS]:
    print(e)

for e in cx2[CxConstants.VIEWS]:
    print(e)

for e in cx2[CxConstants.VISUAL_PROPERTIES]:
    print(e)

for e in cx2['nodeCitations']:
    print(e)

for e in cx2['edgeCitations']:
    print(e)

for e in cx2['nodeSupports']:
    print(e)

for e in cx2['edgeSupports']:
    print(e)

for e in cx2['supports']:
    print(e)

for e in cx2['citations']:
    print(e)

for e in cx2['functionTerms']:
    print(e)

print()
print()

# Getting and printing post meta data
print('post meta data:')
for e in cx_reader.get_post_meta_data():
    print(e)

print()
print()
print('OK')
