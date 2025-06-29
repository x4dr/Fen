# Mecha
Mecha, short for mechanical, are typically giant walking robots, ruleswise, everything consisting of parts, having systems and having weight is handled as mecha, such as: cars, bikes, static defense towers, artillery installations, giant walking robots, giant treaded robots, Fridges and so on.

A Mech has a size in Sectors which corresponds (roughly) to its weight, and a class, which is relevant for usage, representation in world and so on.

A mech can have multiple systems to accomplush tasks or Manage resources, like
[Movement](movement), [Energy](energy), [Heat](heat), [Offensive](offensive), [Defensive](defensive) and [Support](support), as well as a [Seal](support) to protect against Contamination.

## Sizes
| Sectors | Mech Class        | Weight |
|---------|-------------------|--------|
| 0       | Tool, Exo         | 0.1    |
| 1       | Exo               | 0.6    |
| 2       | Exo, Tiny         | 1      |
| 3       | Tiny              | 2      |
| 4       | Tiny, Very Light  | 4      |
| 5       | Very Light        | 10     |
| 6       | Very Light, Light | 18     |
| 7       | Light             | 40     |
| 8       | Light, Medium     | 70     |
| 9       | Medium            | 150    |
| 10      | Medium, Heavy     | 300    |
| 11      | Heavy             | 500    |
| 12      | Heavy, Very Heavy | 700    |
| 13      | Very Heavy        | 900    |
| 14      | Very Heavy        | 1200   |
| 15      | Very Heavy, Ultra | 1500   |
| 16+     | Ultra             | >1500  |

# Modules
- Modules are assigned to sectors.
- Each sector has a size of 1; a module takes up some of that size.
- Modules can be spread over multiple adjacent sectors, though this increases the likelihood of damage.
- Some modules require a hardpoint. There is usually only **one hardpoint per sector**.
- A mech’s **effective tech level** is based on the 90% point of the size-ranked modules sorted by tech level.
- **Contamination damage** applies to the highest-tech modules first.
- Each module can be damaged individually.


## Costs
Legacy Example cost with Trading Unit costs

| Tech | Credits Cost | Examples                                                                                                                                                                                                            |
|------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| B    | 4            | Water Distillery, Rail-based movement system, simple wheels, Manned gun, Ramshield, Flotation, Metal Armorplating, Extra Cargo (10), Steam engine, Passive cooling                                                  |
| L    | 5            | Lowtech Detox-Decon Equip (LDDE; +1), Suspended wheels, Tracks, Bipedal, Dynamo, Autoturret, Jumpjets, Mech-sized Sword, Water cooling circle, Basic Heatsink                                                       |
| M    | 6            | Shields, Flexible/balanced bipedal, Boostjets, Deployable Solar Panel, Sensor Array, MDDE (+2), Base AI system, Mech-sized Vibro/Electro/Monofilament Sword, Rocketlauncher, Water venting system, Midtech Heatsink |
| H    | 7            | BCI, Advanced AI, Weapon Laser, Sustained Flight, Advanced Shields, Nano Repair Cloud, Automedic, OVERDRIVE mode, Hightech Heatsink                                                                                 |
| E    | 8            | Quantum Lookahead Sensors, Blink Teleporter, Timerift Shields (Delays Damage 1d10 rounds), Energy Sword                                                                                                             |

## Misc Example Modules

All of these Are out of Date and kept for example purposes
### Basetech
#### Water Distillery
- **Energy Cost:** 50 kW
- **Heat:** 10
- **Weight:** 0.5t
- Converts 1L of dirty water into 1L of contaminated water per minute
- Requires **Reprocessing**

#### Cargo Compartment
- **Stores:** up to 1t of cargo   
- **Weight:** 0.5t for size calculation  
- **Speed Calc:** 0.1t (empty), 1.1t (full if relevant)

## Lowtech
### Basic Food Processor
- **Energy Cost:** 10 kW in operation
- **Heat:** 5
- **Size:** 0.5t
- Detoxes and prepares up to 5kg of food in 30 minutes
- Requires **Reprocessing**
- 
### Basic Air Filter
- **Energy Cost:** 15 kW per operation
- **Heat:** 2
- **Size:** 0.5t
- Decontaminates and pressurizes 3000L of air in 10 minutes (or double without pressurizing)
- Requires **Decon 1**

