# import struct
#
# res = struct.pack('i', 1234567777)
# print(res,type(res),len(res))
# res_1 = struct.unpack('i',res)[0]
# print(res_1, type(res_1))

name = 'get 1.png'
res, file_name = name.split()
print(res)
print(file_name)