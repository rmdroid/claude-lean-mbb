# Scrum Master Integration (PSM III Niveau)

Diese Referenz beschreibt, wie Scrum auf Professional Scrum Master III Niveau mit Lean Six Sigma DMAIC integriert wird.

## Scrum Grundlagen

### Die 3 Säulen (Empirismus)

| Säule | Beschreibung | LSS-Anwendung |
|-------|--------------|---------------|
| **Transparenz** | Arbeit und Fortschritt sichtbar | Visuelle KPIs, Kontrollkarten, Boards |
| **Überprüfung** | Regelmäßige Inspektion | Tollgates, Sprint Reviews, SPC |
| **Anpassung** | Bei Abweichung korrigieren | PDCA, Kaizen, Reaktionspläne |

### Die 5 Werte

| Wert | Beschreibung | LSS-Relevanz |
|------|--------------|--------------|
| **Commitment** | Verbindlichkeit zum Sprint-Ziel | Projektziele, CTQ-Erreichung |
| **Focus** | Fokus auf Sprint-Arbeit | Eine Phase nach der anderen |
| **Openness** | Offenheit über Arbeit und Hindernisse | Transparente Daten, ehrliche Analyse |
| **Respect** | Respekt im Team | Stakeholder-Einbindung |
| **Courage** | Mut, schwierige Themen anzusprechen | Root Cause offenlegen, unbequeme Wahrheiten |

### Scrum Events

| Event | Zweck | Timebox | DMAIC-Anwendung |
|-------|-------|---------|-----------------|
| **Sprint** | Container für Arbeit | 1-4 Wochen | Mini-DMAIC-Zyklus |
| **Sprint Planning** | Sprint-Scope definieren | 8h (4-Wochen-Sprint) | Phase planen |
| **Daily Scrum** | Synchronisation | 15 min | Täglicher Kurz-Check |
| **Sprint Review** | Ergebnis präsentieren | 4h | Tollgate-Präsentation |
| **Retrospektive** | Prozess verbessern | 3h | Lessons Learned |

### Scrum Artefakte

| Artefakt | Beschreibung | DMAIC-Äquivalent |
|----------|--------------|------------------|
| **Product Backlog** | Priorisierte Anforderungsliste | CTQs, Verbesserungsmaßnahmen |
| **Sprint Backlog** | Arbeit für aktuellen Sprint | Phasen-Arbeitspaket |
| **Increment** | Nutzbares Produktinkrement | Abgeschlossene Phase, Pilotversuch |
| **Definition of Done** | Qualitätskriterien | Tollgate-Kriterien |

## DMAIC-zu-Scrum Mapping

### Phasenstruktur

**Option A: DMAIC als Sprint-Struktur**
```
Sprint 0 │ Sprint 1 │ Sprint 2 │ Sprint 3 │ Sprint 4 │ Sprint 5
(Setup)  │ (Define) │ (Measure)│ (Analyze)│ (Improve)│ (Control)
```

**Option B: DMAIC innerhalb von Sprints**
```
Sprint 1        │ Sprint 2        │ Sprint 3
D → M (Teil)    │ M → A (Teil)    │ A → I → C (Teil)
```

**Empfehlung:** Option A für Standardprojekte, Option B für komplexe Transformationen.

### Rollen-Mapping

| Scrum-Rolle | LSS-Rolle | Verantwortung in LSS |
|-------------|-----------|---------------------|
| **Product Owner** | Sponsor / Champion | Vision, Priorisierung, Business Case |
| **Scrum Master** | Master Black Belt | Prozess-Facilitation, Hindernisse beseitigen |
| **Developers** | Black Belt, Green Belt, Team | DMAIC-Durchführung, Analyse, Implementierung |

### Event-Mapping

| Scrum Event | DMAIC-Nutzung |
|-------------|---------------|
| **Sprint Planning** | Phase planen, Arbeitspakete definieren, Ziele setzen |
| **Daily Scrum** | Fortschritt bei Datensammlung, Analysen, Maßnahmen |
| **Sprint Review** | Tollgate-Präsentation, Stakeholder-Feedback |
| **Retrospektive** | Was lief gut/schlecht in der Phase, Prozessverbesserung |

## Scrum-Artefakte für LSS

### Product Backlog für LSS

**Struktur:**

| ID | User Story / Item | Phase | Priorität | Story Points | Status |
|----|-------------------|-------|-----------|--------------|--------|
| 1 | Als Sponsor möchte ich einen quantifizierten Business Case, um das Projekt zu rechtfertigen | Define | Hoch | 5 | Done |
| 2 | Als Team möchten wir VOC erheben, um CTQs zu definieren | Define | Hoch | 8 | Done |
| 3 | Als Analyst möchte ich Baseline-Daten, um den Ist-Zustand zu quantifizieren | Measure | Hoch | 13 | In Progress |
| 4 | Als Team möchten wir Root Causes validieren, um gezielt zu verbessern | Analyze | Mittel | 8 | Backlog |

**User Story Format für LSS:**
```
Als [Rolle]
möchte ich [Ziel/Deliverable]
damit [Nutzen/Outcome]

Akzeptanzkriterien:
- [ ] Kriterium 1
- [ ] Kriterium 2
- [ ] Tollgate-Kriterium erfüllt
```

### Definition of Done (DoD) für DMAIC

**DoD Define:**
- [ ] Project Charter vollständig
- [ ] SIPOC erstellt
- [ ] VOC erhoben (≥10 Datenpunkte)
- [ ] CTQ-Tree mit Spezifikationen
- [ ] Stakeholder-Analyse abgeschlossen
- [ ] Business Case quantifiziert
- [ ] Sponsor-Freigabe erhalten

