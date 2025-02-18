# Mass with Friction Simulation using Kalman Filter and Full-State Feedback Control

## Overview
This Jupyter Notebook implements a simulation of a mass with friction, utilizing a **Kalman Filter** for state estimation and **Full-State Feedback Control** for trajectory tracking. The simulation uses **Runge-Kutta 4th order (RK-4)** integration to model the system dynamics and incorporates sensor noise to reflect real-world measurements.

## Features
- **Kalman Filter**: Estimates the position and velocity of the mass from noisy sensor measurements.
- **Full-State Feedback Control**: Adjusts the control force to track a desired target state.
- **Runge-Kutta 4th Order (RK-4) Integration**: Numerically solves the system’s differential equations.
- **Plotly Visualization**: Provides interactive plots of estimated state, measurements, and control performance.

## Dependencies
Ensure you have the following Python packages installed:

```bash
pip install numpy plotly
```

## Files in this Repository
- **Threecontroltopics.ipynb**: The Jupyter Notebook containing the implementation.
- **README.md**: This documentation file explaining the notebook's purpose and usage.

## How to Run
1. Open the Jupyter Notebook using:
   ```bash
   jupyter notebook Threecontroltopics.ipynb
   ```
2. Run all cells sequentially to execute the simulation.
3. The output plots will visualize:
   - The estimated position and velocity over time.
   - The noisy sensor measurements.
   - The applied control force and system response.

## Key Functions
### `kalman_filter(state_est, control_force, P_est, measurement, A, B, C, Q, R)`
Performs the Kalman filtering algorithm with **prediction and measurement update** steps.

### `full_state_feedback_control(target_state, current_state, K)`
Implements **state feedback control** to compute the necessary control force.

### `rk4_step(func, t, state, dt, friction, control_force)`
Integrates the system dynamics using the **Runge-Kutta 4th order** method.

### `sensor_eq(state, noise_std=1.0)`
Simulates a sensor by adding **Gaussian noise** to the true state.

## Visualization
The notebook generates interactive plots using **Plotly**, showing:
- The estimated position (`state_est[0]`) and velocity (`state_est[1]`).
- The noisy **sensor measurements**.
- The **target position** as a reference.

## Future Improvements
- Extend to **nonlinear** system models.
- Implement **adaptive noise covariance tuning** for better estimation.
- Add **control constraints** to model real-world actuators.

## License
This project is provided under the MIT License. Feel free to modify and use it as needed!

---

For questions or suggestions, please reach out!

