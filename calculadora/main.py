import matematica

print("Escolha qual operação deseja realizar: ")


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

sub = matematica.subt(num1, num2)
soma = matematica.soma(num1, num2)
mult = matematica.mult(num1, num2)
div = matematica.div(num1, num2)

print(f"{num1} + {num2} == {soma}")
print(f"{num1} - {num2} == {sub}")
print(f"{num1} * {num2} == {mult}")
print(f"{num1} / {num2} == {div}")