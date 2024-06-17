nome = input('Qual é o seu nome? ')
idade = int(input('Qual é a sua idade? '))
altura = float(input('Qual é a sua altura? '))  # DIGITAR NESSE ESTILO EX: (1.75)
peso = float(input('Qual é o seu peso? '))

imc = float(peso / (altura * altura))
resultado = imc
print(resultado)

def calculo_imc():
    if imc < 18.5:
        print(f' Seu IMC é de {imc}, e ele é classificado como Magreza!')
    elif imc > 18.5 and imc < 24.9:
        print(f' Seu IMC é de {imc}, e ele é classificado como Normal!')
    elif imc > 25 and imc < 29.9:
        print(f' Seu IMC é de {imc}, e ele é classificado como Sobrepeso I!')
    elif imc > 30.0 and imc < 39.9:
        print(f' Seu IMC é de {imc}, e ele é classificado como Obesidade II!')
    elif imc > 40.00:
        print(f' Seu IMC é de {imc}, e ele é classificado como Obesidade grave III!')

calculo_imc()

