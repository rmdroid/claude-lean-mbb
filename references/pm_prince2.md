# PRINCE2 Practitioner Integration

Diese Referenz beschreibt, wie PRINCE2 auf Practitioner-Niveau mit Lean Six Sigma DMAIC integriert wird.

## PRINCE2 Grundprinzipien

### Die 7 Prinzipien

| Prinzip | Beschreibung | LSS-Relevanz |
|---------|--------------|--------------|
| **Fortlaufende geschäftliche Rechtfertigung** | Projekt muss Business Case haben | Quantifizierter Business Case in Define |
| **Lernen aus Erfahrung** | Lessons Learned nutzen | Lessons Learned in Control |
| **Definierte Rollen und Verantwortlichkeiten** | Klare Projektorganisation | Team-Charter, RACI |
| **Steuern über Phasen** | Meilensteine und Entscheidungspunkte | DMAIC-Tollgates |
| **Steuern nach Ausnahmen** | Toleranzen und Eskalation | Control Limits, OOC-Reaktion |
| **Produktorientierung** | Fokus auf Ergebnisse | CTQ, messbare Outputs |
| **Anpassung an Projektumgebung** | Tailoring | Komplexitätsbasierte Skalierung |

### Die 7 Themen

| Thema | PRINCE2-Inhalt | DMAIC-Mapping |
|-------|----------------|---------------|
| **Business Case** | Wirtschaftliche Rechtfertigung | Define: Business Case, ROI |
| **Organisation** | Rollen, Verantwortlichkeiten | Define: Project Charter, Team |
| **Qualität** | Qualitätserwartungen, -kriterien | Measure: CTQ, Spezifikationen |
| **Pläne** | Projektplan, Phasenpläne | Define: Projektplan, Meilensteine |
| **Risiko** | Risikoidentifikation und -management | Improve: FMEA |
| **Änderungen** | Änderungssteuerung | Control: Standardisierung |
| **Fortschritt** | Überwachung und Steuerung | Measure/Control: KPIs, SPC |

### Die 7 Prozesse

| Prozess | Aktivitäten | DMAIC-Phase |
|---------|-------------|-------------|
| **Starting Up** | Projektidee, Team, Projektauftrag | Vor Define |
| **Initiating** | PID, Pläne, Business Case detailliert | Define |
| **Directing** | Entscheidungen, Freigaben | Alle Tollgates |
| **Controlling a Stage** | Arbeit beauftragen, überwachen | Measure, Analyze, Improve |
| **Managing Product Delivery** | Arbeitspakete ausführen | Alle Arbeitspakete |
| **Managing Stage Boundary** | Phasenübergang, Reporting | DMAIC-Tollgates |
| **Closing** | Projektabschluss, Übergabe | Control |

## DMAIC-zu-PRINCE2 Mapping

### Phasenstruktur

```
PRINCE2-Sicht:
┌─────────────────────────────────────────────────────────────────┐
│ Initiierungsphase │ Durchführungsphase(n)        │ Abschluss   │
│ (Define)          │ (Measure → Analyze → Improve)│ (Control)   │
└─────────────────────────────────────────────────────────────────┘

DMAIC-Sicht:
┌─────────┬─────────┬─────────┬─────────┬─────────┐
│ Define  │ Measure │ Analyze │ Improve │ Control │
│ Tollgate│ Tollgate│ Tollgate│ Tollgate│ Tollgate│
└─────────┴─────────┴─────────┴─────────┴─────────┘
```

### Dokumenten-Mapping

| PRINCE2-Dokument | LSS-Äquivalent | Erstellt in |
|------------------|----------------|-------------|
| **Project Brief** | Problem Statement, Projektidee | Vor Define |
| **Project Initiation Document (PID)** | Project Charter | Define |
| **Business Case** | Business Case mit ROI | Define, Update in Control |
| **Projektproduktbeschreibung** | CTQ, Spezifikationen | Define/Measure |
| **Produktstrukturplan** | SIPOC, Prozess-Map | Define/Measure |
| **Phasenplan** | DMAIC-Projektplan | Define |
| **Arbeitspaket** | Spezifische Analyse/Maßnahme | Measure/Analyze/Improve |
| **Highlight Report** | Status-Report | Wöchentlich |
| **End Stage Report** | Tollgate-Präsentation | Jeder DMAIC-Übergang |
| **End Project Report** | Projektabschlussbericht | Control |
| **Lessons Log** | Lessons Learned | Fortlaufend, finalisiert in Control |

