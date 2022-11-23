import numpy as np
import pygame
from extra_functions import *
from class_quat import *


class Cube():

    """
        Uma classe que modela um cubo com seu centro de massa na Origem
    """

    def __init__(self, s=1, color=(200, 100, 50)) -> None:
        """
        x-----x
        |     |
        |     |
        x-----x

        """
        # Cor do cubo
        self.color = color

        # Vertices do cubo
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

    def lines(self, v):
        """
            Função que gera as linhas do cubo dado a condição uma lista de vértices
        """

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

    def draw(self, window, stroke=5):
        """
            Função que desenha o cubo
        """
        # Desenha cada linha do cubo
        for l in self.lines(self.v):
            pygame.draw.line(window, self.color, l[0][:2], l[1][:2], stroke)

        # Desenha um circulo nos vérices
        for v in self.v:
            pygame.draw.circle(window, (255, 255, 255),
                               world_to_screen(v[:2]), stroke)

    def rot(self, axis, angle, window=False):
        """
        Função que rotaciona os vertcies do cubo usando
        a conjugação por quaternion unitário.

        Args:
            axis (vec3): Eixo de rotação
            angle (float): Angulo da rotação
            window (pygame): Tela para desenhar o eixo
        """

        # Normalizar o eixo de rotação
        axis = axis / norm(axis)

        # Desenhar o eixo de rotação na tela
        if window:
            pygame.draw.line(window, (200, 200, 50), world_to_screen(
                [0, 0]), world_to_screen(axis[:2]), 5)

        # Quaternionr de rotação
        q = rot_quat(axis, angle)

        # conjugado de q
        qconj = q.conjugate()

        # Aplica a rotação para cada vertice do cubo
        for i in range(len(self.v)):
            # Considerando a posição dos vértices como quaternions puros
            u = Quat(0, self.v[i][0], self.v[i][1], self.v[i][2])

            # Formula de conjugação para rotação
            res = q * u * qconj

            # convertendo para R3 novamente
            self.v[i] = [res.i, res.j, res.k]

    def drawSlerp(self, screen, ax1, a, ax2, b, t, stroke=5):
        """
            Função que desenha o SLERP das duas rotações
        """
        # Quaternions de rotação correspondetes
        q0 = rot_quat(ax1, a)
        q1 = rot_quat(ax2, b)

        # Interpolando os quaternions
        q_interpol = uni_q_exp(q1 * q0.conjugate(), t) * q0
        #q_interpol = q0 * uni_q_exp(q0.conjugate() * q1, t)
        #beta = np.arccos(q_cos(q0, q1))
        # q_interpol = q0.scaled(np.sin((1 - t) * beta) / np.sin(beta)
        #                        ) + q1.scaled(np.sin(t * beta) / np.sin(beta))

        new_v = self.v.copy()
        # Aplica a rotação para cada vertice do cubo
        for i in range(len(self.v)):
            # Considerando a posição dos vértices como quaternions puros
            u = Quat(0, self.v[i][0], self.v[i][1], self.v[i][2])

            # Formula de conjugação para rotação
            res = q_interpol * u * q_interpol.conjugate()

            # convertendo para R3 novamente
            new_v[i] = [res.i, res.j, res.k]

        # Desenha cada linha do cubo
        for l in self.lines(new_v):
            pygame.draw.line(screen, self.color, l[0][:2], l[1][:2], stroke)


if __name__ == '__main__':
    print("ERRO :: Este arquivo só contem uma classe, e não foi feito para ser executado, tente executar rotation.py ou slerp.py!!")
