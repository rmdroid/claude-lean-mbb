# DMAIC Measure Phase – MBB Niveau

Die Measure-Phase etabliert eine faktische Baseline durch systematische Datenerhebung und Prozessanalyse.

## Werkzeuge der Measure-Phase

### 1. Datensammlungsplan

Der Datensammlungsplan definiert WAS, WIE, WO, WANN und von WEM Daten erhoben werden.

| Element | Frage | Beispiel |
|---------|-------|----------|
| **Was messen?** | Welche CTQs aus Define? | Durchlaufzeit, Fehlerquote |
| **Messtyp** | Kontinuierlich oder diskret? | Zeit (kontinuierlich), Fehler ja/nein (diskret) |
| **Operational Definition** | Wie genau wird gemessen? | "Durchlaufzeit = Zeitstempel Auftragseingang bis Zeitstempel Versandmeldung" |
| **Datenquelle** | Woher kommen die Daten? | ERP-System, manuelle Erfassung |
| **Stichprobe** | Wie viele Datenpunkte? | n=50 für Prozessfähigkeit, n=30 für t-Test |
| **Verantwortlich** | Wer erhebt? | Teamleiter Vertrieb |
| **Zeitraum** | Wann wird erhoben? | KW 45-48 |

**Stichprobengrößen-Richtwerte:**

| Analyse | Minimale Stichprobe | Empfohlen |
|---------|---------------------|-----------|
| Prozessfähigkeit (Cp/Cpk) | 30 | 50-100 |
| t-Test | 15 pro Gruppe | 30 pro Gruppe |
| ANOVA | 15 pro Gruppe | 20 pro Gruppe |
| Korrelation/Regression | 30 | 50+ |
| Kontrollkarte | 20 Subgruppen | 25 Subgruppen |

### 2. Operational Definitions

Eine Operational Definition beschreibt EXAKT, wie eine Messung durchgeführt wird.

**Struktur:**
1. **Metrik:** Name der Kennzahl
2. **Einheit:** Messeinheit
3. **Messverfahren:** Schritt-für-Schritt-Anleitung
4. **Grenzwerte:** Spezifikationsgrenzen (USL, LSL)
5. **Ausnahmen:** Was wird nicht gezählt?

**Beispiel:**
```
Metrik: Durchlaufzeit Auftragsbearbeitung
Einheit: Arbeitstage (dezimal, eine Nachkommastelle)
Messverfahren:
  1. Zeitstempel Auftragseingang aus ERP (Feld: ORDER_CREATED)
  2. Zeitstempel Versandmeldung aus ERP (Feld: SHIPMENT_SENT)
  3. Differenz berechnen, Wochenenden abziehen
Grenzwerte: USL = 3 Tage, Ziel = 2 Tage
Ausnahmen: Kundenrückfragen (separater Prozess), Teillieferungen
```

### 3. Messsystemanalyse (MSA)

Die MSA validiert, dass das Messsystem zuverlässig ist, bevor Prozessdaten interpretiert werden.

**Gage R&R (Repeatability & Reproducibility):**

| Komponente | Bedeutung | Akzeptabel |
|------------|-----------|------------|
| **Repeatability** | Gleicher Prüfer, gleiches Teil → Variabilität | < 10% der Gesamtvariabilität |
| **Reproducibility** | Verschiedene Prüfer, gleiches Teil → Variabilität | < 10% der Gesamtvariabilität |
| **Gage R&R gesamt** | Repeatability + Reproducibility | < 10% exzellent, < 30% akzeptabel |
| **Number of Distinct Categories** | Unterscheidbare Kategorien | ≥ 5 |

**Gage R&R Durchführung:**
1. 10 Teile auswählen (über Prozessbereich verteilt)
2. 3 Prüfer bestimmen
3. Jeder Prüfer misst jedes Teil 2-3 mal (randomisiert, verblindet)
4. ANOVA-Analyse durchführen

**Für attributive Daten (gut/schlecht):**
- Kappa-Analyse
- Attribute Agreement Analysis
- Ziel: Kappa > 0,75

### 4. Prozess-Mapping

**Detailliertes Prozessflussdiagramm:**

Symbole:
- ⬭ Oval: Start/Ende
- ▭ Rechteck: Prozessschritt
- ◇ Raute: Entscheidung
- ▷ Pfeil: Flussrichtung
- D: Verzögerung/Warten
- ▽ Dreieck: Lager/Bestand

