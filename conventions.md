---
cssclass: clean-embeds
outgoing links: []
tags: []
title: conventions
---


title: Konventionen  
tags: []
[TOC]
# XP
## Kontext
[Siehe hier](/archive/level up)
## Kurz
T - Training/Herumprobieren (optional: (wochen/gefordert))
L - Lehrer
K - Kritische Anwendung
P - Praxis (optional: (wochen/gefordert))
X - mit Allgemein-XP gekauft
V - Versagen
I - Inspiration
[Region] - Perspektive
S - Entsprechende Tat(Gesellenstück bis Legendäre Tat)

# Wiki
## Infolets
[[info]] fügt direkt ein
![[info#example|n-h1]] fügt ausklappbar ein
[name[[info]]] fügt ausklappbar mit extra überschrift ein
info hat folgende optionen

* weapon:waffenname:waffenmods
* armor:rüstungsname:rüstungsmods
* specific:seite:specificselektor
* q:seite:specificselektor

### Waffenmods
[LR]<Anzahl>[HSCB]+
LR: entscheidet ob *nach* links  oder *nach* rechts applied wird (nach links ist von oben nach unten)
anzahl entscheidet wie weit gezählt wird, 10 sind alle
HSCB entscheidet welcher schadenscode modifiziert wird
waffenmods sind komma-trennbar

### Specificselektor
selektiert auf einer seite eine überschrift a:b sucht nach der überschrift b in a
es wird die erste passende überschrift ausgewählt und gelesen bis die nächste überschrift auf der selben oder höheren ebene gefunden wird. a:b:c wählt c innerhalb von b aus (falls c vorher schon auftritt)
ein :- am ende wählt die Überschrift nicht mit aus
ein - als seite sorgt dafür, dass zuerst auf der aktuellen seite gesucht wird und dann prices und items durchsucht werden.

### Rüstungsmods
sind komma-getrennt und fangen mit *einem* großbuchstaben an der den effekt festlegt. Mods die nicht mit einem dieser großbuchstaben anfangen werden in [shorthand](shorthand) nachgeschaut. wenn sie da nicht sind, wird der mod ignoriert.
Zahlenwerte werden durch das ergebnis der angegebenen Formel ersetzt. Die erste unbekannte variable wird mit dem aktuellen wert ersetzt. Es wird auf der kleinsten verfügbaren Einheit berechnet (Gramm bzw Kupfer)
Beispiel: a * 3
x+1
(x/1000)**2 (quadriert auf kilo-basis)

|Kürzel|Effekt|
|---|---|
|N|Name. An die Stelle von "<>" wird der ursprüngliche name gesetzt|
|P|Schutzwert(Protection)|
|S|Stabilität|
|W|Ge*W*icht|
|K|Kosten|
|R|Reparaturkosten|

# Charasheet
## Charakterwerte 
sind unter der Überschrift `#Werte` in Kategorien `##Stärke` usw, jeweils in Attribute, Fähigkeiten und Vorteile als Tabellen einzufügen. Die Kopfzeile und Formatierungsangabe werden Ignoriert.

Angehängte Fähigkeiten sind mit _ geprefixt (und zählen nur halb), Vorteile, die nicht mitgezählt werden ebenso
Waffe(Dolch) ist Schlichtweg als Dolch zu schreiben, bzw am besten sind speziell für Waffen, die namen die auch in [mit werten versehen und integriert sind](weapons)

## Charakterdaten 
zB Name, Alter usw sind in einer Tabelle under `#Charakter` abzulegen
Text direkt unter überschriften unter #Charakter wird ebenfalls Interpretiert

## XP
Um XP irgendwo anzurechnen muss der entsprechende Eintrag in der Kategorie unter der entsprechenden Subkategorie (Fähigkeit,Zauber,Quellen,Aspekte,Vorteile) stehen.
Wenn eine Fähigkeit (auch wenn sie 0 ist) beim Zusammenrechnen der Punkte einer Kategorie gefunden wird, wird nach XP gesucht.

Dazu wird unter der Überschrift XP(oder Erfahrung) nach einer Tabelle gesucht die XP Zeilen enthält.

### Beispiel für Xp zeile
|Beispielfähigkeit | TTT P(8/24)I[Seegard, Tantor] (Limasu)|
Dies, ohne eine Aussage über das aktuelle Level zu machen, sagt aus, dass 3 Trainingseinheiten absolviert wurden, eine Praxis nochnicht absolviert wurden, Inspiration gehabt wurde (was Level 0->1 impliziert) und Seegard und Tantor besucht worden sind um dort die lokale Kultur von Beispielfähigkeit aufzusaugen. Leerzeichen(Limasu) entfernt das Leerzeichen mit (wichtig) und ist lediglich eine Notiz. [Seegard,Tantor](Limasu) würde ] entfernen und auf einmal werden aus TTT+I+Tantor+Seegard = 6 TTT+I+[+T+a+n+t+o+r usw, was wesentlich mehr als 6 sind.
Dinge in (Klammern) werden nicht gezählt, aber Klammern invalidieren das Zeichen direkt davor P(22/12) zählt immernoch als 0, [] ist 0, mit etwas zwischen den Klammern ist es 1 + Anzahl der kommata.

### Warnung
Das hat den Nebeneffekt, dass wenn eine Fähigkeit mehrfach vertreten ist bzw in mehreren Kategorien bzw gleich heisst, alle JEWEILS die XP angerechnet bekommen.

## Inventar

unter der Überschrift Inventar kann eine Tabelle angelegt werden die folgende Kopfzeilen enthalten sollte:
Name, Gewicht, Preis
Anzahl ist optional (ohne wird immer 1 angenommen)
Die Reihenfolge ist beliebig und es können beliebige andere Spalten angegeben werden.
Jeder Eintrag bei dem Gewicht und Preis leer gelassen worden sind wird aus [prices](prices) bzw [items](items) befüllt.
Außerdem wird für jeden Eintrag versucht details zu finden die eingesetzt werden sollen. Zuerst auf der aktuellen seite, dann prices und dann items.

