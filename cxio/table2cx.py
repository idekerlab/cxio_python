import sys
import re
import os.path
import time
from cxio.cx_writer import CxWriter
from cxio.cx_constants import CxConstants
from cxio.element_maker import ElementMaker

SEP = re.compile('[\s,]+')

UPDATE_TIME = int(round(time.time() * 1000))
ASPECT_VERSION = "1.0"
ASPECT_CONSISTENCY_GROUP = 1

if len(sys.argv) != 3:
    print()
    print('usage: table2cx <infile> <outfile>')
    print()
    sys.exit(1)

fi_name = sys.argv[1]
fo_name = sys.argv[2]

if not os.path.isfile(fi_name):
    print()
    print('infile "' + fi_name + '" does not exist')
    print()
    sys.exit(1)

if os.path.exists(fo_name):
    print()
    print('outfile "' + fo_name + '" already exists')
    print()
    sys.exit(1)

fi = open(fi_name, 'r')
fo = open(fo_name, 'w')

print('Infile : ' + str(fi.name))
print('Outfile: ' + str(fo.name))
print()

id_nn = {}
nn_id = {}
edges = []
edge_count = 0
node_count = 0
with fi as lines:
    for line in lines:
        l = SEP.split(line)
        if len(l) > 2:
            n1 = l[0]
            n2 = l[1]
            interaction = l[2]
            if n1 not in nn_id:
                nn_id[n1] = node_count
                id_nn[node_count] = n1
                node_count += 1
            if n2 not in nn_id:
                nn_id[n2] = node_count
                id_nn[node_count] = n2
                node_count += 1
            edges.append(ElementMaker.create_edges_aspect_element(edge_count, nn_id[n1], nn_id[n2], interaction))
            edge_count += 1

w = CxWriter(fo)

w.set_pretty_formatting(True)

id_count = node_count + edge_count + 1

w.add_pre_meta_data(ElementMaker.create_pre_metadata_element(CxConstants.NODES, ASPECT_CONSISTENCY_GROUP,
                                                             ASPECT_VERSION, UPDATE_TIME, [], id_count,
                                                             len(id_nn)))
w.add_pre_meta_data(ElementMaker.create_pre_metadata_element(CxConstants.EDGES, ASPECT_CONSISTENCY_GROUP,
                                                             ASPECT_VERSION, UPDATE_TIME, [], id_count,
                                                             len(edges)))

w.start()
w.start_aspect_fragment(CxConstants.NODES)
for node_id, nn in id_nn.items():
    w.write_aspect_element(ElementMaker.create_nodes_aspect_element(node_id, nn))
w.end_aspect_fragment()
w.write_aspect_fragment(edges)
w.end()

print('Aspect elements written: ')
for name, count in w.get_aspect_element_counts().items():
    print(name + ': ' + str(count))

print()
print('OK')



