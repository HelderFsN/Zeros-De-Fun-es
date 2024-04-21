import numpy as np
import matplotlib.pyplot as plt
from math import sin, pi, cos

def f(id):
    return sin(id) - id + 1

x = np.linspace(-np.pi,np.pi,35)
y = np.sin(x) - x + 1
plt.plot(x, y)
plt.xlim(-np.pi,np.pi)
plt.grid(True)
plt.show()
def bisseccao (x1, x2, TOL, iter=16):
    hp = (x1 + x2) / 2.0
    if f(x1) * f(x2) > 0:
        print('nenhuma raíz encontrada')
    else:
        c = 0
        ERRO = abs(x2 - x1) /2

        while ERRO > TOL and c < iter:
            hp = (x1 + x2) / 2.0
            if f(hp) == 0:
                return [hp,c]
            elif f(x1) * f(hp) < 0:
                x2 = hp
                c+=1
            else:
                c+=1
                x1 = hp
            ERRO = abs(x2 - x1) / 2
        return {'hp': hp, 'iteração': c}

resp = bisseccao(x1=0,x2=pi,TOL=0.1, iter=16)
print(f'raíz aprox {resp["hp"]:.4f}')
print(f'O número de iterações foi {resp["iteração"]}')
print(f'{pi/32< 0.1}')