**DoD Measure:**
- [ ] Datensammlungsplan umgesetzt
- [ ] MSA bestanden (Gage R&R <30%)
- [ ] Baseline für alle CTQs berechnet
- [ ] Prozess-Mapping abgeschlossen
- [ ] Daten validiert

**DoD Analyze:**
- [ ] Ishikawa/Brainstorming durchgeführt
- [ ] Pareto-Analyse abgeschlossen
- [ ] 5-Why für Top-Ursachen
- [ ] Statistische Validierung erfolgt
- [ ] Grundursachen dokumentiert

**DoD Improve:**
- [ ] Lösungen entwickelt und bewertet
- [ ] FMEA durchgeführt
- [ ] Pilot erfolgreich
- [ ] Implementierungsplan erstellt
- [ ] Change Management vorbereitet

**DoD Control:**
- [ ] Kontrollplan aktiv
- [ ] SPC implementiert
- [ ] SOPs dokumentiert
- [ ] Schulungen durchgeführt
- [ ] Übergabe erfolgt

### Sprint Backlog für LSS

**Kanban-Board für LSS:**

```
┌───────────────┬───────────────┬───────────────┬───────────────┐
│    Backlog    │  In Progress  │    Review     │     Done      │
│               │    (WIP: 3)   │    (WIP: 2)   │               │
├───────────────┼───────────────┼───────────────┼───────────────┤
│ FMEA erstellen│ Pilot durch-  │ Ishikawa      │ Baseline      │
│               │ führen        │ validieren    │ berechnet     │
│ Kontrollplan  │ Schulungs-    │               │ VOC erhoben   │
│ schreiben     │ material      │               │               │
│               │               │               │ Daten-        │
│ SOP erstellen │               │               │ sammlung      │
└───────────────┴───────────────┴───────────────┴───────────────┘
```

## Agile Metriken für LSS

### Sprint-Metriken

| Metrik | Beschreibung | Zielwert |
|--------|--------------|----------|
| **Velocity** | Story Points pro Sprint | Stabil ±20% |
| **Sprint Burndown** | Arbeit über Sprint-Dauer | Linear abnehmend |
| **Sprint Goal Achievement** | Wurde Sprint-Ziel erreicht? | 100% |

### Release-Metriken

| Metrik | Beschreibung | Zielwert |
|--------|--------------|----------|
| **Release Burnup** | Fortschritt zum Projektziel | Planmäßig |
| **Cumulative Flow** | WIP und Durchfluss | Gleichmäßiger Fluss |
| **Lead Time** | Zeit von Backlog bis Done | Möglichst kurz |

### LSS-spezifische Metriken

| Metrik | Beschreibung | Messung |
|--------|--------------|---------|
| **CTQ-Fortschritt** | Verbesserung der CTQs über Zeit | Pro Sprint tracken |
| **Tollgate-Einhaltung** | Wurden Tollgate-Kriterien erfüllt? | Ja/Nein pro Phase |
| **Sigma-Level-Trend** | Entwicklung des Sigma-Levels | Baseline → Aktuell |

## Scrum Master als Facilitator

### Facilitation in DMAIC

| Phase | Facilitation-Fokus |
|-------|-------------------|
| **Define** | Workshop-Moderation für SIPOC, VOC, Stakeholder-Mapping |
| **Measure** | Klärung von Operational Definitions im Team |
| **Analyze** | Brainstorming-Facilitation, 5-Why-Sessions |
| **Improve** | Lösungs-Workshops, Priorisierungs-Sessions |
| **Control** | Übergabe-Moderation, Retrospektiven |

### Hindernisse beseitigen

**Typische Hindernisse in LSS-Projekten:**

| Hindernis | Scrum Master Aktion |
|-----------|---------------------|
| Daten nicht verfügbar | IT/Fachbereich eskalieren, Workarounds finden |
| Stakeholder blockiert | 1:1 Gespräch, Sponsor einschalten |
| Team überlastet | Scope reduzieren, Priorisieren |
| Technische Hürde | Experten einbinden, Spike planen |
| Widerstand gegen Änderung | Change-Gespräche, Quick Wins zeigen |

### Coaching auf PSM III Niveau

**Team-Coaching:**
- Selbstorganisation fördern (nicht dirigieren)
- Retrospektiven effektiv nutzen
- Psychological Safety schaffen
- Continuous Improvement kultivieren

**Stakeholder-Coaching:**
- Product Owner in Priorisierung unterstützen
- Management-Erwartungen managen
- Agile Prinzipien vermitteln
- Transparenz einfordern

**Organisations-Coaching:**
- Impediments auf Org-Ebene adressieren
- Lean Thinking verbreiten
- Scaling-Fragen klären
- Kulturwandel unterstützen

## Hybrid: Scrum + PRINCE2

Für große Transformationen kann beides kombiniert werden:

```
PRINCE2 (Governance-Ebene)
├── Lenkungsausschuss (monatlich)
├── Stage Gates = DMAIC Tollgates
├── Exception Management
└── Formale Dokumentation

Scrum (Delivery-Ebene)
├── Sprint-Zyklen für Arbeit
├── Daily Syncs
├── Sprint Reviews = Tollgate-Präsentation
└── Retrospektiven für kontinuierliche Verbesserung
```

**Wann Hybrid:**
- Große, regulierte Umgebungen
- Formale Governance erforderlich
- Agile Umsetzung gewünscht
- Beste aus beiden Welten
