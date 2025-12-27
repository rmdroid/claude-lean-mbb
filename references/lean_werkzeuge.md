# Lean Werkzeuge

Diese Referenz beschreibt die wichtigsten Lean-Werkzeuge für Prozessverbesserung.

## Grundprinzipien

### Die 5 Lean-Prinzipien

| Prinzip | Beschreibung | Frage |
|---------|--------------|-------|
| **1. Wert definieren** | Wert aus Kundensicht verstehen | Wofür zahlt der Kunde? |
| **2. Wertstrom identifizieren** | Alle Schritte von Anfang bis Ende | Welche Schritte sind nötig? |
| **3. Fluss erzeugen** | Unterbrechungsfreier Ablauf | Wo stockt es? |
| **4. Pull einführen** | Produktion nach Bedarf | Wird nur produziert, was gebraucht wird? |
| **5. Perfektion anstreben** | Kontinuierliche Verbesserung | Wie können wir noch besser werden? |

## Die 8 Verschwendungsarten (TIMWOODS)

### Übersicht

| Verschwendung | Japanisch | Beschreibung | Beispiele |
|---------------|-----------|--------------|-----------|
| **T**ransport | Muda | Unnötiges Bewegen von Material | Lange Transportwege, mehrfaches Umlagern |
| **I**nventar | Muda | Überschüssige Bestände | Hohe Lagerbestände, WIP-Berge |
| **M**ovement | Muda | Unnötige Bewegung von Menschen | Suchen, Laufen, Greifen |
| **W**aiting | Muda | Warten auf Material, Info, Entscheidung | Leerlauf, Bottlenecks, Genehmigungen |
| **O**verproduction | Muda | Mehr produzieren als benötigt | Auf Lager produzieren, vorzeitige Produktion |
| **O**verprocessing | Muda | Mehr tun als der Kunde verlangt | Überqualität, unnötige Features, Reports |
| **D**efects | Muda | Fehler, Nacharbeit, Ausschuss | Reklamationen, Korrekturen, Ausschuss |
| **S**kills | Muda | Ungenutztes Mitarbeiterpotenzial | Keine Einbindung, Demotivation |

### Identifikation in der Praxis

**Transport:**
- Spaghetti-Diagramm erstellen
- Transportwege messen
- Materialfluss visualisieren

**Inventar:**
- WIP-Bestände zählen
- Lagerumschlag berechnen
- Obsoleszenz-Rate prüfen

**Movement:**
- Bewegungsdiagramm erstellen
- Arbeitsplatz-Layout analysieren
- Suchzeiten messen

**Waiting:**
- Wartezeiten messen
- Bottlenecks identifizieren
- Genehmigungszeiten tracken

**Overproduction:**
- Lageraufbau analysieren
- Push vs. Pull prüfen
- Losgrößen hinterfragen

**Overprocessing:**
- Kundenbedürfnisse klären
- Prozessschritte hinterfragen
- Gold-Plating identifizieren

**Defects:**
- Fehlerquoten messen
- Nacharbeit erfassen
- Ausschusskosten berechnen

**Skills:**
- Mitarbeiterbefragung
- Verbesserungsvorschläge zählen
- Qualifikationsmatrix prüfen

## Wertstromanalyse (Value Stream Mapping)

### Symbole

| Symbol | Bedeutung |
|--------|-----------|
| ▭ Rechteck | Prozessschritt |
| ◇ Raute | Entscheidung |
| ▽ Dreieck | Bestand/Lager |
| ═══▷ Pfeil (fett) | Push-Fluss |
| ───▷ Pfeil (dünn) | Pull-Fluss |
| ⚡ Blitz | Kaizen-Burst (Verbesserungspotenzial) |
| 👁️ Auge | Supermarket (Kanban) |

### Daten pro Prozessschritt

| Kennzahl | Abkürzung | Beschreibung |
|----------|-----------|--------------|
| Zykluszeit | C/T | Zeit für eine Einheit |
| Rüstzeit | C/O | Changeover-Zeit |
| Verfügbarkeit | Uptime | Betriebszeit in % |
| Losgröße | Batch | Einheiten pro Los |
| Anzahl Mitarbeiter | # | Personal am Prozess |
| First Pass Yield | FPY | Gut beim ersten Mal |

### Zeitlinie

```
Prozess 1    Warten    Prozess 2    Warten    Prozess 3
   2h         24h         1h          48h         3h
   ▬▬▬▬       ═══════     ▬▬          ═══════════  ▬▬▬
   
Wertschöpfend:  6h (7,6%)
Nicht wertschöpfend: 72h (92,4%)
Durchlaufzeit: 78h
```

