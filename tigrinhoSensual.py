import random

dindin = 1000
print("-"*40 + "\n....Bem-vindo(a) ao Tigrinho Sensual....\n" + "-"*40)

while dindin != 0:
    print(f"\nDinheiro restante: R$ {dindin:.<19}")
    aposta = float(input("Digite quanto dinheiro você quer apostar: "))
    if aposta > dindin:
        print("Dinheiro insuficiente")
        continue
    aposta = random.choice([(aposta*-1), (aposta*1.5)])
    dindin += aposta
        
print(f"\nDinheiro restante: R$ {dindin:.<19}")
print("\nVocê faliu, seu pobre!")
