# Autonomous Spacecraft Navigation in Dynamic Asteroid Fields

A comprehensive simulation comparing motion planning algorithms for autonomous spacecraft navigating through dynamic asteroid fields in 2D space.

## 🎯 Project Overview

This project implements and compares five different motion planning algorithms:

- **A\*** - Optimal grid-based pathfinding with heuristics
- **Greedy Best First Search** - Fast greedy pathfinding
- **RRT (Rapidly-exploring Random Trees)** - Probabilistic motion planning
- **RRT\*** (RRT Star) - Optimal variant of RRT with path rewiring
- **Potential Field Method** - Physics-inspired navigation with attractive and repulsive forces

### Simulation Parameters

- **Space**: 1000 × 1000 grid
- **Start**: (50, 50)
- **Goal**: (950, 950)
- **Obstacles**: 34 moving asteroids with velocities
- **Spacecraft Speed**: 18 units/step
- **Max Steps**: 320

## 📊 Metrics Tracked

For each algorithm, the notebook records:
- ✅ Success/Failure
- 📏 Total path length
- ⏱️ Planning time
- 💥 Number of collisions
- 🔄 Number of replans

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip or conda

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Spacecraft-navigation.git
   cd Spacecraft-navigation
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Notebook

```bash
jupyter notebook "Autonomous Spacecraft Navigation in Dynamic Asteroid Fields.ipynb"
```

Or with JupyterLab:
```bash
jupyter lab "Autonomous Spacecraft Navigation in Dynamic Asteroid Fields.ipynb"
```

## 📁 Project Structure

```
Spacecraft-navigation/
├── Autonomous Spacecraft Navigation in Dynamic Asteroid Fields.ipynb
├── create_spacecraft_notebook.py
├── requirements.txt
├── README.md
├── .gitignore
└── .animation_temp/              (generated animations)
```

## 🔄 Notebook Sections

1. **Introduction** - Project overview and concepts
2. **Import Libraries** - Load required dependencies
3. **Environment Setup** - Configuration and utility functions
4. **Asteroid Class** - Moving obstacle implementation
5. **Spacecraft Class** - Vehicle that navigates the environment
6. **Motion Planning Algorithms** - Implementations of all 5 algorithms
7. **Collision Detection** - Safety checking utilities
8. **Dynamic Simulation Loop** - Main simulation and execution
9. **Visualization (Animations)** - Step-by-step algorithm visualizations
10. **Performance Comparison** - Metrics and comparison charts
11. **Visualization Comparison** - Path overlay comparison
12. **Conclusion** - Results summary

## 📈 Example Output

The notebook generates:
- **Individual Animations** for each algorithm showing:
  - Asteroid positions and movements
  - Spacecraft trail
  - Current planned path
  - Real-time collision detection
  
- **Comparison Charts**:
  - Path length comparison
  - Planning time comparison
  - Success rate comparison
  - Collision count comparison

- **Final Comparison Visualization** - All paths overlaid on single plot

## 🎨 Visualization

The animations are generated using matplotlib and displayed as interactive HTML animations within the notebook. Each frame shows:
- 🌕 Start and goal zones (cyan and lime circles)
- 🔴 Moving asteroids (orange circles)
- ⚪ Spacecraft position (white dot)
- 🟦 Spacecraft trail (cyan line)
- 🟨 Current planned path (yellow dashed line)

## 💡 Algorithm Details

### A* Search
Grid-based algorithm with heuristic guidance. Guarantees optimal path if one exists.

### Greedy Best First
Faster than A* but doesn't guarantee optimality. Uses only heuristic distance.

### RRT
Probabilistic algorithm that rapidly explores configuration space. Good for complex environments but may not be optimal.

### RRT*
Improves upon RRT by rewiring the tree to find better paths. Asymptotically optimal.

### Potential Field
Physics-inspired method using attractive forces toward goal and repulsive forces from obstacles. Fast but may get stuck in local minima.

## 🔧 Customization

You can modify these parameters in the notebook:

```python
SPACE_WIDTH = 1000          # Environment width
SPACE_HEIGHT = 1000         # Environment height
ASTEROID_COUNT = 34         # Number of asteroids
GRID_SIZE = 50              # Cell size for grid-based algorithms
MAX_STEPS = 320             # Maximum simulation steps
SPACECRAFT_SPEED = 18.0     # Spacecraft movement speed
REPLAN_INTERVAL = 6         # Replanning frequency
```

## 📊 Performance Tips

- **A\*** and **Greedy Best First**: Good for structured/grid-like environments
- **RRT\***: Best for complex, unstructured environments
- **Potential Field**: Fastest but may fail in tight spaces
- **RRT**: Balance between speed and reliability

## 🛠️ Troubleshooting

### Animations not showing
- Ensure you're using Jupyter Notebook or JupyterLab, not JupyterHub
- Try restarting the kernel and running all cells again
- Check that `.animation_temp/` directory is writable

### Memory issues
- Reduce `ASTEROID_COUNT`
- Decrease `MAX_STEPS`
- Reduce animation frame count

### Slow performance
- Try algorithms in order: Potential Field → Greedy → RRT → RRT\* → A\*
- Increase `GRID_SIZE` for faster grid-based algorithms

## 📝 Notes

- The code is intentionally written in a clear, readable style for educational purposes
- All algorithms run with the same random seed for fair comparison
- Replanning occurs dynamically when obstacles block the current path

## 📚 Educational Use

This project is ideal for:
- Learning motion planning algorithms
- Understanding collision detection in 2D spaces
- Comparing algorithm performance empirically
- Visualizing path planning in dynamic environments
- College-level robotics/AI projects

## 📄 License

This project is provided as-is for educational purposes.

## 🤝 Contributing

Feel free to fork, modify, and improve! Suggestions:
- Add more algorithms (D*, Theta*, etc.)
- Implement 3D simulation
- Add dynamic obstacle avoidance
- Create performance plots
- Add wind/drift forces

## 📧 Questions?

If you have questions about the algorithms or implementation, refer to standard robotics/motion planning textbooks or academic papers on path planning.

---

**Happy path planning! 🚀**
