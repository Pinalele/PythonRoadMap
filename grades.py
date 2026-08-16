notas = []

for i in range(3):
    nota = float(input(f"introduza a nota {i + 1}: "))
    notas.append(nota)


def average(notas):
    return sum(notas) / len(notas)


def approved(media):
    return "Aprovado" if media >= 9.5 else "Reprovado"


media = average(notas)
print(f"Média das tres notas: {average(notas):.2f}")
print(f"Avaliaçao final: {approved(media)}")
print(f"Nota mais alta:  {max(notas)}")
print(f"Nota mais baixa: {min(notas)}")