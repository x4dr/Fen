## Computers

Computers come in many different shapes and sizes, but in **Endworld** they are all abstracted into their available memory and their available processing powers.

Computers in Endworld are different from our own, since they had to be designed to be much easier, much more modular, and much more resistant. They are usually quite big and heavy, but also incredibly sophisticatedly parallelized.  
Also they are heavily abstracted and should not be confused with real computers.

### Processing Power

Processing power is a computer’s capability to achieve computation and general work, including I/O. It is measured in **Computational Power Usage**, and a Processor provides **CPU capacity**.

Processing power is occupied by programs, taking as much as they need or failing to start if there is not enough. A _Theory, Computer Usage_ (and relevant skill for computer administration, clocking or similar) Roll can be used to shift `[8, 12, 17, 20]` processing from one program to another or free that processing power up.

A program running below its required processing power will perform worse. Scale any applicable metric to the utilized processing power, rounding unfavorably for purposes of the program. Programs with no direct metric still produce lesser effects, or may not work at all.

A program running above its required processing power usually does not do its tasks better, but might perform them faster.

### Storage Space

Storage space is a computer’s capability to store data and programs.  
It is measured in **Storage**.

### Programs

For any program to run, it needs to either be loaded from storage or be present as built-in **RROM**.

#### RROM

**Robust Read Only Memory** is a storage medium directly integrated into a processor and by custom usually made from non-volatile, corruption-resistant materials like woven strands of wire and beads.

Since a program is needed to load a program, some processors have built-in RROM acting as a **bootstrap loader** for the main program used to load other programs more efficiently.

Since the RROM is using its own **Computational Power**, it cannot be reused, and the Bootloader is effectively its own computer system.  
It starts executing as soon as it is turned on, and the program cannot be changed or modified while the processor is running.

However, simply physically replacing the program is enough — and so RROM has a big advantage over hardware or even electro-mechanical computing techniques.

#### Execution

Programs have a set of goals that they will try to accomplish and through their programming take steps toward.  
This culminates in the abstracted behavior of programs performing actions — some with a predetermined degree of success, some providing parts or all of the statistics needed for a check.

Programs can load other programs either in **parallel** (while they are still running) or in **series** (as they are completing). When a program is completed, it unloads, and at the end of the turn any resources it used are freed.

#### Operating System

An **Operating System** or _"Main"_ is simply another program that can be dynamically tasked by the user to load other programs.

A user interaction usually requires one turn, after which the Operating System performs a predetermined series of loads and supplies each program with its parameters.

#### Parameters

Parameters are the context a specific program needs to accomplish its goal.

Parameters are usually abstracted away as long as it is reasonable to assume that all programs _“know”_ what they are acting upon.

### Programming

To create a program requires some knowledge of what the program is trying to accomplish, and **Computer Programming** and usually **Theory**.

If the process is more exploratory and there is no clear goal, **Insight** is used instead to merely determine if a solution can be found.

For **Theory** checks — given that the programmer could conceivably find a series of instructions — the Storyteller and Player determine a set of:

- CPU requirements
- Storage space needed for the program
- Auxiliary data requirements
- Flat check results or purposeful statistics
- Other programs loaded and runtime, as far as applicable

Use similar programs and their checked quality as templates.

After the check is made, the Storyteller offers several configurations of the above values that could be achieved with the roll, and the Player chooses one.

Alternatively, the Player designs a new program — its configuration and effects — and the Storyteller tells the player the interval of the programming rolls and the total sum of check results needed to achieve the desired goal.

The program, its name, its statistics, and effects are then noted down by the Player.

---

### Example – Shield Daemon

- **Name:** Shield Daemon
- **CPU:** 0.5
- **Size:** 1
- **Requirement:** Internal Computerization, Shields
- **Effect:** If a switch inside the cockpit is flipped to “bring shields up”, load one Shield Configurator for each shield that is down.  
    If it is flipped to “NOW”, load one Shield Burster for each shield that is down.
- **Runtime:** Ongoing
- **To program:** Shields or relevant piloting skill, 1 workday per roll, total: 100
- **Limits:** Specific to exact programs and mech

---

### Example – Shield Configurator

- **Name:** Shield Configurator
- **CPU:** 3
- **Size:** 1
- **Requirement:** Shield
- **Effect:** Configure Shield with flat result of 10
- **Runtime:** 1 Turn
- **To program:** Shields, 1 workday per roll, any 3 rolls of 16+
- **Limits:** Specific to exact shield

---

### Example – Shield Burster

- **Name:** Shield Burster
- **CPU:** 1
- **Size:** 1
- **Requirement:** Shield
- **Effect:** Configure Shield with flat result of 0
- **Runtime:** Instantly
- **To program:** Shields, 1 workday per roll, total of 30+
- **Limits:** Specific to exact shield
