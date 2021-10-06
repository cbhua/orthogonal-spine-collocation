import numpy as np
from numpy.polynomial.legendre import leggauss


def collocation1d(n:int, r:int) -> tuple[np.array, np.array]:
    ''' Get One Variable Partition and Collocation Points on [0, 1]

    Args:
        - n: <int> number of partition.
        - r: <int> dimension of polynomials. 
    Returns:
        - partition: <np.array> [n + 1] location of partition points. 
        - collocation: <np.array> [n * (r - 1)] location of collocation points.
    '''
    # Partition Points
    partition = np.linspace(0., 1., num=n + 1, endpoint=True)
    # Collocation Points
    gaussian = (np.array(leggauss(r - 1)[0]) + 1)/2
    collocation = []
    for i in range(n):
        for j in range(r - 1):
            collocation.append(partition[i] + 1/n * gaussian[j])
    collocation = np.squeeze(np.array(collocation))
    return partition, collocation


if __name__ == '__main__':
    print(collocation1d(3, 3))
