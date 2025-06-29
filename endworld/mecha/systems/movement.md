# Movement Systems

| Type            | E/r  | Ground Coef (t) | Area/Sector | Power/t | Hardpoints | Extra                 |
|-----------------|------|-----------------|-------------|---------|------------|-----------------------|
| **Basetech**    |      |                 |             |         |            |                       |
| Rail            | 55   | 0.001           | 20          | 500     | 50%        | Rails                 |
| Simple Wheels   | 100  | 8               | 1           | 750     | 25%        | Flat terrain          |
| Floatation      | 15   | 2               | 1000        | 90      | 10%        | Water                 |
| **Lowtech**     |      |                 |             |         |            |                       |
| Complex Wheels  | 175  | 6               | 3           | 1500    | 25%        | Somewhat flat terrain |
| Tracks          | 100  | 0.02            | 40          | 600     | 33%        | Rough terrain         |
| 2 Simple Legs   | 30   | 0.5             | 100         | 450     | 25%        | All terrain           |
| 4 Simple Legs   | 30   | 0.2             | 200         | 450     | 25%        | All terrain           |
| 6 Simple Legs   | 30   | 0.13            | 300         | 450     | 25%        | All terrain           |
| Jumpjets        | 1000 | 50              | 1           | 1000    | 1          | Upwards only          |
| **Midtech**     |      |                 |             |         |            |                       |
| 2 Flexible Legs | 100  | 10              | 10          | 1000    | 30%        | Humanoid              |
| 4 Flexible Legs | 100  | 1               | 100         | 1000    | 30%        | Stable walk           |
| 6 Flexible Legs | 100  | 0.3             | 1000        | 1000    | 30%        | High stability        |
| Boostjets       | 2000 | 5               | 0.1         | 1000    | 2          | Any direction         |
| **Hightech**    |      |                 |             |         |            |                       |
| Spiderwalker    | 150  | 0.1             | 500         | 400     | 50%        | Any surface           |

**Speed Calculations**:

* **Acceleration**:

  * Round 1: 50%
  * Round 2: 80%
  * Round 3: 100%

* **Friction**:
  `F = Mass * Ground Coefficient / 100 * 9.81`

* **Air Drag**:

  ```
  Airdrag = (49 * Speed² * Area) / 80
  Speed = Power / (Friction + Airdrag)
  ```
