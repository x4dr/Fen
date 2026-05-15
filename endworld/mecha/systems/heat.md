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

## The Flux Loop

The **fluxpool** is a single shared buffer for the whole mecha. Heat moves through it in three phases each turn.

The pool has a maximum capacity equal to the mecha's **Total Flux** (sum of flux provided by all active systems). Disabled systems contribute zero flux. It cannot go over its max and cannot go below 0.

### Phase 1: Inbound (Systems -> Pool)

The player chooses which active systems to pull heat from. Heat fills the pool until it hits max or there is no more heat to pull.

Any heat that could not be moved stays in the generating system as **Residual Heat**, which may trigger an [Overheat Check](#overheating).

### Phase 2: Outbound (Pool -> Heat Systems)

The player chooses how much heat to push from the pool into each heat system (sinks, vents, anything with capacity). Systems without heat capacity (most non-heat systems) cannot receive heat. Heat empties from the pool until it hits 0 or there are no more heat systems to fill.

### Phase 3: Dissipation

Each heat system follows its own rules to remove or process heat (see Heat Systems table). Vents actively dump heat when supplied with energy. Sinks bleed heat slowly through passive cooling.

Because the pool fills first then empties, a full cycle moves at most Total Flux worth of heat through each direction per turn. If the pool is not emptied, less room is available to fill next turn.

### Residual Heat

Any heat left in a generating system after Phase 1 is **Residual Heat**. If a system has more heat than its capacity (most non-heat systems have 0 capacity), it risks overheating each turn.

If the fluxpool stays full for more than one turn, the mecha suffers chassis-wide instability -- speed is halved, computer systems crash, and the reactor automatically scram.

## Overheating

Thermal failure occurs when systems store more heat internally than their capacity allows (most non-Heatsystems have 0 capacity). Components with **Residual Heat** begin to **Overheat**, risking malfunction or explosive failure.

### Overheat Check

At the end of any turn where a component has more heat than its capacity, the pilot must perform an [Affinity Check](endworld/ewrules#the-selector-system), using a heat management skill if they have one, and the thermal hardening level (if applicable) of the system as Skills.

The result of this check is compared against the component's **Residual Heat**. If the result is lower than the heat stored, the system suffers a consequence.

| Result | Outcome                      | Effect                                                                                                |
|:-------|:-----------------------------|:------------------------------------------------------------------------------------------------------|
| 11+    | **Heat Accumulation**        | 1 [Penalty Die](endworld/ewrules#bonus-and-penalty-dice) on all subsequent heat rolls for this system |
| 8-10   | **Thermal Glitch**           | System flickers. -1 to all actions with this system until reset/cooldown                              |
| 5-7    | **Compromised Control**      | System automatically shuts down for 1 turn.                                                           |
| 3-4    | **Malfunction**              | System is Damaged. See [Damage](endworld/combat#damage) table.                                        |
| 1-2    | **Catastrophic Malfunction** | Total destruction of the system. Cookoff/explosions possible                                          |

Any 6-[Resonance](endworld/ewrules#resonance) in the Overheat Check introduces additional heat.

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
