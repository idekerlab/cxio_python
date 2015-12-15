import io
from cxio.cx_reader import CxReader
from cxio.cx_writer import CxWriter
from cxio.cx_constants import CxConstants
from cxio.element_maker import ElementMaker

import unittest


class MyTestCase(unittest.TestCase):
    def test_1(self):
        print('\n---------- cxio tests start -----------\n')



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

    def test_12(self):
        e = ElementMaker.create_pre_metadata_element('nodes', 1, 'v2.2', 123, [], 456)
        self.assertEquals(e.get_name(), CxConstants.META_DATA)
        d = e.get_data()
        self.assertEquals(d['name'], 'nodes')
        self.assertEquals(d['version'], 'v2.2')
        self.assertEquals(d['idCounter'], 456)
        self.assertEquals(d['properties'], [])
        self.assertEquals(d['lastUpdate'], 123)
        self.assertEquals(d['consistencyGroup'], 1)

    def test_13(self):
        e = ElementMaker.create_post_metadata_element('nodes', 456)
        self.assertEquals(e.get_name(), CxConstants.META_DATA)
        d = e.get_data()
        self.assertEquals(d['name'], 'nodes')
        self.assertEquals(d['idCounter'], 456)

    def test_14(self):
        e = ElementMaker.create_sub_networks_aspect_element(1200, [1, 2], [3])
        self.assertEquals(e.get_name(), CxConstants.SUB_NETWORKS)
        d = e.get_data()
        self.assertEquals(d['@id'], 1200)
        self.assertEquals(d['nodes'][0], 1)
        self.assertEquals(d['nodes'][1], 2)
        self.assertEquals(d['edges'][0], 3)

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
        sn = ElementMaker.create_sub_networks_aspect_element(1200, [1, 2], [3])

        prmd = ElementMaker.create_pre_metadata_element('nodes', 1, 'v2.2', 1234567, [], 2)
        pomd1 = ElementMaker.create_post_metadata_element('nodes', 2)
        pomd2 = ElementMaker.create_post_metadata_element('edges', 1)

        fo = io.StringIO('')

        w = CxWriter(fo)

        w.add_pre_meta_data([prmd])

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

        w.start_aspect_fragment(CxConstants.SUB_NETWORKS)
        w.write_aspect_element(sn)
        w.end_aspect_fragment()

        w.add_post_meta_data([pomd1, pomd2])

        w.end(True, "no error")

        json_str = fo.getvalue()
        print(json_str)

        # READING

        fi = io.StringIO(json_str)

        cx_reader = CxReader(fi)

        self.assertEquals(len(cx_reader.get_pre_meta_data()), 1)

        cx = cx_reader.parse_as_dictionary()

        self.assertEquals(cx_reader.get_error_msg(), "no error")
        self.assertEquals(cx_reader.get_is_success(), True)

        self.assertEquals(len(cx_reader.get_post_meta_data()), 2)

        self.assertEquals(len(cx[CxConstants.NODES]), 2)
        self.assertEquals(len(cx[CxConstants.EDGES]), 1)
        self.assertEquals(len(cx[CxConstants.CARTESIAN_LAYOUT]), 2)
        self.assertEquals(len(cx[CxConstants.NODE_ATTRIBUTES]), 2)
        self.assertEquals(len(cx[CxConstants.EDGE_ATTRIBUTES]), 2)
        self.assertEquals(len(cx[CxConstants.NETWORK_ATTRIBUTES]), 2)
        self.assertEquals(len(cx[CxConstants.SUB_NETWORKS]), 1)



if __name__ == '__main__':
    unittest.main()
