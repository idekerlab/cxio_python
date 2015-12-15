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

w.emit_cx_edge(1, 2, "1->2")

w.emit_cx_cartesian_layout_element(1, None, 20, 30)

w.emit_cx_cartesian_layout_element(1, None, -20, -30)

w.emit_cx_node_attribute(1, "node attribute 1", "value 1", CxConstants.DATA_TYPE_STRING)

w.emit_cx_node_attribute(2, "node attribute 2", "1293827302", CxConstants.DATA_TYPE_LONG)

w.emit_cx_edge_attribute(1, "edge attribute 1", "value 1", CxConstants.DATA_TYPE_STRING)

w.emit_cx_network_attribute(1, "size", "12", CxConstants.DATA_TYPE_INTEGER)

w.emit_cx_network_list_attribute(1, "expressions", ["12", "13"], CxConstants.DATA_TYPE_LIST_OF_INTEGER)

w.emit_cx_sub_networks(1200, [1, 2], [3, 4])

w.emit_cx_node_citation(1, 22)

w.emit_cx_edge_citation(2, 11)

w.emit_cx_node_support(1, 111)

w.emit_cx_edge_support(2, 222)

w.emit_cx_support(1, "bcl2 review")

w.emit_cx_citation("review", "bcl2 review", "John Reed", "123", "about bcl2")

w.emit_cx_function_term("function 1")

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
#     do something with e

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

for e in cx2[CxConstants.SUB_NETWORKS]:
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
