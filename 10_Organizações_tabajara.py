print(" :::: Programa Cálculo para Reajuste Salarial :::: ")
print(" De acordo com o que se é pedido preencha os requesitos para calcular os reajustes de cada faixa salarial.")

sal_trab = float(input("Salário: R$ "))

if sal_trab <= 280:
    slr = sal_trab * 1.20
    aumento = slr - sal_trab
    print("Seu salário no momento é: R$")
    print("Reajuste de 20%")
    print("Reajustem em R$: ", aumento)
    print("O salário após o reajuste é: R$",slr)

elif sal_trab > 280 and sal_trab <= 700:
    r1 =1.15
    slr = sal_trab * r1
    aumento = slr -sal_trab
    print("Seu salário no momento é R$:",sal_trab)
    print("Reajuste de 15%")
    print("Reajuste em R$: ", aumento)
    print("O salário após o reajuste é: R$", slr)

elif sal_trab > 700 and sal_trab <= 1500:
    r2 = 1.10
    slr = sal_trab * r2
    aumento= slr - sal_trab
    print("Seu salário no momento é R$:", sal_trab)
    print("Reajuste de 10%")
    print("Reajustem e R$: ", aumento)
    print("O salário após o reajuste é: R$", slr)

elif sal_trab > 1500:
    r3 =1.05
    slr = sal_trab * r3
    aumento = slr - sal_trab
    print("Seu salário no momento é R$:", sal_trab)
    print("Reajuste de 5%")
    print("Reajustem em R$: ", aumento)
    print("O salário após o reajuste é: R$", slr)

else:
    print("Valor inválido!")
    print("Programa encerrado!")

