import io
from cxio.cx_reader import CxReader
from cxio.cx_writer import CxWriter
from cxio.aspect_element import AspectElement
from cxio.cx_constants import CxConstants
from cxio.element_maker import ElementMaker

import unittest


class MyTestCase(unittest.TestCase):

    def test_1(self):
        print('\n---------- cxio tests start -----------\n')

        node_0 = AspectElement(CxConstants.NODES, {"id": "_:0"})
        node_1 = AspectElement(CxConstants.NODES, {"id": "_:1"})

        nodes = []
        nodes.append(node_0)
        nodes.append(node_1)

        fo = io.StringIO()

        # Creating a CX writer
        w = CxWriter(fo)

        # Starting the json list
        w.start()

        w.start_aspect_fragment(CxConstants.NODES)

        w.write_aspect_element(node_0)
        w.write_aspect_element(node_1)

        w.end_aspect_fragment()

        w.end()

        #self.assertEqual()

    def test_2(self):
        n1 = ElementMaker.create_nodes_aspect_element(1, 'node 1', 'N1')
        n2 = ElementMaker.create_nodes_aspect_element(2, 'node 2', 'N2')
        e = ElementMaker.create_edges_aspect_element(3, 1, 2, '1->2')
        s = ElementMaker.create_status_element(True, "msg")
        nea = ElementMaker.create_network_attributes_aspect_element(1200, 'size', 12.3, CxConstants.DATA_TYPE_DOUBLE)
        noa = ElementMaker.create_node_attributes_aspect_element(1200, 1, 'weight', '12.0', CxConstants.DATA_TYPE_FLOAT)
        eda = ElementMaker.create_edge_attributes_aspect_element(1200, 3, 'length', 303.409883, CxConstants.DATA_TYPE_DOUBLE)

        print(str(n1))
        print(str(n2))
        print(str(e))
        print(str(s))
        print(str(nea))
        print(str(noa))
        print(str(eda))

if __name__ == '__main__':
    unittest.main()
