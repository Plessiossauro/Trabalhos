dg1_tempo = float(input("Tempo decorrido pelo dragão 2 (Horas)"))
dg1_distancia = float(input("Distãncia percorrida pelo dragão 2 (Km)"))

dg2_tempo = float(input("Tempo decorrida pelo dragão 2 (Horas)"))
dg2_distancia = float(input("Distãncia percorrida pelo dragão 2 (Km)"))

dg1_velocidade = dg1_distancia / dg1_tempo
dg2_velocidade =  dg2_distancia / dg2_tempo

if dg1_velocidade > dg2_velocidade:
    print("Dragão 1 é mais rápido")
elif dg2_velocidade > dg1_velocidade:
    print("Dragao 2 e mais rápido")
else:
    print("Hulk gosta de dragoes")