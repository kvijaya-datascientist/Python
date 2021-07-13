def sumTest(num1,num2):
    try:
        result = num1 + num2
    except Exception as e:
        result = None
    return result
def subTest(num1, num2):
    try:
        result = num1 - num2
    except Exception as e:
        result = None
    return  result
def divTest(num1,num2):
    try:
        result = num1 / num2
    except ZeroDivisionError as e:
        print('Zero Division Error')
        result = None
    except TypeError as e:
        print('Type Error')
        result = None
    except Exception as e:
        print('Exception type is ',type(e).__name__)
        result = None
    return  result
