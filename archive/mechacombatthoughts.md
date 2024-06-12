---
title: mechacombatthoughts  
tags: []
outgoing links: ''  
---
  attacks have attackvalue (assume -1..12 rn)



mecha has armor rating -2..2 (considering switching to 1-5 system to avoid negative numbers)

shields have rating -2..2 (or numeric value? maybe too much math again)



incoming attack goes to shield, if shield looses the roll, it is overpowered (with effects depending on shield) and spills the remaining attack value through to the armor. No shield gets directly passed through to the armor. If the Armor fails as well, damage is inflicted.

(quickfire +x bonus vs shields -x penalty vs armor, kineticstrike -x penalty vs shield +x bonus vs armor and so on, prolly just advantages, maybe flat boni? might reintroduce math into combat though, then again ... battleshipcannon vs sturdy platemail vs the mostpenetrating rifle ever vs battleship)







examples:



defender midtech mech: 6 hp, shield 1 (2d10) coming online 3 turns after it goes offline, armor 1 (2d10)

attacker longrange antimech installation: rifle 1 (2d10)

(in this example percentages add up until they reach 100 and then just trigger, not that realistic but pretty average)

shooting shield: 43% chance to penetrate shields or armor

shot 1 : 43

shot 2 : 86

shot 3 : 129 ==> hit, shield goes down

shot 4 : 172

shot 5 : 215 ==> hit, 5/6 hp

shot 6 : 258 shield goes up

shot 7 : 301 ==> hit, shield goes down

shot 8 : 344

shot 9 : 387

shot 10: 430 ==> hit, 4/6 hp, shield goes up

shot 11: 473 

shot 12: 516 ==> hit, shield goes down

shot 13: 559

shot 14: 602 ==> hit, 3/5 hp

shot 15: 645 shield goes up

shot 16: 688

shot 17: 731 ==> hit, shield goes down

shot 18: 774 

shot 19: 817 ==> hit, 2/6 hp

shot 20: 860 shield goes up

shot 21: 903 ==> hit, shield goes down

shot 22: 946

shot 23: 989

shot 24: 1032 ==> hit, 1/6 hp, shield goes up

shot 25: 1075

shot 26: 1118 ==> hit, shield goes down

shot 27: 1161

shot 28: 1204 ==> hit, destroyed



same mech, rifle 2 (3d10)



54% chance



shot 1 : 54

shot 2 : 108 ==> hit, shield down

shot 3 : 162

shot 4 : 216 ==> hit, 5/6

shot 5 : 270 shield up

shot 6 : 324 ==> hit, shield down

shot 7 : 378 

shot 8 : 432 ==> hit 4/6

shot 9 : 486 shield up

shot 10: 540 ==> hit, shield down

shot 11: 594 

shot 12: 648 ==> hit, 3/6

shot 13: 702 ==> hit, 2/6, shield up

shot 14: 756

shot 15: 810 ==> hit, shield down

shot 16: 864

shot 17: 918 ==> hit, 1/6

shot 18: 972 shield up

shot 19: 1026==> hit, shield down

shot 20: 1080

shot 21: 1134==> hit, destroyed



conclusion: 6 HP is a lot, hit chances are ok, speed might need to be its own roll, lightmechs should have 1-2 hp, heavy tanks maybe 8. 10-20 HP is not doable alone with normal weapons (even if it is it just takes hours, every shot is two people rolling dice, a normal WoD fight has maybe 20-30 instances of dicerolling but there the circumstances change)



extra damage weapons, specialist ammunition and drawing back when damaged should be the focus, it is good that mechs take a long time to destroy, but the question is if it should feel like a grind.



3-4 HP should be normal

shieldtypes to counter/encourage damage types like faster regen ones (1-2 turns) to encourage bursting and adaptive shields (gaining +1 to their roll for every attack made against them in a round) to encourage spread out damage. modulation to physical/energy attacks and so on. of course there is heat and energy costs and shields shutting off after a time, special actions to reload/activate/have active at all (from stopping and hunkering over moving at a certain speed to hitting an attack) should make shields interesting



forgoing shield for another system should be feasible, more guns = more damage, more movement system(s) = more speed/options



fixed tonnage?

size = triangle



Movement, Energy, Heat, Weapons, Shield, Armor, Cargo



M             1

M E           2

M E H         3

M E H S       4

M E H S A     5

M E H S A W   6

M E H S A W C 7

             28 = (n*n(+1))/2



M

E H

S A W



hmmm promising ...

threshholds: per movement system for movement speeds

speed, dice,       needed%, speed%

rapid (+2/3d10h):    45%    200%

fast  (+1/2d10h):    35%    150%

[normal] (0/1d10g):  25%    100%