### Rollen-Mapping

| PRINCE2-Rolle | LSS-Rolle | Verantwortung |
|---------------|-----------|---------------|
| **Executive** | Sponsor | Entscheidungen, Ressourcen, Business Case |
| **Senior User** | Process Owner | Nutzeranforderungen, Akzeptanz |
| **Senior Supplier** | Champion | Fachliche Unterstützung |
| **Project Manager** | Master Black Belt / Black Belt | Projektleitung, DMAIC-Durchführung |
| **Team Manager** | Green Belt | Arbeitspaket-Leitung |
| **Project Assurance** | Quality Assurance | Unabhängige Qualitätsprüfung |
| **Project Support** | Projektbüro | Administrative Unterstützung |

## PRINCE2-Artefakte für LSS

### Project Initiation Document (PID)

**PID-Struktur für LSS-Projekte:**

1. **Projektdefinition**
   - Hintergrund (Warum dieses Projekt?)
   - Projektziele (SMART)
   - Scope (In/Out)
   - Deliverables (DMAIC-Outputs)
   - Ausnahmen und Annahmen

2. **Business Case**
   - Problemkosten (quantifiziert)
   - Erwarteter Nutzen
   - Projektkosten
   - ROI und Payback

3. **Projektorganisation**
   - Sponsor, Champion, MBB/BB/GB
   - RACI-Matrix
   - Kommunikationsmatrix

4. **Qualitätsmanagement**
   - CTQs und Spezifikationen
   - Tollgate-Kriterien
   - Qualitätsprüfungen

5. **Risikomanagement**
   - Top-Risiken
   - Mitigationsmaßnahmen
   - Risikoappetit

6. **Pläne**
   - DMAIC-Phasenplan
   - Meilensteine
   - Ressourcenplan

### Exception Report

**Wann nutzen:**
- Prozessfähigkeit wird nicht erreicht
- Zeitplan/Budget überschritten
- Grundursache nicht validierbar
- Lösung scheitert im Pilot

**Struktur:**
1. Beschreibung der Abweichung
2. Auswirkung auf Business Case
3. Handlungsoptionen (mind. 2)
4. Empfehlung
5. Entscheidungsbedarf

### Checkpoint Report

**Wöchentlicher Status:**

| Element | Inhalt |
|---------|--------|
| Berichtszeitraum | KW XX |
| Gesamtstatus | 🟢 / 🟡 / 🔴 |
| Erledigte Arbeit | Was wurde abgeschlossen |
| Geplante Arbeit | Was steht an |
| Risiken/Issues | Aktuelle Probleme |
| Entscheidungsbedarf | Offene Punkte für Sponsor |

## Toleranzen und Eskalation

### Toleranz-Definition (für LSS-Projekte)

| Dimension | Toleranz | Eskalation wenn |
|-----------|----------|-----------------|
| **Zeit** | ±1 Woche pro Phase | > 2 Wochen Verzug gesamt |
| **Budget** | ±10% | > 10% Überschreitung |
| **Qualität** | Cpk ±0,1 vom Ziel | Cpk < 1,0 (nicht fähig) |
| **Scope** | Kleinere Anpassungen | Grundlegende Scope-Änderung |
| **Risiko** | RPN < 100 | RPN > 200 |
| **Nutzen** | ±20% vom geplanten Nutzen | Nutzen < 50% |

### Eskalationspfad

```
Projektteam (GB/BB)
        │
        ▼ (Toleranz überschritten)
Projektleitung (MBB)
        │
        ▼ (Projekt-Toleranz überschritten)
Champion
        │
        ▼ (Stage-Toleranz überschritten)
Sponsor / Lenkungsausschuss
        │
        ▼ (Unternehmens-Toleranz überschritten)
Geschäftsführung
```

## Tailoring für LSS-Projekte

### Quick Win (1-4 Wochen)

- PID: Verkürzt auf 1-2 Seiten
- Reporting: Nur bei Abschluss
- Tollgates: Kombiniert (D-M und A-I-C)
- Dokumentation: Minimal

### Standard-Projekt (1-3 Monate)

- PID: Vollständig
- Reporting: Wöchentlich
- Tollgates: Alle 5 separat
- Dokumentation: Standard

### Transformation (3-12 Monate)

- PID: Umfassend mit Anhängen
- Reporting: Wöchentlich + monatlich Lenkungsausschuss
- Tollgates: Formale Reviews mit Lenkungsausschuss
- Dokumentation: Umfassend, revisionssicher
