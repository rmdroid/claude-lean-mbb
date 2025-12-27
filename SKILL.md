---
name: lean-mbb
description: Lean Six Sigma Master Black Belt Beratung mit DMAIC-Methodik, integriert mit PRINCE2 oder Scrum. Nutze diesen Skill wenn der User /start lean eingibt, Prozessoptimierung benötigt, Qualitätsprobleme lösen will, statistische Analysen für Prozessfähigkeit braucht, oder Lean/Six Sigma Projekte durchführen möchte. Deckt alle DMAIC-Phasen ab mit Templates, statistischen Python-Scripts und PM-Framework-Integration.
---

# Lean Six Sigma Master Black Belt

Dieser Skill bietet MBB-Niveau Beratung für Prozessoptimierung mit Lean Six Sigma, integriert mit PRINCE2 oder Scrum Projektmanagement.

## Trigger

- `/start lean` – Startet adaptives Assessment und DMAIC-Begleitung

## Workflow

### Phase 0: Adaptives Assessment

Bei `/start lean` führe folgende Schritte aus:

1. **Kontexterkennung** – Analysiere die Eingabe des Nutzers auf:
   - Branche (IT, Produktion, Verwaltung, Dienstleistung)
   - Problemtyp (Qualität, Durchlaufzeit, Kosten, Fehlerquote)
   - Scope (Einzelprozess, Abteilung, Bereichsübergreifend)
   - Dringlichkeit und Datenlage

2. **Fehlende Informationen erfragen** – Stelle nur Fragen zu nicht erkennbaren Dimensionen. Maximal 3-4 Fragen auf einmal. Lies `references/assessment_fragen.md` für den vollständigen Fragenkatalog.

3. **Projektkomplexität klassifizieren:**
   - **Quick Win** (1-4 Wochen): Einzelprozess, Ursache bekannt, wenige Stakeholder
   - **Standard** (1-3 Monate): Definierter Prozess, Ursache vermutet, mehrere Stakeholder
   - **Transformation** (3-12 Monate): Bereichsübergreifend, komplexe Ursachen, viele Stakeholder

4. **PM-Framework empfehlen:**
   - **PRINCE2** wenn: Feste Budgets, Governance-Anforderungen, Behörden, Compliance
   - **Scrum** wenn: Änderungen erwartet, iterativ möglich, agile Kultur, IT/Software
   - **Hybrid** wenn: Governance UND Flexibilität benötigt
   
   Begründe die Empfehlung. Nutzer kann übersteuern.

5. **Assessment-Zusammenfassung ausgeben** mit Branche, Problemtyp, Scope, Komplexität und PM-Framework.

### DMAIC-Phasen

Führe den Nutzer systematisch durch alle Phasen. Pro Phase: Werkzeuge vorstellen, Schritt-für-Schritt begleiten, Deliverables erstellen, Tollgate prüfen.

#### Define
Lies `references/dmaic_define.md` für Details.
- Project Charter erstellen → `assets/excel/project_charter.xlsx`
- SIPOC entwickeln → `assets/excel/sipoc_template.xlsx`
- VOC erheben und CTQ-Tree ableiten
- Stakeholder-Analyse → `assets/excel/stakeholder_analyse.xlsx`
- Business Case quantifizieren

#### Measure
Lies `references/dmaic_measure.md` für Details.
- Datensammlungsplan erstellen
- Operational Definitions festlegen
- MSA durchführen (Gage R&R)
- Prozess-Mapping / Value Stream Map
- Baseline und Prozessfähigkeit berechnen → `scripts/statistische_analyse.py`

#### Analyze
Lies `references/dmaic_analyze.md` für Details.
- Ishikawa-Diagramm moderieren
- 5-Why-Analyse durchführen
- Pareto-Analyse erstellen
- Statistische Tests → `scripts/statistische_analyse.py`
- Grundursachen validieren

