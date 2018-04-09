# with open('newfile.csv','w') as writer:
#     for d in data:
#         d=[i for i in d if str(i).isdigit()]
#         string = str(d)
#         writer.write(string+'\n')
import re

pattern = r"^103\.235\.252\.([0-9]|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])$"
reg = re.compile(pattern)

data = []
with open('tracefile3.txt') as reader:
    for index, line in enumerate(reader):
        d = line.split()
        if d and d[0].isdigit() and reg.match(d[-1]):
            data.append(d[1:])
print(data)
Datasets = []
for d in data:
    for i in range(len(d)):
        if d[i].isdigit():
            Datasets.append(int(d[i]))
Datasets = sorted(Datasets)
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
plt.show()

