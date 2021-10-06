import numpy as np
import matplotlib.pyplot as plt


def plot_collocation1d(partition, collocation, n, r):
    ''' Plot Partition and Collocation Points'''
    with plt.style.context('bmh'):
        font = {'color': 'darkred', 'size': 12, 'family': 'serif'}
        font_legend = {'size': 12, 'family': 'serif'}
        fig, axs = plt.subplots(1, figsize=(12, 4))
        axs.scatter(collocation, np.zeros(n * (r - 1)), label='Collocation Points', marker='o', color='tomato')
        axs.scatter(partition, np.zeros(n + 1), label='Partition Points', marker='o', color='blue')
        axs.set_xlim([-0.1, 1.1])
        axs.set_ylim([-1.0, 1.0])
        axs.set_xlabel('x', fontdict=font)
        axs.set_ylabel('y', fontdict=font)
        axs.set_title('Collocation Points', fontdict=font)
        axs.legend(loc='upper right', prop=font_legend)
        labels = axs.get_xticklabels() + axs.get_yticklabels()
        [label.set_fontname('serif') for label in labels]

def plot_simulation1d(position, simulation, ground_truth, partition, collocation, n, r):
    with plt.style.context('bmh'):
        font = {'color': 'darkred', 'size': 12, 'family': 'serif'}
        font_legend = {'size': 12, 'family': 'serif'}
        fig, axs = plt.subplots(1, figsize=(12, 4))
        axs.scatter(collocation, np.zeros((n) * (r - 1)), label='Collocation Points', marker='o', color='tomato')
        axs.scatter(partition, np.zeros(n + 1), label='Partition Points', marker='o', color='blue')
        axs.plot(position, simulation, label='Solver', color='red', alpha=1)
        axs.plot(position, ground_truth, label='Ground Truth', color='blue', alpha=1)
        axs.set_xlim([-0.1, 1.1])
        axs.set_xlabel('x', fontdict=font)
        axs.set_ylabel('y', fontdict=font)
        axs.set_title('Solver Result', fontdict=font)
        axs.legend(loc='upper right', prop=font_legend)
        labels = axs.get_xticklabels() + axs.get_yticklabels()
        [label.set_fontname('serif') for label in labels]
