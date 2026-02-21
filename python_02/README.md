# Garden Guardian
## Data Engineering for Smart Agriculture
**Version:** 2.1

---

# Project Summary
Build resilient data pipelines for your smart garden! Learn to handle sensor failures, process agricultural data streams, and create robust monitoring systems that keep your digital greenhouse thriving.

---

# Chapter I — Foreword
Welcome to the world of agricultural data engineering.  
Your digital greenhouse must be resilient. Python exception handling is your toolkit for building bulletproof pipelines.

---

# Chapter II — AI Instructions
- Use AI to reduce repetitive tasks.
- Develop prompting skills for coding and non-coding tasks.
- Understand how AI works to avoid mistakes and bias.
- Always verify AI output; seek peer review.
- Only use AI-generated content you fully understand.

---

# Chapter III — Introduction
You will learn:
- Real-time validation and cleaning of agricultural data streams
- Failure modes in IoT sensor networks
- Creating custom agricultural alerts
- Data pipeline fault tolerance and recovery
- Ensuring data integrity in distributed farming systems

Each exercise builds one component of the smart agriculture system.

---

# Chapter IV — General Instructions
- Python 3.10+
- Flake8 standards
- Functions/methods must include type hints
- Each exercise in its own file
- Demonstrate normal and error scenarios
- Use built-in exceptions appropriately
- Programs must never crash
- Use try/except/finally/raise

---

# Exercise 0 — Agricultural Data Validation Pipeline
**File:** `ft_first_exception.py`  
**Objective:** Validate temperature input from sensors.

### Requirements
- Function `check_temperature(temp_str)`
  - Convert string to number
  - Temperature must be 0–40°C
  - Handle invalid input
- Function `test_temperature_input()`
  - Test valid input: `"25"`
  - Test invalid input: `"abc"`
  - Test extreme values: `"100"`, `"-50"`

---

# Exercise 1 — Different Types of Problems
**File:** `ft_different_errors.py`  
**Objective:** Handle multiple built-in errors.

### Requirements
- Function `garden_operations()`:
  - `ValueError`: invalid input
  - `ZeroDivisionError`: divide by zero
  - `FileNotFoundError`: missing file
  - `KeyError`: missing dictionary key
- Function `test_error_types()`:
  - Demonstrate each error
  - Catch and explain each
  - Show program continues

---

# Exercise 2 — Making Your Own Error Types
**File:** `ft_custom_errors.py`  
**Objective:** Create custom exceptions.

### Requirements
- Exception classes:
  - `GardenError`
  - `PlantError` (inherits GardenError)
  - `WaterError` (inherits GardenError)
- Functions to raise and catch these exceptions
- Demonstrate catching `GardenError` catches all garden errors

---

# Exercise 3 — Finally Block: Always Clean Up
**File:** `ft_finally_block.py`  
**Objective:** Ensure cleanup always happens.

### Requirements
- Function `water_plants(plant_list)`:
  - Open watering system
  - Water each plant
  - Handle invalid plant names
  - Always close system in `finally`
- Function `test_watering_system()`:
  - Normal watering
  - Watering with error
  - Show cleanup happens in all cases

---

# Exercise 4 — Raising Your Own Errors
**File:** `ft_raise_errors.py`  
**Objective:** Raise your own exceptions for validation.

### Requirements
- Function `check_plant_health(plant_name, water_level, sunlight_hours)`:
  - Plant name cannot be empty
  - Water level 1–10
  - Sunlight 2–12 hours
  - Raise errors with helpful messages
  - Return success message if valid
- Function `test_plant_checks()`:
  - Test good values
  - Test invalid name
  - Test invalid water
  - Test invalid sunlight
  - Catch and handle errors

---

# Exercise 5 — Garden Management System
**File:** `ft_garden_management.py`  
**Objective:** Combine all previous concepts in one system.

### Requirements
- `GardenManager` class:
  - `add_plant(plant_name)` — handle invalid input
  - `water_plant()` — cleanup with `finally`
  - `check_plant_health(plant_name, water_level, sunlight_hours)` — raise errors
  - Use custom exceptions (`PlantError`, `WaterError`, `GardenError`)
  - Keep working after errors
- Function `test_garden_management()`:
  - Add plants (valid/invalid)
  - Water plants
  - Check health
  - Show error recovery

---

# Chapter XI — Turn in & Submission
- Submit only requested files
- Must explain exception handling
- Demonstrate error recovery and resilience
- Clean, readable code required