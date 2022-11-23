from extra_functions import *


class Quat:

    def __init__(self, r, i, j, k) -> None:
        """Função para inicializar o quaternion
        a partir de cada coordenada
        Args:
            r (float): Parte real do quaternion
            i (float): partes imaginarias do quaternion
            j (float): partes imaginarias do quaternion
            k (float): partes imaginarias do quaternion
        """

        self.r = float(r)
        self.i = float(i)
        self.j = float(j)
        self.k = float(k)

    # def __init__(self, eixo, angle) -> None:
    #     """Função para inicializar o quaternion
    #     a partir de um eixo de rotação e angulo
    #     Args:
    #         r (float): Parte real do quaternion
    #         i (float): partes imaginarias do quaternion
    #         j (float): partes imaginarias do quaternion
    #         k (float): partes imaginarias do quaternion
    #     """
    #     self.r = np.cos(angle / 2)
    #     self.i = np.sin(angle / 2) * eixo[0]
    #     self.j = np.sin(angle / 2) * eixo[1]
    #     self.k = np.sin(angle / 2) * eixo[2]
    def __add__(self, other):
        return Quat(self.r + other.r, self.i + other.i, self.j + other.j, self.k + other.k)

    def __mul__(self, other):
        """Função que implementa a multiplicação de quaternions
        usando apenas 8 multiplicações entre pontos flutuantes.

        Args:
            other (quat): Quaternion a ser multiplicado.

        Returns:
            quat: quaternion resultante.
        """

        c_1 = (self.r + self.i) * (other.r + other.i)
        c_2 = (self.k - self.j) * (other.j - other.k)
        c_3 = (self.i - self.r) * (other.j + other.k)
        c_4 = (self.j + self.k) * (other.i - other.r)
        c_5 = (self.i + self.k) * (other.i + other.j)
        c_6 = (self.i - self.k) * (other.i - other.j)
        c_7 = (self.r + self.j) * (other.r - other.k)
        c_8 = (self.r - self.j) * (other.r + other.k)

        f_1 = c_2 + (-c_5 - c_6 + c_7 + c_8) / 2
        f_2 = c_1 - (c_5 + c_6 + c_7 + c_8) / 2
        f_3 = - c_3 + (c_5 - c_6 + c_7 - c_8) / 2
        f_4 = - c_4 + (c_5 - c_6 - c_7 + c_8) / 2

        return Quat(f_1, f_2, f_3, f_4)

    def conjugate(self):
        return Quat(self.r, -self.i, -self.j, -self.k)

    def scaled(self, alpha):
        return Quat(self.r * alpha, self.i * alpha, self.j * alpha, self.k * alpha)

    def __repr__(self) -> str:
        return f'{self.r} + {self.i}i + {self.j}j + {self.k}k'


def rot_quat(eixo, angle):
    """Função que retorna um quaternion
    a partir de um eixo de rotação e angulo
    """
    return Quat(np.cos(angle / 2), np.sin(angle / 2) * eixo[0], np.sin(angle / 2) * eixo[1], np.sin(angle / 2) * eixo[2])


def q_inn(p, q):
    return p.r * q.r + p.i * q.i * p.j * q.j + p.k * q.k


def q_cos(p, q):
    return q_inn(p, q) / np.sqrt(q_inn(p, p) * q_inn(q, q))


def uni_q_exp(q, t):
    alpha = np.arccos(q.r)
    axis = [q.i, q.j, q.k] / np.sin(alpha)
    return rot_quat(axis, 2 * alpha * t)


if __name__ == '__main__':
    print("ERRO :: Este arquivo só contem uma classe, e não foi feito para ser executado, tente executar rotation.py ou slerp.py!!")
