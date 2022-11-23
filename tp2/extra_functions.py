import random
import numpy as np

width, height = 640, 640


def flip(y):
    """inverte a coordenada y pois o pygame possui a origem 
    na esquerda superior e com y positivo para baixo.

    Args:
        y (float): coordenada y de algum vetor

    Returns:
        float: coordenada invertida na tela do pygame
    """

    return -y + height


def world_to_screen(v):
    """Converte coordenadas do cubo -1 1 
    para coordenadas na tela do pygame

    Args:
        v (vec3 / vec2): vetores 2d ou 3d

    Returns:
        vec3/vec2: com cordenadas do pygame 
    """
    k = v.copy()
    for i in range(len(k)):
        if i == 1:
            k[i] = flip(((k[i] + 1) / 2 * width))
        else:
            k[i] = ((k[i] + 1) / 2 * width)

    return k


def norm(v):
    """
    Retorna a norma Euclidiana de um vetor em Rn
    """
    sum = 0
    for coord in v:
        sum += coord**2
    return np.sqrt(sum)


def raxis():
    """
    Retorna um eixo aleatório
    """
    v = [random.random() - 0.5, random.random() -
         0.5, random.random() - 0.5] * 2
    v = [random.random(), random.random(), random.random()]
    return v / norm(v)
