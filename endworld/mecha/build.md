---
outgoing links:
- endworld/mecha/mecha#sizes
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
A Size is chosen from the [Mecha size table](endworld/mecha/mecha#sizes). This defines the total number of Sectors.
## 2. Sectors & Topology Setup
Sectors must be formally named (e.g., "Left Arm," "Core," "Upper Torso") to house systems. A stable structural topology is required:
- **Adjacency**: A full list of links between sectors must be established. All sectors must be connected.
- **Facing Sectors**: These are the sectors most hit (see [Targeting](endworld/combat#targeting)). Facing sectors may not be linked to each other.
- **Stability Score**: Stability = (Facing Sectors * 5) - (Non-Facing Sectors * 3) + (Links * 1). The score must be 0 or higher.
- **Topology Sketch**: A sketch of the mecha layout is recommended.
### Minimum Facing Sectors Table
These minima result from the stability rule above and are provided to save calculation effort.
| Size (Total Sectors) | Min. Facing Sectors |
| :--- | :--- |
| 1–3 | 1 |
| 4–7 | 2 |
| 8–11 | 3 |
| 12–15 | 4 |
| 16 | 5 |
## 3. Module Allocation
Modules are assigned to named sectors.
- **Hardpoints**: Some systems require a hardpoint. Only one system requiring a hardpoint may be assigned to a sector.
- **Seal**: Every mecha must be equipped with a [Seal](endworld/mecha/systems/support#seals) to protect against Contamination.
- **Allocation Guidelines**: A typical combat mecha consists of roughly 50% defensive systems ([Armor](endworld/mecha/systems/armor) and [Shields](endworld/mecha/systems/defensive)), 10-15% each for [Heat](endworld/mecha/systems/heat), [Energy](endworld/mecha/systems/energy), and [Offensive](endworld/mecha/systems/offensive) systems, with remaining weight allocated to [Support](endworld/mecha/systems/support) and cargo.
- **Cargo**: All unused weight capacity of the chosen Mech size may be declared as cargo space, which is assumed to be full for speed calculations.
## 4. Verification Checklist
- **Tonnage**: The weight of all installed systems together must be equal to or less than the Tonnage limit in the [Size Table](endworld/mecha/mecha#sizes). If the tonnage increases beyond the limit, an extra sector might need to be provisioned, requiring a re-design of the topology.
- **Energy**: Ensure there is a valid loadout where generated energy >= used energy (see [How Power Works](endworld/mecha/systems/energy#how-power-works)).
- **Heat**: Ensure flux capacity meets or exceeds peak heat generation. Ensure that at the loadout that works, heat reaches a steady state (see [Flux Pool](endworld/mecha/systems/heat#the-flux-pool)).
- **Tech Level**: Note the highest Tech Level among all installed systems.
- **Stability**: Stability Score must be 0 or higher.
- **Sectors**: Ensure all sectors are valid, connected, and that systems are assigned to sectors.