**Value Stream Map (VSM):**

Erfasse für jeden Prozessschritt:
- Zykluszeit (C/T)
- Rüstzeit (C/O)
- Verfügbarkeit (Uptime %)
- Losgröße (Batch)
- Anzahl Mitarbeiter
- Lagerbestand davor/danach
- Wartezeit zwischen Schritten

**Kennzahlen aus VSM:**
- **Durchlaufzeit (Lead Time):** Gesamtzeit durch den Prozess
- **Prozesszeit (Value-Added Time):** Nur wertschöpfende Zeit
- **Prozesseffizienz:** Prozesszeit / Durchlaufzeit × 100%

Typische Prozesseffizienz:
- < 10%: Viel Verschwendung, großes Potenzial
- 10-25%: Durchschnitt
- > 25%: Lean-optimiert

### 5. Baseline-Metriken

Dokumentiere den Ist-Zustand aller CTQs:

| CTQ | Baseline | Periode | Ziel | Gap |
|-----|----------|---------|------|-----|
| Durchlaufzeit | 5,2 Tage | Q3/2024 | 2,0 Tage | -3,2 Tage |
| Fehlerquote | 8,3% | Q3/2024 | 2,0% | -6,3 Pkt. |
| Kundenzufriedenheit | 72% | Q3/2024 | 90% | +18 Pkt. |

**Prozessfähigkeits-Baseline:**

| Kennzahl | Bedeutung | Zielwert |
|----------|-----------|----------|
| **Cp** | Potenzielle Fähigkeit (ohne Zentrierung) | ≥ 1,33 |
| **Cpk** | Tatsächliche Fähigkeit (mit Zentrierung) | ≥ 1,33 |
| **Pp** | Langzeit-Performance (potentiell) | ≥ 1,33 |
| **Ppk** | Langzeit-Performance (tatsächlich) | ≥ 1,33 |
| **DPMO** | Defects per Million Opportunities | abhängig von Sigma-Level |

**Sigma-Level Übersicht:**

| Sigma | DPMO | Yield |
|-------|------|-------|
| 2σ | 308.537 | 69,15% |
| 3σ | 66.807 | 93,32% |
| 4σ | 6.210 | 99,38% |
| 5σ | 233 | 99,977% |
| 6σ | 3,4 | 99,99966% |

### 6. Datenvalidierung

Bevor Daten analysiert werden:

**Prüfungen:**
- [ ] Keine fehlenden Werte (oder Strategie für Umgang)
- [ ] Keine offensichtlichen Ausreißer ohne Erklärung
- [ ] Daten plausibel (Wertebereich, Einheiten)
- [ ] Zeitreihe stabil (keine Trends während Erhebung)
- [ ] MSA bestanden (Messsystem fähig)

**Grafische Prüfungen:**
- Histogramm (Verteilung)
- Zeitreihendiagramm (Stabilität)
- Box-Plot (Ausreißer)
- Normalverteilungstest (für Prozessfähigkeit)

## Tollgate-Kriterien Measure

Die Measure-Phase gilt als abgeschlossen, wenn:

- [ ] Datensammlungsplan erstellt und umgesetzt
- [ ] Operational Definitions für alle CTQs dokumentiert
- [ ] MSA durchgeführt (Gage R&R < 30% oder Kappa > 0,75)
- [ ] Prozess-Mapping (detailliertes Flussdiagramm oder VSM)
- [ ] Baseline für alle CTQs quantifiziert
- [ ] Prozessfähigkeit berechnet (Cp, Cpk)
- [ ] Daten validiert und dokumentiert

## PRINCE2 Integration

| Measure-Element | PRINCE2-Äquivalent |
|-----------------|-------------------|
| Baseline-Metriken | Projektprodukt-Beschreibung (Qualitätskriterien) |
| Datensammlungsplan | Arbeitspaket-Definition |
| Prozess-Mapping | Produktstrukturplan |

## Scrum Integration

| Measure-Element | Scrum-Äquivalent |
|-----------------|-----------------|
| Datenerhebung | Sprint(s) für Datensammlung |
| Baseline | Definition of Done für Measure |
| Ergebnisse | Sprint Review mit Stakeholdern |
