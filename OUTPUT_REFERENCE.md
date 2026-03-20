# 📊 Visualization & Output Reference

## What Gets Generated When You Run the Notebook

### Animation GIFs (5 files in `gifs/` folder)

#### 1. **astar_animation.gif** (A* Algorithm)
- Grid-based pathfinding with heuristic guidance
- Shows: asteroids, spacecraft position, trail, current planned path
- File size: ~2-3 MB
- Animation length: Up to 320 frames at 10 FPS (~32 seconds)

#### 2. **greedy_animation.gif** (Greedy Best First)
- Faster than A* but less optimal
- Shows: Same visualization as A*
- File size: ~2-3 MB
- Animation length: Up to 320 frames at 10 FPS

#### 3. **rrt_animation.gif** (RRT Algorithm)
- Probabilistic motion planning
- Shows: Random exploration, tree growth, path convergence
- File size: ~2-3 MB
- Animation length: Up to 320 frames at 10 FPS

#### 4. **rrt_star_animation.gif** (RRT* with Path Rewiring)
- Optimal variant of RRT
- Shows: Improved paths through rewiring
- File size: ~2-3 MB
- Animation length: Up to 320 frames at 10 FPS

#### 5. **potential_field_animation.gif** (Potential Field Method)
- Physics-inspired navigation
- Shows: Attractive and repulsive forces in action
- File size: ~2-3 MB
- Animation length: Up to 320 frames at 10 FPS

### Performance Charts (3 files in `images/` folder)

#### 1. **comparison_metrics.png** (3-Chart Grid)

**Layout:**
```
┌─────────────────────────────────┐
│ Path Length  │ Planning Time  │ Success Rate │
│  (Bar Chart) │  (Bar Chart)   │  (Bar Chart) │
└─────────────────────────────────┘
```

**Details:**
- Left: Path length comparison (units traveled)
- Center: Total planning time (seconds)
- Right: Success rate (0 = failed, 1 = success)
- File size: ~150-200 KB
- Colors: Blue, Green, Yellow for distinction

#### 2. **collision_comparison.png** (Single Chart)
- Bar chart showing collision count per algorithm
- X-axis: Algorithm names
- Y-axis: Number of collisions
- File size: ~80-150 KB
- Color: Red bars for alarm
- Shows which algorithm is safest

#### 3. **path_comparison_overlay.png** (Combined Visualization)
- All 5 algorithm paths overlaid on same environment
- Start position: Cyan dot (top-left area)
- Goal position: Lime dot (bottom-right area)
- Asteroids: Not shown (would clutter view)
- Each algorithm path: Unique color
- File size: ~100-200 KB
- Legend: Shows which line is which algorithm

