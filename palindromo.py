import re


p = 'luz azul'  # Nome exemplo


def palindromo(nome):

    nome = re.sub(r"\s+", "", nome)     # Retirando os espaços do nome dado
    l = len(nome)   # Tamanho da String
    s1 = nome[l::-1]  # String invertida
    s2 = re.sub(r"\s+", "", s1)   # String invertida sem espaço

    if s2 == nome:
        print('O nome dado é palindromo.')
    else:
        print('O nome dado não é palindromo.')


palindromo(p)
