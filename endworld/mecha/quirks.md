---
outgoing links: []
tags:
- ''
title: quirks
---

# Quirks - Reference Tables

## Rolling

Roll three d10 in sequence:

**Roll 1 - Severity**

| d10 | Table |
|-----|-------|
| 1-5 | Light |
| 6-8 | Medium |
| 9-10 | Heavy |

**Roll 2 - Band (within the tier)**

| Tier | d10 | Band |
|------|-----|------|
| Light | 1-5 | Common |
| Light | 6-8 | Uncommon |
| Light | 9-10 | Rare |
| Medium | 1-4 | Common |
| Medium | 5-6 | System Stress |
| Medium | 7-8 | Control Oddities |
| Medium | 9-10 | Rare |
| Heavy | 1-4 | Common |
| Heavy | 5-7 | Uncommon |
| Heavy | 8-10 | Rare |

**Roll 3 - Quirk (d10 on that sub-table)**
If you hit a "Reroll on the table above" result, roll again on the reroll's sub-table (same d10 for band, no need to re-roll severity).

## Light Quirks

### Common

| d10 | Name | Effect |
|-----|------|--------|
| 1 | **Hot Run** | +1 heat/turn while active |
| 2 | **Thermal Affinity** | Reinterpret Affinity <= 8: system takes 2 heat |
| 3 | **Thermal Feedback** | If on and ends turn with residual heat, produces 1 extra heat |
| 4 | **Sympathetic Vibration** | On activation, all other systems in the same sector take 1 heat |
| 5 | **Ion Burst** | Fills nearby area with ions - lightning, sparks, chemical traces |
| 6 | **Data Echo** | All data outputs corrupted, including logs. Real-time fine, degrades computer integration |
| 7 | **Resonant Chatter** | System hums, interferes with nearby sensitive equipment (-2 very sensitive, -1 normal sensors) |
| 8 | **Rattling Bits** | Something loose / left inside. Rattles. |
| 9+ | **Repair** | Roll on Repair table instead |

### Uncommon

| d10 | Name | Effect |
|-----|------|--------|
| 1 | **Fragile** | All stress thresholds -1 |
| 2 | **Tricky Boot** | Threshold [5,11]: <=5 = +2 turns, 6-11 = +1, 12+ = instant |
| 3 | **Unstable Output** | First Usage each Scene Reinterpret Affinity: <= 6: -1 effect; >= 7: +1 effect |
| 4 | **Jolty** | On use, 1 surge strain to own sector from power surge |
| 5 | **Uncanny** | Disturbs living things |
| 6 | **Hot Start** | Needs 10 heat in flux pool after outbound phase to start |
| 7 | **Slow Reset** | Reboot takes +1 turn |
| 8+ | **Common** | Reroll on the table above |

### Rare

| d10 | Name | Effect |
|-----|------|--------|
| 1 | **Thermal Overload** | Residual heat: functions at higher level, mech interior fills with smoke |
| 2 | **Feedback Siphon** | Surge stress: makes system function at higher level |
| 3 | **Rain-Sensitive** | -1 effect in rain/humid conditions |
| 4 | **tinted glass** | Cockpit glass and sensor feeds tint at random, even without sun |
| 5+ | **Uncommon** | Reroll on the table above |

## Medium Quirks

### Common

| d10 | Name | Effect |
|-----|------|--------|
| 1 | **Greedy** | Energy cost doubled |
| 2 | **Tied Together** | Two systems share on/off. Disable/destroy one => other turns off |
| 3 | **Sprawl** | Also exists in an adjacent sector |
| 4 | **Vocal Diagnostic** | Loudly announces status. Cannot silence without overhaul |
| 5 | **Jumpy Safety Cutout** | Any sharp movement/hit (even non-damaging) triggers 1-turn safety shutdown |
| 6 | **Crosstalk** | Electrically noisy; detectable by active sensors at 2x normal range |
| 7 | **Reversed Polarity** | As long as there is energy and system can turn on, it turns on. Auto-reboots if shut down |
| 8 | **Hot Reload** | Generates 10 heat on boot |
| 9 | **Voltage Sag** | During boot, other systems function at -1 |
| 10 | **Delayed Shutdown** | Refuses shutdown for indeterminate time |

### System Stress