**Colors in Overlay:**
- A*: Blue (#4ea8de)
- Greedy Best First: Orange (#f9844a)
- RRT: Teal (#43aa8b)
- RRT*: Yellow (#f9c74f)
- Potential Field: Salmon (#e76f51)

## Console Output During Execution

### When Running Simulations
```
Running motion planning simulations...
----------------------------------------
  A*                 ... ✓
  Greedy Best First  ... ✓
  RRT                ... ✓
  RRT*               ... ✓
  Potential Field    ... ✓
----------------------------------------
✓ All simulations completed!
```

### When Creating Animations
```
✓ Saved: gifs/astar_animation.gif
✓ Saved: gifs/greedy_animation.gif
✓ Saved: gifs/rrt_animation.gif
✓ Saved: gifs/rrt_star_animation.gif
✓ Saved: gifs/potential_field_animation.gif
```

### Performance Comparison Results
```
===========================================================================
PERFORMANCE COMPARISON RESULTS
===========================================================================
A*                 | Path:   1520.45 | Time: 0.0234s | ✓ SUCCESS     | Collisions: 0
Greedy Best First  | Path:   1650.23 | Time: 0.0156s | ✓ SUCCESS     | Collisions: 0
RRT                | Path:   1890.12 | Time: 0.1234s | ✓ SUCCESS     | Collisions: 0
RRT*               | Path:   1510.89 | Time: 0.1456s | ✓ SUCCESS     | Collisions: 0
Potential Field    | Path:   1780.34 | Time: 0.0078s | ✓ SUCCESS     | Collisions: 0
===========================================================================
✓ Saved: images/comparison_metrics.png
✓ Saved: images/collision_comparison.png
```

### Conclusion Output
```
===========================================================================
SIMULATION SUMMARY
===========================================================================

🏆 Best Algorithm: RRT*
   Path Length: 1510.89 units
   Planning Time: 0.1456 seconds
   Replans: 8
   Success: ✓

⚡ Fastest Planner: Potential Field
   Planning Time: 0.0078 seconds

📊 Generated Files:
   ✓ images/comparison_metrics.png
   ✓ images/collision_comparison.png
   ✓ images/path_comparison_overlay.png
   ✓ gifs/astar_animation.gif
   ✓ gifs/greedy_animation.gif
   ✓ gifs/rrt_animation.gif
   ✓ gifs/rrt_star_animation.gif
   ✓ gifs/potential_field_animation.gif

===========================================================================
```

## Expected File Sizes

| File | Size | Typical Range |
|------|------|---------------|
| astar_animation.gif | 2.1 MB | 2.0-2.5 MB |
| greedy_animation.gif | 2.3 MB | 2.0-2.8 MB |
| rrt_animation.gif | 2.4 MB | 2.1-2.9 MB |
| rrt_star_animation.gif | 2.2 MB | 2.0-2.7 MB |
| potential_field_animation.gif | 1.9 MB | 1.8-2.4 MB |
| comparison_metrics.png | 165 KB | 150-200 KB |
| collision_comparison.png | 95 KB | 80-150 KB |
| path_comparison_overlay.png | 142 KB | 100-200 KB |
| **TOTAL FILES** | **~13.5 MB** | **~13-20 MB** |

## GitHub Display Preview

### On GitHub Notebook Viewer

```
Autonomous Spacecraft Navigation in Dynamic Asteroid Fields

## 9. Visualization (Algorithm Animations)

[Image displays here in notebook]

### A* Animation
[GIF image displays and animates in browser]

### Greedy Best First Animation
[GIF image displays and animates in browser]

...etc for all 5 algorithms

## 10. Performance Comparison

PERFORMANCE COMPARISON RESULTS
===========================================================================
A*                 | Path:   1520.45 | Time: 0.0234s | ✓ SUCCESS
...

[comparison_metrics.png displays inline]
[collision_comparison.png displays inline]

## 11. Visualization Comparison

[path_comparison_overlay.png displays inline with legend]
```

## Tips for Viewing Outputs

### Local Viewing
```bash
# View animations in browser
open gifs/astar_animation.gif

# View in image viewer
open images/comparison_metrics.png
```

### GitHub Viewing
1. Navigate to repository
2. Click on notebook file
3. Scroll through to see images
4. Click GIFs to see animations

### In Jupyter Notebook
```python
from IPython.display import Image, display
display(Image('images/comparison_metrics.png'))
display(Image('gifs/astar_animation.gif'))
```

## Modifying Output Settings

### Change Animation Quality
In `create_animation()` function:
```python
# For higher quality (larger files):
ani.save(gif_path, writer="pillow", fps=20)  # was 10

# For lower quality (smaller files):
ani.save(gif_path, writer="pillow", fps=5)   # was 10
```

### Change Image Resolution
In plot saving cells:
```python
# For higher quality (larger files):
plt.savefig(filename, dpi=300)  # was 150

# For lower quality (smaller files):
plt.savefig(filename, dpi=100)  # was 150
```

### Reduce Animation Frame Count
Modify environment settings:
```python
MAX_STEPS = 200  # was 320 (saves ~33% on GIF sizes)
```

## GitHub Upload Checklist

- [ ] Run notebook locally
- [ ] Verify all output files created
- [ ] Check file sizes are reasonable
- [ ] View files locally (images, GIFs)
- [ ] Commit all files including gifs/ and images/
- [ ] Push to GitHub
- [ ] Visit GitHub.com to verify display
- [ ] Share link! 🎉

## Troubleshooting Display Issues

### GIFs not animating on GitHub
- **Cause:** File too large (>5 MB)
- **Solution:** Reduce FPS or MAX_STEPS

### Images appear blurry
- **Cause:** DPI too low
- **Solution:** Increase DPI to 200 or 300

### Files not showing on GitHub
- **Cause:** Not committed to git
- **Solution:** `git add gifs/ images/` then push

### GitHub page loads slowly
- **Cause:** Large files
- **Solution:** Reduce DPI/FPS/frame count

## Animation Legend

All animations show the same visualization:

```
┌────────────────────────────────────┐
│  Cyan Circle       = START POSITION│
│  Lime Circle       = GOAL POSITION │
│  Orange Circles    = MOVING OBSTACLES (ASTEROIDS)
│  White Dot         = SPACECRAFT    │
│  Cyan Line         = PATH TAKEN   │
│  Yellow Dash Line  = CURRENT PLAN │
│  Dark Background   = FREE SPACE   │
└────────────────────────────────────┘
```

## Summary Table

| Output | Type | Location | Size | Format |
|--------|------|----------|------|--------|
| Animations | GIF | `gifs/` | ~2-3 MB each | Pillow |
| Metrics | PNG | `images/` | ~165 KB | matplotlib |
| Collisions | PNG | `images/` | ~95 KB | matplotlib |
| Path Overlay | PNG | `images/` | ~142 KB | matplotlib |

---

**All outputs are GitHub-ready and optimized for web display!** ✓
