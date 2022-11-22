
class Quat:

    def __init__(self, r, i, j, k) -> None:
        """Função para inicializar o quaternion
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

    def __repr__(self) -> str:
        return f'{self.r} + {self.i}i + {self.j}j + {self.k}k'
