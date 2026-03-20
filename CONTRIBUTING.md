# Contributing to Spacecraft Navigation

Thank you for your interest in contributing! Here's how you can help.

## 🐛 Reporting Issues

Found a bug? Please create an issue with:

1. **Description**: What happened?
2. **Steps to reproduce**: How to replicate the issue?
3. **Expected behavior**: What should happen?
4. **Screenshots/Videos**: If applicable
5. **Environment**: Python version, OS, etc.

Example:
```
Title: Animation not showing for RRT algorithm

Steps:
1. Run all cells in notebook
2. Scroll to RRT animation section
3. No animation displays

Expected: See RRT path animation
Environment: Python 3.10, Windows 11, matplotlib 3.10.8
```

## 💡 Feature Requests

Have an idea? Submit a feature request with:
- **Description**: What feature?
- **Use case**: Why needed?
- **Possible implementation**: Any ideas?

Example ideas:
- Add D* algorithm implementation
- Create 3D visualization
- Add performance benchmarking tools
- Support for custom obstacle shapes
- Real-time parameter adjustment

## 🔧 Code Contributions

### Development Setup

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR-USERNAME/Spacecraft-navigation.git
   cd Spacecraft-navigation
   ```

3. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. Install in development mode:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

### Making Changes

1. **Follow the existing code style**:
   - Use clear, descriptive variable names
   - Add comments for complex logic
   - Keep functions focused and concise
   - Follow PEP 8 conventions

2. **Format**: The notebook uses clean, educational style:
   - Comment each major section
   - Use `# Section Name` for organization
   - Keep cell sizes manageable
   - Add docstrings for classes

3. **Test your changes**:
   - Run the notebook from top to bottom
   - Verify all outputs display correctly
   - Check performance hasn't degraded significantly

### Submitting Changes

1. Commit with clear messages:
   ```bash
   git add .
   git commit -m "Add D* algorithm implementation"
   ```

2. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

3. Create a Pull Request with:
   - Clear title
   - Description of changes
   - Any breaking changes noted
   - Verification of functionality

## 📝 Adding a New Algorithm

### Steps:

1. **Create a search function** (follows existing pattern):
   ```python
   def my_algorithm_search(start, goal, asteroids, **kwargs):
       """
       Implement your algorithm here.
       
       Args:
           start: Starting position [x, y]
           goal: Goal position [x, y]
           asteroids: List of Asteroid objects
           **kwargs: Algorithm-specific parameters
           
       Returns:
           List of waypoints from start to goal
       """
       # Your implementation
       return path_points
   ```

2. **Add to `plan_path()` function**:
   ```python
   def plan_path(algorithm_name, start, goal, asteroids):
       # ... existing code ...
       if algorithm_name == "My Algorithm":
           return my_algorithm_search(start, goal, asteroids)
   ```

3. **Add to `run_all_algorithms()`**:
   ```python
   algorithm_names = [
       # ... existing ...
       "My Algorithm",
   ]
   
   seed_map = {
       # ... existing ...
       "My Algorithm": 21,
   }
   ```

4. **Create animation section**:
   ```python
   def animate_my_algorithm():
       return create_animation(results["My Algorithm"], "My Algorithm Animation")
   ```

5. **Add markdown header and call**:
   ```markdown
   ### My Algorithm Animation
   ```

6. **Test thoroughly** and submit PR!

## 🎨 Enhancement Ideas

### Algorithm Enhancements
- [ ] Add theta* algorithm
- [ ] Implement D* Lite
- [ ] Add anytime algorithms (ARA*)
- [ ] Implement trajectory optimization
- [ ] Add constraint satisfaction

### Visualization Improvements
- [ ] 3D environment simulation
- [ ] Real-time parameter adjustment
- [ ] Performance graphs during simulation
- [ ] Heat maps of algorithm exploration
- [ ] Side-by-side comparison view

### Features
- [ ] Load custom environments from files
- [ ] Record videos of simulations
- [ ] Batch processing tool
- [ ] Parameter optimization
- [ ] Collision prediction

### Documentation
- [ ] Algorithm theory explanations
- [ ] Performance analysis guide
- [ ] Tuning parameters guide
- [ ] Video tutorials

## 📊 Code Quality

### Before submitting:
- [ ] Code runs without errors
- [ ] Follows existing style
- [ ] Comments explain complex logic
- [ ] No debugging print statements left in
- [ ] Tested with different parameters

## 🚀 Performance Guidelines

For new algorithms:
- Should complete in < 5 seconds for typical parameters
- Memory usage should be reasonable (< 1GB)
- Results should show meaningful comparison with existing algorithms

## 📚 Resources

- [Motion Planning Algorithms](http://planning.cs.umn.edu/) by Steve LaValle
- [Planning and Decision Making in Robotics](http://www.cs.cmu.edu/~maxim/classes/)
- [ROS Navigation Stack](http://wiki.ros.org/navigation)

## 🤝 Community

- Be respectful and constructive
- Welcome feedback on your contributions
- Help review others' PRs
- Share ideas and knowledge

## ✅ PR Checklist

Before submitting your PR:

- [ ] Code follows project style
- [ ] All functions have docstrings
- [ ] Notebook runs without errors
- [ ] All cells output correctly
- [ ] No temporary files committed
- [ ] PR description is clear
- [ ] Related issues are linked

## 📄 License

By contributing, you agree that your contributions will be licensed under the same license as the project.

---

**Thank you for contributing to make this project better! 🎉**

Questions? Open an issue or start a discussion!