| d10 | Name | Effect |
|-----|------|--------|
| 1 | **Backblast** | Resonance: amplitude stress to own sector for additional effect |
| 2 | **Double Burden** | Stress from one type (heat/damage/contamination) doubled for this system |
| 3 | **Power Vampire** | When shut down, if other systems are running in its sector, one powers off at random and this stays on instead |
| 4 | **Cascade Error** | Any system uncontrolled shutdown: this shuts down too |
| 5 | **Low Contamination Resistance** | Contamination doubled for threshold purposes |
| 6 | **Overheat Prone** | On resonance 6: generates 6 x amplitude heat |
| 7 | **Filter Clog** | Resonance frequency 1: clogs accumulate (+1 per amplitude). +1 heat per clog level. Clearable 1 turn |
| 8 | **Backfeed** | When this system takes stress, half (rounded down) also applied to longest-running energy system |
| 9 | **Unstable Capacitor** | 8 resonance: +50% x amplitude effect, then shuts down |
| 10 | **System** | Roll system-specific quirk. If this system already has one, roll Common instead |

### Control Oddities

| d10 | Name | Effect |
|-----|------|--------|
| 1 | **Shutdown: Flux Overload** | Shuts down whenever fluxpool > 50% |
| 2 | **Shutdown: Armor Breach** | Shuts down on any damage through armor |
| 3 | **Corrupted Diagnostics** | No information about status |
| 4 | **Over-Lubricated Actuators** | +1 initiative, -1 accuracy |
| 5 | **Cockpit Feedback** | Unpleasant chassis vibrations; pilot takes -1 cumulative penalty each turn active (recovers 1 per inactive turn) |
| 6 | **Diagnostic-shimmed** | Broadcasts telemetry to everyone: cooldowns, ammo, etc. |
| 7 | **Spool Whine** | Audible pitch tells enemies rough status. 1 bonus die for anticipating |
| 8 | **Sticky** | System might reactivate next round / stay activated |
| 9 | **Magnetic** | Part is decently magnetic. Generally 1 penalty die, depends on system |
| 10 | **System** | Roll system-specific quirk. If this system already has one, roll Common instead |

## Heavy Quirks

### Common

| d10 | Name | Effect |
|-----|------|--------|
| 1 | **Chatterbox** | +1 penalty die to sensor-reliant systems while this is on |
| 2 | **Flicker** | Reinterpret Affinity <= 5: does nothing this turn |
| 3 | **Flimsy** | All stress thresholds halved (rounded down) |
| 4 | **Dramatic Irony** | Once/session, at worst possible moment, system auto-fails. No roll |
| 5 | **Unstable Mount** | On incoming hit with ANY resonance: knocked offline 1 turn |
| 6 | **Absolute Seal** | Contamination resistance +5, thermal resistance -5 |
| 7 | **Overpressure** | Residual heat causes damage |
| 8 | **Harmonic Resonance** | +1 heat on use per other system with harmonic resonance |
| 9 | **Timed Shutdown** | After 3 turns of being on, shuts down automatically |
| 10 | **unsealable** | Contamination threshold lowered for sector |

### Uncommon

| d10 | Name | Effect |
|-----|------|--------|
| 1 | **Interference** | Works at reduced level unless only system in the sector |
| 2 | **Berserk** | Once firing, keeps firing each turn if physically able. Pilot spends action to stop |
| 3 | **Intermittent Arcing** | Any roll with resonance 7: this sector gains amplitude EMP |
| 4 | **Eager** | System may power up/use by itself on specific resonance |
| 5 | **Brittle Repairs** | Any amount of stress increase on the system shuts it off |
| 6 | **Limited Use** | Limited activations (e.g. 3) before deactivation; needs field repair |
| 7 | **Drifting Calibration** | 1 malus die |
| 8+ | **Common** | Reroll on the table above |

### Rare

| d10 | Name | Effect |
|-----|------|--------|
| 1 | **Contamination Leak** | Each use adds 1 contamination to this sector |
| 2 | **Terminal Surge** | Use frequency 1 with amplitude 3+: destroyed, deals 10 damage to sector |
| 3 | **Glitchy Internals** | Crashes after any resonance event; needs reboot |
| 4 | **Signal Lag** | Inputs delayed 1 turn; acts on previous turn's orders |
| 5+ | **Uncommon** | Reroll on the table above |

