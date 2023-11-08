class Math:
    def addition(self, num1, num2):
        result = num1 + num2
        print(f"Addition result {result}")

    def subtraction(self, num1, num2):
        result = num1 - num2
        print(f"Subtraction result {result}")

    def multiplication(self, num1, num2):
        result = num1 * num2
        print(f"Multiplication result {result}")

    def division(self, num1, num2):
        if num2 != 0:
            result = num1 / num2
            print(f"Division result {result}")
        else:
            print("Division by zero is not possible")



calc = Math()


calc.addition(5, 3)
calc.subtraction(10, 7)
calc.multiplication(4, 6)
calc.division(8, 2)
calc.division(10, 0)