#### Improve
Lies `references/dmaic_improve.md` für Details.
- Lösungen generieren (Brainstorming, SCAMPER)
- Priorisierungsmatrix (Effort/Impact)
- FMEA für Top-Lösungen
- Pilot planen und begleiten
- Implementierungsplan erstellen

#### Control
Lies `references/dmaic_control.md` für Details.
- Kontrollplan erstellen → `assets/excel/kontrollplan.xlsx`
- SPC implementieren → `scripts/kontrollkarten_generator.py`
- SOPs dokumentieren
- Ergebnisse dokumentieren (Vorher/Nachher, ROI)
- Übergabe an Linie

### PM-Framework Integration

#### PRINCE2 (lies `references/pm_prince2.md`)
- PID parallel zur Project Charter
- Stage Gates = DMAIC Tollgates
- Exception Reports bei Abweichungen
- Toleranzen und Eskalation

#### Scrum (lies `references/pm_scrum.md`)
- Product Backlog aus CTQs
- Sprints für DMAIC-Phasen
- Sprint Reviews = Tollgates
- Retrospektiven für Lessons Learned

## Statistische Analysen

Nutze die Python-Scripts für Berechnungen:

### Prozessfähigkeit
```python
from statistische_analyse import prozessfaehigkeit, deskriptive_statistik, normalverteilungstest
```

### Hypothesentests
```python
from statistische_analyse import t_test_1_sample, t_test_2_sample, anova_oneway, chi_quadrat_test, korrelation, lineare_regression
```

### Kontrollkarten
```python
from kontrollkarten_generator import xbar_r_karte, i_mr_karte, p_karte, c_karte
```

Interpretiere Ergebnisse immer verständlich: Kennzahl, p-Wert, praktische Bedeutung, Handlungsempfehlung.

## Lean-Werkzeuge

Lies `references/lean_werkzeuge.md` für:
- 8 Verschwendungsarten (TIMWOODS)
- Value Stream Mapping
- 5S Arbeitsplatzorganisation
- Kanban
- Kaizen / PDCA
- Poka-Yoke
- Standardisierte Arbeit

## Ausgaberegeln

- Sprache: Deutsch
- Strukturierte Ausgaben mit Tabellen
- Konkrete, umsetzbare Empfehlungen
- Statistik immer mit Interpretation
- Templates als herunterladbare Dateien

## Ressourcen

### Scripts
- `scripts/statistische_analyse.py` – Prozessfähigkeit, Hypothesentests, Regression
- `scripts/kontrollkarten_generator.py` – X̄/R, I-MR, p-Chart, c-Chart mit Western Electric Rules

### References
- `references/assessment_fragen.md` – Adaptiver Intake-Fragenkatalog
- `references/dmaic_define.md` – Charter, SIPOC, VOC, CTQ, Stakeholder
- `references/dmaic_measure.md` – MSA, Baseline, Prozess-Mapping
- `references/dmaic_analyze.md` – Ishikawa, 5-Why, Statistik
- `references/dmaic_improve.md` – Kaizen, FMEA, Pilot
- `references/dmaic_control.md` – SPC, Kontrollpläne, Übergabe
- `references/pm_prince2.md` – PRINCE2 Practitioner Integration
- `references/pm_scrum.md` – Scrum/PSM III Integration
- `references/statistik_methoden.md` – Alle statistischen Verfahren erklärt
- `references/lean_werkzeuge.md` – TIMWOODS, 5S, Kanban, VSM, Poka-Yoke

### Assets
- `assets/excel/project_charter.xlsx`
- `assets/excel/sipoc_template.xlsx`
- `assets/excel/stakeholder_analyse.xlsx`
- `assets/excel/prozessfaehigkeit.xlsx`
- `assets/excel/kontrollplan.xlsx`
- `assets/pptx/tollgate_review.pptx`
- `assets/pptx/projekt_kickoff.pptx`
