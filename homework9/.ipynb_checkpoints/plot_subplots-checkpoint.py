import numpy as np
import matplotlib.pyplot as plt

def plot_side_by_side():
    """
    This function creates two subplots side by side (horizontal):
    - Left subplot: h(x) = cos(x)
    - Right subplot: k(x) = sin(x)
    
    The domain of x is [0, 2 * pi].
    It includes a title, axis labels, and the functions plotted on each subplot.
    
    Outputs: None (Displays the plot)
    """
    x = np.linspace(0, 4 * np.pi, 100)
    
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    
    axes[0].plot(x, np.cos(x), color='red', label='h(x) = cos(x)')
    axes[0].set_title('Plot of h(x) = cos(x)', fontsize=14)
    axes[0].set_xlabel('x', fontsize=12)
    axes[0].set_ylabel('h(x)', fontsize=12)
    axes[0].legend()
    
    axes[1].plot(x, np.sin(x), color='blue', label='k(x) = sin(x)')
    axes[1].set_title('Plot of k(x) = sin(x)', fontsize=14)
    axes[1].set_xlabel('x', fontsize=12)
    axes[1].set_ylabel('k(x)', fontsize=12)
    axes[1].legend()
    
    # Adjust the layout to avoid overlap
    plt.tight_layout()
    
    plt.show()


def plot_top_bottom():
    """
    This function creates two subplots stacked vertically (top to bottom):
    - Top subplot: h(x) = cos(x)
    - Bottom subplot: k(x) = sin(x)
    
    The domain of x is [0, 2 * pi].
    It includes a title, axis labels, and the functions plotted on each subplot.
    
    Outputs: None (Displays the plot)
    """
    x = np.linspace(0, 4 * np.pi, 100)
    
    fig, axes = plt.subplots(2, 1, figsize=(8, 10))
    
    # Plot h(x) = cos(x) on the top subplot
    axes[0].plot(x, np.cos(x), color='red', label='h(x) = cos(x)')
    axes[0].set_title('Plot of h(x) = cos(x)', fontsize=14)
    axes[0].set_xlabel('x', fontsize=12)
    axes[0].set_ylabel('h(x)', fontsize=12)
    axes[0].legend()
    
    # Plot k(x) = sin(x) on the bottom subplot
    axes[1].plot(x, np.sin(x), color='blue', label='k(x) = sin(x)')
    axes[1].set_title('Plot of k(x) = sin(x)', fontsize=14)
    axes[1].set_xlabel('x', fontsize=12)
    axes[1].set_ylabel('k(x)', fontsize=12)
    axes[1].legend()
    
    plt.tight_layout()
    
    plt.show()

import numpy as np
import matplotlib.pyplot as plt


