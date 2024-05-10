import os
import shutil
import numpy as np
import matplotlib.pyplot as plt
from to_gif import to_gif

def transform_coordinates(x, y, schwarzschild_radius):
    """Transform coordinates to simulate spacetime curvature."""
    r = np.sqrt(x**2 + y**2)
    safe_r = np.maximum(r, schwarzschild_radius + 0.01)
    warp_factor = 1 - schwarzschild_radius / safe_r
    return x * warp_factor, y * warp_factor

def generate_plots(frames, max_radius, width):
    """Generate and save plots depicting spacetime curvature."""
    for frame_index in range(frames):
        schwarzschild_radius = frame_index / (frames / max_radius)
        x = np.linspace(-2, 2, width)
        y = np.linspace(-2, 2, width)
        X, Y = np.meshgrid(x, y)
        Xt, Yt = transform_coordinates(X, Y, schwarzschild_radius)

        plt.figure(figsize=(14, 9))
        for i in range(width):
            plt.plot(Xt[i, :], Yt[i, :], "black", linewidth=0.2)
            plt.plot(Xt[:, i], Yt[:, i], "black", linewidth=0.2)

        plt.gca().set_aspect("equal", adjustable="box")
        plt.axis("off")
        plt.title(f"Spacetime Curvature at Radius {schwarzschild_radius:.2f}")
        
        plt.savefig(f"output/output_{frame_index:03}.png")
        plt.close()

def setup_directory(directory="output"):
    shutil.rmtree(directory, ignore_errors=True)
    os.makedirs(directory, exist_ok=True)

def main():
    max_radius = 1.2
    frames = 100
    duration = 30
    grid_width = 50
    

    setup_directory()
    generate_plots(frames, max_radius, grid_width)
    to_gif(duration=duration)

if __name__ == "__main__":
    main()
