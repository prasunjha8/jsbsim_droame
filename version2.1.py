import jsbsim
import time
import matplotlib.pyplot as plt

# Create JSBSim instance
sim = jsbsim.FGFDMExec(None)
sim.set_debug_level(0)

# Load aircraft and initial conditions
sim.load_model("c172p")
sim.set_property_value("ic/alt-ft", 1000)
sim.set_property_value("ic/u-fps", 100)
sim.set_property_value("ic/psi-deg", 0)
sim.set_property_value("ic/theta-deg", 0)
sim.set_property_value("ic/phi-deg", 0)
sim.run_ic()

# Set control inputs
sim.set_property_value("fcs/throttle-cmd-norm", 0.8)
sim.set_property_value("fcs/elevator-cmd-norm", 0.0)
sim.set_property_value("fcs/aileron-cmd-norm", 0.0)
sim.set_property_value("fcs/rudder-cmd-norm", 0.0)

# Simulation loop parameters
dt = 0.01  # Time step
steps = 1000  # Number of steps = 10 seconds

# Data storage
time_data = []
altitude_data = []
airspeed_data = []
pitch_data = []

# Run simulation
for i in range(steps):
    sim.run()
    current_time = i * dt
    time_data.append(current_time)
    altitude_data.append(sim.get_property_value("position/h-sl-ft"))
    airspeed_data.append(sim.get_property_value("velocities/vc-kts"))
    pitch_data.append(sim.get_property_value("attitude/pitch-deg"))
    time.sleep(dt)  # Optional

print("Simulation complete. Now plotting...")

# Plotting the results
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(time_data, altitude_data, label="Altitude (ft)", color="blue")
plt.ylabel("Altitude (ft)")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(time_data, airspeed_data, label="Airspeed (kts)", color="green")
plt.ylabel("Airspeed (kts)")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(time_data, pitch_data, label="Pitch (deg)", color="red")
plt.xlabel("Time (s)")
plt.ylabel("Pitch (°)")
plt.grid(True)

plt.tight_layout()
plt.suptitle("JSBSim Cessna 172P Flight Data", y=1.02)
plt.show()