### Prozesseffizienz

**Formel:**
```
Prozesseffizienz = Wertschöpfende Zeit / Durchlaufzeit × 100%
```

**Benchmarks:**
- < 5%: Massives Potenzial
- 5-15%: Typisch für nicht-optimierte Prozesse
- 15-25%: Gut
- > 25%: Lean-optimiert

## 5S Arbeitsplatzorganisation

### Die 5 Schritte

| Schritt | Japanisch | Deutsch | Aktion |
|---------|-----------|---------|--------|
| **1. Seiri** | 整理 | Sortieren | Trennen von Notwendigem und Unnötigem |
| **2. Seiton** | 整頓 | Systematisieren | Alles hat seinen Platz |
| **3. Seiso** | 清掃 | Säubern | Reinigen und dabei inspizieren |
| **4. Seiketsu** | 清潔 | Standardisieren | Standards festlegen und visualisieren |
| **5. Shitsuke** | 躾 | Selbstdisziplin | Disziplin halten, Audits durchführen |

### 5S-Audit-Checkliste

| Kriterium | 0 | 1 | 2 | 3 | 4 |
|-----------|---|---|---|---|---|
| Unnötige Gegenstände entfernt | Nein | Wenig | Teilweise | Größtenteils | Vollständig |
| Feste Plätze definiert | Nein | Wenig | Teilweise | Größtenteils | Vollständig |
| Arbeitsplatz sauber | Nein | Wenig | Teilweise | Größtenteils | Vollständig |
| Standards sichtbar | Nein | Wenig | Teilweise | Größtenteils | Vollständig |
| Standards eingehalten | Nein | Wenig | Teilweise | Größtenteils | Vollständig |

**Bewertung:** 0-5 kritisch, 6-10 verbesserungswürdig, 11-15 gut, 16-20 exzellent

## Kanban

### Grundprinzipien

1. **Visualisieren** des Arbeitsflusses
2. **WIP begrenzen** (Work in Progress)
3. **Fluss managen** und messen
4. **Regeln explizit** machen
5. **Feedback-Schleifen** implementieren
6. **Kontinuierlich verbessern** (Kaizen)

### Kanban-Board Design

```
┌─────────────┬─────────────┬─────────────┬─────────────┐
│   Backlog   │  In Work    │   Review    │    Done     │
│             │   WIP: 5    │   WIP: 2    │             │
├─────────────┼─────────────┼─────────────┼─────────────┤
│ ┌─────┐     │ ┌─────┐     │ ┌─────┐     │ ┌─────┐     │
│ │Task │     │ │Task │     │ │Task │     │ │Task │     │
│ │  A  │     │ │  B  │     │ │  E  │     │ │  F  │     │
│ └─────┘     │ └─────┘     │ └─────┘     │ └─────┘     │
│ ┌─────┐     │ ┌─────┐     │             │ ┌─────┐     │
│ │Task │     │ │Task │     │             │ │Task │     │
│ │  C  │     │ │  D  │     │             │ │  G  │     │
│ └─────┘     │ └─────┘     │             │ └─────┘     │
└─────────────┴─────────────┴─────────────┴─────────────┘
```

### WIP-Limits festlegen

**Faustregel:** 1-2 Aufgaben pro Person im Team

**Anpassung:**
- Zu viel WIP: Aufgaben dauern lange, viel Kontextwechsel → Limit senken
- Zu wenig WIP: Leerlauf, Bottlenecks → Limit erhöhen

### Kanban-Metriken

| Metrik | Beschreibung | Berechnung |
|--------|--------------|------------|
| **Lead Time** | Zeit von Eingang bis Fertigstellung | Endzeit - Startzeit |
| **Cycle Time** | Zeit in aktiver Bearbeitung | Bearbeitungszeit |
| **Throughput** | Erledigte Aufgaben pro Zeiteinheit | Anzahl / Zeitraum |
| **WIP** | Aktuelle Arbeit im System | Anzahl offener Tasks |

**Little's Law:**
```
Lead Time = WIP / Throughput
```

## Kaizen

### PDCA-Zyklus

```
    ┌─────────────────────┐
    │       Plan          │
    │  Problem analysieren│
    │  Lösung planen     │
    └─────────┬───────────┘
              │
              ▼
┌─────────────────────────────────┐
│            Do                    │
│   Lösung im kleinen testen      │
└─────────────┬───────────────────┘
              │
              ▼
    ┌─────────────────────┐
    │       Check         │
    │  Ergebnis prüfen    │
    │  Ziel erreicht?     │
    └─────────┬───────────┘
              │
              ▼
┌─────────────────────────────────┐
│            Act                   │
│  Standardisieren oder anpassen  │
└─────────────────────────────────┘
              │
              └──────────────► (zurück zu Plan)
```

