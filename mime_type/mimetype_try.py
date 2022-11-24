import mimetypes

import magic


def file_path_mime(file_path):
    mime=magic.from_file(file_path,mime=True)
    return mime

def check_in_memory_mime(in_memory_file):
    mime=magic.from_buffer(in_memory_file.read(),mime=True)
    return mime

# file_path_mime('/path/to/table_example.jpg')
# print(file_path_mime)

file_path_mime('path/to/a_file.jpg')
print(file_path_mime)

