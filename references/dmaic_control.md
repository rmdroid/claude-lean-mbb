# DMAIC Control Phase – MBB Niveau

Die Control-Phase sichert die erreichten Verbesserungen nachhaltig und übergibt an die Linienorganisation.

## Werkzeuge der Control-Phase

### 1. Kontrollplan

Der Kontrollplan dokumentiert alle Maßnahmen zur Prozessüberwachung.

**Kontrollplan-Elemente:**

| Element | Beschreibung |
|---------|--------------|
| **Prozessschritt** | Welcher Schritt wird kontrolliert |
| **CTQ / Merkmal** | Was wird gemessen |
| **Spezifikation** | Grenzwerte (LSL, USL, Ziel) |
| **Messmethode** | Wie wird gemessen |
| **Stichprobe** | Häufigkeit und Umfang |
| **Verantwortlich** | Wer misst und bewertet |
| **Reaktionsplan** | Was tun bei Abweichung |

**Beispiel Kontrollplan:**

| Schritt | Merkmal | Spez. | Messung | Stichprobe | Wer | Reaktion |
|---------|---------|-------|---------|------------|-----|----------|
| Auftragserfassung | Vollständigkeit | 100% | Checkliste | 100% | Sachbearbeiter | Rückfrage an Kunden |
| Bearbeitung | Durchlaufzeit | ≤2 Tage | ERP-Timestamp | 100% | Teamleiter | Eskalation wenn >3 Tage |
| Versand | Fehlerfreiheit | ≥99% | Stichprobe | 10/Tag | QS | 8D-Report wenn <95% |

### 2. Statistical Process Control (SPC)

#### Kontrollkarten-Typen

**Für kontinuierliche Daten:**

| Kontrollkarte | Anwendung | Subgruppen |
|---------------|-----------|------------|
| **X̄/R-Karte** | Mittelwert und Spannweite | n = 2-10 |
| **X̄/s-Karte** | Mittelwert und Standardabweichung | n > 10 |
| **I-MR-Karte** | Einzelwerte und Moving Range | n = 1 |

**Für attributive Daten:**

| Kontrollkarte | Anwendung | Voraussetzung |
|---------------|-----------|---------------|
| **p-Karte** | Anteil fehlerhafter Einheiten | Variable Stichprobe |
| **np-Karte** | Anzahl fehlerhafter Einheiten | Konstante Stichprobe |
| **c-Karte** | Anzahl Fehler pro Einheit | Konstante Prüfgelegenheit |
| **u-Karte** | Fehler pro Einheit | Variable Prüfgelegenheit |

#### Kontrollgrenzen berechnen

**X̄-Karte:**
- UCL = X̄̄ + A₂ × R̄
- CL = X̄̄
- LCL = X̄̄ - A₂ × R̄

**R-Karte:**
- UCL = D₄ × R̄
- CL = R̄
- LCL = D₃ × R̄

**Konstanten (Beispiele):**

| n | A₂ | D₃ | D₄ |
|---|-----|-----|-----|
| 2 | 1,880 | 0 | 3,267 |
| 3 | 1,023 | 0 | 2,574 |
| 4 | 0,729 | 0 | 2,282 |
| 5 | 0,577 | 0 | 2,114 |

#### Regeln für Out-of-Control

**Western Electric Rules:**

| Regel | Beschreibung | Signal für |
|-------|--------------|------------|
| **1** | 1 Punkt außerhalb 3σ | Ausreißer |
| **2** | 9 Punkte in Folge auf einer Seite | Shift |
| **3** | 6 Punkte in Folge steigend/fallend | Trend |
| **4** | 14 Punkte alternierend auf/ab | Überreaktion |
| **5** | 2 von 3 Punkten außerhalb 2σ | Warnung |
| **6** | 4 von 5 Punkten außerhalb 1σ | Warnung |

#### Reaktion auf Signale

```
Out-of-Control erkannt
        │
        ▼
┌─────────────────────────────┐
│ 1. Produktion stoppen?      │ → Wenn Qualitätsrisiko
├─────────────────────────────┤
│ 2. Ursache suchen           │ → 5-Why, Ishikawa
├─────────────────────────────┤
│ 3. Korrekturmaßnahme        │ → Sofort oder geplant
├─────────────────────────────┤
│ 4. Dokumentieren            │ → Kontrollkarte annotieren
├─────────────────────────────┤
│ 5. Kontrollplan aktualisieren│ → Falls nötig
└─────────────────────────────┘
```

### 3. Standardisierung

#### Prozessdokumentation

**Erforderliche Dokumente:**

| Dokument | Inhalt | Zielgruppe |
|----------|--------|------------|
| **Prozessbeschreibung** | High-Level-Ablauf, Verantwortlichkeiten | Management |
| **Arbeitsanweisung** | Schritt-für-Schritt-Anleitung | Mitarbeiter |
| **Checkliste** | Kritische Prüfpunkte | Mitarbeiter |
| **Quick Reference Card** | 1-Seiter mit Kernpunkten | Mitarbeiter |

#### Standard Operating Procedure (SOP)

