# Movement Systems

| Type            | Energy | Heat | Anchor | Dynamics | Thrust/t | Extra                 |
|-----------------|--------|------|--------|----------|----------|-----------------------|
| **Basetech**    |        |      |        |          |          |                       |
| Rail            | 55     | 0    | 0.001  | 500      | 50       | Rails                 |
| Simple Wheels   | 100    | 0    | 8      | 20       | 20       | Flat terrain          |
| Floatation      | 15     | 0    | 0      | 5        | 90       | Water                 |
| **Lowtech**     |        |      |        |          |          |                       |
| Complex Wheels  | 175    | 1    | 3      | 100      | 40       | Somewhat flat terrain |^
| Tracks          | 100    | 3    | 1      | 15       | 60       | Rough terrain         |
| 2 Simple Legs   | 30     | 2    | 2      | 14       | 45       | All terrain           |
| 4 Simple Legs   | 30     | 4    | 1      | 12       | 45       | All terrain           |
| 6 Simple Legs   | 30     | 6    | 0.5    | 10       | 45       | All terrain           |
| Jumpjets        | 1000   | 10   | 50     | 50       | 100      | Upwards only          |
| **Midtech**     |        |      |        |          |          |                       |
| 2 Flexible Legs | 100    | 3    | 3      | 10       | 100      | Humanoid              |
| 4 Flexible Legs | 100    | 5    | 2      | 8        | 100      | Stable walk           |
| 6 Flexible Legs | 100    | 7    | 1      | 6        | 100      | High stability        |
| Boostjets       | 2000   | 15   | 20     | 250      | 120      | Any direction         |
| **Hightech**    |        |      |        |          |          |                       |
| Spiderwalker    | 150    | 9    | 0.1    | 5        | 200      | Any surface           |

**Speed Calculations**:

under construction!

calculate base friction by calculating (Anchor/100)*total mech weight 
Thrust (times tonnage) divided by the total weight of the mech is acceleration
net acceleration is acceleration - base friction
Maximum speed is the square root of (10 * Dynamics * net acceleration)
Example
60 ton mech with thrust 60 at anchor 1
friction is 0.6
acceleration =  60/60 = 1
net_accel = 0.4
sqrt(10*15*0.4)=7.75 m/s (ir roughly 27 kmh)
at 2 tons that would be  net_accel of 1.4 raising speed to 14.5 m/s or 18 with 3tons
(which is 52km/h and 64 km/h respectively)
filling the mech somehow with 50% tracks:
acceleration = 59.4 ==> 66 m/s 


acceleration duration is sqrt(dynamics*10)/sqrt(net_acceleration)*3 rounds ... ish... for now



* **Friction**:
  `F = Mass * Ground Coefficient / 100 * 9.81`

* **Air Drag**:

  ```
  Airdrag = (49 * Speed² * Area) / 80
  Speed = Power / (Friction + Airdrag)
  ```
