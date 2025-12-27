# 🎯 Claude Lean MBB

> **Dein Master Black Belt in der Tasche** – Lean Six Sigma Beratung auf höchstem Niveau, direkt in Claude integriert.

[![Claude Skill](https://img.shields.io/badge/Claude-Skill-blueviolet)](https://claude.ai)
[![Lean Six Sigma](https://img.shields.io/badge/Lean%20Six%20Sigma-MBB-green)](https://de.wikipedia.org/wiki/Six_Sigma)
[![PRINCE2](https://img.shields.io/badge/PRINCE2-Practitioner-blue)](https://www.axelos.com/certifications/prince2)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Was ist das?

Ein **Claude Skill**, der dich durch komplette Lean Six Sigma Projekte begleitet – von der Problemdefinition bis zur nachhaltigen Kontrolle. Kombiniert DMAIC-Methodik mit PRINCE2 oder Scrum Projektmanagement.

**Kein oberflächliches ChatGPT-Gelaber.** Echte MBB-Expertise mit:
- Statistischen Analysen (Prozessfähigkeit, Hypothesentests, SPC)
- Professionellen Templates (Excel, PowerPoint)
- Strukturierter Projektführung nach bewährten Standards

---

## ✨ Features

### 🧠 Adaptives Assessment
Der Skill erkennt deinen Kontext und stellt nur die Fragen, die wirklich fehlen. Keine endlosen Fragebögen – direkt zum Punkt.

### 📊 Vollständiges DMAIC
Alle 5 Phasen mit Tollgate-Kriterien:

| Phase | Was du bekommst |
|-------|-----------------|
| **Define** | Project Charter, SIPOC, VOC, CTQ-Tree, Stakeholder-Analyse |
| **Measure** | Datensammlungsplan, MSA, Baseline, Prozessfähigkeit (Cp/Cpk) |
| **Analyze** | Ishikawa, 5-Why, Pareto, statistische Validierung |
| **Improve** | Lösungsbewertung, FMEA, Pilot-Begleitung |
| **Control** | Kontrollpläne, SPC, SOPs, Übergabe |

### 🔬 Echte Statistik
Python-Scripts für:
- **Prozessfähigkeit:** Cp, Cpk, Pp, Ppk, Sigma-Level, DPMO
- **Hypothesentests:** t-Tests, ANOVA, Chi², Korrelation, Regression
- **Kontrollkarten:** X̄/R, I-MR, p-Chart, c-Chart mit Western Electric Rules

### 🏗️ PM-Framework Integration
Der Skill empfiehlt basierend auf deinem Projektkontext:
- **PRINCE2** für Governance, Behörden, feste Budgets
- **Scrum** für agile Umgebungen, IT-Projekte
- **Hybrid** wenn beides gebraucht wird

### 📁 Professionelle Templates
Fertige Excel- und PowerPoint-Vorlagen:
- Project Charter
- SIPOC
- Stakeholder-Analyse
- Prozessfähigkeits-Berechnung
- Kontrollplan
- Tollgate Review Präsentation
- Projekt Kickoff Präsentation

---

## 🚀 Installation

### Voraussetzungen
- Ein Claude Pro/Team Account mit aktivierten Skills
- Zugang zum Skills-Verzeichnis

### Schritt-für-Schritt

**Option A: Direkter Download**

1. **Repository klonen oder ZIP herunterladen:**
   ```bash
   git clone https://github.com/rmdroid/claude-lean-mbb.git
   ```

2. **Skill-Ordner kopieren:**
   ```bash
   cp -r claude-lean-mbb/lean-mbb /pfad/zu/deinen/claude/skills/user/
   ```

3. **Claude neu starten** und fertig!

**Option B: Manuell**

1. Lade die [neueste Release-ZIP](https://github.com/rmdroid/claude-lean-mbb/releases) herunter
2. Entpacke den `lean-mbb` Ordner
3. Kopiere ihn in dein Claude Skills-Verzeichnis unter `/mnt/skills/user/`

### Verzeichnisstruktur nach Installation

```
/mnt/skills/user/
└── lean-mbb/
    ├── SKILL.md
    ├── references/
    ├── scripts/
    └── assets/
```

---

## 💡 Verwendung

### Skill starten

Gib einfach in Claude ein:

```
/start lean
```

### Was dann passiert

1. **Assessment** – Claude analysiert deinen Kontext und fragt gezielt nach
2. **Klassifizierung** – Quick Win, Standard-Projekt oder Transformation?
3. **PM-Empfehlung** – PRINCE2, Scrum oder Hybrid?
4. **DMAIC-Begleitung** – Schritt für Schritt durch alle Phasen

### Beispiel-Prompts

```
/start lean

Wir haben ein Problem in der Auftragsbearbeitung. Die Durchlaufzeit 
ist zu lang (aktuell 5 Tage, Ziel wäre 2 Tage). Betrifft den 
Vertriebsinnendienst mit 12 Mitarbeitern.
```

```
/start lean

IT-Projekt: Unser Deployment-Prozess hat zu viele Fehler. 
Agiles Team, 2-Wochen-Sprints. Brauche Unterstützung bei 
der Root Cause Analyse.
```

```
Berechne die Prozessfähigkeit für folgende Messwerte:
[10.2, 10.5, 9.8, 10.1, 10.3, 10.0, 9.9, 10.4, 10.1, 10.2]
USL = 10.8, LSL = 9.2
```

---

## 📂 Was ist enthalten?

```
lean-mbb/
├── SKILL.md                          # Haupt-Workflow
│
├── references/                       # Methodenwissen (10 Dateien)
│   ├── assessment_fragen.md          # Strukturierter Intake
│   ├── dmaic_define.md               # Define-Phase Details
│   ├── dmaic_measure.md              # Measure-Phase Details
│   ├── dmaic_analyze.md              # Analyze-Phase Details
│   ├── dmaic_improve.md              # Improve-Phase Details
│   ├── dmaic_control.md              # Control-Phase Details
│   ├── pm_prince2.md                 # PRINCE2 Integration
│   ├── pm_scrum.md                   # Scrum Integration
│   ├── statistik_methoden.md         # Statistische Verfahren
│   └── lean_werkzeuge.md             # Lean Tools (5S, Kanban, etc.)
│
├── scripts/                          # Python-Analysen
│   ├── statistische_analyse.py       # Prozessfähigkeit, Tests
│   └── kontrollkarten_generator.py   # SPC-Karten
│
└── assets/
    ├── excel/                        # Excel-Templates
    │   ├── project_charter.xlsx
    │   ├── sipoc_template.xlsx
    │   ├── stakeholder_analyse.xlsx
    │   ├── prozessfaehigkeit.xlsx
    │   └── kontrollplan.xlsx
    └── pptx/                         # PowerPoint-Templates
        ├── tollgate_review.pptx
        └── projekt_kickoff.pptx
```

---

## 🎓 Für wen ist das?

- **Lean Six Sigma Berater** die einen intelligenten Assistenten wollen
- **Projektleiter** die DMAIC-Projekte strukturiert durchführen möchten
- **Qualitätsmanager** die statistische Analysen brauchen
- **Führungskräfte** die Prozessoptimierung verstehen und steuern wollen
- **Trainer** die Lean Six Sigma vermitteln

---

## 🔧 Anpassung

Der Skill ist vollständig anpassbar:

- **Eigene Templates:** Ersetze die Excel/PPTX-Dateien in `assets/`
- **Erweiterte Statistik:** Ergänze `scripts/statistische_analyse.py`
- **Branchen-Spezifik:** Passe `references/` an deine Domäne an
- **Sprache:** Aktuell Deutsch – für Englisch die References übersetzen

---

## 📜 Lizenz

MIT License – nutze es frei, auch kommerziell.

---

## 🤝 Beitragen

Pull Requests sind willkommen! Besonders für:
- Weitere statistische Methoden (DOE, Regressionsdiagnostik)
- Branchen-spezifische Templates
- Übersetzungen
- Bug-Fixes

---

## 👤 Autor

**Robert Meyer**

Freelance AI Consultant & Instructor mit 15+ Jahren Beratungserfahrung und PRINCE2 Zertifizierung. Spezialisiert auf KI-Transformation für KMU und Behörden.

- 🌐 [ai.rm-on.de](https://ai.rm-on.de)
- 📚 Autor zahlreicher KI-Fachbücher
- 💼 [LinkedIn](https://www.linkedin.com/in/robert-meyer-666b39315)

---

## ⭐ Gefällt dir der Skill?

Gib dem Repo einen Stern! ⭐

---

*"Qualität ist kein Zufall, sie ist immer das Ergebnis angestrengten Denkens."* – John Ruskin