**SOP-Struktur:**
1. Zweck und Geltungsbereich
2. Begriffe und Abkürzungen
3. Verantwortlichkeiten
4. Voraussetzungen
5. Schritt-für-Schritt-Anleitung
6. Prüfungen und Dokumentation
7. Umgang mit Abweichungen
8. Änderungshistorie

### 4. Training und Wissenstransfer

#### Schulungsplan

| Zielgruppe | Inhalt | Methode | Dauer | Wann |
|------------|--------|---------|-------|------|
| Mitarbeiter | Neuer Prozess | Workshop | 2h | Vor Go-Live |
| Teamleiter | Kontrollplan, SPC | Training | 4h | 1 Woche vor |
| Management | Kennzahlen, Eskalation | Präsentation | 1h | Bei Übergabe |

#### Kompetenznachweis
- [ ] Schulung durchgeführt
- [ ] Verständnistest bestanden
- [ ] Praxis-Begleitung abgeschlossen
- [ ] Zertifizierung ausgestellt

### 5. Projektabschluss

#### Ergebnisdokumentation

**Vorher-Nachher-Vergleich:**

| KPI | Baseline | Nach Improve | Verbesserung | Ziel | Status |
|-----|----------|--------------|--------------|------|--------|
| Durchlaufzeit | 5,2 Tage | 1,9 Tage | -63% | ≤2 Tage | ✓ |
| Fehlerquote | 8,3% | 1,8% | -78% | ≤2% | ✓ |
| Kosten | 240k€/Jahr | 95k€/Jahr | -60% | ≤100k€ | ✓ |

**Finanzielle Ergebnisse:**

| Kategorie | Berechnung | Jährlicher Wert |
|-----------|------------|-----------------|
| Kosteneinsparung | Alte Kosten - Neue Kosten | 145.000€ |
| Qualitätskosten vermieden | Fehlerkosten × Reduktion | 80.000€ |
| Kapazitätsgewinn | Zeitersparnis × Stundensatz | 25.000€ |
| **Gesamtnutzen** | | **250.000€** |
| Projektkosten | Personal + Material | 40.000€ |
| **Netto-Nutzen** | | **210.000€** |
| **ROI** | Nutzen / Kosten × 100 | **525%** |

#### Lessons Learned

**Kategorien:**
- Was lief gut? (Wiederholen)
- Was lief schlecht? (Vermeiden)
- Was haben wir gelernt? (Teilen)
- Empfehlungen für zukünftige Projekte

**Lessons Learned Template:**

| Kategorie | Erkenntnis | Empfehlung |
|-----------|------------|------------|
| Stakeholder | Frühe Einbindung war Erfolgsfaktor | Bei jedem Projekt sofort einbinden |
| Daten | Datenqualität unterschätzt | MSA immer zu Beginn |
| Pilot | 2 Wochen zu kurz | Mindestens 4 Wochen planen |

### 6. Übergabe an Linie

#### Übergabe-Checkliste

**Dokumentation:**
- [ ] Kontrollplan finalisiert und genehmigt
- [ ] SOPs erstellt und freigegeben
- [ ] Schulungsunterlagen übergeben
- [ ] Kennzahlen-Dashboard eingerichtet

**Organisation:**
- [ ] Prozesseigner benannt
- [ ] Verantwortlichkeiten klar
- [ ] Eskalationswege definiert
- [ ] Regelmäßige Reviews geplant

**Technisch:**
- [ ] Messsysteme kalibriert
- [ ] Tools/Templates übergeben
- [ ] Zugänge eingerichtet

#### Nachhaltigkeitsplan

**Review-Rhythmus:**
- Woche 1-4 nach Übergabe: Wöchentlich
- Monat 2-3: Zweiwöchentlich
- Ab Monat 4: Monatlich
- Langfristig: Quartalsweise

**Nachhaltigkeits-KPIs:**
- Prozess-KPIs bleiben in Zielkorridor
- Keine Rückfälle in alte Muster
- Kontrollkarten zeigen Stabilität
- Mitarbeiterzufriedenheit stabil/steigend

## Tollgate-Kriterien Control

Die Control-Phase gilt als abgeschlossen, wenn:

- [ ] Kontrollplan erstellt und genehmigt
- [ ] SPC implementiert (wo anwendbar)
- [ ] SOPs dokumentiert und freigegeben
- [ ] Schulungen durchgeführt
- [ ] Ergebnisse dokumentiert (Vorher/Nachher)
- [ ] ROI berechnet und bestätigt
- [ ] Lessons Learned dokumentiert
- [ ] Übergabe an Prozesseigner erfolgt
- [ ] Projektabschluss vom Sponsor genehmigt

## PRINCE2 Integration

| Control-Element | PRINCE2-Äquivalent |
|-----------------|-------------------|
| Kontrollplan | Produktbeschreibung (Qualitätskriterien) |
| Übergabe | Projektabschluss (Closing a Project) |
| Lessons Learned | Lessons Log / End Project Report |
| Dokumentation | Konfigurationsmanagement |

## Scrum Integration

| Control-Element | Scrum-Äquivalent |
|-----------------|-----------------|
| SPC | Definition of Done |
| Standardisierung | Team Working Agreements |
| Reviews | Regelmäßige Retrospektiven |
| Übergabe | Release / Deployment |
