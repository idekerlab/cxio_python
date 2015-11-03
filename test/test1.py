import io
from cxio.cx_reader import CxReader
from cxio.cx_writer import CxWriter
from cxio.aspect_element import AspectElement
from cxio.cx_constants import CxConstants
from cxio.cx_util import CxUtil

import unittest


class MyTestCase(unittest.TestCase):

    def test_1(self):
        node_0 = AspectElement(CxConstants.NODES, {"id": "_:0"})
        node_1 = AspectElement(CxConstants.NODES, {"id": "_:1"})

        nodes = []
        nodes.append(node_0)
        nodes.append(node_1)

        fo = io.StringIO("")

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


if __name__ == '__main__':
    unittest.main()
