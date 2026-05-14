# Repair

Systems and sectors can be repaired in the field or at a proper facility. Field repairs are quick but leave **quirks**. Facility overhauls restore full function.

## Field Repair

To repair a system or sector, roll against its repair thresholds. Default thresholds are [5, 9, 13], modified by tech level:

| Tech | Thresholds |
|------|------------|
| Base | [5, 9, 13] |
| Low | [5, 10, 14] |
| Mid | [6, 11, 16] |
| High | [7, 13, 18] |
| Experimental | [8, 15, 20] |

A repair roll uses the relevant skill (Engineering, Practice, or a system-specific skill) and takes time:

- **Quick patch**: 10 minutes per threshold reached
- **Proper field repair**: 1 hour per threshold reached

### Results

| Threshold | Result |
|-----------|--------|
| Below first | No effect. Damage remains. |
| First [5] | System functions again but gains a **quirk** (see below). Accumulated damage reduced by one step (e.g., Critical → Heavy). |
| Second [9] | System fully functional. Optionally pick a minor quirk or leave it clean. Accumulated damage cleared. |
| Third [13] | Flawless repair. No quirks. Accumulated damage cleared. System functions as new. |

### Multi-System Sectors

A field repair on a sector repairs the most damaged system in that sector. Clearing a sector's damage fully requires repairing each system individually.

## Facility Overhaul

At a workshop, hangar, or drydock of appropriate size, accumulated damage is cleared from all systems and all quirks are removed. Requires parts matching the system's tech level (weight in parts × 50% for full overhaul).

See [Armor Refit](endworld/mecha/systems/armor) for armor-specific repair rules.

## Quirks

A quirk is a persistent oddity that remains until a facility overhaul. Quirks are named so they can be tagged on systems for automatic hover effects in the UI.

When a field repair leaves a quirk, the GM picks one from the table below or invents one fitting the situation. These are examples - GMs should create quirks that tell a story.

### Example Quirks

| d10 | Name | Effect |
|-----|------|--------|
| 1 | **Feedback Loop** | Reinterpret Pilot ≤ 5 on any system use: system takes 2 heat |
| 2 | **Flicker** | Reinterpret Pilot ≤ 7 on activation: system doesn't respond this turn |
| 3 | **Overeager** | Reinterpret Pilot ≥ 12 on use: system performs at +1 level, then shuts down |
| 4 | **Ghost Reading** | Reinterpret Scan ≤ 5: system reports false status |
| 5 | **Slow Reset** | Reboot takes +1 turn |
| 6 | **Intermittent** | Reinterpret Pilot ≤ 5 on each use: system does nothing this turn |
| 7 | **Hot Run** | System generates +2 heat per turn while active |
| 8 | **Resonant Chatter** | Reinterpret Pilot ≥ 14 on use: system emits visible pulse, +2 detectability 1 turn |
| 9 | **Ammo Hungry** | Weapon consumes double ammo on Reinterpret Attack ≤ 5 |
| 10 | **Unstable Output** | Reinterpret Pilot even: +1 damage. Odd: -1 damage |
