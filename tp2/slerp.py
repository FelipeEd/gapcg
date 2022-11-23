import numpy as np
import pygame
import time
from class_quat import *
from class_cube import *
from extra_functions import *
"""
! Para rodar o programa é necessario instalar os pacotes numpy e pygame.!

Implementar:

1. Multiplicação de quaternion usando 8 multiplicações de ponto flutuante.(implementado no arquivo quat.py)
2. Rotação usando quaternions.
3. Slerp.

Esse arquivo possui a implementação do Slerp, atualmente ele gera duas rotações
aleatórias e exibe uma animação da rotação que interpola elas usando quaternions

obs: A implementação da função SLERP se encontra no arquivo "class_cube.py" como método da classe, "drawSlerp".

"""


def main():
    random.seed(time.time())
    pygame.init()
    screen = pygame.display.set_mode([width, height])

    # Controla a velocidade do programa para não depender do desenpenho
    clock = pygame.time.Clock()
    fps = 60
    # Editar aqui--------------------------------------------------------------
    # t do slerp
    t = 0.0
    # 0.5 é o tamanho do cubo considerando que a tela vai de  -1 a 1
    cube_ini = Cube(0.5, (0, 200, 50))
    cube_fin = Cube(0.5, (200, 10, 50))
    cube_iter = Cube(0.5)

    # Gerando eixos e angulos aleatórios
    eixo1 = raxis()
    eixo2 = raxis()

    angulo1 = random.random() * 2 * np.pi
    angulo2 = random.random() * 2 * np.pi

    # Colocando a posição inicial dos cubos
    cube_ini.rot(eixo1, angulo1)
    cube_fin.rot(eixo2, angulo2)

    # --------------------------------------------------------------------------

    running = True
    while running:
        # Cor do fundo da tela
        screen.fill((30, 30, 45))
        for event in pygame.event.get():
            # Detecta click em fechar
            if event.type == pygame.QUIT:
                running = False

        # ----------------------------------------------------------------------

        # Desenha os cubos
        cube_ini.draw(screen, 1)
        cube_fin.draw(screen, 1)

        # Desenha a animação do slerp
        cube_iter.drawSlerp(screen, eixo1, angulo1, eixo2, angulo2, t)

        # Faz parar quando t = 1
        if t <= 1:
            t = t + 0.005

        # ----------------------------------------------------------------------

        # Exibe informações
        myFont = pygame.font.SysFont("Times New Roman", 18)
        msg = myFont.render(
            f't = {t:.2f}', 1, (255, 255, 255))
        screen.blit(msg, (0, 0))
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()


if __name__ == '__main__':
    main()
