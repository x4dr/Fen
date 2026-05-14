
## Energy Systems and Loadouts

Energy systems provide power when they are switched on, while usually consuming something.
If two values are given, the second one is an alternative "overdrive" mode. For simplicities' sake,
energy systems are either off and consume nothing, in base mode or in overdrive.

### How Power Works

Energy is supply vs demand. Active reactors produce a budget. Each system that is turned on deducts its energy cost from that budget. A system cannot be turned on if it would bring the available budget below 0. If a system is turned off, its cost is freed.

The budget is recalculated whenever a system changes state (turned on or off, damaged, runs out of fuel, or is affected by a quirk). There is no per-turn tracking -- the system either has enough power or it does not.

### Fuel

Fuel is consumed in bulk when a system is activated, based on its runtime. For example, "1 ton of coal/hour" means 1 ton is consumed at startup and the system runs for an hour. If the system is turned off before the time is up, the remaining fuel is lost.

Some systems consume fuel at a rate that makes them relevant in combat (e.g., overdrive modes burning through reserves in a few turns). Track fuel consumption per turn in those cases.

### Loadouts

Every unique combination of active reactors creates a **budget bracket** -- the available E from those reactors. For example, with reactors producing 30, 60, and 90 E, the brackets are all unique sums:

`[0] [30] [60] [90] [120] [150] [180]`

(30+60=90 is already in the list, so no duplicate.)

A loadout is the order in which systems are turned on, written out with the budget brackets as breakpoints:

`[0], WeaponPod, ShieldGrid, [30], Sensors, [60], ActiveVents, [90]`

At budget 30: WeaponPod + ShieldGrid are active. At budget 60: Sensors also come online. Systems past the current budget stay off. The last bracket marks the highest budget tier where all listed systems are active.

Players are encouraged to create several loadouts covering different situations. Switching between them is done by turning systems on or off to match the target configuration, which may involve boot times for some systems.

### Values

Values are given per ton and can be scaled up and down.

**Terminology**:

* **E**: Energy output.
* **Heat**: Baseload heat generated per turn while active.
* **Input**: Fuel type or energy storage.
* **Efficiency**: Output/input ratio.

**Energy Units**:
Energy units are abstract, but originally:
* 1 Energy (E) = 5 kW over 1 round (5 seconds)
* 1 MJ = 200 E

| Type             | E      | Heat    | Shutoff | Input              | Efficiency                    |
|------------------|--------|---------|---------|--------------------|-------------------------------|
| **Basetech**     |        |         |         |                    |                               |
| Steam Power      | 2/4    | 3/8     | 10      | Coal               | 10%                           |
| Flywheel         | 20     | 0       | 0       | Stored             | spins down even if unused     |
| Crew             | 0.3    | 0       | 0       | 10 Crew Labor      | Crew tire after 30min*Fitness |
| **Lowtech**      |        |         |         |                    |                               |
| Combustion Motor | 50/150 | 1/2     | 3       | Combustible Liquid | 40%                           |
| **Midtech**      |        |         |         |                    |                               |
| Fission Core     | 150    | 15      | 5       | Rods               | 8%                            |
| PEM              | 50/100 | 0.1/0.3 | 1       | Hydrogen           | 90%                           |
| Solar Panel      | 10     | 2       | 0       | Sunlight           | Contamination Dependent       |
| Batteries        | 10     | 2       | 0       | Stored             | Loses 10% per month           |
| **Hightech**     |        |         |         |                    |                               |
| Reactor          | 300    | 5       | 3       | Fuel Rods          | 8%                            |
| CF Reactor       | 40     | 0.1     | 1       | Deuterium          | 80%                           |
| Micro-Fusion     | 600    | 30      | 1       | Pellets            | 80%                           |
| Capacitor        | 1000   | 8       | 0       | Stored             | Loses 10% per hour            |

**Notes**:

* **Solar Panel**: can be deployed/undeployed. Halves output per 5 contamination levels. Daylight only. Output halved for the first and last 4 hours of the 12-hour operational time (so effectively 8 hours of sunlight per day). Deployed solar panel gives 
  
* **CF Reactor**: Requires startup energy equal to output for at least one round.
* **Capacitor**: Generates 1 Heat per 100E moved.

**Fuel Storage**:

* **Deuterium (1 kg)**: 4.5 TJ → 900,000,000E (80% eff. = 720 ME = 1042 days at 40 energy)
* **Fuel Rod (1 kg)**: 75 TJ → 15,000,000,000E (8% eff. = 120 ME = 231 days at 300 energy)
* **Hydrogen (70kg/1000L)**: 10,082 MJ → 2,016,400E (90% eff. = 1,814,760E = 25 hours at 100 energy)

  * HFC-10 (10L): 1,800E = 1.5 minutes at 100 energy
  * HFC-50 (50L): 9,000E, includes low-power startup subsystem = 1.5 minutes at 100 energy
* **Combustion Fuel (1000L/800kg)**: 8,000,000E (40% eff = 3.2 ME = ~30h at 150 energy)
* **Battery**: 180,000E/t
