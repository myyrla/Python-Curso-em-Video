from math import hypot
cat1 = float(input("Digite o valor do primeiro cateto: "))
cat2 = float (input ("Digite o valor do segundo cateto: "))
hipotenusa = hypot (cat1, cat2)
print(f"A hipotenusa do triaângulo retângulo com catetos {cat1} e {cat2} é {hipotenusa:.2f}")