slow  (-1/2d10l):    15%    33%

lumbering (-2/3d10l): 5%    10%





example modules (costs are per active module)

[Cargo holds 10]



AlacastFoundry BWS022-3

BipedalWalkingSystem: Speed Bonus is dodge bonus in combat, ignore tracking

transportation mode: walking, stepping

Costs: 0.2 Energy Idle, 0.1 Heat (.2/.1) Idle, 1 Energy, 0.5 (1/.5) Heat in Use (.2/.1//1/.5)

Speed: Idle: 3km/h, Active 30km/h



Hella WABWS7 Mk II

BipedalWalkingSystem: Speed Bonus is dodge bonus in combat, ignore tracking

WheelAssisted: when smooth driving is possible, raise speed by 70km/h, tracking applies

transportation mode: walking, stepping, smooth driving

costs: 0.5 Energy Idle, 0 Heat  Idle, 1.2 Energy, 0.5 Heat In Use (.5/0//1.2/0.5)

Speed: Idle: 10km/h Active 35km/h



Exo-plore BWS Conquistador

BipedalWalkingSystem: Speed Bonus is dodge bonus in combat, ignore tracking

Opposable Thumb: Able to pick up and carry things

transportation mode: walking, stepping, rough terrain (0.1/0.1), climbing(0.2/0.5)

Self Contained: Only counts half for Threshhold calculations

Stores: 100 Energy, 10 Heat

Dissipates: 0.01

Costs: (0/0//0.01/0.1)

Speed: Idle: 2km/h, Active 15 km/h







Starburst Reactor

Reactor: Consumes Fuelrod (0.1/day Idle // 0.1/minute Active)

Output: 0.8 Energy/ 0.3 Heat Idle // 1.5 Energy/ 0.5 Heat Active

Storage: 100 Energy (withdrawing costs 0.2Heat per Energy) 1 Fuelstorage



Hella PEM

Reactor: Consumes HFC (0.5/day Idle // 0.2/minute Active)

Output: 0.5 Energy / 0.5 Heat // 2.5Energy / 1.5 Heat

Storage: 2 Fuelstorage



KrunkIndustries "ChunkOfCrystalKnot"(tm)

Storage: 500 Energy (withdrawing costs 0.1 Heat * retrieved Energy^2 (0.1, 0.4, 1.6, 2.5, 3.6 ...)





EdenInitiative Green Alternative v0.9

Generator: Works only in daylight (12-contamination level hours per day) and while deployed

Deployment: Costs 1 Energy to deploy, or 5 minutes manual work outside the mech

Output: 0.03 Energy, 0 Heat (Hourly 108 Energy)

Storage: 50 Energy (withdrawing costs 0.5 Heat* retrieved Energy + 0.1 Heat * retrieved Energy)





Hella HeatVent

Vent: Idle 1 Heat, Active 6 Heat, Increases Heat Signature by Vented amount * 2

Ventilation and Pumps: Costs 0.5 Energy while Active



ATH3NA HeatSink

Storage: 25 Heat, Increases Heat Signature by stored amount

Unisolated Dissipation: 0.2 Heat under 15 Heat stored, 0.5 on 15-24, 1 when full

Glowing Infra: Increases Heat Signature by Dissipated Amount^2



Starburst CoolantSystem

Storage: 15 Heat, Increases Heat Signature by stored amount

Unisolated Dissipation: 0.5 Heat, 1 when full.

Glowing Infra: Increases Heat Signature by Dissipated Amount^2

CoolantDump: Increases Ambient Heat Signature by Vented Amount * 2 (decaying by 1 each turn) an Storage becomes 0

Refill: 5 Energy, Consumes 1 Coolant and sets Storage to amount depending on Coolant (10 for water)



EvilGenius IsolatedHeatSink

Storage: 50 Heat, Does not Increase Heat Signature

No Dissipation: Costs 0.5 Energy per Heat retreived





Modules can be Dedicated to a specific Task, Shields with Less Coverage than their Mech, have their roll reduced by 1 per 10% (rounded up) uncovered mech, on a draw, the enemy attack hits exposed modules, without the shield collapsing



ATH3NA Aegis

Shield 1: Provides a Shield Level 1 (2d10h) ((again, maybe 4 is better so level 1 doesnt sound like crap also level -1...?)

Overwhelm: Turns off, releases 7 heat and enters Charging Mode when overwhelmed

Cost: 0.2 While shield is Active, 1 While Charging, 3 Heat per Absorbed Attack

Coverage: Covers 10+Coverage*6 Modules

Reboot: Takes 12/Reboot (rounded up) to restart.

ColdBoot: After Being Offline for At least 5 minutes, Costs 3 Energy per Module to Start





EvilGenius Magnetosphere

Shield 2: Provides a Shield level 2 (3d10h)

Overwhelm: Turns off, releases 5 Heat and enters Charging Mode when overwhelmed

Costs: 5 while active, 0 While Charging, 8 Heat per Absorbed Attack

Coverage: Covers 15+Coverage*5 Modules

Reboot: Takes 5-Reboot and Modules^2 Energy to restart (0 length means immediately)

ColdBoot: After Being Offline for at least 1 hour, Costs 10 Energy to start

Retribution: When being Attacked by Material attacks, throw their attack back at them (at -2)



XXL HIGH QUALITY BUY NOW Shield Generator

Shield -2: Provides a Shield Level -2 (3d10l)

Overwhelm: Turns off, releases 10 Heat and enters Charging Mode when overwhelmed

Costs: 2 while active, 0.1 while Charging, 5 Heat per Absorbed Attack

Coverage: Coverage*10 Modules

Reboot: Takes 5-sqrt(Reboot) and 5 Energy to Restart.

ColdBoot: See Reboot



KrunkIndustries Outrider Dynamic Deflector

Shield -1: Provides a Shield Level -1 (2d10l)

Overwhelm: Turns off and releases 20 Energy when overwhelmed

Costs: 0.1 while Active, 1 while charging, 1 Heat per Absorbed Attack

Coverage: 10+Coverage*2 Modules

Reboot: Takes passing at least 5 tons of Metal in less than 5 meters distance at 100-(Reboot*5) km/h or more and 30(-1 per 5km/h over the required speed, minimum 0) Energy to Reboot

ColdBoot: Takes 30 Energy and standing still for 10 seconds (while charging) to Boot.



Fortress Invincibilityfield

Shield 2: Provides a Shield Level 2 (3d10h)

Overwhelm: If shield level is above -2, shield goes down one level. If shield level is -2, Turns Off and releases 100 Heat

Costs: 1 while Active, 1 while charging, 5 Heat per Absorbed Attack

Coverage: Coverage*15 Modules

Reboot: None

ColdBoot: After not Being Used for 10 Minutes, Takes  100/Reboot (rounded up) to Boot

TurnOff: If Energy is not supplied, shield is overwhelmed and disabled for 5, then turns back on.







Bighaul Cargo Liner

Armor -2: Provides Armor Level -2 (3d10l)

Health: (2*sqrt(Modules)) rounded mathematically

Coverage: 14*Modules

Cargo: 7 Spaces per module

Damage: Damage Destroys One Module, Cargo is destroyed/dropped



SpeedboatsUnited Thunderclap Chassis

Armor -1: Provides Armor Level -1 (2d10l)

Health: 2

Coverage: 10+5*Modules

Output: 1 Energy per 50 km/h

Vent: 1 Heat per 50 km/h, increases Heat Signature by Vented Heat

Damage: 50%(rounded down on the first time, rounded up on the second) of Modules are damaged. Fixing (2 Hours, 0.5 Lowtech Scraps, destroy (including materials) on 5 or less, fix on 9 or more)



Kodal Militia Standard Issue Mech Armor

Armor 0: Provides Armor Level 0 (1d10)

Health: 4

Coverage: 15+8*Modules

Damage: Damage Bricks 1 Module. Armor first, then Movement, then Heat



AlacastFoundry MAS5 

Armor 1: Provides Armor Level 1 (2d10h)

Health: (7-sqrt(Modules)) rounded down

Coverage: 12+7*Modules

Costs: 0.2+0.1*Modules Energy (total costs 0.2*Modules+0.1*Modules^2), Every 10% less energy than requirement is 1 less Armor Level

Damage: Damage Shorts out Modules (rounded percentage of lost health), which need Extensive Maintenance (1 hour per Module, destroy on 2 or less, fix on 8 or more) to be reactivated.



ATH3NA Linothorax

Armor 2: Provides Armor Level 2 (3d10h)

Health: sqrt(Modules) rounded down

Coverage: 8*Modules

Damage: Every Lost Healthpoint destroys [new health*2+1] Modules. Modules can be Cobbled together (3 to 1, 30 minutes per produced Module, destroy all input on 8 or less, create new Module on 9 or more)





Weapons



Outclassing: Every Time the sizeclass of the attacked is equal or more than 2 times the intended size of the weapon, subtract 1 from the weapon Level (4x for 2, 8x for 3 and so on). If the Level is -3 the Attack is not rolled and failure to damage is assumed. Every Time the sizeclass of the attacked is equal or less than half of the intended size of the weapon, add 1 to the weapon level. Weapon Levels beyond 2 deal double damage. size 0 is considered half of size 0.5)

The difference in sizeclasses (defender*2^x=attacker) is added to the result of the defenders roll as a flat bonus.

Tracking contains the speed threshholds in km/h at which the attack roll gets disadvantages. Tracking assumes 100 m distance. For other distances calculate effective speed first.

Range contains the Ranges with their respective modifiers



KrunkIndustries Rattatattata:

ProjectileWeapon: Does Projectile damage 

Damage 1: Damage Level 1 (2d10h)

Quickfire: +1 Level vs Shields, -1 vs Armor

Sizeclass: 1

Size: 1 Module

Reload: 1

Tracking: 50/100/200/500/1K

Range: +1 for up to 300 meters, then -1 per 1000 meter distance

Cost: 0.001 Ammunition 0.1 Heat per shot



EvilGenius Deathray: 

EnergyWapon: Does Energy damage

Damage -2+X: Damage Level starts at -2 (3d10l) but is increased by X

Beam: After Firing increase X by 1. If not fired, decrease X by 1

Sizeclass: 2

Size: X caps at number of Capacity Dedicated Modules.

Reload: 1

Tracking: Every 30+5*Tracking Dedicated Module

Range: -1 to the result of the damage roll every 0.5+(0.5*Range Dedicated Module)km

Cost: 1+X Energy, X Heat



Kodal Militia Standart Issue Armament - Adaptive Edition

ProjectileWeapon: Does Projectile damage

Damage Level 0: Deals Damage Level 0 (1d10)

Sizeclass: 3 +1 for every Barrel Dedicated Module

Size: Dedicated Modules

Tracking: Every 5+8* Tracking Dedicated Module

Reload: 2/Reload Dedicated Module rounded up

Cost: 0.01 Ammunition, 0.2*Barrel Dedicated Modules, 0.6*Tracking Dedicated Module

Range: -1 every 0.5+0.5*Range Dedicated Module km)

Adaptive: Modules can be rededicated (10 minutes+100Energy, 0 and below destroys module, 8 and above rededicates)





Hella Shortrange Artillery

ProjectileWeapon: Does Projectile damage

Damage Level 1: Deals Damage Level 1 (2d10h)

Indirect Fire: does not need Line of Sight, targetting roll is done by spotting.

Area of Effect: Damage roll result is reduced by 1 for every 2 meters the Target has moved

Bombshell: On a direct Hit, before the main Attack roll an extra attack at one level below damage level

Shrapnell: Smaller Defendants don't get their size difference as evasion bonus

TravelTime: Hits the Target with a delay of 3

Sizeclass: 15 (2dmg at 3 dice to sizeclasses 3 and below, lvl 1 dmg up to size 30, 240 and above take no damage)

Reload: 60/ Reload Dedicated Modules

Size: 8+Dedicated Modules

Tracking: Every 10 km/h (does not apply when targetting ahead)

Cost: 0.2 Ammunition, 10 Energy, 5 Heat

Range: Range Dedicated Modules in km





Bighaul Shotgun

ProjectileWeapon: Does Projectile damage

Damage Level 0: Deals Damage Level 0 (1d10)

Area of Effect: Damage roll result is reduced by 1 for every 30m distance or difference on the to-hit roll

Multiple Projectiles: Damage is +1 against Shields -1 against Armor

Tracking: Every 50 km/h

Sizeclass: 8

Size: 2

Reload: 2

Cost: 0.1 Ammunition, 3 Heat





SpeedboatsUnited RubyViper Sniper

EnergyWeapon: Does Energy damage

Damage Level 1: Deals Damage Level 1 (2d10h)

Focussed Beam: Damage is -1 against Shields, +1 against Armor

Tracking: Every 30+30*Targetting Modules km/h

Aiming: If Target is aimed at for at least 12/Targetting Modules and doesnt change speed, get +1 to hit

Range: every 2km + 2*Range Modules

Sizeclass: 10+Size Modules

Size: 1+Dedicated Modules

Reload: 30/Reload Modules

Cost: 10 Energy, 10 Heat







cards  

Classes: 

Light startupdeck: 10, Optiondecks: 5x min5, globalmin 50  

Medium statupdeck: 15, optiondecks: 4x min10, globalmin 60  

Heavy startupdeck: 20, optiondecks: 3x min15, globalmin 70  



Cards:  

Capacitor: Startup only: provides energy Storage between turns  

Chargecell: provides instant one time Energy (variable)  

Sink: Startup only: provides Heat Storage (Heat negates draw on a 1:1 basis)  

Cool: destroys Heat (variable)  

Computer: Instant Scries  

Scanner: Looks at Opponents Hand   

Shield: Temp hp (different mechanics)  

Weapon: Startup only: can be activated with ammo or energy, does damage  

Ammo: provides ammo for weapons  

Movement System: draws  





