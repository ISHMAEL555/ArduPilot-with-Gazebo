Add your DroneKit Python script for taking off and landing. Here’s an example:

  from dronekit import connect, VehicleMode
import time

# Connect to the Vehicle
vehicle = connect('udp:127.0.0.1:14550', wait_ready=True)

def basic_takeoff(altitude):
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True
    time.sleep(2)
    vehicle.simple_takeoff(altitude)

    while True:
        print("Reached Height =", vehicle.location.global_relative_frame.alt)

        if vehicle.location.global_relative_frame.alt >= (altitude - 1.5):
            print("Target altitude reached.")
            break
        time.sleep(1)

# Takeoff and landing example
takeoff_altitude = 10
basic_takeoff(takeoff_altitude)

# Land the vehicle
vehicle.mode = VehicleMode('LAND')
print("Landing the Vehicle")

# Close the vehicle object before exiting
vehicle.close()
