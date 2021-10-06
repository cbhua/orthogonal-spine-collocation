import numpy as np
def polynomial1d(partition: np.array, para: np.array, n: int, r: int, num: int) -> tuple[np.array, np.array]:
    ''' Get Value in [0, 1] of Given Polynomial
    
    Args:
        - partition: <np.array> [n + 1]: partition points
        - para: <np.array> [n * (r + 1)] weight parameter for polynomial.
        - n: <int> number of partition. 
        - r: <int> order of polynomial. 
        - num: <int> number of sample points.
    Returns: 
        - position: <np.array> [n * num] position of polynomial value in [0, 1]
        - result: <np.array> [n * num] value of polynomial in [0, 1]
    '''
    position = np.linspace(0, 1, num=n * num, endpoint=False)
    result = np.array([])
    for i in range(n):
        x = np.linspace(partition[i], partition[i + 1], num=num, endpoint=False)
        y = np.zeros(num)
        for j in range(r + 1):
            y += para[i * (r + 1) + j] * x ** j
        result = np.concatenate((result, y))
    return position, result
