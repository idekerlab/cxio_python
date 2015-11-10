from cxio.cx_reader import CxReader
from os.path import join, abspath, dirname

current_directory = dirname(abspath(__file__))
example_data_path = join(current_directory, "example_data/example0.cx")
# print "example_data_path = " + example_data_path
fi = open(example_data_path, 'r')

# Creating a new CX reader
cx_reader = CxReader(fi)

# Getting and printing pre meta data
print('pre meta data: ')
for e in cx_reader.get_pre_meta_data():
    print(e)

print()
print()

# Going through aspect elements (implemented as AspectElement)
for e in cx_reader.aspect_elements():
    print(e)

print()
print()

# Getting and printing post meta data
print('post meta data:')
for e in cx_reader.get_post_meta_data():
    print(e)

print()
print()

# Getting element counts
for name, count in cx_reader.get_aspect_element_counts().items():
    print(name + ': ' + str(count))

print()
print()
print('OK')

