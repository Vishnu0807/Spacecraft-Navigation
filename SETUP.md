# GitHub Setup & Installation Guide

## 🚀 Getting Started

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/Spacecraft-navigation.git
cd Spacecraft-navigation
```

### Step 2: Set Up Python Environment

#### Option A: Using venv (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

#### Option B: Using conda

```bash
conda create -n spacecraft python=3.10
conda activate spacecraft
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Launch Jupyter Notebook

```bash
# Using Jupyter Notebook
jupyter notebook "Autonomous Spacecraft Navigation in Dynamic Asteroid Fields.ipynb"

# OR using JupyterLab (recommended)
jupyter lab "Autonomous Spacecraft Navigation in Dynamic Asteroid Fields.ipynb"
```

## 📋 Requirements

- Python 3.8 or higher
- pip (Python package manager)
- ~500MB free disk space (includes dependencies)

## ✅ Verification

After running through all cells, you should see:

1. ✅ 5 animation sections (one for each algorithm)
2. ✅ Comparison charts showing:
   - Path length comparison
   - Planning time comparison
   - Success rates
   - Collision counts
3. ✅ Final path comparison overlay

## 🎯 Running Just One Algorithm

To run and visualize a single algorithm, you can modify and run specific cells:

```python
# Run this after section 3 (Environment Setup)
results = {}
results["A*"] = run_simulation("A*", seed_value=21)
result = results["A*"]
animation = create_animation(result, "A* Navigation")
display(animation)
```

## 🔄 Customizing the Simulation

Edit these values in Section 3 (Environment Setup):

```python
ASTEROID_COUNT = 34      # Change number of obstacles
GRID_SIZE = 50          # Change resolution for grid algorithms
MAX_STEPS = 320         # Change simulation duration
SPACECRAFT_SPEED = 18.0 # Change spacecraft velocity
GOAL_RADIUS = 25.0      # Change goal zone size
```

Then re-run the simulation with your custom parameters.

## 📊 Understanding the Outputs

### Animation Components

- **Cyan circle**: Start position
- **Lime circle**: Goal position
- **Orange circles**: Moving asteroids
- **White dot**: Current spacecraft position
- **Cyan line**: Spacecraft trail (path taken)
- **Yellow dashed line**: Current planned path

### Performance Metrics

| Metric | Meaning |
|--------|---------|
| Path Length | Total distance traveled by spacecraft |
| Time | Total planning computation time |
| Success | Did the spacecraft reach the goal? |
| Collisions | Number of asteroid collisions |
| Replans | How many times the path was recalculated |

## 🐛 Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'jupyter'`
**Solution**: Run `pip install -r requirements.txt` again

### Issue: Animations don't display
**Solution**: 
- Make sure you're using Jupyter Notebook or JupyterLab
- Try restarting the kernel: Kernel → Restart
- Run all cells from the top

### Issue: `PermissionError` on `.animation_temp/`
**Solution**: Delete `.animation_temp/` folder and restart notebook

### Issue: Out of memory or very slow
**Solution**:
- Reduce `ASTEROID_COUNT` to 15-20
- Reduce `MAX_STEPS` to 200
- Close other applications

## 📱 Viewing on GitHub

When you push this notebook to GitHub:

1. GitHub will automatically render the `.ipynb` file
2. **Static outputs** (charts, final paths) will display ✅
3. **Animations** stored as HTML will show as interactive elements ✅
4. Cell outputs will be visible if you've run the notebook before pushing

To ensure outputs show on GitHub:
```bash
# Before pushing, make sure to save the notebook with outputs
# In Jupyter: File → Save and Checkpoint
# Then commit and push
```

## 🔗 Sharing Your Results

### Share a specific algorithm's results:

1. Run only that algorithm's cells
2. Take a screenshot or use `plt.savefig()`
3. Include in a README section

Example:
```python
# At the end of the notebook
plt.figure(figsize=(10, 8))
# ... plotting code ...
plt.savefig('astar_results.png', dpi=150, bbox_inches='tight')
plt.show()
```

## 🚀 Advanced: Batch Processing

Run multiple simulations with different seeds:

```python
results_batch = {}
for seed in [21, 42, 99, 123]:
    results_batch[seed] = run_all_algorithms()
    # Analyze results_batch[seed]
```

## 📚 Educational Usage

Great for:
- **Computer Science**: Algorithm study
- **Robotics**: Motion planning fundamentals
- **AI/ML**: Search algorithms comparison
- **Projects**: Course assignments or capstone projects

---

**Need help?** Check GitHub Issues or create a detailed bug report!
