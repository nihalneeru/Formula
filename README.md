# ApexAI

ApexAI redefines racing by integrating neural networks into a racing simulation environment, providing an interactive platform for simulating car races, choosing cars and tracks, creating custom tracks, and observing AI-controlled cars evolve over time.

## Overview

"ApexAI" leverages Python and several libraries, including Streamlit, PyDeck, PyMongo, and NEAT-Python, to offer a comprehensive racing simulation platform. Users can select cars with distinct specifications, choose from various iconic racing tracks, design custom tracks, and watch as neural network-based AI competes, learning and improving over time. The project aims to bridge the gap between gaming, AI education, and motorsport engineering, offering insights into how machine learning can influence decision-making in high-speed racing conditions.

### Features
- **Car Selection**: Choose from a variety of cars, each with unique specifications and capabilities.
- **Track Selection**: Select from world-renowned racing tracks or create custom tracks tailored to specific challenges.
- **AI Simulation**: Utilize the NEAT (NeuroEvolution of Augmenting Topologies) algorithm to evolve AI drivers capable of navigating complex tracks.
- **Interactive Visualization**: Use Streamlit and PyDeck for an interactive application, allowing users to engage with the simulation process directly.
  
### Technical Details
- Streamlit is used to create a user-friendly web interface that hosts the entire simulation platform.
- PyDeck allows for the visualization of tracks on an interactive map, enhancing the track selection process.
- MongoDB is integrated for storing and retrieving car and track data, ensuring that users' selections persist across sessions.
- NEAT-Python implements the core AI functionality, evolving neural networks to control the cars effectively.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ApexAI.git
cd ApexAI
2. Run the Streamlit app:
streamlit run app.py

## Usage
After installation, navigate through the Streamlit app's tabs to select cars, choose or create tracks, and start the simulation. The "Run Simulation" tab initiates the NEAT-based AI training process, where users can observe AI performance across generations.

