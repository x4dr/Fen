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

If the attack value is still positive, the target is hit. The leftover attack value may increase damage depending on Weapon type. The damage flow is:

1. **Shields** activate (see [Shields](endworld/mecha/systems/shields))
2. **Armor** reduces remaining (see [Armor](endworld/mecha/systems/armor))
3. Remaining damage adds to the hit sector's **accumulated damage** (see [Sector Damage](endworld/combat#sector-damage))

Otherwise, cover may still be damaged.

---

## Shields & Armor

[Shields](endworld/mecha/systems/shields) trigger before [Armor](endworld/mecha/systems/armor).
Shields subtract their protection from incoming damage. If overwhelmed, they shut down.
Armor rolls its Protection - the result directly reduces remaining damage. If it fails to reduce damage to 0, the armor segment is damaged (Protection drops).

See the respective pages for details.

## Sector Damage (Mecha)

Mecha track damage per sector using **accumulated damage** - a single rising number per sector with thresholds that determine when systems inside it malfunction.

Each system in the sector has three thresholds:

| Threshold | Effect |
|-----------|--------|
| **Damaged** | +1 penalty die to relevant actions. Cumulative per system. |
| **Disabled** | System shuts down. Gains a specific malfunction from the table below. |
| **Destroyed** | System is gone. May cause cookoff or secondary damage (GM discretion). |

Thresholds are determined by the system's own stats. Higher tech systems pack more performance into less space, which makes them more fragile. Default values:

| Tech | Damaged | Disabled | Destroyed |
|------|---------|----------|-----------|
| Experimental | 5 | 12 | 25 |
| High | 6 | 15 | 30 |
| Mid | 8 | 18 | 35 |
| Low | 10 | 22 | 40 |
| Base | 12 | 25 | 50 |

When damage enters a sector that exceeds a threshold without reaching it yet, all systems at or below that threshold trigger their effect. Multiple hits accumulate. A sector that reaches Destroyed on any system is in danger of total destruction.

### Malfunctions

When a system triggers its **Heavy** threshold, pick a malfunction from this table (GM chooses what fits the situation and weapon type):

| Malfunction | Effect | Relevant Actions |
|-------------|--------|-------------------|
| **Sensor Glitch** | +1 Penalty Die | Perception, Targeting, Scanning |
| **Actuator Jam** | +1 Penalty Die | Movement, Melee Attacks, Dodging |
| **Power Leak** | +10% Energy Cost | Affected System |
| **Circuits Frying** | +2 Heat/Turn | Affected System |
| **FCS Error** | +1 Penalty Die | Ranged Attacks |
| **Structural Weakness** | Extra damage from hits | All hits to this sector |

Multiple malfunctions in the same sector are cumulative.

### Accumulated Damage and Repair

Damage stays on the sector until repaired. Field repairs reduce accumulated damage by the roll result against thresholds (see [Repair](endworld/mecha/repair)). A system that was at Heavy or Critical may function again but can gain a **quirk** - a permanent oddity until overhauled.

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

1. **Pick a targetable sector.** Only facing sectors can be targeted directly. See [Mech Generation](endworld/mecha/mecha) for how sectors are defined.
   The GM decides which facing sectors are available based on positioning (e.g., Front if face-to-face, Rear if flanked).

2. **Called shots** let the attacker shift the hit before rolling. Each shift costs 1 malus die. Max shifts before hitting 5 malus dice.

3. **After the roll**, the attack roll's own [resonance](endworld/ewrules#resonance) shifts the hit:
   - **Defender shifts**: total amplitude of frequencies 1-5. The defender pushes the hit toward a less critical sector.
   - **Attacker shifts**: total amplitude of frequencies 6-10. The attacker pulls the hit toward the sector they want.

   Each shift moves the hit one sector along the mech's adjacency diagram. Empty space adjacent to a sector counts as a miss.

4. The defender's defense roll may also influence positioning (GM discretion).

*Example: A size-5 mech has sectors Front, Rear, Head, Torso, Limbs. The attacker aims at Front. The roll is [3,3,5,8,9]:*
- *Resonance 1-5: pair of 3s → amplitude 1 → defender shifts 1 step*
- *Resonance 6-10: none → attacker shifts 0*
- *Net: hit lands on Limbs (neighbor of Front) instead of Front.*

### Humanoid Targets

For a human target the hitzones are: Grazing, Legs, Torso, Arms, Head. "Torso" is usually the facing hitzone.
A hitzone adjustment shifts to a neighbor. Empty space surrounds all sides - pushing a hit off the edge means a miss.


### Sniping

The opportunity to attack is spent, making a roll with perception, sniping and the weapon in question, modified with bonus/malus dice by factors like light, weather, crowds, cover, distance and so on and modified additively by target evasive maneuvers, complete lack of movement and other factors that detract from/help with zeroing-in.
The distance modifier is 0 between minimum and optimum range, from there it is -1, for every started 3 times the drop interval

The result clearing the basic threshhold to hit (usually 5) is halved (rounded up) and applied as an additive bonus if the next action is sniping/attacking the same target
