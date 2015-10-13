from cxio.cx_reader import CxReader

fi = open('/Users/cmzmasek/WORK/PROG/PYTHON/CXIO/cxio/example_data/example0.cx', 'r')

# Creating a new CX reader
cx_reader = CxReader(fi)

# Getting pre meta data
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

print('post meta data:')
for e in cx_reader.get_post_meta_data():
    print(e)

print()
print()
print('OK')

