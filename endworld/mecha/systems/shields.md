Defensesystems are configured using the relevant [Technical Skill](endworld/descriptions/abilityskills#defense),
the relevant usage Method, usually [Computer Usage](endworld/descriptions/abilityskills#defense),
with (if not defined otherwise) the threshholds [5,9,13,17,20] or automatically by a [Program](endworld/mecha/computers).

Configuration, Protection are the [armor](endworld/mecha/armor)-equivalent statistics a shield provides.  
Configuration is required to start a Shield and takes 1 Action, if the lowest threshhold is not hit, the Configuration  
is 0, but the Shield still starts.

Coldboot can only be done after all Systems (not just shield ones) have been shut off for at least one turn.

Shields turn off when overwhelmed and have to meet the Reboot requirements (and be configured again) to turn  
back on.  
Config X means that the specific Configuration Threshhold of X has to be reached.  
Each Shield protects one sector, which can be chosen during configuration. 
Deflectors and Dampeners provide their effects to the entire mech, if their coverage is less than the amount of sectors
the provided bonus is scaled to the fraction they cover (rounded down).

Deflectors add ther Evasion to the defending side when an attack is made, reducing enemy accuracy

Deflectors work on missiles, but not on melee strikes.

Dampeners subtract from enemy damage, helping armor and shields. If an attack is reduced below 0, its slowed so much it
does not land. 

Dampeners work on melee strikes, but not on missiles. 

An attack is any attack action, or round of fire sustained from one weapon, unless that weapon states that it counts as several attacks for the purposes at hand.

| Type              | Protection              | Weight | Cost            | Failure | Reboot | Coldboot               |
|-------------------|-------------------------|--------|-----------------|---------|--------|------------------------|
| **Basetech**      |                         |        |                 |         |        |                        |
| Applique-Armor    | Strength 1              | 1      | -               | block   | -      | physically applying it |
| **Lowtech**       |                         |        |                 |         |        |                        |
| Basic Deflector   | 1 Evasion               | 0.2    | 10 e, 1H/attack | -       | -      | 1r, Config 5           |
| Basic Dampener    | 5 + Config Reduction    | 0.5    | 20 e, 3H/attack | -       | -      | 3r                     |
| **Midtech**       |                         |        |                 |         |        |                        |
| Shield            | Strength 3              | 1      | 40 e, 1H/attack |         | 5r     | 5r                     |
| Complex Deflector | 3 Evasion               | 0.8    | 40 e, 2H/attack | -       | -      | 8r, Config 10          |
| Heavy Dampener    | 30 + Config×3 Reduction | 1      | 60 e, 5H/attack | -       | -      | 10r                    |
| Flash Shield      | Strength 1              | 1      | 20E, 2H/attack  | block   | X×H    | 2r                     |
| **Hightech**      |                         |        |                 |         |        |                        |
| Advanced Shield   | Strength 4              | 1      | 200E/r or 20E/r | block   | 1r     | 5r                     |

---

**Deflectors** need to be Configured with the Deflector skill and require a minimum degree of success to  
work and provide flat evasion-level bonuses.

**Dampeners** need to be Configured with the Shield skill and provide a flat damage reduction to all  
attacks that are influenced by shields, they usually scale with the Quality of the Configuration.

**Flash Shield** As soon as the configuration is done, they turn back on.  
X is set to 0 at Coldboot and increased by 1, everytime the Shield is broken.  
A 10-Resonance on the Configuration reduces X by its Amplitude, even going negative.  
While X is negative, reboots don't generate heat.

**Cost:** per sector for being active.  
**Failure:** Normal behaviour on Failure is for the shield to turn off until rebooted.  
**Dampeners and Deflectors** don't fail from damage.
