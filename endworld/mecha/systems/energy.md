
## Energy Systems

**Terminology**:

* **Power to Weight**: Max output per weight unit.
* **Input**: Fuel type or energy storage (e.g. batteries).
* **Efficiency**: Output/input ratio, depending on usage mode.
* **Output Modes**:

  * Power Saving
  * Full Throttle
    Usage marked per full hour. If energy <1h remains, round-based calculation applies.

**Energy Units**:

* 1 Energy (E) = 5 kW over 1 round (5 seconds)
* 1 MJ = 200 E

| Type             | E/t  | Heat/r/t | Input       | Efficiency              |
|------------------|------|----------|-------------|-------------------------|
| **Basetech**     |      |          |             |                         |
| Steam Power      | 0.7  | 8        | Coal        | 10%                     |
| Flywheel         | 20   | 0        | Stored      | Loses 10% per turn      |
| Crew             | 0.01 | 0        | Labor       | 10%                     |
| **Lowtech**      |      |          |             |                         |
| Combustion Motor | 140  | 2        | Combustible | 40%                     |
| **Midtech**      |      |          |             |                         |
| PEM              | 100  | 0.1      | Hydrogen    | 90%                     |
| Solar Panel      | 10   | 2        | Sunlight    | Contamination Dependent |
| Batteries        | 10   | 2        | Stored      | Loses 10% per month     |
| **Hightech**     |      |          |             |                         |
| Reactor          | 300  | 5        | Fuel Rods   | 8%                      |
| CF Reactor       | 40   | 0.1      | Deuterium   | 80%                     |
| Capacitor        | 1000 | X        | Stored      | Loses 10% per hour      |

**Notes**:

* **Solar Panel**: 5 turns or 5 minutes to deploy per 100W. Halves output per 5 contamination levels. Daylight only.
* **CF Reactor**: Requires startup energy equal to 1 round of output.
* **Capacitor**: Generates 1 Heat per 10E moved.

**Fuel Storage**:

* **Deuterium (1 kg)**: 4.5 TJ → 900,000,000E (80% eff. = 720 ME)
* **Fuel Rod (1 kg)**: 75 TJ → 15,000,000,000E (8% eff. = 120 ME)
* **Hydrogen (70kg/1000L)**: 10,082 MJ → 2,016,400E (90% eff. = 1,814,760E)

  * HFC-10 (10L): 1,800E
  * HFC-50 (50L): 9,000E, includes low-power startup subsystem
* **Combustion Fuel (1000L/800kg)**: 8,000,000E (3.2 ME)
* **Battery**: 180,000E/t
