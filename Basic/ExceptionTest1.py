def divTest(num1,num2):
    try:
        res = num1 / num2
    except Exception as e:
        res=None
    return res

if __name__ == "__main__":
    number1 = int(input("Enter number "))
    number2 = int(input("Enter number "))
    divResult1 = divTest(number1,number2)
    print("Division result--> ",divResult1)