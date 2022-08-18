# Using readline()
file1 = open('test.txt', 'r')
count = 0
res=[]
temp = 0

x_max = 0
y_max = 0
res_max = 0
pre = 0
x_start = 0
y_start = 0
x_flag = 0
 
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
    temp = float(line[24:28])
    print(temp)

    if temp <= 10 and (temp-pre)< temp*0.05 and x_flag == 0 and count > 30: 
        x_start  = count
        y_start = temp
        x_flag = 1

    # if count == 1: 
    #     res.append(temp)
    #     count = 0
    #     temp = 0
    res.append(temp)
    if temp > res_max: 
        res_max = temp 
        x_max = count
        y_max = temp 
    if count%5 ==0:
        pre = temp
    

 
file1.close() 

print(res)

# print(len(res))



import matplotlib.pyplot as plt
import numpy as np

xpoints = np.arange(x_start)
ypoints = np.array(res[0:x_start])
x1points = np.arange(x_start, len(res))
y1points = np.array(res[x_start:])

xlabels = np.arange(x_start)
ylabels = np.ones(x_start)*(-5)

x1labels = np.arange(x_start, len(res))
y1labels = np.ones(len(res)-x_start)*(-5)

plt.xlabel(" Time ")
plt.ylabel("Resource Using Rate")

plt.plot(xpoints, ypoints,'b',label="CPU")
plt.plot(x1points, y1points,'r', label = "CPU")
plt.plot(xlabels, ylabels,'b')
plt.plot(x1labels, y1labels,'r')
plt.legend(loc="upper right")

plt.annotate('Max point', xy=(x_max, y_max), xytext=(18, 210),
             arrowprops=dict(facecolor='black', shrink=0.1),
             )

plt.annotate('Turning point', xy=(x_start, y_start), xytext=(60, 170),
             arrowprops=dict(facecolor='red', shrink=0.1),
             )

# ax=plt.axes([0.1, 0.1, 0.8, 0.7])
an1 = plt.annotate("Training", xy=(30, -5), xycoords="data",
                  va="center", ha="center",
                  bbox=dict(boxstyle="round", fc="w"))

an2 = plt.annotate("Post Training", xy=(80, -5), xycoords="data",
                  va="center", ha="center",
                  bbox=dict(boxstyle="round", fc="w"))
plt.show()