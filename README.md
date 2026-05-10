# DeltaPrime
DeltaPrime is an experimental AI-driven drone perception and control system that combines:
Computer Vision
Object Detection
Scene Analysis
Decision Making
Physics Simulation
Drone Dynamics
Real-Time Control
The project is built with a hybrid architecture using:
Python → AI / Vision Layer
C++ → Physics / Control Layer
Architecture
Plain text
DeltaPrime/
│
├── Bridge/              # AI perception layer (Python)
│   ├── Delta_YOLO.py
│   ├── Delta_YOLO_analyze.py
│   ├── Delta_decision.py
│   ├── Delta_Sensors.py
│   └── Delta_brain.py
│
├── Core/                # Central system logic (C++)
│   ├── main.cpp
│   ├── DeltaBrain.cpp
│   └── DeltaBrain.h
│
├── Physics/             # Physics and control layer (C++)
│   ├── include/
│   ├── src/
│   ├── PID.cpp
│   ├── Dynamics.cpp
│   ├── Planner.cpp
│   └── Sensors.cpp
│
├── config/
│   └── config.yaml
│
├── .devcontainer/
│   └── devcontainer.json
│
├── CMakeLists.txt
├── requirements.txt
├── README.md
└── LICENSE
Main Goals
DeltaPrime is designed to evolve step-by-step:
DeltaPrime V1
YOLO object detection
Basic target selection
Scene analysis
Decision making
Safety override system
DeltaPrime V2
Fine-tuned YOLO on drone datasets:
VisDrone
UAVDT
xView
DeltaPrime V3
PX4 integration
Real drone communication
Flight control bridge
DeltaPrime V4
Voice interaction system
Speech recognition
AI assistant integration
DeltaPrime V5
ROS modules
Distributed robotic architecture
Multi-node communication
Technologies
AI / Computer Vision
Python
OpenCV
Ultralytics YOLO
NumPy
Physics / Control
C++
PID Controller
Drone Dynamics
Aerodynamic Calculations
Future Integrations
PX4
ROS2
Kalman Filter
Trajectory Planning
Sensor Fusion
Current Features
Vision System
Real-time object detection
Target prioritization
Bounding-box visualization
Decision System
LEFT / RIGHT / FORWARD logic
Target-based movement decisions
Sensor safety override
Sensor System
Obstacle detection logic
Safe path selection
Emergency stop handling
Physics Layer
Drone state simulation
Velocity and acceleration updates
Drag and thrust calculations
Example Pipeline
Plain text
Camera Input
    ↓
YOLO Detection
    ↓
Scene Analysis
    ↓
Decision System
    ↓
Safety Layer
    ↓
Physics & Control
    ↓
Drone Action
Installation
Clone Repository
Bash
git clone <repository-url>
cd DeltaPrime
Python Dependencies
Install Python requirements:
Bash
pip install -r requirements.txt
Build C++ Core
Bash
mkdir build
cd build

cmake ..
make
Run DeltaPrime
Python Vision Layer
Bash
python Bridge/Delta_brain.py
C++ Physics Layer
Bash
./DeltaPrime
Datasets
Planned datasets for training:
VisDrone
UAVDT
xView
Philosophy
DeltaPrime is not intended to be “just another YOLO wrapper”.
The long-term goal is to create a modular AI drone system capable of:
understanding visual environments,
estimating physical behavior,
planning movement,
reacting safely,
and eventually integrating with real robotic ecosystems.
License
This project is licensed under the MIT License.
See the LICENSE file for details.