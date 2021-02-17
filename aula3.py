
# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))
#
# if a > b and a > c:
#     print(f'O maior número é {a} ')
#
# elif b > a and b > c:
#     print(f'O maior número é {b}')
# else:
#     print(f'O maior número é {c} ')
#
# print('!!! Final do programa !!!')


# a = int(input('Entre com o primeiro valor: '))
# b = int(input('Entre com o segundo valos: '))
#
# rest = a % 2
# rest_B = b % 2
#
# if rest == 0 or rest_B == 0:
#     print('Foi digitado um número par')
# else:
#     print('Nenhum número par foi digitado')
soma = 0
for c in range(3):
    n = int(input(f'Digite a nota do {c+1}º bimestre: '))
    while n > 10:
       n = int(input('Número inválido, digite novamente: '))
    else:
        soma = soma + n

media = soma / 3

print(f'{media:.1f}')
