---
outgoing links: []
tags: []
title: heat
---
# Heat Management

Heat is a logistics problem. Efficiently moving thermal energy from generators to sinks is as important as managing ammunition.

## Components

A [Mecha](endworld/mecha/mecha) uses three types of thermal systems to manage its state:

*   **Coolant Systems**: Represent the pipe network and fluid loops. They provide **Flux**, which is the maximum rate at which heat can be moved per turn.
*   **Heat Sinks**: Provide **Capacity** to store burst heat during combat.
*   **Vents & Radiators**: Remove heat from the mecha. Vents are active and require [Energy](endworld/mecha/systems/energy), while Radiators tend to be passive but heavier.

## The Flux Pool

Heat moves through the mech in three phases each turn.
The **fluxpool** is a single shared buffer. 

The pool has a maximum capacity equal to the mech's **Total Flux** (sum of flux provided by all active systems). isabled systems do not contribute anything. It cannot go over its capacity and cannot go below 0.

### Phase 1: Inbound (Systems -> Pool)

The player chooses which active systems to pull heat from. Heat fills the pool until it hits max or there is no more heat to pull.

Any heat that could not be moved stays in the generating system as **Residual Heat**, which contributes to sector stress (see [Sector Stress](endworld/combat#sector-stress)).

### Phase 2: Outbound (Pool -> Heat Systems)

The player chooses how much heat to push from the pool into each system able to accept it (sinks, vents, anything with heat capacity that is not full). Heat empties from the pool until it hits 0 or there are no more systems with available capacity.

### Phase 3: Dissipation

Each heat system follows its own rules to remove or process heat (see Heat Systems table). Vents actively dump heat when supplied with energy. Sinks bleed heat slowly through passive cooling.

Because the pool fills first then empties, a full cycle moves at most Total Flux worth of heat through each direction per turn. If the pool is not emptied, less room is available to fill next turn.

### Residual Heat

Any heat left in a generating system after Phase 1 is **Residual Heat**. Heat that cannot be stored in a system (most non-heat systems have 0 capacity) adds to the sector's **stress** (see [Sector Stress](endworld/combat#sector-stress)). Residual heat from any system in a sector spreads to all systems — an overheating weapon can cook the ammunition stored next to it.

If the fluxpool stays full for more than one turn, the mecha suffers chassis-wide instability -- speed is halved, computer systems crash, and the reactor automatically scram.

### Reactor Shutoff Delay

Energy Systems may not stop generating heat instantly. Every [Energy System](endworld/mecha/systems/energy) has a **Shutoff Delay**. When a reactor is deactivated, it continues to output its full baseload heat for a number of turns equal to its **Shutoff Delay**.

## Heat Systems

| Type               | Energy | Capacity | Flux | Passive | Active |
|--------------------|--------|----------|------|---------|--------|
| **Basetech**       |        |          |      |         |        |
| Small Heatsink     | 0      | 30       | 1    | 1/15    |        |
| **Lowtech**        |        |          |      |         |        |
| Radiator Vent      | 2      | 10       | 5    | 1       | 10     |
| Large Heatsink     | 0      | 50       | 1    | 1/15    |        |
| Water cooling      | 1      | 5        | 5    |         |        |
| **Midtech**        |        |          |      |         |        |
| Optimized Heatsink | 0      | 40       | 1    | 1/25    |        |
| Phase Change Loop  | 3      | 2        | 10   |         |        |
| Heatpipes          | 0      | 0        | 5    |         |        |
| Coolant Dump       | 100    | 25       | 10   |         | 25     |
| Radiator Wings     | 5      | 50       | 5    |         | 1/5    |
| **Hightech**       |        |          |      |         |        |
| Fractal Heatsink   | 10     | 100      | 5    | 2       | -2     |
| liquid metal Loop  | 5      | 10       | 50   |         |        |
| OVERDRIVE          | 100    | -        | 0    | -       |        |

**Notes**:

* **Radiator Wings**: 5 turns to deploy. Vulnerable while extended (no armor applies).
* **Coolant Dump**: Discharges 25 heat + 25L Coolant as a decoy mist or smoke screen.
* **Overdrive**: Once activated, the **fluxpool** is uncapped. Heat in the **fluxpool** instead annihilates heat when assigned to a sink. Mech shuts down once the **fluxpool** either stays full or all the heat has been annihilated. Requires repair (`Practice, Gadgets` check) afterward. While this is running, the mech acts twice as fast. 
* **Fractal Heatsink**: Can be activated to STOP its heat output, which is useful for stealth.
