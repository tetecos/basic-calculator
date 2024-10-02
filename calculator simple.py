unidade = input("digite uma unidade (+, -, *, /):")
num1 = float(input("digite o primeiro numero:"))
num2 = float(input("digite o segundo numero:"))

if unidade == "+":
    result = num1 + num2
    print(f"resultado equivale a {result}")
elif unidade == "-":
    result = num1 - num2
    print(f"resultado equivale a {result}")
elif unidade == "*":
    result = num1 * num2
    print(f"resultado equivale a {result}")
elif unidade == "/":
    result = num1 / num2
    print(f"resultado equivale a {result}")