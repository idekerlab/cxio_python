import sys
import os.path
from cxio.cx_reader import CxReader
from cxio.cx_writer import CxWriter


if len(sys.argv) != 3:
    print()
    print('usage: cx2cx <infile> <outfile>')
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

r = CxReader(fi)

cx = r.parse_as_dictionary()

w = CxWriter(fo)

w.set_pretty_formatting(True)

w.add_pre_meta_data(r.get_pre_meta_data())
w.add_post_meta_data(r.get_post_meta_data())

w.start()
for name, fragment in cx.items():
    w.write_aspect_fragment(fragment)
w.end()

print('Aspect elements written: ')
for name, count in w.get_aspect_element_counts().items():
    print(name + ': ' + str(count))

print()
print('OK')



