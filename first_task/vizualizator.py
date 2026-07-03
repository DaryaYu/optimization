import matplotlib.pyplot as plt
import numpy as np


def plot_representation(
        space_limit: float,
        centers: np.ndarray, 
        radii: np.ndarray, 
        title: str = "Visual Representation"
        ):
    
    plt.figure(figsize=(7, 7))
    ax = plt.gca()
    ax.set_xlim(0, space_limit)
    ax.set_ylim(0, space_limit)
    ax.set_aspect('equal')
    plt.grid(True, linestyle='--', alpha=0.5)
    
    for i, (center, r) in enumerate(zip(centers, radii)):
        circle = plt.Circle(
            center, 
            r, 
            color='royalblue', 
            alpha=0.25, 
            edgecolor='darkblue', 
            lw=1.2
        )
        ax.add_patch(circle)
        plt.plot(
            center[0], 
            center[1], 
            'ro', 
            markersize=4
        )
        plt.text(
            center[0], 
            center[1] + 0.15, 
            str(i+1), 
            fontsize=9, 
            weight='bold', 
            ha='center'
        )
        
    plt.title(title, fontsize=12, weight='bold')
    plt.show()