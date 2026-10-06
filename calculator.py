# calculator

from math import sqrt

class Calculator:
    '''Simple object oriented calcultor'''
    def __init__(self):
        self.history=[]
        
    #basic operations
    def add(self,a,b):
        return a+b
    def subtract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        if b==0:
            raise ZeroDivisionError("Can't divide by zero")
        return a/b
    def module(self,a,b):
        if b==0:
            raise ZeroDivisionError("Can't use zero as diviser")
        return a%b
    def numPower(self,a,b):
        return a**b
    def square(self,a):
        return a**2
    def square_root(self,a):
        if a<0:
            raise ValueError("Can't calculate of negative integer")
        return sqrt(a)
    def percentage(self,a,b):
        if b==0:
            raise ZeroDivisionError("Can't divide with denomitor of zero")
        return (a/b)*100
    
    #.....Calculation Engine....
    def calculate(self,operation,a,b=None):
        operations={
            "+":self.add,
            "-":self.subtract,
            "*":self.multiply,
            "/":self.divide,
            "%":self.module,
            "**":self.numPower,
        }
        
        if operation=="sqrt":
            result=self.square_root(a)
            expression=f"Sqrt {a}"
        elif operation=="square":
            result=self.square(a)
            expression=f"square {a}"
        elif operation=="percentage":
            result=self.percentage(a,b)
            expression=f"{a} by {b} per"
        elif operation in operations:
            if b is None:
                raise ValueError("Second num is required")
            result=operations[operation](a,b)
            expression=f"{a} {operation} {b}"
        else:
            raise ValueError("Invalid operation")
        
        self.history.append(f"{expression} = {result}")
        return result
    
    #.......History......
    def show_history(self):
        if not self.history:
            print("\nNo calculation history")
            return
        print("\n.....History......")
        
        for num,calculation in enumerate(self.history,start=1):
            print(f"{num}.{calculation}")
        
        print("="*35)

    #clear history
    def clear_history(self):
        self.history.clear()
        print("\nClear history")
                    
class CalculatorApp:
    '''Help user interaction with calculator'''
    def __init__(self):
        self.calculator=Calculator()
        
    # menu
    def show_menu(self):
        print("_"*20)
        print("\nWelcome to Simple Calculator to perform tasks")
        print("_"*20)
        print("\n")
        print("*"*25)    
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")
        print("6. NumPower (**)")
        print("7. Square ")
        print("8. Square root (Sqrt)")
        print("9. Percentage (Per)")
        print("10. Show History")
        print("11. Clear History")
        print("0. Exit")
        print("*"*25)
        
    def get_number(self,message):
            while True:
                try:
                    return float(input(message))
                except ValueError:
                    print("Invalid choice, Please enter a valid number")
    
    def perform_operation(self,choice):
        operations={
            "1":"+",
            "2":"-",
            "3":"*",
            "4":"/",
            "5":"%",
            "6":"**"
        }
        #square
        if choice=="7":
            number=self.get_number("Enter num: ")
            
            try:
                result=self.calculator.calculate("square",number)
                print("Result",result)
            except ValueError as error:
                print("X ",error)
        #square root    
        elif choice=="8":
            number=self.get_number("Enter num: ")
            
            try:
                result=self.calculator.calculate("sqrt",number)
                print("Result",result)
            except ValueError as error:
                print("X ",error)

        elif choice=="9":
            number1=self.get_number("Enter first num: ")
            number2=self.get_number("Enter second num: ")
            
            try:
                result=self.calculator.calculate("percentage",number1,number2)
                print("Result:",result)
            except ZeroDivisionError as error:
                print("X", error)
                
            except ValueError as error:
                print("X", error)

            #Basic operations
        elif choice in operations:
                
            first=self.get_number("Enter first num: ")
            second=self.get_number("Enter second num: ")                
            operation=operations[choice]
            try:
                result=self.calculator.calculate(operation,first,second)
                print("Result: ",result)
            except ZeroDivisionError as error:
                print("X",error)
            except ValueError as error:
                print("X",error)
        else:
            print("Invalid choice, Please try again")
            
    def run(self):
        while True:
            self.show_menu()
            choice=input("Choose an option: ").strip()
            if choice=="0":
                print("\nCalculator closed.\nGoodbye!")
                break
            elif choice=="11":
                self.calculator.clear_history()
            elif choice=="10":
                self.calculator.show_history()
            elif choice in ["1","2","3","4","5","6","7","8","9"]:
                self.perform_operation(choice)
            else:
                print(f"X Invalid option. Please try again")

if __name__=="__main__":
    app=CalculatorApp()
    app.run()
    