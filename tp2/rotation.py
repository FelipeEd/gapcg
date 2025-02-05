import numpy as np
import pygame
from class_quat import *
from class_cube import *
"""
! Para rodar o programa é necessario instalar os pacotes numpy e pygame. ! 

Implementar:

1. Multiplicação de quaternion usando 8 multiplicações de ponto flutuante.(implementado no arquivo quat.py)
2. Rotação usando quaternions.
3. Slerp.

Esse arquivo possui a implementação da rotação por conjugação de quaternions
unitários, modificando a variavel "eixo" e "angulo_por_frame" no inicio do main
obterá novas rotações.

obs: A função de rotação se encontra no arquivo "class_cube.py" como método "rot" da classe cube.
 
A multiplicação de quaternions usando 8 multiplicações de float está em "class_quat.py" como método "__mul__" da classe quat

"""


def main():
    pygame.init()
    screen = pygame.display.set_mode([width, height])

    # Controla a velocidade do programa para não depender do desenpenho
    clock = pygame.time.Clock()
    fps = 60
    # Editar aqui--------------------------------------------------------------

    # 0.5 é o tamanho do cubo considerando que a tela vai de  -1 a 1
    cube = Cube(0.5)

    # Não precisa ser unitário pois a função de rotação normaliza
    eixo = [1, 1, 1]

    # Caso queira um eixo aleatorio descompente a linha de baixo
    #eixo = raxis()

    angulo_por_frame = 0.01

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

        # Desenha o cubo
        cube.draw(screen)
        # A cada frame rotaciona o cubo por um eixo e angulo,
        # Desenhando na tela o eixo
        cube.rot(eixo, angulo_por_frame, screen)

        # ----------------------------------------------------------------------

        # Exibe informações
        myFont = pygame.font.SysFont("Times New Roman", 18)
        msg = myFont.render(
            f'Eixo {eixo[0]:.2f} {eixo[1]:.2f} {eixo[2]:.2f}  Angulo/s {angulo_por_frame}', 1, (255, 255, 255))
        screen.blit(msg, (0, 0))
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()


if __name__ == '__main__':
    main()
