def add(n1,n2):
    return n1+n2
def substract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
operations={'+' :add ,'-' :substract ,'*' :multiply ,'/' :divide}
import artcalci
def calculator():
    print(artcalci.logo)
    num1=float(input('Write the first number:'))
    for key in operations:
        print(key)
    should_continue=True
    while should_continue==True:
        function=input('What operator due you want to use:')
        num2=float(input('Write the next number:'))
        if function in operations:
            c=operations[function]
            ans=c(num1,num2)
            print(f'{num1} {function} {num2} = {ans}')
            choice=input(f'Do you want to continue with {ans} .Type y for yes or n for no: ').lower()
            if choice=='y':
                num1=ans
                should_continue=True
            else:
                should_continue=False
                calculator()
        else:
            print('Enter a valid operation')
            calculator()
calculator()
