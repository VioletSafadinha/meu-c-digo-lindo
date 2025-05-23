import time
import random

tempo_bacana_c_ctz_n_eh_aleatorio_e_ss_pq_o_codigo_ta_carregando = random.randint(10, 20)
problemas = []

print("Quando quiser parar de enviar problemas, digite 188")
while True:
    seu_problema = input("Digite os seus problemas: ")
    if seu_problema == "188":
        break
    problemas.append(seu_problema)

if problemas != []:
    print("Seus problemas:")         
    for problema in problemas:
        print(problema)
    print("~" * 20)
    print("Resolvendo seus problemas...")
    time.sleep(tempo_bacana_c_ctz_n_eh_aleatorio_e_ss_pq_o_codigo_ta_carregando)
    problemas.clear()

    print("Prontinhooo rsrsss!!")
    print("Seus problemas agora:")
    print(problemas)
else:
    print("Se tu não tens um problema...\nEntão EU te darei um agora!")
    time.sleep(5)
    comecar_putaria = time.time()
    while time.time() < comecar_putaria + 10:
                NUMERO_LEGAL_DEMAIS = random.randint(10, 20)
                numero_muito_chato = random.randint(-2, 3)
                o_numero_mais_legal_que_voce_ja_viu = (numero_muito_chato*2)**2
                print(" " * numero_muito_chato, "HA" * NUMERO_LEGAL_DEMAIS)
                print(" " * o_numero_mais_legal_que_voce_ja_viu, "ha" * NUMERO_LEGAL_DEMAIS)
    print("Papai noel não vai vir no seu próximo natal, ok?")
