import numpy as np
from typing import Callable


def generator1d(partition: np.array, 
                collocation: np.array, 
                n: int, 
                r: int, 
                f: Callable,
                b1: float, 
                b2: float) -> tuple[np.array, np.array]:
    ''' Generator Algebraic Equation Matrix
    
    Args:
        - partition: <np.array> [n + 1] partition points.
        - collocation: <np.array> [n * (r + 1)] collocation points.
        - n: <int> number of partition. 
        - r: <int> order of polynomial. 
        - b1: <float> left boundary value
        - b2: <float> right boundary value
    Returns:
        - weight: <np.array> [n * (r + 1), n * (r + 1)] weight matrix of algebraic equation.
        - value: <np.array> [n * (r + 1)] value array of algebra equation.
    '''
    weight = []
    value = []
    # Partition Points
    for i in range(n):
        start_idx = i * (r - 1)
        end_idx = (i + 1) * (r - 1)
        # Collocation Points
        for j, xi in enumerate(collocation[start_idx:end_idx]):
            coll_idx = i * (r - 1) + j
            weight.append(substitute1d(xi, coll_idx, n, r, 0) + substitute1d(xi, coll_idx, n, r, 1) + substitute1d(xi, coll_idx, n, r, 2))
            value.append([f(xi)]) # I dont know why but should be this
        # C1 Continuous
        if i == n - 1: continue
        c1_value, c1_dev = continuous1d(partition[i + 1], i + 1, n, r)
        weight.append(c1_value)
        weight.append(c1_dev)
        value.append([0])
        value.append([0])
    # Boundary Condition
    left_bd, right_bd = boundary1d(n, r)
    weight.insert(0, left_bd)
    weight.append(right_bd)
    value.insert(0, [b1])
    value.append([b2])
    return np.array(weight), np.array(value)


def substitute1d(x: float, k: int, n: int, r: int, ord: int) -> np.array:
    ''' Generator the Equation of Substituting Collocation Value into the Original Equation
    
    Args:
        - x: <float> value of the collocation point gonna to use. 
        - k: <int> index of the collocation point gonna to use. 
        - n: <int> number of partition. 
        - r: <int> order of polynomial. 
        - ord: <int> order of deverate, should be non-negetive. 
    '''
    result = np.zeros(n * (r + 1))
    poly_idx = int(k / (r - 1))
    for i in range(r + 1):
        start_idx = poly_idx * (r + 1)
        temp = x ** (i - ord)
        for j in range(ord):
            temp *= i - j
        result[start_idx + i] = temp
    return result


def continuous1d(x: float, k: int, n: int, r: int) -> tuple[np.array, np.array]:
    ''' Generate the Equation of C1 Continuouse
    
    Args:
        - x: <float> value of the partition point gonna to use. 
        - k: <int> index of the partition point gonna to use. 
        - n: <int> number of partition. 
        - r: <int> order of polynomial. 
    Returns:
        - value: <np.array> [n * (r + 1)] value equal equiation
        - dev: <np.array> [n * (r + 1)] deverate equal equition
    '''
    value = np.zeros(n * (r + 1))
    dev = np.zeros(n * (r + 1))
    # Previous Polynomial
    poly_idx = (k - 1) * (r + 1)
    for i in range(r + 1):
        value[poly_idx + i] = x ** i
        dev[poly_idx + i] = i * x ** (i - 1)
    # Next Polynomial
    poly_idx = k * (r + 1)
    for i in range(r + 1):
        value[poly_idx + i] = - x ** i
        dev[poly_idx + i] = - i * x ** (i - 1)
    return value, dev


def boundary1d(n: int, r: int):
    ''' Generate the Equation of Boundary Condition
    
    Args:
        - n: <int> number of partition. 
        - r: <int> order of polynomial. 
    Returns:
        - left: <np.array> [n * (r + 1)] left boundary condition equation.
        - right: <np.array> [n * (r + 1)] right boundary condition equation.
    '''
    left = np.zeros(n * (r + 1))
    right = np.zeros(n * (r + 1))
    # Left Boundary Condition
    idx = 0
    for i in range(r + 1):
        left[i] = 0 ** i
    # Right Boundary Condition
    idx = (n - 1) * (r + 1)
    for i in range(r + 1):
        right[idx + i] = 1 ** i
    return left, right
