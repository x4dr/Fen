---
outgoing links:
- endworld/mecha/mecha
- endworld/mecha/systems/armor
- endworld/mecha/systems/heat
- endworld/mecha/systems/energy
- endworld/mecha/systems/offensive
- endworld/mecha/systems/defensive
- endworld/mecha/systems/support
tags:
- ''
title: build
---

# Build

The construction of a Mecha follows a standardized process to ensure structural integrity and operational viability.

## 1. Chassis Definition
A Size is chosen from the [Mecha](endworld/mecha/mecha) size table. This defines the total number of Sectors.

## 2. Topology Setup
A stable structural topology is required. Sectors must be formally named to describe their placement within the mecha (e.g., "Left Arm," "Core," "Upper Torso").

### Adjacency List
A full list of links between sectors must be established. This list defines the topology. Facing sectors may not be linked to each other. A sketch of the mecha layout is recommended.

### Stability Score
Stability = (Facing Sectors * 5) - (Non-Facing Sectors * 3) + (Links * 1)

The Stability Score must be 0 or higher.

### Minimum Facing Sectors Table

These minima result from the rule above and are provided to save some calculation

| Size (Total Sectors) | Min. Facing Sectors |
| :--- | :--- |
| 1–3 | 1 |
| 4–7 | 2 |
| 8–11 | 3 |
| 12–15 | 4 |
| 16 | 5 |

## 3. Module Allocation
Modules are assigned to named sectors.
- **Hardpoints**: Some systems require a hardpoint. Only one hardpoint exists per sector unless otherwise specified.
- **Spreading**: Modules can be spread over multiple adjacent sectors, which increases the likelihood of damage if a sector is struck.
- **Resource Management**: Install systems from the following categories:
    - [Offensive](endworld/mecha/systems/offensive)
    - [Defensive](endworld/mecha/systems/defensive)
    - [Armor](endworld/mecha/systems/armor)
    - [Heat](endworld/mecha/systems/heat)
    - [Energy](endworld/mecha/systems/energy)
    - [Support](endworld/mecha/systems/support)

## 4. Verification Checklist
- **Tonnage**: The total weight of all installed systems must be equal to or less than the Tonnage limit of the chosen size.
- **Tech Level**: The Mecha Tech Level is determined by the highest Tech Level among all installed systems.
- **Stability**: Stability Score must be 0 or higher.
- **Hardpoints**: No sector may exceed one hardpoint.
- **Topology**: Every sector is included in the named list and the adjacency link list.