### Kaizen-Event (Blitz-Kaizen)

**Dauer:** 3-5 Tage intensiv

**Ablauf:**
- Tag 1: Problem verstehen, Ist-Zustand dokumentieren
- Tag 2-3: Lösungen entwickeln und implementieren
- Tag 4: Testen und anpassen
- Tag 5: Dokumentieren, nächste Schritte

**Erfolgsvoraussetzungen:**
- Management-Commitment
- Cross-funktionales Team (5-10 Personen)
- Dedizierte Zeit (keine Nebentätigkeiten)
- Entscheidungsbefugnis im Team
- Sofortige Umsetzung möglich

## Poka-Yoke (Fehlervermeidung)

### Prinzip

Fehler unmöglich machen durch Design, nicht durch Inspektion.

### Typen

| Typ | Wirkung | Beispiel |
|-----|---------|----------|
| **Kontakt** | Physische Form verhindert Fehler | USB-C passt nur richtig herum |
| **Zählung** | Richtige Menge sicherstellen | Blister zeigt fehlende Teile |
| **Sequenz** | Reihenfolge erzwingen | Mikrowelle startet nur bei geschlossener Tür |
| **Alarm** | Warnung bei Fehler | Piepen bei offenem Sicherheitsgurt |

### Design-Levels

| Level | Beschreibung | Effektivität |
|-------|--------------|--------------|
| **Unmöglich machen** | Fehler kann nicht passieren | ★★★★★ |
| **Erschweren** | Fehler ist schwer zu machen | ★★★★☆ |
| **Erkennen** | Fehler wird sofort erkannt | ★★★☆☆ |
| **Warnen** | Hinweis auf möglichen Fehler | ★★☆☆☆ |

### Implementierungsschritte

1. Fehlerart identifizieren (aus FMEA, Reklamationen)
2. Ursache verstehen (5-Why)
3. Poka-Yoke-Lösung designen
4. Prototyp testen
5. Implementieren und überwachen

## Standardisierte Arbeit

### Komponenten

| Element | Beschreibung |
|---------|--------------|
| **Taktzeit** | Verfügbare Zeit / Kundenbedarf |
| **Arbeitssequenz** | Reihenfolge der Schritte |
| **Standard-WIP** | Mindest-Bestand im Prozess |

### Standard Work Sheet

| Schritt | Beschreibung | Zeit | Qualitätspunkt |
|---------|--------------|------|----------------|
| 1 | Material entnehmen | 5s | Position prüfen |
| 2 | Einspannen | 10s | Fest sitzen? |
| 3 | Bearbeiten | 45s | Maß kontrollieren |
| 4 | Entnehmen | 5s | Sichtprüfung |
| 5 | Ablegen | 5s | Richtige Box? |
| **Gesamt** | | **70s** | |

### Vorteile

- Basis für Training neuer Mitarbeiter
- Grundlage für Verbesserung (ohne Standard keine Verbesserung messbar)
- Qualitätssicherung durch Wiederholbarkeit
- Ermöglicht Problemerkennung (Abweichung vom Standard)

## Heijunka (Nivellierung)

### Prinzip

Gleichmäßige Verteilung von Produktionsvolumen und -mix über die Zeit.

### Beispiel

**Vor Heijunka (Batch):**
```
Mo: AAAA AAAA
Di: BBBB BBBB
Mi: CCCC CCCC
```

**Nach Heijunka (nivelliert):**
```
Mo: ABC ABC ABC
Di: ABC ABC ABC
Mi: ABC ABC ABC
```

### Vorteile

- Gleichmäßige Auslastung
- Kürzere Durchlaufzeiten
- Weniger Lagerbestand
- Flexiblere Reaktion auf Schwankungen

## Gemba Walk

### Prinzip

"Geh zum Ort des Geschehens" – Probleme dort verstehen, wo sie entstehen.

### Vorgehen

1. **Vorbereitung:** Fokusthema festlegen
2. **Beobachten:** Ohne sofort zu urteilen
3. **Fragen stellen:** 5× Warum?
4. **Respekt zeigen:** Mitarbeiter einbeziehen
5. **Dokumentieren:** Beobachtungen festhalten
6. **Nachverfolgen:** Maßnahmen umsetzen

### Typische Fragen

- Was ist der Standardprozess?
- Was ist heute anders?
- Wo gibt es Probleme?
- Was würden Sie verbessern?
- Was hindert Sie an guter Arbeit?
