from matplotlib import pyplot as plt

plt.style.use('ggplot')  #  OR
#plt.xkcd()
# Median Developer Salaries by Age
x_age = [25,26,27,28,29,30,31,32,33,34,35]
y_dev_sal =[1100,2200,3300,4400,5500,6600,7700,8800,9900,23400,24000]
plt.plot(x_age,y_dev_sal,label='All Developers',color='R',lineStyle='--')
# Median Python Developer Salaries by Age
y_py_dev_sal = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
plt.plot(x_age,y_py_dev_sal,label='Python Developers')
# Median JavaScript Developer Salaries by Age
y_js_dev_sal =  [37810, 43515, 46823, 49293, 53437,56373, 62375, 66674, 68745, 68746, 74583]
plt.plot(x_age,y_js_dev_sal,label= 'JS Developers',color = '#5a7d9a')
plt.xlabel('Ages')
plt.ylabel('Salaries')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
plt.savefig('Plot1.jpg')
