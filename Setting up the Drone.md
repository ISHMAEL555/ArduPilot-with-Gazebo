# Prelude: Forging the Weapon

In the coding forge of Python, we craft our tools like weapons for an impending aerial battle. The time has come to summon our allies, `dronekit` and `time`, to arm ourselves for the skies. With a stroke of code, we bring forth the components needed to control our flying war machines.
    
    # Import Necessary Packages
    from dronekit import connect, VehicleMode, LocationGlobalRelative
    import time
These lines are no ordinary imports—they are the armory's keystones, equipping us with the power to manipulate the battlefield. The dronekit package gives us command over our airborne warriors, while time ensures the operations unfold with military precision, each maneuver executed in the beat of our war drum.
# Act I: Establishing Command – The Battle Link

The battle cannot begin without control. We must first establish an unbreakable link with our drone warriors, forging the communication channel that will direct their every movement. The `connect()` function becomes our war horn, signaling the commencement of operations.

    # Connecting the Vehicle
    vehicle = connect('udpin:127.0.0.1:14551', baud=115200)
# Act II: Entering Combat Mode – GUIDED Mode Activation
The warriors are linked, but they are not yet in formation. The call to arms is issued by shifting to GUIDED mode, preparing the drones to receive direct orders from the battlefield commander.
    
    vehicle.mode = VehicleMode("GUIDED")

The VehicleMode() spell transitions our war machines into combat readiness, like soldiers standing at attention, awaiting the command to charge. They are now listening, awaiting our signal to engage in the fight.
# Act III: Arming the War Machines – Weapons Ready
No soldier goes to war without their weapons armed. We must prepare the drones for battle by activating their motors, signaling the readiness to unleash havoc from the skies.
    
    vehicle.armed = True
    time.sleep(2)

With motors armed, our drones are transformed into lethal instruments, engines growling like battle cries. The brief pause allows us to ensure that all systems are primed, every weapon locked and loaded for the first strike.
# Act IV: The Assault Begins – Taking to the Sky
The moment is upon us. With the simple_takeoff() command, our drones ascend from the ground, rising like an army of airborne predators ready to dominate the battlefield.

    # Takeoff the Vehicle 
    takeOffAltitude = 10
    vehicle.simple_takeoff(takeOffAltitude)

The altitude serves as our vantage point, the high ground from which we command the air. Each meter climbed sharpens the advantage, setting the stage for a deadly dance among the clouds.
# Act V: Vigilance in the Sky – Maintaining Formation
As the drones hold their positions in the air, the battle script stays vigilant, monitoring their altitude to ensure the formation remains intact. The loop acts as a watchful sentinel, keeping our airborne warriors within the designated strike zone.

    while True:
    print("Reached Height =", vehicle.location.global_relative_frame.alt)

    if vehicle.location.global_relative_frame.alt >= (takeOffAltitude - 1.5):
        break
    time.sleep(1)

Every beat of the war drum echoes in the code's loop, each check a scouting report from the front lines, ensuring our formation remains unbroken.
# Finale: The Retreat – Returning to Base
The mission concludes, and the order is given to retreat. With a shift in mode, our drones descend from the battlefield, returning to base in a controlled withdrawal.

    vehicle.mode = VehicleMode('LAND')

The once-lethal machines now glide back to Earth, the weapons deactivated, but their readiness undiminished. They descend not in defeat, but in anticipation of the next call to war.
