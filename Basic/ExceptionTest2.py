import Operations as ops
if __name__ == "__main__":
    number1 = int(input("Enter number "))
    number2 = int(input("Enter number "))
    addResult = ops.sumTest(number1,number2)
    print(f"Sum of {number1,number2} is ",addResult)
    subResult = ops.subTest(number1, number2)
    print(f'Subtraction from {number1} to {number2} is  ',subResult)
    divResult = ops.divTest(number1, number2)
    print(f'{number1} divided by {number2} is   ', divResult)