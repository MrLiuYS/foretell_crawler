# -*-coding:utf-8 -*-
from oss2.crc64_combine import xrange

f = open("西拉.txt", "rb")
n = f.read()
f.close()
m = n.decode().split("\n")
print("---------------------m=",m)
m1 = []
for i in xrange(len(m)):
    if not m[i] in m1:
        m1.append(m[i])
# print("m1=", m1)
filename = open("1.0.txt", "wb")

for i in xrange(len(m1)):
    with open("1.0.txt", 'a+') as f:
        print("正在写入：", m1[i])
        f.write(m1[i] + '\n')


# for i in xrange(len(m1)):
#     print("++++++++++++++++m=", m1[i])
#     filename.write(m1[i])