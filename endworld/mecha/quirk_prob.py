#!/usr/bin/env python3
"""
Quirk table cascade explorer.
Flat d100 tables with severity split 5:3:2 (Light:Medium:Heavy).
All per-quirk probabilities kept above ~0.5%.
"""

from collections import Counter

def pct_table(name, total_pct, sub_rolls):
    """
    sub_rolls: list of (label, count, roll_range)
    e.g. ("Common", 12, (1, 70)) means 12 common quirks, d100 1-70
    """
    print(f"\n  {name} (total {total_pct:.0f}%)")
    print(f"  {'d100':>4}  {'Band':>10}  {'# Q':>4}  {'Each':>6}  {'Sub-roll':>12}")
    print(f"  {'----':>4}  {'----':>10}  {'---':>4}  {'----':>6}  {'--------':>12}")
    for label, count, (lo, hi) in sub_rolls:
        band_pct = (hi - lo + 1) / 100 * total_pct
        each = band_pct / count if count else 0
        sr = ""
        if count == 1:
            sr = "direct"
        elif count <= 10:
            sr = f"d{count}"
        elif count <= 12:
            sr = f"d12 (reroll {count+1}-12)"
        else:
            sr = f"d% split {count} ways"
        print(f"  {lo:>3}-{hi:<3}  {label:>10}  {count:>4}  {each:>5.2f}%  {sr:>12}")

# Count quirks per severity per frequency
light_counts = {"Common": 12, "Uncommon": 2, "Rare": 4}
medium_counts = {"Common": 7, "Uncommon": 24, "Rare": 3}
heavy_counts = {"Common": 11, "Uncommon": 3, "Rare": 7}

print("=" * 60)
print("  QUIRK CASCADE — d100 based")
print(f"  Light:Medium:Heavy = 50%:30%:20%")
print("  All individual quirk chances > 0.5%")
print("=" * 60)

# ===== LIGHT: 50% =====
# 12 common, 2 uncommon, 4 rare
# Common gets 70% of Light = 35% total, 35/12 = 2.92% each
# Uncommon gets 15% of Light = 7.5% total, 7.5/2 = 3.75% each
# Rare gets 15% of Light = 7.5% total, 7.5/4 = 1.875% each

light_pct = 50.0
light_common_pct = 35.0
light_uncommon_pct = 7.5
light_rare_pct = 7.5

print(f"\n{'='*60}")
print(f"  LIGHT — 50% of all quirks")
print(f"{'='*60}")
print(f"  d100 01-70 (70% of Light = 35% total): Common (d12)")
print(f"  d100 71-85 (15% of Light =  7.5% total): Uncommon (d2)")
print(f"  d100 86-00 (15% of Light =  7.5% total): Rare (d4)")
print(f"  ─────────────────────────────────────")
print(f"  Common per quirk:   {light_common_pct/12:.2f}%")
print(f"  Uncommon per quirk: {light_uncommon_pct/2:.2f}%")
print(f"  Rare per quirk:     {light_rare_pct/4:.2f}%")

pct_table("Light breakdown", 50, [
    ("Common", 12, (1, 70)),
    ("Uncommon", 2, (71, 85)),
    ("Rare", 4, (86, 100)),
])

# ===== MEDIUM: 30% =====
# 7 common, 24 uncommon, 3 rare
# Common gets 30% of Medium = 9% total, 9/7 = 1.29% each
# Uncommon gets 55% of Medium = 16.5% total, 16.5/24 = 0.69% each
# Rare gets 15% of Medium = 4.5% total, 4.5/3 = 1.5% each

medium_pct = 30.0
medium_common_pct = 9.0
medium_uncommon_pct = 16.5
medium_rare_pct = 4.5

print(f"\n{'='*60}")
print(f"  MEDIUM — 30% of all quirks")
print(f"{'='*60}")
print(f"  d100 01-30 (30% of Medium =   9% total): Common (d7)")
print(f"  d100 31-85 (55% of Medium = 16.5% total): Uncommon (needs sub-split, 24 quirk)")
print(f"  d100 86-00 (15% of Medium =  4.5% total): Rare (d3)")
print(f"  ───────────────────────────────────────")
print(f"  Common per quirk:   {medium_common_pct/7:.2f}%")
print(f"  Uncommon per quirk: {medium_uncommon_pct/24:.2f}%")
print(f"  Rare per quirk:     {medium_rare_pct/3:.2f}%")

# Medium uncommon has 24 quirks. Need to split into sub-tables.
# d% 31-55 = Uncommon A (12 quirks, 7.5% total)
# d% 56-80 = Uncommon B (12 quirks, 7.5% total)
# d% 81-85 = Uncommon C (overflow)
# Or: 31-60 = A (12 quirks, 9% total), 61-85 = B (12 quirks, 7.5% total)
print(f"\n  Medium Uncommon split (24 quirk):")
print(f"    d100 31-60: Uncommon A (12 quirk, d12, 9%/12 = 0.75% each)")
print(f"    d100 61-85: Uncommon B (12 quirk, d12, 7.5%/12 = 0.625% each)")
print(f"    Combined: {16.5/24:.2f}% per quirk")

pct_table("Medium breakdown", 30, [
    ("Common", 7, (1, 30)),
    ("Uncommon A", 12, (31, 60)),
    ("Uncommon B", 12, (61, 85)),
    ("Rare", 3, (86, 100)),
])

# ===== HEAVY: 20% =====
# 11 common, 3 uncommon, 7 rare
# Common gets 50% of Heavy = 10% total, 10/11 = 0.91% each
# Uncommon gets 20% of Heavy = 4% total, 4/3 = 1.33% each
# Rare gets 30% of Heavy = 6% total, 6/7 = 0.86% each

