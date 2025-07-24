---
outgoing links: []
tags: !!set
  mech: null
title: mechtest
---

# Description

# Systems

## Movement

|        | Energy | Heat | Thrust | Anchor | Dynamics | Mass | Amount | Enabled |
|--------|--------|------|--------|--------|----------|------|--------|---------|
| Wheels | 80.0   | 5    | 400.0  | 0.5    | 5.0      | 2.0  | 10.0   | [ ]     |
| Rails  | 100.0  | 3    | 200.0  | 0.001  | 1000.0   | 3.0  | 10.0   | [x]     |

## Energy

|                     | Energy | Mass | Amount | Enabled |
|---------------------|--------|------|--------|---------|
| baseloadreactor     | 50.0   | 5.0  | 3.0    | [x]     |
| peakload stage 1    | 20.0   | 5.0  | 3.0    | [x]     |
| peakload stage 2    | 20.0   | 5.0  | 2.0    | [x]     |
| backup generator    | 15.0   | 1.0  | 1.0    | [x]     |
| emergency generator | 10.0   | 1.0  | 1.0    | [x]     |

## Heat

|         | Energy | Mass | Amount | Capacity | Passive | Active | Flux | Current | Enabled |
|---------|--------|------|--------|----------|---------|--------|------|---------|---------|
| Vent    | 30.0   | 0.25 | 2.0    | 100.0    | 10%     | 2      | 5.0  | 0.0     | [x]     |
| Coolant | 5.0    | 0.1  | 1.0    | 50.0     | 0       | 10     | 25.0 | 0.0     | [x]     |
| Sink    | 0.0    | 1.0  | 1.0    | 400.0    | 1%      | 0.01   | 0.0  | 0.0     | [x]     |

## Offensive

|         | Energy | Mass | Amount | Enabled |
|---------|--------|------|--------|---------|
| AutoGun | 30.0   | 7.0  | 1.0    | [x]     |

## Defensive

|            | Energy | Mass | Amount | Enabled |
|------------|--------|------|--------|---------|
| Junk Armor | 0.0    | 5.0  | 5.0    | [x]     |

## Support

|                | Energy | Mass | Amount | Enabled |
|----------------|--------|------|--------|---------|
| Coffee machine | 30.0   | 1.0  | 1.0    | [ ]     |

## Seal

|                            | Level |
|----------------------------|-------|
| External Experimental Seal | 25.0  |

# Loadouts

## Default
[0], Wheels, [10.0], Rails, [15.0], Vent, [25.0], Coolant, Sink, Junk Armor, AutoGun, [40.0], Coffee machine, [50.0]
