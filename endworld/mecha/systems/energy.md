
## Energy Systems

Energy systems provide energy when they are switched on, while usually consuming something. 
if two values are given, the second one is an alternative "overdrive" move. For simplicities' sake, 
Energy systems are either off and consume nothing, in base mode or in overdrive.
Systems which don't have enough energy to run turn off and might have to be rebooted.

Values are given per ton and can be scaled up and down
**Terminology**:

* **E**: Energy output. 
* **Heat**: 
* **Input**: Fuel type or energy storage (e.g. batteries). For the sake of simplicity, 
* **Efficiency**: Output/input ratio, depending on usage mode.
**Energy Units**:
Energy units are now abstract, but originally they were
* 1 Energy (E) = 5 kW over 1 round (5 seconds)
* 1 MJ = 200 E

| Type             | E      | Heat    | Input              | Efficiency                    |
|------------------|--------|---------|--------------------|-------------------------------|
| **Basetech**     |        |         |                    |                               |
| Steam Power      | 2/4    | 3/8     | Coal               | 10%                           |
| Flywheel         | 20     | 0       | Stored             | spins down even if unused     |
| Crew             | 0.3    | 0       | 10 Crew Labor      | Crew tire after 30min*Fitness |
| **Lowtech**      |        |         |                    |                               |
| Combustion Motor | 50/150 | 1/2     | Combustible Liquid | 40%                           |
| **Midtech**      |        |         |                    |                               |
| PEM              | 50/100 | 0.1/0.3 | Hydrogen           | 90%                           |
| Solar Panel      | 10     | 2       | Sunlight           | Contamination Dependent       |
| Batteries        | 10     | 2       | Stored             | Loses 10% per month           |
| **Hightech**     |        |         |                    |                               |
| Reactor          | 300    | 5       | Fuel Rods          | 8%                            |
| CF Reactor       | 40     | 0.1     | Deuterium          | 80%                           |
| Capacitor        | 1000   | 8       | Stored             | Loses 10% per hour            |

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