heavy_pct = 20.0
heavy_common_pct = 10.0
heavy_uncommon_pct = 4.0
heavy_rare_pct = 6.0

print(f"\n{'='*60}")
print(f"  HEAVY — 20% of all quirks")
print(f"{'='*60}")
print(f"  d100 01-50 (50% of Heavy =   10% total): Common (d11)")
print(f"  d100 51-70 (20% of Heavy =    4% total): Uncommon (d3)")
print(f"  d100 71-00 (30% of Heavy =    6% total): Rare (d7)")
print(f"  ───────────────────────────────────────")
print(f"  Common per quirk:   {heavy_common_pct/11:.2f}%")
print(f"  Uncommon per quirk: {heavy_uncommon_pct/3:.2f}%")
print(f"  Rare per quirk:     {heavy_rare_pct/7:.2f}%")

pct_table("Heavy breakdown", 20, [
    ("Common", 11, (1, 50)),
    ("Uncommon", 3, (51, 70)),
    ("Rare", 7, (71, 100)),
])

# ===== SUMMARY =====
print(f"\n{'='*60}")
print(f"  ALL PER-QUIRK PROBABILITIES")
print(f"{'='*60}")
print(f"\n  {'Tier':>8}  {'Freq':>10}  {'Count':>5}  {'Each %':>7}")
print(f"  {'----':>8}  {'----':>10}  {'-----':>5}  {'------':>7}")

all_data = [
    ("Light", "Common", 12, 35.0, 50.0),
    ("Light", "Uncommon", 2, 7.5, 50.0),
    ("Light", "Rare", 4, 7.5, 50.0),
    ("Medium", "Common", 7, 9.0, 30.0),
    ("Medium", "Unc A", 12, 9.0, 30.0),
    ("Medium", "Unc B", 12, 7.5, 30.0),
    ("Medium", "Rare", 3, 4.5, 30.0),
    ("Heavy", "Common", 11, 10.0, 20.0),
    ("Heavy", "Uncommon", 3, 4.0, 20.0),
    ("Heavy", "Rare", 7, 6.0, 20.0),
]

min_pct = 999.0
max_pct = 0.0
for tier, freq, count, band_pct, tier_pct in all_data:
    each = band_pct / count
    min_pct = min(min_pct, each)
    max_pct = max(max_pct, each)
    print(f"  {tier:>8}  {freq:>10}  {count:>5}  {each:>6.2f}%")

print(f"\n  Range: {min_pct:.2f}% – {max_pct:.2f}%")
print(f"  Floor: {'OK' if min_pct >= 0.5 else 'BELOW 0.5%!'}")

# ===== ALTERNATIVE: SINGLE d% ROLL =====
print(f"\n{'='*60}")
print(f"  ALTERNATIVE: SINGLE d100 (combined table)")
print(f"{'='*60}")
print(f"""
  Instead of a two-roll cascade (tier then quirk),
  you could flatten everything into one big d100:

  01-35: Light Common     (12 quirk, 35% total, 2.92% each)
  36-42: Light Uncommon   (2 quirk,  7% total, 3.5% each)
  43-49: Light Rare       (4 quirk,  7% total, 1.75% each)
  50-58: Medium Common    (7 quirk,  9% total, 1.29% each)
  59-70: Medium Uncommon  (24 quirk need sub-roll)
  71-74: Medium Rare      (3 quirk,  4% total, 1.33% each)
  75-84: Heavy Common     (11 quirk, 10% total, 0.91% each)
  85-87: Heavy Uncommon   (3 quirk,  3% total, 1.0% each)
  88-00: Heavy Rare       (7 quirk,  13% total, 1.86% each)
  
  But this still needs sub-rolls for the big bands (Light Common,
  Medium Uncommon). So the two-roll cascade is cleaner.
""")

# ===== THREE-ROLL CASCADE (d10 only) =====
print(f"\n{'='*60}")
print(f"  ALTERNATIVE: THREE-ROLL CASCADE (d10 only)")
print(f"{'='*60}")
print(f"""
  Roll 1: Severity
    d10 1-5: Light
    d10 6-8: Medium
    d10 9-10: Heavy

  Roll 2: Rarity Band (within tier)
    Light:    d10 1-7 Common, 8 Uncommon, 9-10 Rare
    Medium:   d10 1-3 Common, 4-8 Uncommon, 9-10 Rare
    Heavy:    d10 1-5 Common, 6-7 Uncommon, 8-10 Rare

  Roll 3: Specific Quirk
    Light Common:     d12 (1-12, reroll blanks)
    Light Uncommon:   d2 (1-2)
    Light Rare:       d4 (1-4)
    Medium Common:    d7 (1-7)
    Medium Uncommon:  two sub-tables of d12 each
    Medium Rare:      d3 (1-3)
    Heavy Common:     d11 (1-11)
    Heavy Uncommon:   d3 (1-3)
    Heavy Rare:       d7 (1-7)

  Per-quirk probabilities:
    Light Common:   50% * 70% / 12 = 2.92%
    Light Uncommon: 50% * 10% / 2  = 2.50%
    Light Rare:     50% * 20% / 4  = 2.50%
    Medium Common:  30% * 30% / 7  = 1.29%
    Medium Uncommon: 30% * 50% / 24 = 0.63%
    Medium Rare:    30% * 20% / 3  = 2.00%
    Heavy Common:   20% * 50% / 11 = 0.91%
    Heavy Uncommon: 20% * 20% / 3  = 1.33%
    Heavy Rare:     20% * 30% / 7  = 0.86%
""")
