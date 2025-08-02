---
outgoing links:
- endworld/ewrules#Bonus-and-Penalty-Dice
- endworld/descriptions/attributes#physical
- endworld/descriptions/attributes#special
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

Depending on the circumstances, the attack roll is made, involving [Dexterity](endworld/descriptions/attributes#physical) for normal weapons, [Focus](endworld/descriptions/attributes#special) for Mech weapons and so on, the weapon skill, and another skill depending on the situation.

This result of this roll, called **attack value** from here, is then modified by range depending on the weapon.

If the attack value is positive, the general vicinity of the target is hit.  
Then, the enemy defense from dodging, deflectors or cover is subtracted.

If the attack value is still positive, the target is hit and damage calculation starts. The leftover attack value may increase damage depending on Weapon type 
Otherwise, cover may still be damaged, depending on the circumstances.

---

## Damage

Each entity is made of several hitzones (like arms, legs, head).  
When a hit succeeds, a hitzone is affected. Defense, which is usually rolled reduces the attack’s value, which is usually fixed. If anything remains, the hitzone takes damage.
[Shields](endworld/mecha/systems/shields) trigger before [Armor](endworld/mecha/systems/armor) and are handled according to their own rules.

Damage doesn’t use fixed HP values. Instead, it causes malfunctions and penalties such as weakened limbs or malfunctioning components, negative [resonance](endworld/ewrules#resonance)s giving [penalty dice](endworld/ewrules#bonus-and-penalty-dice), performing at a lower level or no longer functioning.

If armor or a defensive layer breaks, it stops protecting. Some defenses may leak damage through while they break.

For living targets, damage represents wounds, which may heal.

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

Generally, a center-mass targeting is assumed.  
From there, deviations occur, spreading the damage over neighboring parts.

For a human target, the hitzones are determined by d10, or by the resonance of the attack roll if any.  
If there are several resonances, the attacker gets to pick.

|Roll|Target|
|---|---|
|1–3|Torso|
|4–6|Legs|
|7–8|Arms|
|9|Hands or Feet|
|10|Head|

---

### Called Shots

To ensure that a specific area is hit, a called shot can be made, risking missing altogether.  
A penalty to the attack value is taken, to hit the specific body part.

A resonance with a number corresponding to a body part less than what was aimed for will instead attack that part, as above.

|Target|Penalty|
|---|---|
|Head|3|
|Hands or Feet|2|
|Legs|1|
|Torso|1|
