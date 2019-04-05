title: Forma  
tags: Forma, Magie  
###Zauber
Zauber bestehen aus bis zu [n] aneinandergereite Forma,  
Jede Forma hat eine Castzeit von einer Runde und gibt dem Caster 1 Belastung.  
ein zauber muss am anfang einer runde in der keine Forma gewirkt wurde ausgelöst werden  
Wurf(kleinste Formastufe,Konzept)@(2+n)  
Zauber fallen lassen: pro Runde Kann ein Aktiver Zauber kostenlos in der freien Phase deaktiviert werden. Pro weiter Zauber der in der gleichen Runde deaktiviert wird +1 Würfel auf die Tabelle.  
Reihenfolge der Forma verändert den Zauber nicht   
###Vorteile
|Vorteil|Wirkung|  
|:---|:----|  
|Schnell Zaubern|Zauber am Ende der Runde auszulösen stat am Anfang der nächsten, erhöht die Komplexität um 2 |
|In Bewegung Zaubern|beim Zaubernbewegen mit langsames gehen/gehen/schnelles gehen/dauerlauf/normales rennen|  
|Zauber biegen [k]|Komplexität eines Zaubers um k erhöen um den Effekt um k stufen zu verändern |
|Konzentration [k]|k Zauber gleichzeitig aufrecht zu erhalten ???|
|Schlafzauber|Zauber beim schlaf aufrecht erhalten, keine Strain Reduktion in der Nacht|  
|Kampfzaubern|Bonus auf Auweichen beim Zaubern in der Kampfphase (Talent?)|
|Zauber halten[k]|zauber auslösen um k runden verzögern| 
|Fokussieren|Zauber in n(n+1)/2 Runde wirken für insgesamt 1 Strain|  

  
##Zauberparameter:  

|Eigenschaft|Art der Bestimmung|  
|:---|:----|  
|Reichweite| Niedrigste im Zauber verwendete|  
|Dauer| Niedrigste im Zauber verwendete|  
|Tickrate| Niedrigste im Zauber verwendete|  
|Reinheitsstufe| Niedrigste im Zauber verwendete|  
|Wurfmodifikator| Produkt aller Wurfmodifikatoren|  


###Effekt_Forma:  
Kerneffekte des Zaubers  
###Synergie_Forma:  
Verändern den Kerneffekt eines Zaubers  
###Modifikator_Forma:    
Modifizieren den Zauber ohne den Kerneffekt zu verändern.     
Benötigt mindestens eine nicht Modifikator_Forma im Zauber 
   
##Forma
###Impello:
|Typ|Art|  
|:---|:----|  
|Wirkung| gibt einem Objekt einen Richtungsvektor mit [Wurf]*3Kg Zug|  
| | beschränkt auf 20m/runde (15 km/h) |  
|Typ| Effekt_Forma|  
|Reichweite| Berührung|  
|Dauer|Konzentration|  
|Tickrate| 1 pro Runde|  
|Wurfmodifikator| 1, 0.5 auf Personen|  
|Reinheitsmodifikator| +1Kg Zug|  
|Beispiel_Biegungen| Flugbahn statt Vektor, größere Geschwindigkeiten|  

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
|Beispiel_Biegungen| Fokus, Explosion geht vom Objekt aus statt es explodieren zu lassen, Explosionsrichtung |  

###Sisto
|Typ|Art|  
|:---|:----|  
|Wirkung| Stoppt etwas, Reduktion um [Wurf]|  
|Typ| Effekt_Forma|  
|Reichweite| Berührung|  
|Dauer|Konzentration|  
|Tickrate| 1 pro Runde|  
|Wurfmodifikator| 1/2 wenn nicht weiter spezifiziert, sonst 1|  
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
|Reinheitsmodifikator|  +1 Feuerstack pro Runde|  
|Beispiel_Biegungen| Flammen Farbe,|  
  
    
###Meta
|Typ|Art|  
|:---|:----|  
|Wirkung| erlaubt Zauber an einem Ort in Reichweite zu zaubern|  
|Typ| Modifikator_Forma|  
|Reichweite| ununterbrochene Verbindung|  
|Wurfmodifikator| 1, -1/(2+x) meter|  
|Reinheitsmodifikator| +x |  
|Beispiel_Biegungen|+x, Zauber geht direkt vom Zielort aus|  
  
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
|Wurfmodifikator| 1/2 |  
|Reinheitsmodifikator| + Radius|  
|Beispiel_Biegungen||   

