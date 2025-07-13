---
outgoing links:
- endworld/ewrules
- endworld/alacast
tags:
- ''
title: healing
---
## Healing

For living entities, damage is tracked as **wounds**, with severity equal to the remaining damage after defenses.  
While a wound is healing, the result of a Fitness check (usually no skills) divided by 2 is accumulated, then the Contamination exceeding the characters [Resistance](endworld/ewrules) is subtracted, once per day.
If multiple days pass with roughly the same conditions, the average of 3 rolls is taken and extrapolated.

If in active care, the healing skill/treatment level may be used as skill in the checks.

Healing rate can be modified by environment, therapy, or resonance:

- **Resonance 1**: lowers healing rate by amplitude (can go negative)
- **Resonance 10**: improves healing rate by amplitude

Wounds don’t always cause death or permanent damage, but long-untreated or out-of-control wounds may cause severe consequences (including death) at the Storyteller’s discretion.

When the accumulated healing progress equals the current severity, the wound severity drops by 1, and progress resets to 0.  
If healing rate is **negative**, and regeneration falls below 0, progress resets to current severity and severity increases by 1.

### Healing Time
When the healing rate is determined and the situation is somewhat stable, here is the expected time to heal per healing rate

| Severity | 1     | 2     | 3     | 4     | 5     | 6     | 7     | 8     | 9     | 10    |
|----------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| 1        | 1    | 1    | 1    | 1    | 1    | 1    | 1    | 1    | 1    | 1    |
| 2        | 3    | 2    | 2    | 2    | 2    | 2    | 2    | 2    | 2    | 2    |
| 3        | 6    | 4    | 3    | 3    | 3    | 3    | 3    | 3    | 3    | 3    |
| 4        | 10   | 6    | 5    | 4    | 4    | 4    | 4    | 4    | 4    | 4    |
| 5        | 15   | 9    | 7    | 6    | 5    | 5    | 5    | 5    | 5    | 5    |
| 6        | 21   | 12   | 9    | 8    | 7    | 6    | 6    | 6    | 6    | 6    |
| 7        | 28   | 16   | 12   | 10   | 9    | 8    | 7    | 7    | 7    | 7    |
| 8        | 36   | 20   | 15   | 12   | 11   | 10   | 9    | 8    | 8    | 8    |
| 9        | 45   | 25   | 18   | 15   | 13   | 12   | 11   | 10   | 9    | 9    |
| 10       | 55   | 30   | 22   | 18   | 15   | 14   | 13   | 12   | 11   | 10   |
| 11       | 66   | 36   | 26   | 21   | 18   | 16   | 15   | 14   | 13   | 12   |
| 12       | 78   | 42   | 30   | 24   | 21   | 18   | 17   | 16   | 15   | 14   |
| 13       | 91   | 49   | 35   | 28   | 24   | 21   | 19   | 18   | 17   | 16   |
| 14       | 105  | 56   | 40   | 32   | 27   | 24   | 21   | 20   | 19   | 18   |
| 15       | 120  | 64   | 45   | 36   | 30   | 27   | 24   | 22   | 21   | 20   |
| 16       | 136  | 72   | 51   | 40   | 34   | 30   | 27   | 24   | 23   | 22   |
| 17       | 153  | 81   | 57   | 45   | 38   | 33   | 30   | 27   | 25   | 24   |
| 18       | 171  | 90   | 63   | 50   | 42   | 36   | 33   | 30   | 27   | 26   |
| 19       | 190  | 100  | 70   | 55   | 46   | 40   | 36   | 33   | 30   | 28   |
| 20       | 210  | 110  | 77   | 60   | 50   | 44   | 39   | 36   | 33   | 30   |
| 21       | 231  | 121  | 84   | 66   | 55   | 48   | 42   | 39   | 36   | 33   |
| 22       | 253  | 132  | 92   | 72   | 60   | 52   | 46   | 42   | 39   | 36   |
| 23       | 276  | 144  | 100  | 78   | 65   | 56   | 50   | 45   | 42   | 39   |
| 24       | 300  | 156  | 108  | 84   | 70   | 60   | 54   | 48   | 45   | 42   |
| 25       | 325  | 169  | 117  | 91   | 75   | 65   | 58   | 52   | 48   | 45   |

---

## Treatment

Treatment is started via a **Competence or Theory + Healing Skill** check, depending on approach.  
Medicines and equipment provide bonuses or penalties, if the roll clears the [5] threshhold, the healing skill can be used for the healing rolls as long as treatment continues.

- Many wounds require medicine to treat. Without it, treatment may be impossible or penalized.
- At the Thresholds of [8, 11, 14, 17, 20], Bonusdice are applied to the healing process as long as the healing is maintained. retrying the roll is not possible without a change in treatment or the expenditure of resources
* Results < 5 may cause negative effects.


### Treating Contamination

- Requires at least **10g of Alacast**
- Apply **sum of all dice that are below or at the threshold of the technology used** as a new wound
- Ingress wound level and contamination drop by  [8, 11, 14, 17, 20].

In all cases [Alacast](endworld/alacast) is used to precipitate Contamination from the body, the  
crudest way is to introduce Alacast into the bloodstream to precipitate the contamination inside the body and hope the body expels  it on its own, more refined ways are basically a dialysis or a very specific targeting of crystallization seeds  and retrieval of precipitation clusters.

#### Treatment Methods
| Name                              | Threshhold |
| --------------------------------- | ---------- |
| Nano-Directed Dialysis            | 1          |
| Filtered Dialysis                 | 3          |
| Saline-Alacast Solution Injection | 8          |
| Directly applied Alacast powder   | 9          |

---

## Medicine

Medicine is consumed during treatment:  
`severity × 100g` per wound.

- **Naturopathy**: Healing + field; solid baseline and threshold bonuses.
- **Specialized Medicine**: Healing + ailment field; no floor but best scaling.
- **Broadband Medicine**: Healing + Science (Medicine) + Red Biotech; decent floor, weak scaling.
- **Alacast**: No healing bonus, fights contamination.
- **Elixir of Life**: Heals nearly everything but contaminates the user.
