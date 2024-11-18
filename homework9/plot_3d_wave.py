import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_3d_wave():
    """
    This function creates a 3D surface plot of the function z(x, y) = sin(sqrt(x^2 + y^2)),
    which creates a wave pattern.
    
    The plot displays the surface in 3D with appropriate labels, title, and colormap.
    
    Outputs: None (Displays the plot)
    """
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    
    # Create meshgrid for 2D grid points
    X, Y = np.meshgrid(x, y)
    
    # Compute Z values for each point in the grid
    Z = np.sin(np.sqrt(X**2 + Y**2))
    
    fig = plt.figure(figsize=(8, 6))
    
    # Create a 3D axis
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot the surface
    surface = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', label='z(x, y) = sin(sqrt(x^2 + y^2))')
    
    ax.set_title("3D Surface Plot of $z(x, y) = \sin(\sqrt{x^2 + y^2})$", fontsize=16)
    ax.set_xlabel('X-axis', fontsize=12)
    ax.set_ylabel('Y-axis', fontsize=12)
    ax.set_zlabel('Z-axis', fontsize=12)
    
    # Add a color bar to indicate the range of values for Z
    fig.colorbar(surface, ax=ax, shrink=0.5, aspect=5)
    
    ax.legend(loc='best')
    
    plt.show()
