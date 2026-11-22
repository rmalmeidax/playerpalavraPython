
palavra =('telhado')
num_letras =len (palavra)
print(f"Total de letras {num_letras}")

print(" ")
print("###################JOGO PALALVRA ##################")
print(" ")
jogadas = int (input("Quatidade de partidas: "))
for i in range (1, jogadas +1):

    for letra  in palavra:
        print(letra)
        player = input("Digite uma palavra para jogo: ")
    if player in palavra:
        print(f"A palavra Correta, Você venceu o jogo!!  {palavra}")
        break
    else:
        print(f"Palavra errada, Você perdeu o jogo")

