import numpy as np
import pygame
from quat import *

width, height = 640, 640
max_x, max_y = width // 2, height // 2

# inverte a coordenada y pois o pygame possui a origem na esquerda superior
# e com y positivo para baixo.


def flip(y):
    return -y + height


def world_to_screen(v):
    k = v.copy()
    for i in range(len(k)):
        if i == 1:
            k[i] = flip(((k[i] + 1) / 2 * width))
        else:
            k[i] = ((k[i] + 1) / 2 * width)

    return k


class Cube():

    def __init__(self, s=1, color=(200, 100, 50)) -> None:
        """
        x-----x
        |     |
        |     |
        x-----x

        """
        self.color = color
        self.v = [
            [-s, -s, s],
            [s, -s, s],
            [s, s, s],
            [-s, s, s],
            [-s, -s, -s],
            [s, -s, -s],
            [s, s, -s],
            [-s, s, -s],
        ]

    # def faces(self):
    #     v = self.v
    #     return [[v[0], v[1], v[2], v[3]],  # front face
    #             [v[4], v[5], v[6], v[7]],  # back face
    #             [v[3], v[2], v[7], v[6]],  # top face
    #             [v[0], v[1], v[4], v[5]],  # down face
    #             [v[1], v[2], v[5], v[6]],  # right face
    #             [v[0], v[3], v[4], v[7]],  # left face
    #             ]

    def lines(self):
        v = self.v
        # Função que gera as linhas do cubo dado a condição atual dos vértices
        return [
            [world_to_screen(v[0]), world_to_screen(v[1])],
            [world_to_screen(v[1]), world_to_screen(v[2])],
            [world_to_screen(v[2]), world_to_screen(v[3])],
            [world_to_screen(v[3]), world_to_screen(v[0])],

            [world_to_screen(v[0 + 4]), world_to_screen(v[1 + 4])],
            [world_to_screen(v[1 + 4]), world_to_screen(v[2 + 4])],
            [world_to_screen(v[2 + 4]), world_to_screen(v[3 + 4])],
            [world_to_screen(v[3 + 4]), world_to_screen(v[0 + 4])],

            [world_to_screen(v[0]), world_to_screen(v[0 + 4])],
            [world_to_screen(v[1]), world_to_screen(v[1 + 4])],
            [world_to_screen(v[2]), world_to_screen(v[2 + 4])],
            [world_to_screen(v[3]), world_to_screen(v[3 + 4])]
        ]

    def draw(self, window):
        # Desenha cada linha do cubo
        for l in self.lines():
            pygame.draw.line(window, self.color, l[0][:2], l[1][:2], 5)

        # Desenha um circulo nos vérices
        for v in self.v:
            pygame.draw.circle(window, (255, 255, 255),
                               world_to_screen(v[:2]), 5)

    def rot(self, axis, angle, window):

        # Normalizar o eixo de rotação
        axis = axis / np.sqrt(axis[0]**2 + axis[1]**2 + axis[2]**2)

        # Desenhar o eixo de rotação na tela
        pygame.draw.line(window, (200, 200, 50), world_to_screen(
            [0, 0]), world_to_screen(axis[:2]), 5)

        # Quaternionr de rotação
        q = Quat(np.cos(angle / 2), np.sin(angle / 2) *
                 axis[0], np.sin(angle / 2) * axis[1], np.sin(angle / 2) * axis[2])

        # conjugado de q
        qconj = Quat(np.cos(angle / 2), -np.sin(angle / 2) *
                     axis[0], -np.sin(angle / 2) * axis[1], -np.sin(angle / 2) * axis[2])

        # Aplica a rotação para cada vertice do cubo
        for i in range(len(self.v)):
            # considerando a posição dos vértices como quaternions puros
            u = Quat(0, self.v[i][0], self.v[i][1], self.v[i][2])

            # Formula de conjugação para rotação
            res = q * u * qconj

            # convertendo para R3 novamente
            self.v[i] = [res.i, res.j, res.k]
