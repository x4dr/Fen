# Design Notes (from previous AI sessions)

Cleaned-up concepts from earlier design docs. Most of the original framing was based on a misunderstanding of the heat system (flux as "throughput limit") - these are the salvageable parts.

## 3-5 Round Rule

A mecha at full combat load (all weapons, max speed, high-draw shields) should begin to overheat after 3 to 5 turns. This is enforced by sink capacity vs net heat accumulation.

### Example: Standard Walker
- Total Sink Capacity: 200
- Baseload Heat: 10/turn (reactor + movement idle)
- Combat Heat: +40/turn (firing + shields)
- Net Generation: 50/turn
- Dissipation: ~12/turn (vent 10 + passive 2)
- Net Accumulation: 38/turn
- Time to Critical: 200/38 ≈ 5.2 turns

## Archetypes

| Type | Sink Cap | Combat Load | Rounds to Full |
|------|----------|-------------|----------------|
| Scout | 50 | ~15/turn | ~3 |
| Heavy | 300 | ~20/turn | ~15 |
| Suicide | 100 | ~10/turn | ~10 |

## 100-Token Goal

Heat values aimed at a 0-100 range for most mecha. Small to Medium mechs target Total Flux of 30-50. Values above 100 represent critical instability.

## Fluxpool Saturation

If the fluxpool stays full for more than one turn:
- Movement speeds halved
- Computer systems crash, target locks lost
- Reactor auto-scram (total shutdown)

## Radiator Wings

- 5 turns to deploy
- While extended: passive cooling doubled, but no armor applies
- Any hit to the sector damages the wings first
- Destroyed wings may cause coolant leaks

## Coolant System Integrity

Damage to a coolant system directly reduces its Flux contribution. Example: a system with Flux 60 getting damaged may drop to 30.

## High-Alpha Penalty

Weapons with high burst heat per shot need specialized high-flux coolant, or they damage the mecha on every shot.

## Tech Level Thermal Profiles

| Tech | Baseload | Flux (Avg) | Style |
|------|----------|------------|-------|
| Base | Low (1-3) | 10-15 | Passive-heavy (sinks) |
| Low | Mid (5-8) | 20-30 | Balanced |
| Mid | High (10-15) | 40-60 | Active-heavy (vents) |
| High | Very High (20+) | 80+ | Extreme cooling |

## Flux Partitioning (Tactical Choice)

Pilots choose which systems to cool first when flux is limited - keep the reactor stable or allow weapons to cool. This is resolved through the player-choice mechanic in heat phases 1 and 2.