> Airtank (10L @ 300 bar) = 3000L of air  
> Air consumption: ~10L/min (5 hours walking; less for strenuous activity)  
> 3.675 kg of air + 15 kg for tank, valve, and hose

### Basic Decon Equipment
- **Energy Cost:** 20 kW per operation
- **Clean Water Cost:** 10:1
- **Heat:** 10
- **Size:** 0.5
- Decontaminates objects by washing
- 1 hour per kg
- Contamination reduced to 1/10 of original
- Used water becomes contaminated

### Optical Sensors
- **Energy:** 1
- **Size:** 0.25
- **Rating:** 100
- Provides targeting lock
- Visual Lock: Distance / Rating ≤ Target Size (adjusted for camouflage and impairments)

### Thermal Sensors
- **Energy:** 1
- **Size:** 0.25
- **Rating:** 100
- Thermal Lock: Distance / Rating ≤ Target Thermal Signature

### Basic Computer System
- **Weight:** 500kg
- **Energy:** 0.1
- **Module Type:** Processor or Memory

## Midtech
### Computer System
- **Weight:** 100kg
- **Energy:** 0.1
- **Module Type:** Processor or Memory

### Nondeterministic Computation Core
- **Size:** 0.5
- **Energy:** 0.5
- **Module Type:** Processor
- **Requirement:** Black Biotech 3

### Extended Decon Equipment
- **Energy Cost:** 36kW (10/s)
- **Alacast Cost:** 5g per operation
- **Size:** 1
- Decontaminates 100kg/h of objects
- On humans:
- Roll Red Biotech
- On 9+: remove one character taint
- Always inflicts a wound: 11 - Roll Result
- **Requires:** Decon 3

### Extended Detox Equipment
- **Energy Cost:** 36kW (10/s)
- **Size:** 0.75
- Detoxes/prepares up to 1t/h
- On humans:
- Roll Red Biotech
- On 6+: remove all infections and toxins
- Always inflicts a wound: 8 - Roll Result
- **Requires:** Detox 3

### Automedic
- **Energy Cost:** 6kW (variable — 10/s for 10 min)
- **Size:** 0.75
- Provides tools and ideal conditions for medical procedures
- Reduces medicine usage by half
- Allows **stasis** (medical coma)
- Slows down time-related effects (healing, contamination) by 10x per energy point/sec
- Roll Red Biotech:
- If roll > wound severity: grants temporary Medic skill + double advantage or attempts procedure autonomously (Lvl 3, mod -1)
- Else: grants one advantage
- Software may provide roll autonomously

## Hightech
### Advanced Detox-Decon Equipment
- **Size:** 1
- **Energy Cost:** 72kW (variable, 20/s for 1h)
- **Alacast Usage:**
- 1g/t of raw material
- 10g/human (if decontaminating)
- Detoxes and detaints up to 5t of material (air, water, objects)
- **Living beings are unharmed**
- Used with red biochroma and decontamination, living beings lose one contamination level
- Also removes all infections and appropriate toxins

### Advanced Automedic
- **Energy Cost:** 3kW (variable — 5/s for 10 min)
- **Size:** 1
- Grants excellent conditions for medical procedures
- Reduces medicine use by 90%
- **Allows resurrection**

#### To Treat a Wound:
- Roll Red Biotech
- If roll > wound: grants temporary Medic skill + 3 bonus dice or autonomous procedure (Lvl 4, mod -1)
- Else: grants one advantage or attempts procedure at Level 2
- Software can provide roll autonomously

#### To Resurrect:
- Requires 1g of **EOL** per total spent points on character (or 20× average level for NPCs)
- Roll **Black Biochroma**
- -1 to result for every 15% of the corpse missing or order of magnitude in days since death
- On success:
- Character gains **5 wounds of severity (15 - result)**
- Loses **1 level** from highest ability and highest skill
- Returns to life
- On failure:
- 5% of corpse and full EOL dose is lost

