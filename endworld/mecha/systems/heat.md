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

Any heat left in a generating system after Phase 1 is **Residual Heat**. Heat that cannot be stored in a system (most non-heat systems have 0 capacity) adds to the sector's **stress** (see [Sector Stress](endworld/combat#sector-stress)). Residual heat from any system in a sector spreads to all systems - an overheating weapon can cook the ammunition stored next to it.

If the fluxpool stays full for more than one turn, the mecha suffers chassis-wide instability -- speed is halved, computer systems crash, and the reactor automatically scram.

### Reactor Shutoff Delay

Energy Systems may not stop generating heat instantly. Every [Energy System](endworld/mecha/systems/energy) has a **Shutoff Delay**. When a reactor is deactivated, it continues to output its full baseload heat for a number of turns equal to its **Shutoff Delay**.

## Heat Systems

Sinks scale with installed weight. All values for sinks are per ton.

| Type               | Weight | Energy | Capacity | Flux | Passive | Active | Hardpoint |
|--------------------|--------|--------|----------|------|---------|--------|-----------|
| **Basetech**       |        |        |          |      |         |        |           |
| Refractory Block   | per t  | 0      | 30       | 0.5  | 1/25    |        | no |
| Blowoff Valve      | 0.5    | 0      | 15       | 15   |         | 15     | yes |
| **Lowtech**        |        |        |          |      |         |        |           |
| Radiator Vent      | 0.5    | 5      | 10       | 5    | 1       | 10     | yes |
| Water Reservoir    | per t  | 0      | 80       | 5    | 1/25    |        | no |
| Water cooling      | 0.5    | 3      | 5        | 5    |         |        | no |
| Anti-Detonant Inj. | 2.0    | 5      | 15       | 15   |         | 15     | no |
| **Midtech**        |        |        |          |      |         |        |           |
| Phase Change Cell  | per t  | 4      | 50       | 10   | 1/30    |        | no |
| Phase Change Loop  | 1      | 5      | 5        | 15   |         |        | no |
| Heatpipes          | 1      | 0      | 0        | 15   |         |        | no |
| Coolant Dump       | 1      | 25     | 25       | 25   |         | 25     | no |
| Heat Exchanger     | 5      | 50     | 160      | 15   | 1/30    | 35     | yes |
| Radiator Wings     | 1      | 10     | 50       | 5    |         | 1/4    | no |
| **Hightech**       |        |        |          |      |         |        |           |
| Fractal Heatsink   | 0.5    | 10     | 100      | 5    | 2       | -2     | no |
| Thermal Capacitor  | per t  | 8      | 60       | 8    | 1/30    |        | no |
| Liquid Metal Loop  | 1      | 15     | 10       | 30   |         |        | no |
| Electrochromic Dissipator | 0.5 | 20 | 11 | 0 | | 11 | yes |
| ECCS               | 0.5    | 20     | 40       | 40   |         | 40     | no |
| OVERDRIVE          | 0      | 100    | -        | 0    | -       |        | no |

**Notes**:

* **Consumable Cooling (Blowoff Valve, ADI, Coolant Dump, ECCS)**: All of these systems create a **Steam-Screen** while active, provided at least half of the consumed fluid was actually used to absorb heat (no heat, no steam).
* **Steam-Screen**: Generates a dense thermal and visual cover field. Blocks visual and thermal locks/line-of-sight in *both directions* (the mech cannot see out, enemies cannot see in). 
* **Blowoff Valve**: Consumes 15kg of Cargo (Water) per turn. Deafeningly loud.
* **Anti-Detonant Injector**: Consumes 15kg of Cargo (Water/Coolant) per turn. Boot time: 1.
* **Coolant Dump**: Consumes 25kg of Cargo (Coolant) per turn. Boot time: 1. Shutoff time: 1.
* **ECCS**: Consumes 50kg of Cargo (Coolant) per turn. Shutoff time: 2 (Minimum 3 turns active, burning massive cargo).
* **Radiator Wings**: 5 turns to deploy. Vulnerable while extended (no armor applies).
* **Overdrive**: Once activated, the **fluxpool** is uncapped. Heat in the **fluxpool** instead annihilates heat when assigned to a sink. Mech shuts down once the **fluxpool** either stays full or all the heat has been annihilated. Requires repair (`Practice, Gadgets` check) afterward. While this is running, the mech acts twice as fast. 
* **Fractal Heatsink**: Can be activated to STOP its heat output, which is useful for stealth.

## Operational Analysis
For non-combat activities - such as travel, active standby, or guarding - mecha designs may be analyzed for thermal equilibrium to save work during gameplay. Players can analyze their [Loadouts](endworld/mecha/mecha#loadouts) for these scenarios and calculate the heat levels at which the systems stabilize.

To determine the steady-state heat for a scenario:
1. **Calculate Load**: Determine the total heat generated by systems required for the specific activity (e.g., travel).
2. **Calculate Dissipation**: Determine the total heat dissipation provided by active systems in that scenario.
3. **Determine Equilibrium**: Compare the two values to identify the heat level where the system stabilizes.

These loadouts can be marked as "Steady State" in the mecha build documentation, noting the stable heat levels to quickly reference during play.