## Weapon Quirks

| Name | Effect |
|------|--------|
| **Jittery** | +1 penalty die aimed/careful, +1 bonus die snap/reaction |
| **Overload** | 2nd consecutive use: +4 damage, then shuts down. Must reactivate |
| **Target Glitching** | Malus against near OR far targets (one band) |
| **Sticky Feed** | Resonance < 3: jams, needs reload to clear |
| **Sluggish Cyclerate** | Cannot fire consecutive turns (must skip a turn) |
| **Glitchy Autoloader** | Frequency 10: fires twice. Frequency 1: jammed, clear requires roll 8+ |
| **Live Ammo** | For 1 round after damage: any resonance < 6 causes cookoff, 4 damage to sector |
| **Uncommanded Mode Switch** | On specific resonance, switches fire mode |
| **Friendly Fire Prone** | Result <= 5: shot goes wide, hits ally in area with (6-result)x3 damage or cover |
| **Momentum Reliant** | +1 effect above 50% speed, -1 below 25% speed (also Movement) |

## Movement Quirks

| Name | Effect |
|------|--------|
| **Tripping Hazard** | Resonance 1: mech falls, must stand back up |
| **Rough Terrain Stall** | Taking hits in rough terrain stops movement |
| **Momentum Reliant** | +1 effect above 50% speed, -1 below 25% speed (also Weapon) |
| **Over-Lubricated Actuators** | +1 initiative, -1 accuracy (also Weapon) |
| **Jammed Actuator** | Specific resonance: movement direction and speed locked |
| **Control Glitch** | Controls reverse randomly, lock to full throttle for 1 round |
| **Creaky** | Joints audibly groan; +1 penalty die to stealth |
| **Limited Steering** | Takes extra time to change facing or direction |
| **Imprecise Movement** | Hard to reach exact positions; overshoots or drifts |
| **Slow Acceleration** | Reaches top speed in 2x normal time |

## Sensor Quirks

| Name | Effect |
|------|--------|
| **Ghost Readings** | Resonance: data might be entirely wrong |
| **Sensor Haunting** | voices of dead or similar|
| **Target Glitching** | Penalty against near OR far targets |
| **Temporal Leak** | Shows data from past/future sometimes |
| **Ads** | Ads play. Practice, Computer + something roll to skip |
| **Motion Blur** | Penalty die against fast-moving targets |
| **Static Bleed** | Penalty die against slow or stationary targets |

## Heat Quirks

| Name | Effect |
|------|--------|
| **Intermittent Cooling** | 6 resonance: no heat transfer for amplitude turns |

## Computer Quirks

| Name | Effect |
|------|--------|
| **Ads** | Ads play. Practice, Computer + something roll to skip (also Sensor) |

## Communications Quirks

| Name | Effect |
|------|--------|
| **IFF Corruption** | Transponder shows wrong faction; allies may fire on this mech |

## Seal Quirks

| Name | Effect |
|------|--------|
| **Unreliable Seal** | Seal level reduced by 1 step (vacuum/hazard protection compromised) |

## Repair Quirks (d10)

Result from imperfect field repairs. Physical or structural oddities affecting maintenance.

| d10 | Name | Effect |
|-----|------|--------|
| 1 | **Parts Hungry** | Requires 2x parts for any repair on this system |
| 2 | **Fiddly** | +1 penalty die on repair rolls for this system |
| 3 | **Temporary Fix** | System lasts one week from last repair, then breaks |
| 4 | **Stubborn** | All repair times doubled for this system |
| 5 | **Exotic Parts** | Requires parts one tech level higher than normal |
| 6 | **Needs Expert** | -1 to skill selector on repair rolls |
| 7 | **Last Resort** | Cannot be field repaired again |
| 8 | **Unsafe Capacitors** | Holds charge after use. Cannot be safely opened/repaired for 24 hours after last power-up - risks explosion or shock |
| 9 | **Sparky** | 7 resonance: fills area with sparks during repair, may injure mechanic |
| 10 | **Expensive Taste** | Repairs cost 2 parts |

## Designing Your Own

These are examples. GMs should create quirks that tell a story. A quirk that reflects how the system was damaged or what jury-rig fixed it is better than a random roll.
