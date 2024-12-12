import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Parameters
N = 1000  # Number of particles
z_planes = [5, 10, 15, 20, 25, 30]  # z-coordinates of the detector planes
detector_size = 10  # Detector plane dimensions (10x10 cm)

# Generate random directions for particles
theta = np.random.uniform(0, 2 * np.pi, N)  # Azimuthal angles
phi = np.random.uniform(0, np.pi / 2, N)  # Polar angles
dx = np.sin(phi) * np.cos(theta)
dy = np.sin(phi) * np.sin(theta)
dz = np.cos(phi)

# Store intersection points
intersection_points = []
for i in range(N):
    particle_points = []
    for z in z_planes:
        t = z / dz[i]
        x = t * dx[i]
        y = t * dy[i]
        if abs(x) <= detector_size / 2 and abs(y) <= detector_size / 2:
            particle_points.append((x, y, z))
    if len(particle_points) == len(z_planes):
        intersection_points.append(particle_points)

# Initialize the figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim(-detector_size / 2, detector_size / 2)
ax.set_ylim(-detector_size / 2, detector_size / 2)
ax.set_zlim(min(z_planes), max(z_planes))
ax.set_xlabel("X (cm)")
ax.set_ylabel("Y (cm)")
ax.set_zlabel("Z (cm)")
plt.title("Particle Trajectories Simulation")

# Animation function
def update(frame):
    ax.clear()
    ax.set_xlim(-detector_size / 2, detector_size / 2)
    ax.set_ylim(-detector_size / 2, detector_size / 2)
    ax.set_zlim(min(z_planes), max(z_planes))
    ax.set_xlabel("X (cm)")
    ax.set_ylabel("Y (cm)")
    ax.set_zlabel("Z (cm)")
    plt.title("Particle Trajectories Simulation")
    
    # Plot trajectories up to the current frame
    for i in range(min(frame + 1, len(intersection_points))):
        x_vals, y_vals, z_vals = zip(*intersection_points[i])
        ax.plot(x_vals, y_vals, z_vals, marker='o')

# Create the animation
ani = FuncAnimation(fig, update, frames=len(intersection_points), interval=200, repeat=False)

# Save the animation as a video or display it
ani.save("particle_simulation.mp4", writer="ffmpeg", dpi=300)  # Save as MP4
plt.show()
