# Setup Instructions

## Prerequisites

- Python 3.x
- Gazebo (version 11 or later)
- ArduPilot (latest version)

## Installing Dependencies

1. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
2. Follow the ArduPilot SITL documentation to set up the software in the loop:
   ```bash
   https://ardupilot.org/dev/docs/SITL-setup-landingpage.html
3. Launch Gazebo:
   ```bash
    gazebo --verbose ~/ardupilot/Tools/autotest/ArduPilotPlugins/worlds/iris_arducopter_runway.world
  
