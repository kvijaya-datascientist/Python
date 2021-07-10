# -------- TEST:1  --------
"""vijaya_expenses = [100,200,400,300]
kanth_expenses = [100,200,400,500]

def total_expenses(expense):
 total_expense = 0
 for exp in expense:
     total_expense = total_expense + exp
 return total_expense

vijaya_total_expenses = total_expenses(vijaya_expenses)
print("Vijaya taotal expense  ",vijaya_total_expenses)
kanth_total_expenses = total_expenses(kanth_expenses)
print("Kanth taotal expense  ",kanth_total_expenses) """
# -------- TEST:2  ---------
"""def sum(a,b):
    total =0
    total = a + b
    return total

sum_val = sum(3,2)
print("sum of ",sum_val)  """
# ------ TEST:3 --------
total =1
def sum(a,b=0):
    """
    This function takes two arguments as inputs , if we donot provide any value for b then it takes 0 as default value.  otherwise it will overide the provided value
    """
    print("inside method a = ",a)
    print("inside method b = ", b)

    total =0
    total = a + b
    print ("total value inside method is ", total)

n = sum(b=3,a=2)
n = sum(3)


print("total value outside method/in class is ", total)



