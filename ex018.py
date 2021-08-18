import math
ang = float(input('Digite o angulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O seno desse ângulo equivale a {:.2f}, seu cosseno {:.2f} e sua tangente {:.2f}.'.format(sen, cos, tan))