# Bar Chart Demo
import matplotlib.pyplot as plt
import numpy as np
company=['Google','amazon','AWS','Facebook','MSFT']
revenue =[90,136,45,27,150]
profit =[40,2,34,12,23]
xpos = np.arange(len(company))
#print(xpos)  # [0,1,2,3,4]
 # Horizontal Bars
""" plt.xticks(xpos,company)
plt.bar(xpos-0.2,revenue,label='Revenue')
#plt.bar(company,revenue,label='Revenue')
#plt.bar(company,profit,label='Profit')
plt.bar(xpos+0.2,profit,label='Profit',width=0.4)   """

# Vertical Bars
ypos =np.arange(len(company))
plt.yticks(ypos,company)
plt.barh(xpos-0.2,revenue,label='Revenue')
plt.barh(xpos+0.2,profit,label='profit')
plt.title('US Tech Stocks')
plt.xlabel('Company names')
plt.ylabel('Revenue(bin)')
plt.legend()
plt.show()