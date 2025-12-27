# DMAIC Define Phase – MBB Niveau

Die Define-Phase legt das Fundament für den gesamten Projekterfolg. Auf MBB-Niveau werden alle Werkzeuge systematisch eingesetzt.

## Werkzeuge der Define-Phase

### 1. Project Charter

Die Project Charter ist das zentrale Projektdokument. Sie enthält:

| Element | Beschreibung | Qualitätskriterium |
|---------|--------------|-------------------|
| **Projekttitel** | Prägnant, aussagekräftig | Max. 10 Worte |
| **Problem Statement** | Quantifiziertes Problem | SMART-Kriterien erfüllt |
| **Business Case** | Wirtschaftliche Rechtfertigung | ROI oder Kostenvermeidung beziffert |
| **Projektziel** | Messbares Ziel | Baseline → Target mit Datum |
| **Scope** | In-Scope / Out-of-Scope | Klar abgegrenzt |
| **Meilensteine** | DMAIC-Phasen mit Terminen | Realistisch geplant |
| **Team** | Rollen und Verantwortlichkeiten | Sponsor, Champion, Team definiert |
| **Ressourcen** | Budget, Zeit, Personal | Bestätigt durch Sponsor |

**Problem Statement Formel:**
```
[WAS] ist das Problem, das [WO] auftritt, [SEIT WANN] besteht, 
und [WIE VIEL] Auswirkung hat (quantifiziert in €, Zeit, Fehler, etc.).
```

**Beispiel:**
"Die Durchlaufzeit der Auftragsbearbeitung im Vertriebsinnendienst beträgt durchschnittlich 5,2 Tage (Baseline: Q3/2024), was zu Kundenbeschwerden und geschätzten 120.000€ Umsatzverlust pro Jahr führt."

### 2. SIPOC-Diagramm

SIPOC gibt einen High-Level-Überblick über den Prozess:

| S – Suppliers | I – Inputs | P – Process | O – Outputs | C – Customers |
|---------------|------------|-------------|-------------|---------------|
| Wer liefert? | Was wird geliefert? | 5-7 Hauptschritte | Was wird produziert? | Wer empfängt? |

**Erstellungsreihenfolge:**
1. **P**rocess zuerst (5-7 High-Level-Schritte)
2. **O**utputs (Was entsteht am Ende?)
3. **C**ustomers (Wer empfängt die Outputs?)
4. **I**nputs (Was braucht der Prozess?)
5. **S**uppliers (Wer liefert die Inputs?)

**Qualitätskriterien:**
- Prozess auf 5-7 Schritte abstrahiert (nicht zu detailliert)
- Start- und Endpunkt klar definiert
- Alle relevanten Inputs/Outputs erfasst
- Interne UND externe Kunden berücksichtigt

### 3. Voice of Customer (VOC)

VOC erfasst die Kundenbedürfnisse systematisch:

**Datenquellen:**
- Kundenbefragungen
- Beschwerden und Reklamationen
- Support-Tickets
- Interviews
- Fokusgruppen
- Social Media / Bewertungen

**VOC → CTQ Übersetzung:**

| VOC (Kundenstimme) | Kundenbedürfnis | CTQ (Critical to Quality) |
|--------------------|-----------------|---------------------------|
| "Das dauert zu lange" | Schnelle Bearbeitung | Durchlaufzeit ≤ 2 Tage |
| "Zu viele Fehler" | Fehlerfreie Lieferung | Fehlerquote < 1% |
| "Ich werde nicht informiert" | Transparenz | Statusupdate alle 24h |

### 4. CTQ-Tree (Critical to Quality)

Der CTQ-Tree übersetzt Kundenbedürfnisse in messbare Anforderungen:

```
Kundenbedürfnis (VOC)
    │
    ├── Treiber 1
    │   ├── CTQ 1.1 (messbar, Spezifikation)
    │   └── CTQ 1.2 (messbar, Spezifikation)
    │
    └── Treiber 2
        ├── CTQ 2.1 (messbar, Spezifikation)
        └── CTQ 2.2 (messbar, Spezifikation)
```

**Beispiel:**
```
Kundenzufriedenheit
    │
    ├── Schnelle Lieferung
    │   ├── Lieferzeit ≤ 3 Werktage (95%)
    │   └── Tracking-Info innerhalb 2h nach Versand
    │
    └── Korrekte Lieferung
        ├── Richtige Menge: 100%
        └── Richtige Artikel: 99,9%
```

**Qualitätskriterien für CTQs:**
- Messbar (Einheit definiert)
- Spezifikation (Grenzwert definiert)
- Relevant für Kunde
- Beeinflussbar durch Prozess

### 5. Stakeholder-Analyse

**Stakeholder-Matrix (Power/Interest Grid):**

```
         INTEREST
         Low          High
    ┌─────────────┬─────────────┐
H   │   Keep      │   Manage    │
i P │  Satisfied  │   Closely   │
g O │             │             │
h W ├─────────────┼─────────────┤
  E │   Monitor   │    Keep     │
L R │   (Minimal) │  Informed   │
o   │             │             │
w   └─────────────┴─────────────┘
```

**Für jeden Stakeholder erfassen:**
- Name / Rolle
- Interesse am Projekt (1-5)
- Einfluss/Macht (1-5)
- Aktuelle Haltung (Unterstützer / Neutral / Widerstand)
- Gewünschte Haltung
- Maßnahmen zur Einbindung

### 6. Business Case

**Komponenten:**
- **Problem-Kosten:** Was kostet das Problem aktuell? (Quantifiziert)
- **Projektkosten:** Was kostet die Lösung?
- **Erwarteter Nutzen:** Einsparungen, Umsatzsteigerung, Qualitätsverbesserung
- **ROI:** (Nutzen - Kosten) / Kosten × 100
- **Payback-Periode:** Wann amortisiert sich das Projekt?

## Tollgate-Kriterien Define

Die Define-Phase gilt als abgeschlossen, wenn:

- [ ] Project Charter vollständig und vom Sponsor genehmigt
- [ ] SIPOC erstellt und validiert
- [ ] VOC erhoben (mind. 3 Quellen oder 10 Datenpunkte)
- [ ] CTQ-Tree mit messbaren Spezifikationen
- [ ] Stakeholder-Analyse mit Maßnahmenplan
- [ ] Business Case quantifiziert
- [ ] Team vollständig besetzt
- [ ] Kick-off durchgeführt

## PRINCE2 Integration

| Define-Element | PRINCE2-Äquivalent |
|----------------|-------------------|
| Project Charter | Project Initiation Document (PID) |
| Business Case | Business Case (Pflichtdokument) |
| Stakeholder-Analyse | Teil der Projektorganisation |
| Scope | Projektproduktbeschreibung |
| Meilensteine | Phasenplan |

## Scrum Integration

| Define-Element | Scrum-Äquivalent |
|----------------|-----------------|
| Project Charter | Product Vision |
| VOC / CTQ | User Stories im Product Backlog |
| Scope | Initial Product Backlog |
| Team | Scrum Team Formation |
| Kick-off | Sprint 0 / Inception |
