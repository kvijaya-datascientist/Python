# Monthly Home Expenses Pie Chart

from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')
home_expenses = [7500,768,500,15000,60000]
home_labels =['Rent','Power bill','Internet Bill','Credit Card Bill','Savings']
explode=[0,0,0,0,0.1]
plt.pie(home_expenses,labels=home_labels,explode=explode,autopct='%1.1f%%',wedgeprops={'edgecolor':'black'},startangle=90)
plt.tight_layout()
plt.title('Feb2020 Monthly Expenses')
plt.show()
plt.savefig('HomeExpenses_Feb2020.jpg',bbox_inches='tight')