"""
Created by catleer on 2018-05-21.
"""
__author__ = 'catleer'

import base64
import gzip


# with open('basefile', 'rb') as f:
#     content = f.read()
#     print(content)
#     print(len(content))
#     contents = content.split(b'/')
#     print(contents)
#     with open('afterfile.tar.gz', 'wb') as af:
#         for content in contents:
#             if len(content) % 4 !=0:
#                 a = len(content) % 4
#                 print(a)
#                 content = content + b'='*(4-a)
#             print(content)
#
#             afbase = base64.decodebytes(content)
#             af.write(afbase)

by = '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'
by = by.encode(encoding='ISO-8859-1')
print("by:", type(by))
print(len(by))
af = base64.b64decode(by)
print(af)
# print(type(af))
print(af.decode())

strr = '你好'.encode(encoding='utf-8')
# print(base64.b64encode(strr))
#
ree = b'5L2g5aW9'
print(type(base64.b64decode(ree)))

# import gzip
# b = gzip.decompress(base64.b64decode(ree))