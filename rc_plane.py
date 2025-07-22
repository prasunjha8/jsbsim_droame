import jsbsim

# Initialize JSBSim
sim = jsbsim.FGFDMExec(root_dir="/Users/prasunjha/jsbsim", debug_level=0)


# Load aircraft model
sim.load_model("rc_plane")

# Set initial conditions
sim.set_property_value("ic/h-sl-ft", 1000.0)
sim.set_property_value("ic/vc-kts", 60.0)
sim.set_property_value("ic/u-fps", 80.0)         # forward velocity in body axis
sim.set_property_value("ic/beta-deg", 0.0)
sim.set_property_value("ic/phi-deg", 0.0)
sim.set_property_value("ic/theta-deg", 5.0)
sim.set_property_value("ic/psi-deg", 0.0)
sim.set_property_value("ic/p-rad_sec", 0.0)
sim.set_property_value("ic/q-rad_sec", 0.0)
sim.set_property_value("ic/r-rad_sec", 0.0)

# Initialize the simulation
sim.run_ic()

# Set control inputs
sim.set_property_value("fcs/throttle-cmd-norm", 0.8)
sim.set_property_value("fcs/elevator-cmd-norm", 0.0)
sim.set_property_value("fcs/aileron-cmd-norm", 0.0)
sim.set_property_value("fcs/rudder-cmd-norm", 0.0)

# Output header
print("Time (s) | Altitude (ft) | Speed (kts) | Pitch (deg) | Roll (deg)")
print("-" * 65)

# Run simulation
for i in range(100):
    if not sim.run():
        print("Simulation ended early")
        break
    if i % 10 == 0:
        print(f"{sim.get_sim_time():8.2f} | {sim.get_property_value('position/h-sl-ft'):11.2f} | "
              f"{sim.get_property_value('velocities/vc-kts'):9.2f} | "
              f"{sim.get_property_value('attitude/theta-deg'):9.2f} | "
              f"{sim.get_property_value('attitude/phi-deg'):8.2f}")

print("\nSimulation completed!")
