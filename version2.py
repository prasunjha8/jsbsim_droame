import jsbsim
import time

# Create a JSBSim instance
sim = jsbsim.FGFDMExec(None)
sim.set_debug_level(0)  # Optional: 0 = no debug, 1 = verbose

# Set the aircraft and initial condition
sim.load_model("c172p")  # Load Cessna 172P
sim.set_property_value("ic/alt-ft", 1000)  # Initial altitude
sim.set_property_value("ic/u-fps", 100)    # Forward speed
sim.set_property_value("ic/psi-deg", 0)    # Heading
sim.set_property_value("ic/theta-deg", 0)  # Pitch
sim.set_property_value("ic/phi-deg", 0)    # Roll
sim.run_ic()  # Initialize the aircraft with the initial conditions

# Set controls
sim.set_property_value("fcs/throttle-cmd-norm", 0.8)  # 80% throttle
sim.set_property_value("fcs/elevator-cmd-norm", 0.0)  # Neutral elevator
sim.set_property_value("fcs/aileron-cmd-norm", 0.0)   # Neutral aileron
sim.set_property_value("fcs/rudder-cmd-norm", 0.0)    # Neutral rudder

# Run the simulation for 10 seconds at 100Hz (timestep ~0.01s)
dt = 0.01
for i in range(1000):
    sim.run()
    altitude = sim.get_property_value("position/h-sl-ft")
    airspeed = sim.get_property_value("velocities/vc-kts")
    pitch = sim.get_property_value("attitude/pitch-deg")
    print(f"Time: {i*dt:.2f}s | Altitude: {altitude:.2f} ft | Airspeed: {airspeed:.2f} kts | Pitch: {pitch:.2f} deg")
    time.sleep(dt)  # Optional: to simulate real time

print("Simulation complete.")
