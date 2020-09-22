from random import randint

cpf = randint(10000000000, 99999999999)
cpf = str(cpf)
cpf_format = cpf[:9]

multiplicador_1 = 10
somador_1 = 0


for number in cpf_format:
    mult = int(number) * multiplicador_1
    somador_1 += mult
    multiplicador_1 -= 1
    
digitCalculation = 11 - (somador_1 % 11)
primeiro_digito = digitCalculation

# Implementada para concatenar os digitos do cpf aos 9 dígitos gerados pelo randint
concatenation = '' 

if primeiro_digito > 9:
    primeiro_digito = 0
    concatenation = cpf_format + str(primeiro_digito)
else:
    concatenation = cpf_format + str(primeiro_digito)

multiplicador_2 = 11
somador_2 = 0


for number in concatenation:
    mult = int(number) * multiplicador_2
    somador_2 += mult
    multiplicador_2 -= 1

digitCalculation = 11 - (somador_2 % 11)
segundo_digito = digitCalculation

if segundo_digito > 9:
    segundo_digito = 0

concatenation += str(segundo_digito)

print('\033[34mCPF\033[m = {}'.format(concatenation))