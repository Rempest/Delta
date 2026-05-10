# 🚀 DeltaPrime

DeltaPrime is an experimental AI-driven drone perception and control system that combines:

- 👁️ Computer Vision
- 🎯 Object Detection
- 🧠 Scene Analysis
- ⚡ Decision Making
- 🌍 Physics Simulation
- 🛩️ Drone Dynamics
- ⏱️ Real-Time Control

The project uses a hybrid architecture:

- **Python** → AI / Vision Layer
- **C++** → Physics / Control Layer

---

# 📂 Architecture

```text
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
│   ├── CmakeList.txt
│   ├── Delta_core.py
│   └── physics_bridge.py
│
├── Physics/             # Physics and control layer (C++)
│   ├── 
│   ├── main.cpp
│   ├── PID.h
│   ├── Dynamics.h
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