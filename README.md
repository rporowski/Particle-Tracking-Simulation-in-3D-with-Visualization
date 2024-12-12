# Particle-Tracking-Simulation-in-3D-with-Visualization
This repository contains a Python-based simulation of particle tracking through a series of detector planes. The simulation models particles emitted from a single source, which propagate along straight trajectories. The system is designed to mimic a simplified particle collision experiment with detectors placed at fixed intervals along the z-axis.
Features
Particle Generation:
Particles are emitted uniformly in spherical angles (theta and phi) from the origin (0, 0, 0).
Trajectories are simulated in 3D space as straight lines.
Detector Plane Setup:

Six detector planes perpendicular to the z-axis are placed at user-defined positions (default: 5, 10, 15, 20, 25, and 30 cm).
Each plane has a 10x10 cm² area.
Trajectory Filtering:

Particles that intersect all six planes are recorded for further analysis.
Intersection points (x, y, z) are calculated for valid trajectories.
Visualization:

A 3D animation of the particle trajectories is created using matplotlib.animation.
Each trajectory is progressively added to the visualization to simulate real-time particle tracking.
Simulation Output
The simulation generates:

3D Animation: A video (particle_simulation.mp4) showing the particle trajectories intersecting the detector planes.
Tracking Data: Coordinates of intersection points for valid trajectories are stored during the simulation and can be extended for further processing, such as machine learning-based trajectory reconstruction.
Example Visualization

Example: A simulation of particles propagating through six detector planes.

Future Enhancements
Data Export: Save intersection points in CSV format for external analysis.
Machine Learning Integration: Implement tracking algorithms to reconstruct trajectories from intersection points.
Realistic Physics: Incorporate noise and particle scattering for a more realistic simulation.
Contributing
Contributions are welcome! Feel free to open issues, fork the repository, and submit pull requests.

License
This project is licensed under the MIT License. See the LICENSE file for details.
