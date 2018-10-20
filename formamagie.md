title: Forma  
tags: Forma, Magie  
###Zauber
Zauber bestehen aus bis zu [n] aneinandergereite Forma,  
jede forma hat eine Castzeit von einer Runde und gibt dem Caster 1 Strain  
ein zauber muss am anfang einer runde in der keine Forma gewirkt wurde ausgelöst werden
Wurf(kleinste Formastufe,zweit kleinste Formastufe)@(2+n)
###Vorteile
|Vorteil|Wirkung|  
|:---|:----|  
|Schnell Zaubern|Zauber am Ende der Runde auszulösen stat am Anfang der nächsten, erzeugt 1 Strain |
|In Bewegung Zaubern|beim Zaubernbewegen mit langsames gehen/gehen/schnelles gehen/dauerlauf/normales rennen|  
|Zauber biegen [k]|Komplexität eines Zaubers um k erhöen um den Effekt um k stufen zu verändern |
|Konzentration [k]|k Zauber gleichzeitig aufrecht zu erhalten ???|
|Schlafzauber|Zauber beim schlaf aufrecht erhalten, keine Strain Reduktion in der Nacht|  
|Kampfzaubern|Bonus auf Auweichen beim Zaubern in der Kampfphase (Talent?)|
|Zauber halten[k]|zauber auslösen um k runden verzögern| 
|Fokussieren|Zauber in n(n+1)/2 Runde wirken für insgesamt 1 Strain|
Zauber fallen lassen: pro Runde Kann ein Aktiver Zauber kostenlos in der freien Phase deaktiviert werden. Pro weiter Zauber der in der gleichen Runde deaktiviert wird +1 Würfel auf die Tabelle.  
Zauber:  
Reichweite: Niedrigste im Zauber verwendete  
Dauer: Niedrigste im Zauber verwendete  
Tickrate: Niedrigste im Zauber verwendete  
Reinheitsstufe: Niedrigste im Zauber verwendete  
Wurfmodifikator: Produkt aller Wurfmodifikatoren  
Reinfolge der Forma verändert den Zauber nicht  
Effekt_Forma:  
Kerneffekte des Zaubers  
Synergie_Forma:  
Verändern den Kerneffekt eines Zaubers  
Modifikator_Forma:  
Modifizieren den Zauber ohne den Kerneffekt zu verändern.   
Benötigt mindestens eine nicht Modifikator_Forma im Zauber  
  
##Forma
###Impello:
|Typ|Art|  
|:---|:----|  
|Wirkung| gibt einem Objekt einen Richtungsvektor mit [Wurf]*3Kg Zug|  
|Typ| Effekt_Forma|  
|Reichweite| Berührung|  
|Dauer|Konzentration|  
|Tickrate| 1 pro Runde|  
|Wurfmodifikator| 1|  
|Reinheitsmodifikator| +1Kg Zug|  
|Beispiel_Biegungen| Flugbahn statt Vektor|  
  
###Disruptio
|Typ|Art|  
|:---|:----|  
|Wirkung|  lässt ein Objekt explodieren|  
|Typ| Effekt_Forma|  
|Reichweite| Berührung|  
|Dauer| Keine|  
|Tickrate| Keine|  
|Wurfmodifikator| 1|  
|Reinheitsmodifikator| ???|  
|Beispiel_Biegungen| Fokus, Explosion geht vom Objekt aus statt es explodieren zu lassen|  
  
###sisto
|Typ|Art|  
|:---|:----|  
|Wirkung|  Stoppt dinge, Reduktion um [Wurf]|  
|Typ| Effekt_Forma|  
|Reichweite| Berührung|  
|Dauer|Konzentration|  
|Tickrate| 1 pro Runde|  
|Wurfmodifikator| 1 (Steht zur Debatte)|  
|Reinheitsmodifikator| ???|  
|Beispiel_Biegungen||  
   
###Fulgur
|Typ|Art|  
|:---|:----|  
|Wirkung|  erzeugt eine Instanz elektrischer Ladung, Ignoriere einen(/alle anderen) Wurfmodifikator|  
|Typ| Effekt_Forma|  
|Reichweite| Berührung|  
|Dauer|Konzentration /bis Instanz verbraucht|  
|Tickrate| 1 pro Runde (bis Instanz verbraucht)|  
|Wurfmodifikator| 1|  
|Reinheitsmodifikator|  mehr Instanz|  
|Beispiel_Biegungen||   
  
###Ignes
|Typ|Art|  
|:---|:----|  
|Wirkung|  erzeugt eine Flamme, AoE schaden in Zaubern|  
|Typ| Effekt-Forma|  
|Reichweite| Berührung|  
|Dauer|Konzentration|  
|Tickrate| 1 pro Runde|  
|Wurfmodifikator| 1/3|  
|Reinheitsmodifikator|  +1 Feuerstack pro Runde  
|Beispiel_Biegungen| Flammen Farbe,|  
  
    
###Meta
|Typ|Art|  
|:---|:----|  
|Wirkung|  ersetzt die Reichweite eines Zaubers durch die Reichweite von Meta, erlaubt Zauber an einen Ort zu zaubern|  
|Typ| Modifikator_Forma|  
|Reichweite| ununterbrochene Verbindung|  
|Wurfmodifikator| 1|  
|Reinheitsmodifikator| ???|  
|Beispiel_Biegungen||  
  
