                         
def calculator(number):
    
    while True:
        numbers = input('Enter number' + str(number) + ':')
        try:
            return float(numbers)
        except ValueError:
            print('Invalid number entered. Try again')
num1 = calculator(1)       
num2 = calculator(2)

sign  = input('Enter the sign + / - * %: ')
print(f'{num1} {sign} {num2}')

result = 0
if sign == '+':
    result = num1 + num2
elif sign == '-':
    result = num1 - num2       
elif sign == '*':
    result = num1 * num2
elif sign == '/':
    if num2 != 0:
        result = num1 / num2 
    else:
        print('Division by zero error')
elif sign == '%':
    result = num1 % num2                
else:
    print('Enter a avlid sign')

print(result)                                       
                                      
                                      # BY: ALITUHA SHABELLA - 25/BSE/BU/R/0016