#Weather Chart Demo

import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8,9,10]
y=[50,51,53,55,56,57,58,60,70,63]

#  format strings in plot function
#plt.plot(x,y,color='green',linewidth=5,linestyle='dotted')
#plt.plot(x,y,'r+') # g+ ---> red color & line style is +
#plt.plot(x,y,color='red',marker='D',linestyle='',markersize=20)
plt.plot(x,y,color='green',alpha=0.2)
plt.xlabel('Day')
plt.ylabel('Temprature')
plt.title('Weather')
plt.show()