notas = [
    {"nome": "Marcio", "nota": 11},
    {"nome": "Lucia", "nota": 15},
    {"nome": "Rita", "nota": 8},
    {"nome": "Maria", "nota": 7},
    {"nome": "Luis", "nota": 9.5},
]
# 2 List comprehension
aprovados = [k["nome"] for k in notas if k["nota"] >= 9.5]



# 3 dict comprehension
aprovadosKeyValue = {no["nome"]: no["nota"] for no in notas if no["nota"] >= 9.5}

# 4
count = len(aprovadosKeyValue)

count2 = len(notas) - count


# 5
print("Aprovados: ")
for i in aprovados:
    print(i)

print("Notas dos Aprovados: ")
for k, v in aprovadosKeyValue.items():
    print(k, v)

print(f"Aprovados: {count}")

print(f"Reprovados: {count2}")