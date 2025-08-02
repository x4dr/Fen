# Armor
Armor encompasses all sorts of armor from personal to mech. It is rolled when damage is taken, and the result directly reduces the damage
if no damage remains, the damage calculation is canceled. By default, armor that fails to reduce damage to below 0, is damaged, losing protection.
Armor at protection 0 still works, but is destroyed if it fails again.

Armor stats: 
- **Protection** - How good this armor is at absorbing damage
- **Structure** - How well it is applied/integrated/coverage and so on.
- **Tech** - the Techlevel of the armor. Worn armor is exposed to its wearer (ignoring seal) once a day.
- **Weight** - Malus dice on actions where the weight of armor is relevant (running, quickshooting), offset by Fitness.

It also can have additive and multiplicative bonuses, multiplicative being applied first.

for every 3 [Sizes](endworld/mecha#sizes) above/below, the number belonging to the bigger system gets multiplied with 2.


Seals get damaged, if there is any damage incoming, and can be repaired with a seal repair kit, within half an hour usually.


## Personal Armor

This is armor on the personal scale, able to be worn by a single person. 

### Hazard suit

- **Protection**: 0 
- **Structure** : 0
- **Tech**: 2
- **Weight**: 0 

Has a lot higher capacity for seals than regular clothes

### Armored clothes

- **Protection**: 1 
- **Structure** : 0
- **Tech**: 1
- **Weight**: 1 

Clothes reinforced with materials like kevlar, having some plates in some spots
 
### Light Armor

- **Protection**: 1 
- **Structure** : 1
- **Tech**: 1
- **Weight**: 1 


The same materials as armored clothes, but with an underlying structure, plate holders, and rigging to allocate the load

### Combat Armor

- **Protection**: 2  
- **Structure**: 2  
- **Tech**: 2
- **Weight**: 3

Modern military-grade body armor with hard plates, modular protection, and moderate sealing options. Effective against small arms and shrapnel.


### Assistive Combat Suit

- **Protection**: 2  
- **Structure**: 3  
- **Tech**: 3
- **Weight**: 2

An armored exoskeleton equipped with military grade modular armor plates, compensating its own weight.

### Heavy Unpowered Armor

- **Protection**: 4  
- **Structure**: 4  
- **Tech**: 2
- **Weight**: 6

Extremely heavy armor, of a low tech

## Mech armor


The **Structure** stat reflects how well armor is installed and integrated. When it has degraded through field repairs it can be restored by doing an armor refit in a Workshop, Hangar, or Drydock of appropriate size.

To refit armor, spend **50% of the armor's total weight** (in tons) in **Parts** of the appropriate Techlevel, to make a check, involving Practice, Engineering (build or repair) and any Proficiency relating to the armor. After reinstallation, the Structure rating becomes one of the following tiers: [5, 9, 13, 17, 20]
Optionally the roll can be kept back until the armor takes its first hit.

A Refit takes **1 day per ton** of armor weight (minimum 1 day). A **rush job** takes **half the time** but imposes **1 Malus Die**. A **meticulous job** takes **7 times the time** but gives **1 Bonus Die**.

Multiple characters may work together, dividing the required time, if each has the necessary proficiency. Only the leader rolls.

Tools and facility quality affect the outcome:
- If the tools/workshop are **1 or more tiers higher**, add **1 Bonus Die**.
- If they are **1 tier lower**, apply **1 Malus Die**.
- More than 1 tier below: reinstallation is **not possible**.
- Having [Blueprints](endworld/crafting)


A Mechs have segments, that need to armored and often layer armor. Weight is given per segment.
If not otherwise given, repair rolls below 5 lower structure.

### Outside Cargo
- **Protection**: 0  
- **Tech**: 1 
- **Weight**: 1.1  
- **Failure**: Cargo Destroyed  

Each of these might provide decent protection if installed correctly, and provides 1 ton of extra cargo storage, however the "armor" in question is precious cargo, which will be destroyed if it is ever overcome (and possible by just being shot at)

### Metal Plating  
- **Protection**: 2  
- **Tech**: 1 
- **Weight**: 2
- **Repair**: always succeeds, but rolls under 12 lower Structure.
Good ol' metal plating. Outmatched against a lot of armorpiercing technology, but then again, a lot of attacks are not armorpiercing.

### Ultra High Density Composite  
- **Protection**: 4  
- **Tech**: 1
- **Weight**: 5  
- **Failure**: block  
- **Repair**:  8+, Resonance 1 lowers Protection by Amplitude
Made from somewhat rare and very dense and durable metals, this might be expensive but is one of the most durable options out there. Even when it fails, it blocks the shot that took it down.

### Sheetmetal  
- **Protection**: 0  
- **Tech**: 2 (Lowtech)  
- **Weight**: 0.1  
- **Repair**: 5 +, structure always lowers. Can be refit at one size category less


### Composite Plating  
- **Protection**: 3  
- **Tech**: 2 (Lowtech)  
- **Weight**: 2.5  
- **Repair**: 5+

Common, but effective


### Active Plating  
- **Protection**: 1 (passive) / 4 (active)  
- **Tech**: 3 (Midtech)  
- **Weight**: 2  
- **Failure**: if active: block
- **Energy**: can be turned on for 5 energy / segment
- **Repair**: 10+
- **Boot**: 2 minutes

If the active part is on, incoming projectiles get counter-blasted by highly charged explosion-liquified metal.
On a resonance with 1, The module turns off and must reboot, on Amplitudes of more than 1, the system is damaged and passive until repaired.

### SpeedShell  
- **Protection**: 1  
- **Tech**: 3 (Midtech)  
- **Weight**: 0.5  
- **Failure**: Destroyed, passthrough  

While speed is higher than 10m/s, this armor provides an extra 2 heat venting / segment 


### Ion Armor  
- **Protection**: 5  
- **Tech**: 4 (Hightech)  
- **Weight**: 1  
- **Failure**: Destroyed, energy system damage, block  
- **Energy**: 2

This hightech armor provides excellent protection, at a risk. The energy costs are very low as the ion field builds, but failure means a shock to the internals which usually damages the linked energy system, as well as turning the module into high tech scrap. Even then, its protection ends **after** the attack.


### Holomatrix  
- **Protection**: 1  
- **Tech**: 5 (Experimental)  
- **Weight**: 0  
- **Failure**: Damaged  
- **Repair**: 500 grams of Experimental Tech Parts, installing/refitting takes 2kg (per sector) instead.

This advanced defensive system has negligible weight and an extremely good protection rating. Its vulnerability to contamination and high repair costs might be its only weaknesses.
