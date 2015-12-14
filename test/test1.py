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

        # self.assertEqual()

    def test_2(self):
        e = ElementMaker.create_nodes_aspect_element(1, 'node 1', 'N1')
        self.assertEquals(e.get_name(), CxConstants.NODES)
        self.assertEquals(e.get_data()['n'], 'node 1')
        self.assertEquals(e.get_data()['@id'], 1)
        self.assertEquals(e.get_data()['r'], 'N1')

    def test_3(self):
        e = ElementMaker.create_edges_aspect_element(3, 1, 2, '1->2')
        self.assertEquals(e.get_name(), CxConstants.EDGES)
        self.assertEquals(e.get_data()['s'], 1)
        self.assertEquals(e.get_data()['t'], 2)
        self.assertEquals(e.get_data()['@id'], 3)
        self.assertEquals(e.get_data()['i'], '1->2')

    def test_4(self):
        e = ElementMaker.create_status_element(True, "msg")
        self.assertEquals(e.get_name(), CxConstants.STATUS)
        d = e.get_data()[0]
        self.assertEquals(d['success'], True)
        self.assertEquals(d['error'], 'msg')

    def test_5(self):
        e = ElementMaker.create_network_attributes_aspect_element(1200, 'size', 12.3, CxConstants.DATA_TYPE_DOUBLE)
        self.assertEquals(e.get_name(), CxConstants.NETWORK_ATTRIBUTES)
        d = e.get_data()
        self.assertEquals(d['s'], 1200)
        self.assertEquals(d['n'], 'size')
        self.assertEquals(d['v'], '12.3')
        self.assertEquals(d['d'], CxConstants.DATA_TYPE_DOUBLE)

    def test_6(self):
        e = ElementMaker.create_node_attributes_aspect_element(1200, 1, 'weight', '12.0', CxConstants.DATA_TYPE_FLOAT)
        self.assertEquals(e.get_name(), CxConstants.NODE_ATTRIBUTES)
        d = e.get_data()
        self.assertEquals(d['s'], 1200)
        self.assertEquals(d['po'], 1)
        self.assertEquals(d['n'], 'weight')
        self.assertEquals(d['v'], '12.0')
        self.assertEquals(d['d'], CxConstants.DATA_TYPE_FLOAT)

    def test_7(self):
        e = ElementMaker.create_edge_attributes_aspect_element(1200, 3, 'length', 303.409883,
                                                               CxConstants.DATA_TYPE_DOUBLE)
        self.assertEquals(e.get_name(), CxConstants.EDGE_ATTRIBUTES)
        d = e.get_data()
        self.assertEquals(d['s'], 1200)
        self.assertEquals(d['po'], 3)
        self.assertEquals(d['n'], 'length')
        self.assertEquals(d['v'], '303.409883')
        self.assertEquals(d['d'], CxConstants.DATA_TYPE_DOUBLE)

    def test_8(self):
        e = ElementMaker.create_network_list_attributes_aspect_element(1200, 'used', [True, False],
                                                                       CxConstants.DATA_TYPE_LIST_OF_BOOLEAN)
        self.assertEquals(e.get_name(), CxConstants.NETWORK_ATTRIBUTES)
        d = e.get_data()
        self.assertEquals(d['s'], 1200)
        self.assertEquals(d['n'], 'used')
        self.assertEquals(str(d['v']), '[True, False]')
        self.assertEquals(d['d'], CxConstants.DATA_TYPE_LIST_OF_BOOLEAN)

    def test_9(self):
        e = ElementMaker.create_node_list_attributes_aspect_element(1200, 1, 'weights', ['1.1', '2.2'],
                                                                    CxConstants.DATA_TYPE_LIST_OF_FLOAT)
        self.assertEquals(e.get_name(), CxConstants.NODE_ATTRIBUTES)
        d = e.get_data()
        self.assertEquals(d['s'], 1200)
        self.assertEquals(d['po'], 1)
        self.assertEquals(d['n'], 'weights')
        self.assertEquals(str(d['v']), "['1.1', '2.2']")
        self.assertEquals(d['d'], CxConstants.DATA_TYPE_LIST_OF_FLOAT)

    def test_10(self):
        e = ElementMaker.create_edge_list_attributes_aspect_element(1200, 3, 'lengths', ['23.3', '13.34'],
                                                                    CxConstants.DATA_TYPE_LIST_OF_DOUBLE)
        self.assertEquals(e.get_name(), CxConstants.EDGE_ATTRIBUTES)
        d = e.get_data()
        self.assertEquals(d['s'], 1200)
        self.assertEquals(d['po'], 3)
        self.assertEquals(d['n'], 'lengths')
        self.assertEquals(str(d['v']), "['23.3', '13.34']")
        self.assertEquals(d['d'], CxConstants.DATA_TYPE_LIST_OF_DOUBLE)

    def test_11(self):
        e = ElementMaker.create_cartesian_layout_element(1, 1200, 1.11, 2.22, 3.33)
        self.assertEquals(e.get_name(), CxConstants.CARTESIAN_LAYOUT)
        d = e.get_data()
        self.assertEquals(d['view'], 1200)
        self.assertEquals(d['node'], 1)
        self.assertEquals(d['x'], 1.11)
        self.assertEquals(d['y'], 2.22)
        self.assertEquals(d['z'], 3.33)

    def test_x(self):
        n1 = ElementMaker.create_nodes_aspect_element(1, 'node 1', 'N1')
        n2 = ElementMaker.create_nodes_aspect_element(2, 'node 2', 'N2')
        e = ElementMaker.create_edges_aspect_element(3, 1, 2, '1->2')
        nea = ElementMaker.create_network_attributes_aspect_element(1200, 'size', 12.3, CxConstants.DATA_TYPE_DOUBLE)
        noa = ElementMaker.create_node_attributes_aspect_element(1200, 1, 'weight', '12.0', CxConstants.DATA_TYPE_FLOAT)
        eda = ElementMaker.create_edge_attributes_aspect_element(1200, 3, 'length', 303.409883,
                                                                 CxConstants.DATA_TYPE_DOUBLE)
        neal = ElementMaker.create_network_list_attributes_aspect_element(1200, 'used', [True, False],
                                                                          CxConstants.DATA_TYPE_LIST_OF_BOOLEAN)
        noal = ElementMaker.create_node_list_attributes_aspect_element(1200, 1, 'weights', ['1.1', '2.2'],
                                                                       CxConstants.DATA_TYPE_LIST_OF_FLOAT)
        edal = ElementMaker.create_edge_list_attributes_aspect_element(1200, 3, 'lengths', ['23.3', '13.34'],
                                                                       CxConstants.DATA_TYPE_LIST_OF_DOUBLE)
        c1 = ElementMaker.create_cartesian_layout_element(1, 1200, 1.11, 2.22, 3.33)
        c2 = ElementMaker.create_cartesian_layout_element(2, 1200, -1.11, -2.22)

        fo = io.StringIO('')

        # Creating a CX writer
        w = CxWriter(fo)

        # Starting the json list
        w.start()

        w.start_aspect_fragment(CxConstants.NODES)
        w.write_aspect_element(n1)
        w.write_aspect_element(n2)
        w.end_aspect_fragment()

        w.start_aspect_fragment(CxConstants.EDGES)
        w.write_aspect_element(e)
        w.end_aspect_fragment()

        w.start_aspect_fragment(CxConstants.CARTESIAN_LAYOUT)
        w.write_aspect_element(c1)
        w.write_aspect_element(c2)
        w.end_aspect_fragment()

        w.start_aspect_fragment(CxConstants.NETWORK_ATTRIBUTES)
        w.write_aspect_element(nea)
        w.write_aspect_element(neal)
        w.end_aspect_fragment()

        w.start_aspect_fragment(CxConstants.NODE_ATTRIBUTES)
        w.write_aspect_element(noa)
        w.write_aspect_element(noal)
        w.end_aspect_fragment()

        w.start_aspect_fragment(CxConstants.EDGE_ATTRIBUTES)
        w.write_aspect_element(eda)
        w.write_aspect_element(edal)
        w.end_aspect_fragment()

        w.end(True, "no error")

        json_str = fo.getvalue()
        print(json_str)

        # READING
        # -------
        fi = io.StringIO(json_str)

        cx_reader = CxReader(fi)

        # for e in cx_reader2.get_pre_meta_data():

        cx = cx_reader.parse_as_dictionary()

        self.assertEquals(len(cx[CxConstants.NODES]), 2)
        self.assertEquals(len(cx[CxConstants.EDGES]), 1)
        self.assertEquals(len(cx[CxConstants.CARTESIAN_LAYOUT]), 2)
        self.assertEquals(len(cx[CxConstants.NODE_ATTRIBUTES]), 2)
        self.assertEquals(len(cx[CxConstants.EDGE_ATTRIBUTES]), 2)
        self.assertEquals(len(cx[CxConstants.NETWORK_ATTRIBUTES]), 2)

        # for e in cx_reader2.get_post_meta_data():


if __name__ == '__main__':
    unittest.main()
