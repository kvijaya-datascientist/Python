# Stack plots Demo
from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')
minutes = [1,2,3,4,5,6,7,8,9]
player1 = [1,2,3,4,5,4,3,6,7]
player2 = [1,1,2,1,2,3,4,1,2]
player3 = [1,2,1,1,1,2,1,1,3]
labels_vals = ['player1','player2','player3']
colors =['#fc4f30','#008fd5','#e5ae37']
plt.stackplot(minutes,player1,player2,player3,labels=labels_vals,colors=colors)
plt.legend(loc=(0.07,0.05))
plt.title('Stack Plots')
plt.xlabel('Minutes')
plt.ylabel('Player Runs')
plt.tight_layout()
plt.show()
