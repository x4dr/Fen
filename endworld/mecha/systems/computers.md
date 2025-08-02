## Computers

Computers in Endworld come in many forms, abstracted by **available memory** and **processing power**.

They are not like real-world computers. Due to their need for modularity and resilience, they are **large**, **heavily parallelized**, and **highly abstracted** — do not mistake them for real computers.

---

### Processing Power

- Measured in **Computational Power Usage (CPU)**
- Programs occupy CPU when run
- Programs won't start if CPU is insufficient
- You may shift `[8,12,17,20]` CPU between programs with a **Theory, Computer Usage** check
- Underpowered programs perform worse (scale all effects unfavorably)
- Overpowered programs usually don’t perform better — only faster

---

### Storage Space

- Measured in **Storage**
- Determines how much data or how many programs a system can hold

---

### Programs

Programs must be loaded from storage or built into **RROM**.

#### RROM

**Robust Read Only Memory**:
- Integrated into the processor
- Corruption-resistant (e.g. wire-and-bead designs)
- Used as a **bootstrap** loader
- Runs immediately on power-up
- Cannot be modified while running
- Replacing the physical media replaces the program

#### Execution

- Programs act toward predefined goals
- May execute checks or generate stats
- Can load other programs in **parallel** or **series**
- On completion, they unload and free used resources

#### Operating System (Main)

- A special program that manages others
- Takes 1 turn per user interaction
- Runs a sequence of loads with parameters

#### Parameters

Abstracted context for the program’s operation  
(e.g. “what to act upon” is assumed to be known)

---

### Programming

To create a program:
- Use **Theory, Computer Programming** and a relevant Skill
- If the task is vague, use **Insight**

Steps:
1. Storyteller + player define:
   - CPU cost
   - Storage size
   - Runtime
   - Other programs needed
   - Effect and checks

2. After the roll, Storyteller offers viable configurations — player picks one  
   **OR**  
   Player proposes config; Storyteller sets required total check result and intervals

---

### Example Programs

#### Shield Daemon
- **CPU**: 0.5
- **Size**: 1
- **Requirements**: Internal Computerization, Shields  
- **Effect**: On switch `"shields up"` — load one *Shield Configurator* per inactive shield  
  On switch `"NOW"` — load one *Shield Burster* per inactive shield  
- **Runtime**: Ongoing  
- **Programming**: Shields skill, 1 workday/roll, total: 100  
- **Limits**: Specific to mech/programs used

#### Shield Configurator
- **CPU**: 3  
- **Size**: 1  
- **Requirements**: Shield  
- **Effect**: Configures shield, flat result 10  
- **Runtime**: 1 Turn  
- **Programming**: Shields skill, 1 workday/roll, any 3 rolls of 16+  
- **Limits**: Shield-specific

#### Shield Burster
- **CPU**: 1  
- **Size**: 1  
- **Requirements**: Shield  
- **Effect**: Configures shield with flat result 0 (emergency config)  
- **Runtime**: Instant  
- **Programming**: Shields skill, 1 workday/roll, total: 30+  
- **Limits**: Shield-specific
