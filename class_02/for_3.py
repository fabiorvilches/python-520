lista = [ 47, 80, 50, 69, 41, 50, 5, 14, 14, 88,]
lista_secundaria = []
soma = 0 

for element in lista:
        if element % 2 == 1:
                lista_secundaria = lista_secundaria + [ element * 3 ]
        else:
                lista_secundaria = lista_secundaria + [element * 2]

print(lista_secundaria)
print(lista)

