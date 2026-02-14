# 🐍 Python Object-Oriented Garden System  
## Module Overview (ex00 → ex06)

This module progressively builds a complete Object-Oriented system using a garden simulation.  
Each exercise introduces a new OOP concept and increases architectural complexity.

---

# 📘 ex00 – Basic Class Structure

**Goal:**  
Create your first class and understand object instantiation.

**Concepts:**
- Defining a class
- Instance attributes
- Instance methods
- `if __name__ == "__main__"` execution pattern

---

# 🌱 ex01 – Class vs Instance Attributes

**Goal:**  
Understand shared vs individual data.

**Concepts:**
- Class attributes
- Instance attributes
- Object state management
- Memory behavior of shared data

---

# 🌿 ex02 – Encapsulation

**Goal:**  
Protect internal object state.

**Concepts:**
- Private attributes (`__attribute`)
- Getters
- Controlled updates
- Data validation

Focus: Control access to internal data.

---

# 🌸 ex03 – Inheritance

**Goal:**  
Create parent-child relationships between classes.

**Concepts:**
- `super()`
- Code reuse
- Extending parent behavior
- Structured hierarchy

Example:


---

# 🌼 ex04 – Method Overriding & Polymorphism

**Goal:**  
Allow child classes to redefine behavior.

**Concepts:**
- Method overriding
- Polymorphism
- Dynamic method dispatch
- Shared interface, different implementation

Example:
```python
plant.grow()
 
 Plant
   ↓
FloweringPlant
   ↓
PrizeFlower

GardenManager
    ├── GardenStats (nested analytics helper)
    ├── Garden
    │       └── Plants
    │            ├── Plant
    │            ├── FloweringPlant
    │            └── PrizeFlower
