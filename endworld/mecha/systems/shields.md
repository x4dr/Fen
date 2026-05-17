---
outgoing links: []
tags: []
title: shields
---
# Defensive Systems

Defensive systems are configured using a relevant [Technical Skill](endworld/descriptions/abilityskills#defense) and Method, usually [Computer Usage](endworld/descriptions/abilityskills#computer), with thresholds [5,9,13,17,20] (or automatically by a [Program](endworld/mecha/computers)).

Configuration takes 1 Action. If the lowest threshold is not reached, the value is 0 but the system still starts. Each threshold reached counts as 1 toward the Config value used by the system.

**Grade** is a property of the individual unit, not the model. Grade 2 is market standard (used but functional). Grade 3 is factory new. Grade 4 is enhanced or hard to source.

Coldboot can only be done after all Systems (not just shield ones) have been off for at least one turn. When a system is overwhelmed or disabled, it must be configured again to turn back on. The timer starts after the Configuration roll succeeds. Energy is required during boot.

**Cost:** Per sector for being active. **Failure:** Normal behavior on failure is for the system to turn off until rebooted.

An attack is any attack action, or round of fire sustained from one weapon, unless that weapon states that it counts as several attacks for the purposes at hand.

---

## Shields

When a shield activates, it makes a **Grade, Config@5** roll against the incoming damage:

Flat Damage Reduction + (roll result) * Roll scaling

Both values are properties of the specific generator and include its weight scaling. If the reduction meets or exceeds the damage, the shield holds. If not, it is overwhelmed and shuts down. Each shield protects one sector, chosen during configuration.

| Name | Tech | Weight | Flat Damage Reduction | Roll scaling | Energy | Heat | Reboot | Failure |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| **Basetech** | | | | | | | | |
| Applique-Armor | 1 | 1t | 2 | 1.0 | 0e | 0H | - | block |
| **Midtech** | | | | | | | | |
| Light Shield | 3 | 0.5t | 3 | 1.4 | 25e | 1H | 5r | |
| Standard Shield | 3 | 1t | 4 | 1.5 | 40e | 2H | 5r | |
| Heavy Shield | 3 | 5t | 9 | 2.1 | 60e | 3H | 5r | |
| Flash Shield | 3 | 1t | 2 | 1.3 | 20e | 2H | 0r | block |
| **Hightech** | | | | | | | | |
| Rapid Shield | 4 | 0.3t | 2 | 1.3 | 30e | 1H | 2r | |
| Advanced Shield | 4 | 1t | 5 | 1.4 | 50e | 2H | 3r | |
| Barrier Projector | 4 | 3t | 9 | 1.5 | 50e | 2H | 5r | |
| Cascade Screen | 4 | 5t | 7 | 2.3 | 80e | 4H | 5r | |
| **Experimental** | | | | | | | | |
| Ghost Wrap | 5 | 0.2t | 0 | 1.5 | 20e | 1H | 3r | |
| Fortress Barrier | 5 | 10t | 16 | 2.3 | 150e | 5H | 5r | destroyed |

**Light Shield:** A compact generator for light mechs or secondary sectors where tonnage is tight.
Lower protection, lower energy draw.

**Standard Shield:** The baseline generator. Its performance curve is the reference point for all
other shields in production.

**Heavy Shield:** A large-frame generator. Same technology as the Standard Shield, just scaled up.

![Heavy Shield Table](tables)

**Flash Shield:** Designed for immediate reboots. When a Flash Shield is overwhelmed, it comes back
as soon as the Configuration action completes, not at end of turn. A pilot who holds an action can
reconfigure after being hit and have the shield back up without waiting.

**Rapid Shield:** A lightweight generator with a short reboot cycle. The reduced boot timer
compensates for the low flat values. Tech 4 electronics make the small package viable.

**Advanced Shield:** The hightech baseline. Higher flat reduction and a shorter reboot timer than
the Standard Shield. The most widely produced hightech generator.

**Barrier Projector:** A reinforced generator with high flat reduction. The roll scaling is moderate,
keeping the reduction in a predictable range regardless of the roll.

**Cascade Screen:** A high roll scaling generator. Extreme roll amplification produces a wide
performance range. Energy cost and heat output are the tradeoffs.

**Ghost Wrap:** An experimental field generator with no flat reduction. All protection comes from
the Grade, Config roll and the roll scaling. The negligible weight makes it usable on any mech that
can supply the energy.

**Fortress Barrier:** An ultra-heavy generator for the largest mech frames. The flat reduction alone
stops most peer weapons. If the barrier is overwhelmed, the generator is destroyed rather than shut
down.

**Applique-Armor:** Bolted or adhesived armor plates. No electronics, no energy cost. The weight is high for the protection, but it requires no power and works on any mech with the tonnage to spare. Coldboot requires physically applying new plates.
## Deflectors

Deflectors need to be Configured with the Deflector skill and require a minimum degree of success
to work and provide flat evasion bonuses.

Deflectors add their Evasion to the defending side when an attack is made, reducing enemy accuracy.

Deflectors work on missiles, but not on melee strikes.

| Type | Evasion | Weight | Cost | Coldboot |
|---|---:|---|---|---|
| Basic Deflector | 1 | 0.2t | 10e, 1H/attack | 1r, Config 5 |
| Complex Deflector | 3 | 0.8t | 40e, 2H/attack | 8r, Config 10 |

Deflectors and Dampeners provide their effects to the entire mech. If their coverage is less than
the number of sectors, the bonus is scaled to the fraction they cover (rounded down).

---

## Dampeners

Dampeners need to be Configured with the Shield skill and provide flat damage reduction against
attacks that rely on kinetic energy. Melee and ballistic damage is reduced; lasers and missiles
are not. The Storyteller decides what counts for other attack types.

Dampeners subtract from enemy damage, helping armor and shields. If an attack is reduced below 0,
it is slowed so much it does not land.

| Type | Reduction | Weight | Cost | Coldboot |
|---|---:|---|---|---|
| Basic Dampener | 5 + Config | 0.5t | 20e, 3H/attack | 3r |
| Heavy Dampener | 10 + Config x2 | 1t | 60e, 5H/attack | 10r |

Dampeners and Deflectors do not fail from damage.


