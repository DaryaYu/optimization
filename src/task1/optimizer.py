import numpy as np

from src.task1.config import N_STATIONS
from src.task1.visualizer import plot_representation
from src.task1.evaluator import estimate_coverage


def optimize_verlet(centers, radii, space_limit=10.0, iterations=200, dt=0.1, damping=0.93, radius_coef=0.9):

    pos = centers.copy()
    prev_pos = centers.copy()
    best_coverage = estimate_coverage(centers, radii)
    
    for step in range(iterations):
        acc = np.zeros_like(pos)
        
        # Calculation of mutual repulsion of circles
        for i in range(N_STATIONS):
            for j in range(N_STATIONS):
                if i == j:
                    continue
                
                delta = pos[i] - pos[j]
                dist = np.linalg.norm(delta)
                min_dist = radii[i] + radii[j]
                
                # The force of repulsion, if circles intersect
                if dist < min_dist:
                    if dist == 0:  # To avoid 0 division
                        direction = np.array([np.cos(i), np.sin(i)])
                        overlap = min_dist
                    else:
                        direction = delta / dist
                        overlap = min_dist - dist
                    
                    # The repulsion force is proportional to the depth of overlap of the circles
                    acc[i] += direction * overlap * 2.5
        
        # Verlet calculation: x_new = x_curr + (x_curr - x_prev) * damping + a * dt^2
        current_pos = pos.copy()
        pos = current_pos + (current_pos - prev_pos) * damping + acc * (dt ** 2)
        prev_pos = current_pos
        
        # Boundary constraints
        for i in range(N_STATIONS):
            pos[i][0] = np.clip(pos[i][0], 0.0 + radius_coef * radii[i], space_limit - radius_coef * radii[i])
            pos[i][1] = np.clip(pos[i][1], 0.0 + radius_coef * radii[i], space_limit - radius_coef * radii[i])

        # Plot results
        plot_representation(pos, radii, f'Visual Representation {step + 1}')

        # Coverage estimation
        coverage = estimate_coverage(pos, radii)
        print(f'Iteration: {step + 1} Coverage: {coverage}')
        if coverage > best_coverage:
            best_coverage = coverage.copy()
            best_pos = pos.copy()

    return best_pos

    