import re

reg = re.compile(r';; ANSWER SECTION:')
reg2 = re.compile(r';; ADDITIONAL SECTION:')
d = []
with open('clin.txt','r') as f:
    for line in f.readlines():
        if reg.match(line):
            d.append(1)
        elif reg2.match(line):
            d.append(0)
print(d)
index = []
for i in range(len(d)):
    if d[i] == 1:
        index.append(i)
print(index)

data = []
for i in range(1,len(index)):
    if (index[i]-index[i-1] > 1):
        data.append(index[i]-index[i-1]-1)

Datasets = sorted([int(i) for i in data])
print(Datasets)
import matplotlib.pyplot as plt

plotDataset = [[],[]]
count = len(Datasets)
for i in range(count):
    plotDataset[0].append(float(Datasets[i]))
    plotDataset[1].append((i+1)/count)

plt.plot(plotDataset[0], plotDataset[1], '-', linewidth=2)
plt.xlabel('delay values')
plt.ylabel('probability')
plt.savefig('hw2.jpg')
plt.show()



