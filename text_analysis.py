from collections import Counter
import re
from pathlib import Path

# 1
texto = """
Python é uma linguagem de programação muito popular para ciência de dados.
Python é fácil de aprender e Python tem uma comunidade enorme.
Muitos programadores escolhem Python para projetos de inteligência artificial.
A sintaxe de Python é simples e Python incentiva código legível.
"""
#2
palavras = re.findall(r'\b\w+\b', texto.lower())
contagem = Counter(palavras)
print(contagem)

#3
tres = contagem.most_common(3)
print(tres)

#4
conteudo = "\n".join(w for w, num in tres)
p = Path("C:/Users/marci/PycharmProjects/PythonRoadMap/resources/text.txt")
p.write_text(conteudo, encoding="utf-8")
print(conteudo)