###Lux
|Typ|Art|  
|:---|:----|  
|Wirkung|  erzeugt eine Lichtkugel in der Handfläche des Zauberes|  
|Typ| Synergie_Forma|  
|Reichweite| Körper|  
|Dauer|Konzentration|  
|Tickrate|Stunde|  
|Wurfmodifikator| 0 (bezüglich Schadens Ermittlung)|  
|Reinheitsmodifikator|  + Lichtfaktor|  
|Beispiel_Biegungen| Farbe, Fokus, alternative Position,|   
  
###Terra
|Typ|Art|  
|:---|:----|  
|Wirkung|  erzeugt Sand solange der Zauber besteht, kann nachträglich noch von Zaubern beeinflusst werden(?)|  
|Typ| Synergie_Forma|  
|Reichweite| Körper|  
|Dauer|Konzentration|  
|Tickrate| 1 pro Runde|  
|Wurfmodifikator| 1|  
|Reinheitsmodifikator| +erzeugte Masse pro Erfolg|  
|Beispiel_Biegungen| statt Sand größeres Granulat (Schotter, Steine, Fels)|  
  
###Zauber Stufe 2
|Forma|Wirkung|  
|:---|:----|     
|Lux-Impello| eine Lichtkugel die einer festgelegten Bewegungsanweisung folgt wenn diese ausgeführt ist erlischt das licht/der Zauber|  
|Lux-Sisto| hält Licht vom Leuchten ab |  
|Lux-Fulgur |erschafft einen extrem hellen Plasmalicht Bogen|  
|Lux-Meta|erschafft eine Lichtquelle an einem Ort|  
|Lux-tutela|Leuchtende Kugel um den Ort des Zaubers|  
|Lux-Terra|erschafft leuchtenden Sand (bzw größer, siehe Biegungen) der getragen werden kann. Tickrate Lux|  
|Lux-Ignes|erschafft Feuer das heller brennt als normales Feuer und sich ansonsten mundan verhält. Tickrate: 0, Dauer: Konzentration|  
|Lux-Persona|ersetzt Zaubernden durch Persona-Ziel |  
|Lux-Disruptio|	Blendgranate |  
|||  
|Impello-Sisto|Verringert die Energie einer berührten Bewegung |  
|Impello-Fulgur|Wirft einen Blitz (Projektil)|  
|Impello-Meta|Bewegt ein entferntes Objekt|  
|Impello-tutela|Alles im Bereich bekommt einen Vektor (Default: der Vektor zeigt von der Mitte weg)|  
|Imepllo-Ignes|Flammenstrahl|  
|Impello-Terra|Sandstrahl (Behindert Ziel wenn es sich auf den Zauberzubewegt: halbierte Bewegungsreichweite, +2 Komplexität)|  
|Impello-Persona|Gibt einer Person den Vektor gleichmäßig (Modifikator 1)|  
|Impello-Disruptio|Druckwelle (Kugelförmig, inklusive Zauberer) |  
|||  
|Sisto-Fulgur|Ladung die Stoppt|   
|Sisto-Meta|Stoppt alle Bewegung von einem Zielobjekt.|  
|Sisto-Tutela|Stoppt alles im Bereich|  
|Sisto-Ignes|Löscht Feuer|  
|Sisto-Terra|Stabilisiert Sand/Stein/Erde|  
|Sisto-Persona|Behindert eine Person|  
|Sisto-Disruptio|Stabilisert ein Objekt gegen Zerbrechen, Tickrate: Stunde, Bonuskosten: 1 jedes mal wenn Objekt schaden erleiden Würde.|  
|||  
|Fulgur-Meta|erschafft Ladung an einem Ort|  
|Fulgur-Tutela|trifft jede Runde das nächste nicht ausgenommene (Biegung) Ziel in Reichweite |  
|Fulgur-Ignes|Plasma: Wurf*3/2 Schaden, Wurf*0.5 Schaden auf selbst (Biegung zum Verhindern), Instabilität bei 1,2,3 |  
|Fulgur-Terra|erzeugt Glas|  
|Fulgur-Persona|Ladung entsteht an der Person|  
|Fulgur-Diruptio|entlädt die Ladung um den Zauberer herum|  
|||  
|Ignes-Terrra|Funken (Steigen weit nach oben) |  
|Ignes-Tutela|Feuerschaden auf alles in Reichweite|  
|Ignes-Persona|Setzt Person in Brand (Single Target Ignes, Feuercounter = Schaden) |  
|Ignes-Meta|erzeugt Feuer am Ziel|  
|Ignes-disruptio| Flammenexplosion|  
|||  
|Terra-Tutela|Sand entsteht überall im Bereich|  
|Terra-Persona|macht Person dreckig|  
|Terra-Meta|erzeugt Sand am Ziel|  
|Terra-disruptio|Sandexplosion|  