def main():
    print("Welcome to the simple calculator.")
    while True:
        num1 = int(input("Enter num1: "))
        num2 = int(input("Enter num2: "))
        operation = input("Enter your desired operation: ")

        sim_cal = SimpleCalculator(num1, num2, operation)

        if operation == "+":
            print(sim_cal.addition())
        elif operation == "-":
            print(sim_cal.subtraction())
        elif operation == "*":
            print(sim_cal.multiplication())
        elif operation == "/":
            print(sim_cal.division())
        else:
            print("Invalid operation.")

        if input("Do you want to continue? (y/n): ").lower() != 'y':
            print("Thanks for using my simple calculator.")
            break



class SimpleCalculator:
    def __init__(self, num1, num2, operation):
        self.num1 = num1
        self.num2 = num2
        self.operation = operation

    def addition(self):
        result = self.num1 + self.num2
        return f"{self.num1} {self.operation} {self.num2} = {result}"


    def subtraction(self):
        result = self.num1 - self.num2
        return f"{self.num1} {self.operation} {self.num2} = {result}"

    
    def multiplication(self):
        result = self.num1 * self.num2
        return f"{self.num1} {self.operation} {self.num2} = {result}"


    def division(self):
        if self.num2 == 0:
            return f"ZeroDivisionError: Cannot divide {self.num1} by 0"
            
        result = self.num1 / self.num2
        return f"{self.num1} {self.operation} {self.num2} = {result}"

if __name__ == "__main__":
    main()
