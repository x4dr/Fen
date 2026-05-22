# Repair

Systems and sectors can be repaired in the field or at a proper facility.

## Field Repair

A field repair takes 2 hours by default. The pilot may take malus dice to shorten this:

| Malus Dice | Time |
|------------|------|
| 0 | 120 min |
| 1 | 60 min |
| 2 | 30 min |
| 3 | 15 min |
| 4 | 5 min |
| 5 | 1 min |

The roll is made against the system's repair thresholds. Default thresholds are [5, 9, 13], modified by tech level:

| Tech | Thresholds |
|------|------------|
| Base | [5, 9, 13] |
| Low | [5, 10, 14] |
| Mid | [6, 11, 16] |
| High | [7, 13, 18] |
| Experimental | [8, 15, 20] |

The threshold reached determines the outcome. Duration does not change based on threshold reached - the time is set by the malus dice chosen before the roll.

| Threshold | Result |
|-----------|--------|
| Below first | Further damage done. System gains a **repair quirk**. |
| First | System operational with a **quirk** and a **repair quirk**. |
| Second | System operational with a **quirk**. |
| Third | As new. No quirks. |

### Sector Stress

Sectors can be repaired similarly - the roll result lowers the sector's stress and repairs its seal. (Needs workshoping - do sectors need their own table?)

## Facility Overhaul

At a workshop, hangar, or drydock of appropriate size and tech level, the pilot can make unlimited retries of the repair roll. This allows removing quirks and fully restoring systems.

## Quirks

When a field repair leaves a quirk, the GM picks one from the [Quirks](endworld/mecha/quirks) tables or invents one fitting the situation.
