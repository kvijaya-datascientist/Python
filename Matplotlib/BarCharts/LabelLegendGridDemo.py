# Axes labels , Legend , Grid

import matplotlib.pyplot as plt
days=[1,2,3,4,5,6,7]
max_t=[50,51,52,53,54,55,56]
min_t =[43,42,40,44,33,35,37]
avg_t =[45,48,48,46,40,42,41]
plt.plot(days,max_t,label='Max Temp')
plt.plot(days,min_t,label='Min Temp')
plt.plot(days,avg_t,label='Avg Temp')
plt.legend(loc='best',shadow=True,fontsize='small') # upper right , upper left , best ,lower left,lower right,right,center left,center right,lower center,upper center,center
plt.grid()
plt.title('Weather')
plt.xlabel('Days')
plt.ylabel('Temprature')
plt.show()