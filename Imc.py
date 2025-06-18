seu_nome= input('Digite o seu nome')
peso=  float(input('Digite o seu peso'))
altura= float(input('Digite sua altura'))
imc=  peso / (altura ** 2)
resultado= round(imc,2)
if imc <= 18.5:
    print(f'{resultado} de imc esta muito baixo')
    print('melhore, coma mais carboidrato')
elif imc <= 24.9: 
    print(f'{resultado} de imc peso normal')
    print('voce está num peso estável') 
elif imc <= 29.9:
    print(f'{resultado} de imc esta sobrepeso')
    print('voce está precisando de um nutricionista!!')
elif imc <= 34.9:
    print(f'{resultado}  de imc esta obesidade Grau 1')
    print(' Voce esta precisando de ajuda')
elif imc <= 39.9:
    print(f'{resultado} de imc esta obesidade Grau 2')
    print('Vai participar dos quilos mortais')
else:
    print(f'{resultado} de imc esta obesidade Grau 3')    
    print('Chama a ANBULANCIA')