###Persona
|Typ|Art|  
|:---|:----|  
|Wirkung|  Erlaubt es einen Zauber auf eine Person/Kreatur zu beziehen|  
|Typ| Modifikator_Forma|  
|Reichweite| Berührung|  
|Wurfmodifikator| 1|  
|Reinheitsmodifikator|  +1Meter Reichweite|  
|Beispiel_Biegungen| Zauber gegen das Ziel (/exclusive gegen das Ziel)|  
  
###Tutela
|Typ|Art|  
|:---|:----|  
|Wirkung|  Zaubereffekt wirkt in einem 5m Radius um den Zauberer  |
|Typ|Modifikator_Forma|  
|Reichweite| Zauberer|  
|Wurfmodifikator| ½|  
|Reinheitsmodifikator| + Radius|  
|Beispiel_Biegungen||   

###Lux
|Typ|Art|  
|:---|:----|  
|Wirkung|  erzeugt eine Lichtkugel in der Handfläche des Zauberes|  
|Typ| Synergie_Forma|  
|Reichweite| Körper|  
|Dauer|Konzentration|  
|Tickrate|???|  
|Wurfmodifikator| 0 (bezüglich Schadens Ermittlung)|  
|Reinheitsmodifikator|  + Lichtfaktor|  
|Beispiel_Biegungen| Farbe, Fokus, alternative Position,|   
  
###Terra
|Typ|Art|  
|:---|:----|  
|Wirkung|  erzeugt Sand solange der Zauber besteht, kann nachträglich noch von Zaubern beeinflusst  werden|  
|Typ| Synergie_Forma|  
|Reichweite| Körper|  
|Dauer|Konzentration|  
|Tickrate| 1 pro Runde|  
|Wurfmodifikator| 1|  
|Reinheitsmodifikator| +erzeugte Masse pro Erfolg|  
|Beispiel_Biegungen| statt Sand, andere Erdprodukte (Steht zur Debatte)|  
  
###Zauber Stufe 2
|Forma|Wirkung|  
|:---|:----|     
|Lux-Impello|eine Lichtkugel die einer festgelegten Bewegungsanweisung folgt wenn diese  			ausgeführt ist erlischt das licht/der Zauber|  
|Lux-sisto| Stoppt Licht|  
|Lux-Fulgur |erschafft einen Licht bogen|  
|Lux-Meta|erschafft eine Lichtquelle an einem Ort|  
|Lux-tutela|Leuchtende Kugel um den Ort des Zaubers|  
|Lux-Terra|???|  
|Lux-Ignes|Blendent Helles Licht (Magnesium Fackel)|  
|Lux-Persona|ersetzt Zaubernden durch Persona-Ziel|  
|Lux-Disruptio|	Blendgranate|  
|||  
|Impello-sisto|Stoppt „nur“ Bewegung|  
|Impello-Fulgur|Wirft einen Blitz|  
|Impello-Meta|Bewegt ein entferntes Objekt|  
|Impello-tutela|Alles im Bereich bekommt einen Vektor (Default: der Vektor zeigt von der Mitte weg)|  
|Imepllo-Ignes|Flammenstrahl|  
|Impello-Terra|Sandstrahler|  
|Impello-Persona|Gibt einer Person den Vektor|  
|Impello-Diruptio|Druckwelle|  
|||  
|sisto-Fulgur|Stoppt „nur“ Blitze|   
|sisto-Meta|Stoppt alle Bewegung von einem Ziel.|  
|sisto-Tutela|Stoppt alles im Bereich|  
|sisto-Ignes|Stoppt „nur“ Feuer|  
|sisto-Terra|Stoppt „nur“ Erde|  
|sisto-Persona|Stoppt „nur“ die Person|  
|sisto-Diruptio|Stoppt „nur“ Explosives|  
|||  
|Fulgur-Meta|erschafft Ladung an einem Ort|  
|Fulgur-Tutela|Ladung entlädt sich im Bereich|  
|Fulgur-Ignes|???|  
|Fulgur-Terra|erzeugt Glas|  
|Fulgur-Persona|Ladung entsteht an der Person|  
|Fulgur-Diruptio|entlädt die Ladung um den Zauberer herum|  
|||  
|Ignes-Terrra|Funken|  
|Ignes-Tutela|...|  
|Ignes-Persona|Flamme entsteht an der Person|  
|Ignes-Meta|...|  
|Ignes-disruptio| Flammenexplosion|  
  
|Terra-Tutela|Sand entsteht überall im Bereich|  
|Terra-Persona|…|  
|Terra-Meta|...|  
|Terra-disruptio|Sandexplosion|  