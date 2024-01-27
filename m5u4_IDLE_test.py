Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

>>> class calc: #no parameters
    def add(x,y):
        answer = x + y
        print(answer)
    def subtract(x,y):
        answer = x - y
        print(answer)
    def multiply(x,y):
        answer = x * y
        print(answer)
    def divide(x,y):
        answer = x / y
        print(answer)

>>> calc.add(5,3)
8
>>> calc.subtract(5,3)
2
>>> calc.multiply(5,3)
15
>>> calc.divide(5,3)
1.6666666666666667

#Tested in IDLE