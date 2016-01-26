import sys

split = int(sys.argv[1])
file_name = sys.argv[2]
data = []

with open(file_name) as f:
    for l in f:
        data.append(l)

lines = int(len(data)/split)
if lines % split != 0:
    lines += 1

for cnt in range(split):
    cnt += 1
    f = open("result-%d.txt" % cnt, 'w')
    f.write(''.join(data[(lines-1)*(cnt-1):(lines-1)*cnt]))
    f.close()

