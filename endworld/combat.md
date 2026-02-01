---
outgoing links:
- endworld/ewrules#Bonus-and-Penalty-Dice
- endworld/descriptions/attributes#physical
- endworld/descriptions/attributes#special
- endworld/mecha/systems/shields
- endworld/mecha/systems/armor
- endworld/ewrules#resonance
- endworld/ewrules#bonus-and-penalty-dice
tags:
- ''
title: combat
---
## Rounds

Combat is done in rounds.  
In Detailed Combat, each round is about 5 seconds long. In Tactical Combat, rounds are of variable length and could last an hour.

Every character present acts in turn (determined by circumstances or a Stealth, Perception, Intuition, or other situational check) and can usually move and act or attack.

Double actions, if possible, usually carry a 2-dice [penalty](endworld/ewrules#Bonus-and-Penalty-Dice) on both actions; further actions carry even more penalties.

---

## Attacks

An attack has to be made on a valid target.  
Targets are valid depending on what weapon is used. A direct fire weapon requires line of sight, for example.

Depending on the circumstances, the attack roll is made, involving [Dexterity](endworld/descriptions/attributes#physical) for normal weapons, [Focus](endworld/descriptions/attributes#special) for Mech weapons and so on, the weapon skill, and another selector depending on the situation, which can be tactics derived for example, or coordinated via command, or from a FCS.

This result of this roll, called **attack value** from here, is then modified by range depending on the weapon.

If the attack value is positive, the general vicinity of the target is hit.  
Then, the enemy defense from dodging, deflectors or cover is subtracted.

If the attack value is still positive, the target is hit and damage calculation starts. The leftover attack value may increase damage depending on Weapon type 
Otherwise, cover may still be damaged.

---

## Damage

Each entity is made of several hitzones (like arms, legs, head).  
When a hit succeeds, a hitzone is affected. Defense, which is usually rolled reduces the attack’s value, which is usually fixed. If anything remains, the hitzone takes damage.
[Shields](endworld/mecha/systems/shields) trigger before [Armor](endworld/mecha/systems/armor) and are handled according to their own rules.

Damage doesn’t use fixed HP values. Instead, it causes malfunctions and penalties such as weakened limbs or malfunctioning components, negative [resonance](endworld/ewrules#resonance)s giving [penalty dice](endworld/ewrules#bonus-and-penalty-dice), performing at a lower level or no longer functioning.

If armor or a defensive layer breaks, it stops protecting. Some defenses may leak damage through while they break.

For living targets, damage represents wounds, which may heal, for systems they represent damage which may be repaired.

### Malfunctions

When a sector or system takes damage, it may suffer a malfunction. Malfunctions typically add **Penalty Dice** to relevant actions.

| Malfunction             | Effect                   | Relevant Actions                 |
|-------------------------|--------------------------|----------------------------------|
| **Sensor Glitch**       | +1 Penalty Dice          | Perception, Targeting, Scanning  |
| **Actuator Jam**        | +1 Penalty Dice          | Movement, Melee Attacks, Dodging |
| **Power Leak**          | +10% Energy Cost         | Affected System                  |
| **Circuits Frying**     | +2 Heat/Turn             | Affected System                  |
| **FCS Error**           | +1 Penalty Dice          | Ranged Attacks                   |
| **Structural Weakness** | Additional System Damage | All hits to this sector          |

Multiple malfunctions in the same sector or affecting the same action are cumulative.

---

## Death

There is no exact number of hit points that causes death.  
Instead, as damage builds up, the character becomes less functional.

A person might pass out.  
A machine might shut down.  
Death or destruction only happens when the Storyteller decides it's appropriate.


---

## Defense

Defense can be gained from dodging, cover, or other situationally appropriate means.  
In general, the defense value is just the result of the roll of the action if it would provide appropriate protection.

Taking cover behind a hanging fishing net or trying to talk down an automated turret might not result in any defense at all.

**Dodging**, usually done with Agility and Acrobatics, Footwork, or Running, requires the action for that round, meaning it needs to be repeated every round, and is subject to double action rules.

**Cover**, once taken with Agility and Tactics, Running, Stealth, Footwork, or whatever is appropriate, provides its defense until it is nullified by flanking or movement is taken. Furthermore, there is the possibility of full cover granting a flat bonus onto the roll.

**Other actions** may include throwing sand, building rapport, talking someone out of shooting, and are resolved by themselves.

---

## Detailed Combat

1. Every participant (technically in secret) decides on what they are going to do.
2. Non-offensive actions are resolved
3. then offensive actions in descending order of rolled result.


---

## Tactical Combat

In many respects much like Detailed Combat, Tactical Combat zooms out over encounters that could take a while. It is not unusual to switch back and forth.

In Tactical Combat, there are usually no single actions. Tactical actions encompass states and processes.

Anytime something changes, everyone who is aware may change what they are doing. If these reactions cascade, Detailed Combat is the natural consequence and actions will proceed in 5-second intervals.

If an actor does more or less the same thing 3 times in a row, it might be appropriate to enter Tactical Combat.  
A state and/or process will interpret the last 3 rolls and take the average of that number.

Rolls that do not succeed fully may carry over some part of the result until the threshold is met, so someone nearly missing will instead hit at a lower rate.

When entering Tactical Combat, some form of time commitment is agreed upon and after each interval one roll is made.

The moment of this roll is also the only time for unprovoked re-evaluation and change of plans.  
The interval should be changed by the Storyteller depending on the density of action.

**Tactical actions might include:**

- Firing on an enemy or a position
- Guarding a position
- Breaking down a door
- Traversing to a point
- Looking out
    

---

## Targeting

To attack something a "facing" (see below) hitzone needs to be selected, for a humanoid target "torso" is usually the facing hitzone
From there, deviations occur, spreading the damage over neighboring parts.

For a human target, the Hitzones are:
Grazing, Legs, Torso, Arms, Head.
For human like Targets
for a Mech they are specific to the mech.
A Hitzone adjustment means adjusting the zone or sector that would be hit to one of its Neighbors, the empty space "around" counts as missing and for technical reasons contains infinitely many empty hitzones in all directions. If a hit lands in the empty space at the end of targeting, it counts as a miss.

First, any Hitzone Adjustments from called shots (see below) are chosen by the attacker
Then, the sum of Amplitudes of Frequencies 1-5 allow the defender adjust hitzones
Then, the sum of Amplitudes of Frequencies 6-10 allow the attacker to adjust hitzones.

### Mech Sectors

A mech has several sectors (determined by its size class, which is determined by its weight), each of which are their own hitzone.
1/3 rounded up of the Sectors need to be "facing" sectors which can be anything, but usually things like "front" or "rear", about half (rounded up) of facing sectors are targeteable in most situations.

### Called Shots

To try to ensure that a specific area is hit, a called shot can be made, any number of times, as long as the attack has less than 5 Malus Dice.  
A called shot allows one hitzone adjustment (see above) for taking 1 Malus dice.
Without perks, this hitzone adjustment is made before the roll


### Sniping

The opportunity to attack is spent, making a roll with perception, sniping and the weapon in question, modified with bonus/malus dice by factors like light, weather, crowds, cover, distance and so on and modified additively by target evasive maneuvers, complete lack of movement and other factors that detract from/help with zeroing-in.
The distance modifier is 0 between minimum and optimum range, from there it is -1, for every started 3 times the drop interval

The result clearing the basic threshhold to hit (usually 5) is halved (rounded up) and applied as an additive bonus if the next action is sniping/attacking the same target
