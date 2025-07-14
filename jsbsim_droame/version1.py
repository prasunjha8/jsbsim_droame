import jsbsim
import matplotlib.pyplot as plt

# Initialize JSBSim
sim = jsbsim.FGFDMExec(None)
sim.set_debug_level(0)

# Load aircraft model
if not sim.load_model("c172p"):
    raise RuntimeError("Failed to load aircraft model.")

# Initialize initial conditions
sim.run_ic()

# Get timestep
dt = sim.get_delta_t()
print(f"Simulation timestep: {dt} seconds")

# Data logging lists
time_log = []
altitude_log = []
pitch_log = []
speed_log = []

# Simulation loop
for i in range(300):
    # Control inputs
    sim["fcs/throttle-cmd-norm"] = 0.8    # 80% throttle
    sim["fcs/elevator-cmd-norm"] = 5.0   # Slight pitch up
    sim["fcs/rudder-cmd-norm"] = 0.0       # No rudder

    # Step the simulation
    sim.run()

    # Read values
    altitude = sim["position/h-sl-ft"]                      # Altitude in feet
    pitch_rad = sim["attitude/pitch-rad"]                   # Pitch in radians
    pitch_deg = pitch_rad * 57.2958                         # Convert to degrees
    speed = sim["velocities/vc-kts"]                        # Calibrated airspeed in knots

    # Log values
    time_log.append(i * dt)
    altitude_log.append(altitude)
    pitch_log.append(pitch_deg)
    speed_log.append(speed)

# Plotting
plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.plot(time_log, altitude_log, label="Altitude")
plt.ylabel("Altitude (ft)")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(time_log, pitch_log, label="Pitch", color="orange")
plt.ylabel("Pitch (deg)")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(time_log, speed_log, label="Speed", color="green")
plt.ylabel("Speed (kt)")
plt.xlabel("Time (s)")
plt.grid(True)

plt.tight_layout()
plt.show()
