# Using readline()
file1 = open('f.txt', 'r')
count = 0
res=[]
temp = 0
 
while True:
    
    count += 1
 
    # Get next line from file
    line = file1.readline()
 
    # if line is empty
    # end of file is reached
    if not line:
        break
    # print("Line{}: {}".format(count, line.strip()))
    # print(str(line[24:27]))
    temp += float(line[24:28])
    if count == 12: 
        res.append(temp)
        count = 0
        temp = 0
 
file1.close() 

print(res)

# print(len(res))



import matplotlib.pyplot as plt
import numpy as np

xpoints = np.arange(len(res))
ypoints = np.array(res)
plt.xlabel(" Time ")
plt.ylabel("Resource Using Rate")

plt.plot(xpoints, ypoints,label="CPU")
plt.legend(loc="upper right")
plt.show()