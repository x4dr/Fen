title: Konventionen  
tags:   
[TOC]
#XP
## Kontext
[Siehe hier](level up)
##Kurz
T - Training/Herumprobieren (optional: (wochen/gefordert))
L - Lehrer
K - Kritische Anwendung
P - Praxis (optional: (wochen/gefordert))
X - mit Allgemein-XP gekauft
V - Versagen
I - Inspiration
[Region] - Perspektive
S - Entsprechende Tat(Gesellenstück bis Legendäre Tat)

#Wiki
## Infolets
[[info]] fügt direkt ein
[[[info]]] fügt ausklappbar ein
[name[[info]]] fügt ausklappbar mit extra überschrift ein
info hat folgende optionen
* weapon:waffenname:waffenmods
* armor:rüstungsname:rüstungsmods
* specific:seite:specificselektor

###waffenmods
[LR]<Anzahl>[HSCB]+
LR: entscheidet ob *nach* links  oder *nach* rechts applied wird (nach links ist von oben nach unten)
anzahl entscheidet wie weit gezählt wird, 10 sind alle
HSCB entscheidet welcher schadenscode modifiziert wird
waffenmods sind komma-trennbar
###specificselektor
selektiert auf einer seite eine überschrift a:b sucht nach der überschrift b in a
es wird die erste passende überschrift ausgewählt und gelesen bis die nächste überschrift auf der selben oder höheren ebene gefunden wird. a:b:c wählt c innerhalb von b aus (falls c vorher schon auftritt)
ein :- am ende wählt die Überschrift nicht mit aus

### rüstungsmods
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

#Charasheet
Die Charakterwerte sind unter der Überschrift `#Werte` in Kategorien `##Stärke` usw, jeweils in Attribute, Fähigkeiten und Vorteile als Tabellen einzufügen. Die Kopfzeile und formatierungsangabe werden Ignoriert.

Angehängte Fähigkeiten sind mit _ geprefixt (und zählen nur halb), Vorteile, die nicht mitgezählt werden ebenso
Waffe(Dolch) ist Schlichtweg als Dolch zu schreiben, bzw am besten sind speziell für Waffen, die namen die auch in [mit werten versehen und integriert sind](weapons)

##Beispiel für Xp zeile
|Beispelfähigkeit | TTT P(8/24)I[Seegard, Tantor] (Limasu)|
Dies, ohne eine Aussage über das aktuelle Level zu machen, sagt aus, dass 3 Trainingseinheiten absolviert wurden, eine Praxis nochnicht absolviert wurden, Inspiration gehabt wurde (was Level 0->1 impliziert) und Seegard und Tantor besucht worden sind um dort die lokale Kultur von Beispielfähigkeit aufzusaugen. Leerzeichen(Limasu) entfernt das Leerzeichen mit (wichtig) und ist lediglich eine Notiz. [Seegard,Tantor](Limasu) würde ] entfernen und auf einmal werden aus TTT+I+Tantor+Seegard = 6 TTT+I+[+T+a+n+t+o+r usw, was wesentlich mehr als 6 sind.
Dinge in (Klammern) werden nicht gezählt, aber Klammern invalidieren das Zeichen direkt davor P(22/12) zählt immernoch als 0, [] ist 0, mit irgendwas zwischen den klammern ist es 1 + anzahl der kommata.

Um XP irgendwo anzurechnen muss der entsprechende Eintrag unter Fähigkeiten stehen.
Wenn enie Fähigkeit (auch wenn sie 0 ist) beim zusammenrechnen der Punkte einer Kategorie gefunden wird, wird nach XP gesucht.
###Warnung
Das hat den Nebeneffekt, dass wenn eine Fähigkeit mehrfach vertreten ist bzw in mehreren Kategorien bzw gleich heisst, alle JEWEILS die XP angerechnet bekommen.

