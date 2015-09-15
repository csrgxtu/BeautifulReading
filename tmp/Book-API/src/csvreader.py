import csv
import sys

f = open(sys.argv[1], 'rt')
mat = []
try:
    reader = csv.reader(f)
    index = 0
    for row in reader:
        mat.append(row)

finally:
    f.close()

newmat = []
for index in range(len(mat)):
    if (len(mat[index]) != 9):
        # print len(mat[index]),
        pass
    else:
        newmat.append(mat[index])

for item in newmat:
    item[8] = int(item[8])

newmat.sort(key=lambda x: x[8])
# print newmat[0: 5]
for item in newmat[-100:]:
    print item[0], item[2].decode('utf-8'), item[8]

# with open('100books.txt', 'w') as f:
#     for item in newmat[-100:]:
#         f.write(unicode(item[2]).decode('utf-8'))
#         f.write('\n')
#     f.close()
