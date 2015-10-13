from cxio.cx_reader import CxReader
from cxio.cx_writer import CxWriter
import io
from cxio.cx_constants import CxConstants

fi = open('/Users/cmzmasek/WORK/PROG/PYTHON/CXIO/cxio/example_data/example0.cx', 'r')

# READING
# -------

# Creating a CX reader
cx_reader = CxReader(fi)

# Getting and printin pre meta data
for e in cx_reader.get_pre_meta_data():
    print(e)

# Read everything into one (huge) dictionary
cx = cx_reader.parse_as_dictionary()

# Getting various aspects from the dictionary
for e in cx[CxConstants.NODES]:
    print(e)

for e in cx[CxConstants.EDGES]:
    print(e)

for e in cx[CxConstants.CARTESIAN_LAYOUT]:
    print(e)

for e in cx[CxConstants.EDGE_ATTRIBUTES]:
    print(e)

for e in cx_reader.get_post_meta_data():
    print(e)


# WRITING
# -------

# Writing to a string pretending to be a file/stream
fo = io.StringIO("")

# Creating a CX writer
w = CxWriter(fo)

# Adding pre meta data
w.add_pre_meta_data(cx_reader.get_pre_meta_data())

# Starting the json list
w.start()

# Writing various aspects
w.start_aspect_fragment(CxConstants.NODES)
for e in cx[CxConstants.NODES]:
    w.write_aspect_element(e)
w.end_aspect_fragment()

w.start_aspect_fragment(CxConstants.EDGES)
for e in cx[CxConstants.EDGES]:
    w.write_aspect_element(e)
w.end_aspect_fragment()

w.start_aspect_fragment(CxConstants.CARTESIAN_LAYOUT)
for e in cx[CxConstants.CARTESIAN_LAYOUT]:
    w.write_aspect_element(e)
w.end_aspect_fragment()

w.start_aspect_fragment(CxConstants.EDGE_ATTRIBUTES)
for e in cx[CxConstants.EDGE_ATTRIBUTES]:
    w.write_aspect_element(e)
w.end_aspect_fragment()

# Ending the json list
w.end()

# Printing to console
json_str = fo.getvalue()
print(json_str)


# READING
# -------
fi2 = io.StringIO(json_str)
cx_reader2 = CxReader(fi2)
cx2 = cx_reader2.parse_as_dictionary()

for e in cx2[CxConstants.NODES]:
    print(e)

for e in cx2[CxConstants.EDGES]:
    print(e)

for e in cx2[CxConstants.CARTESIAN_LAYOUT]:
    print(e)

for e in cx2[CxConstants.EDGE_ATTRIBUTES]:
    print(e)

