# Configuration for Spacecraft Navigation Simulation
# Edit these values to customize your simulation

# Environment dimensions
SPACE_WIDTH = 1000
SPACE_HEIGHT = 1000

# Start and goal positions
START_X = 50
START_Y = 50
GOAL_X = 950
GOAL_Y = 950

# Asteroid parameters
ASTEROID_COUNT = 34          # Number of moving obstacles
ASTEROID_MIN_RADIUS = 14     # Minimum asteroid size
ASTEROID_MAX_RADIUS = 28     # Maximum asteroid size
ASTEROID_MIN_VELOCITY = -3.5 # Minimum speed
ASTEROID_MAX_VELOCITY = 3.5  # Maximum speed
ASTEROID_MIN_VELOCITY_MAG = 0.8  # Minimum speed magnitude

# Spacecraft parameters
SPACECRAFT_SPEED = 18.0      # Units per step
GOAL_RADIUS = 25.0           # How close to goal counts as success

# Simulation parameters
GRID_SIZE = 50               # Resolution for grid-based algorithms
MAX_STEPS = 320              # Maximum simulation duration
REPLAN_INTERVAL = 6          # Steps between replans
COLLISION_MARGIN = 4.0       # Safety margin for collisions
SEGMENT_MARGIN = 6.0         # Safety margin for path segments

# Algorithm parameters
A_STAR_ENABLED = True
GREEDY_ENABLED = True
RRT_ENABLED = True
RRT_STAR_ENABLED = True
POTENTIAL_FIELD_ENABLED = True

# RRT parameters
RRT_ITERATIONS = 900         # Number of sampling iterations
RRT_STEP_SIZE = 65.0         # Distance per step
RRT_GOAL_BIAS = 0.12         # Probability of sampling goal

# RRT* parameters
RRT_STAR_ITERATIONS = 1000
RRT_STAR_STEP_SIZE = 65.0
RRT_STAR_NEIGHBOR_RADIUS = 110.0
RRT_STAR_GOAL_BIAS = 0.12

# Potential field parameters
POTENTIAL_FIELD_ATTRACTIVE_FORCE = 2.4
POTENTIAL_FIELD_INFLUENCE_RADIUS = 130.0
POTENTIAL_FIELD_REPULSIVE_STRENGTH = 2400.0
POTENTIAL_FIELD_SAFE_DISTANCE = 10.0

# Random seed for reproducibility
SEED_VALUE = 21

# Visualization parameters
FIGURE_SIZE = (8, 8)
ANIMATION_INTERVAL = 90      # Milliseconds between frames
ANIMATION_FPS = 12           # Frames per second for save

# Color scheme
BACKGROUND_COLOR = "#07111f"
FIGURE_BACKGROUND = "white"
START_COLOR = "cyan"
GOAL_COLOR = "lime"
ASTEROID_COLOR = "#f3722c"
SPACECRAFT_COLOR = "white"
TRAIL_COLOR = "#90e0ef"
PATH_COLOR = "#ffd166"

# Seed map for each algorithm (for consistent comparisons)
SEED_MAP = {
    "A*": 21,
    "Greedy Best First": 21,
    "RRT": 21,
    "RRT*": 21,
    "Potential Field": 21,
}
