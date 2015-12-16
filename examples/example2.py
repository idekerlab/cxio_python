import io
from cxio.aspect_element import AspectElement
from cxio.cx_reader import CxReader
from cxio.cx_writer import CxWriter
from cxio.cx_constants import CxConstants
from cxio.cx_util import CxUtil

fi = open('example_data/example0.cx', 'r')


# READING
# -------

# Creating a CX reader
cx_reader = CxReader(fi)

# Getting and printing pre meta data
for e in cx_reader.get_pre_meta_data():
    print(e)

# Read everything into one (huge) dictionary
cx = cx_reader.parse_as_dictionary()

# Getting and printing select aspects from the dictionary
for e in cx[CxConstants.NODES]:
    print(e)

for e in cx[CxConstants.EDGES]:
    print(e)

for e in cx[CxConstants.VISUAL_PROPERTIES]:
    print(e)

for e in cx[CxConstants.CARTESIAN_LAYOUT]:
    print(e)

for e in cx_reader.get_post_meta_data():
    print(e)

print()
print()

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

# Writing select aspects

w.write_aspect_fragment(cx[CxConstants.NODES])

w.write_aspect_fragment(cx[CxConstants.EDGES])

w.write_aspect_fragment(cx[CxConstants.VISUAL_PROPERTIES])

w.write_aspect_fragment(cx[CxConstants.CARTESIAN_LAYOUT])

# Adding post meta data
w.add_post_meta_data(cx_reader.get_post_meta_data())

# Printing out element counts written so far
for name, count in w.get_aspect_element_counts().items():
    print(name + ': ' + str(count))

print()
print()

# Adding element counts as post meta data
post = AspectElement(CxConstants.META_DATA, w.get_aspect_element_counts())
w.add_post_meta_data(post)

# Ending the json list
w.end()

# Printing to console
json_str = fo.getvalue()
print(json_str)

print()
print()

# READING (again)
# --------------
fi2 = io.StringIO(json_str)

cx_reader2 = CxReader(fi2)

# Getting and printing pre meta data
print('pre meta data: ')
for e in cx_reader2.get_pre_meta_data():
    print(e)

print()
print()

cx2 = cx_reader2.parse_as_dictionary()
# Note: In real-world application, this would be used instead:
# for e in cx_reader2.aspect_elements():
#     do something with e

for e in cx2[CxConstants.NODES]:
    print(e)

for e in cx2[CxConstants.EDGES]:
    print(e)

for e in cx2[CxConstants.VISUAL_PROPERTIES]:
    print(e)

for e in cx2[CxConstants.CARTESIAN_LAYOUT]:
    print(e)

print()
print()

# Getting and printing post meta data
print('post meta data:')
for e in cx_reader2.get_post_meta_data():
    print(e)

print()
print()
print('OK')
