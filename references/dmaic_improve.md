# DMAIC Improve Phase – MBB Niveau

Die Improve-Phase entwickelt, testet und implementiert Lösungen für die validierten Grundursachen.

## Werkzeuge der Improve-Phase

### 1. Lösungsgenerierung

#### Brainstorming-Regeln
- Quantität vor Qualität
- Keine Kritik während Ideenfindung
- Auf Ideen anderer aufbauen
- Wilde Ideen willkommen
- Zeitlimit setzen (15-30 Min)

#### Kreativitätstechniken

**6-3-5 Brainwriting:**
- 6 Teilnehmer
- 3 Ideen pro Runde
- 5 Minuten pro Runde
- Zettel weitergeben, auf Ideen aufbauen

**SCAMPER:**
- **S**ubstitute: Was kann ersetzt werden?
- **C**ombine: Was kann kombiniert werden?
- **A**dapt: Was kann angepasst werden?
- **M**odify: Was kann verändert werden?
- **P**ut to other use: Andere Verwendung?
- **E**liminate: Was kann entfallen?
- **R**everse: Was kann umgekehrt werden?

**Benchmarking:**
- Best Practices aus anderen Bereichen/Branchen
- Interne Best Practices (andere Standorte, Teams)
- Wettbewerber-Analyse (öffentliche Informationen)

### 2. Lösungsbewertung

#### Priorisierungsmatrix (Effort/Impact)

```
         IMPACT
         Low          High
    ┌─────────────┬─────────────┐
L   │    Don't    │   Quick     │
o E │    Do       │   Wins      │ ← Zuerst
w F │             │             │
  F ├─────────────┼─────────────┤
H O │   Time      │   Major     │
i R │   Sinks     │   Projects  │ ← Planen
g T │             │             │
h   └─────────────┴─────────────┘
```

#### Pugh-Matrix (Entscheidungsmatrix)

| Kriterium | Gewicht | Option A | Option B | Option C | Baseline |
|-----------|---------|----------|----------|----------|----------|
| Wirksamkeit | 5 | + | ++ | 0 | 0 |
| Kosten | 4 | 0 | - | + | 0 |
| Umsetzbarkeit | 3 | + | 0 | ++ | 0 |
| Risiko | 3 | 0 | - | + | 0 |
| Akzeptanz | 2 | + | + | 0 | 0 |
| **Summe** | | +8 | +3 | +10 | 0 |

Legende: ++ = viel besser, + = besser, 0 = gleich, - = schlechter, -- = viel schlechter

#### FMEA (Failure Mode and Effects Analysis)

Für jede Lösung Risiken bewerten:

| Fehlerart | Schwere (S) | Auftreten (O) | Entdeckung (D) | RPN | Maßnahme |
|-----------|-------------|---------------|----------------|-----|----------|
| | 1-10 | 1-10 | 1-10 | S×O×D | |

**RPN-Priorisierung:**
- RPN > 100: Sofortige Maßnahmen
- RPN 50-100: Maßnahmen planen
- RPN < 50: Beobachten

### 3. Lean-Werkzeuge für Verbesserung

#### Kaizen (kontinuierliche Verbesserung)
- Kleine, schnelle Verbesserungen
- Mitarbeiter einbinden
- PDCA-Zyklen (Plan-Do-Check-Act)
- Kaizen-Events: 3-5 Tage intensive Workshops

#### 5S (Arbeitsplatzorganisation)
1. **Seiri (Sortieren):** Unnötiges entfernen
2. **Seiton (Systematisieren):** Ordnung schaffen
3. **Seiso (Säubern):** Reinigen und prüfen
4. **Seiketsu (Standardisieren):** Standards festlegen
5. **Shitsuke (Selbstdisziplin):** Standards einhalten

#### Poka-Yoke (Fehlervermeidung)
Fehler unmöglich machen durch Design:

| Typ | Wirkung | Beispiel |
|-----|---------|----------|
| **Kontakt** | Physische Form verhindert Fehler | USB-Stecker passt nur richtig herum |
| **Zählung** | Richtige Menge sicherstellen | Blister-Verpackung zeigt fehlende Teile |
| **Sequenz** | Reihenfolge erzwingen | Maschine startet nur nach Checkliste |

#### Kanban
- Visualisierung des Arbeitsflusses
- WIP-Limits (Work in Progress)
- Pull-System statt Push
- Kontinuierliche Verbesserung

**Kanban-Board:**
```
┌──────────┬──────────┬──────────┬──────────┐
│ Backlog  │ In Work  │  Review  │   Done   │
│          │  (WIP:3) │  (WIP:2) │          │
├──────────┼──────────┼──────────┼──────────┤
│ Task 4   │ Task 1   │ Task 2   │ Task 0   │
│ Task 5   │ Task 3   │          │          │
│ Task 6   │          │          │          │
└──────────┴──────────┴──────────┴──────────┘
```

#### Standard Work (Standardisierte Arbeit)
- Beste bekannte Methode dokumentieren
- Taktzeit, Arbeitssequenz, Standard-WIP
- Basis für Verbesserung
- Training-Grundlage

### 4. Pilotierung

#### Pilot-Design

**Vor dem Pilot definieren:**
- Scope: Wo wird pilotiert? (Bereich, Team, Zeitraum)
- Dauer: Typisch 2-4 Wochen
- Erfolgskriterien: Messbare KPIs
- Abbruchkriterien: Wann wird gestoppt?
- Verantwortlichkeiten: Wer überwacht?

**Pilot-Checkliste:**
- [ ] Pilotbereich ausgewählt (repräsentativ aber kontrollierbar)
- [ ] Betroffene Mitarbeiter informiert und geschult
- [ ] Baseline-Messung vor Pilot
- [ ] Datenerhebung während Pilot geplant
- [ ] Eskalationspfad definiert
- [ ] Feedback-Mechanismus eingerichtet

#### Pilot-Auswertung

| Metrik | Baseline | Pilot-Ergebnis | Veränderung | Ziel erreicht? |
|--------|----------|----------------|-------------|----------------|
| Durchlaufzeit | 5,2 Tage | 2,8 Tage | -46% | ✓ |
| Fehlerquote | 8,3% | 3,1% | -63% | ✓ |

**Entscheidung nach Pilot:**
- **Erfolg:** Rollout planen
- **Teilweise:** Anpassungen, weiterer Pilot
- **Misserfolg:** Zurück zu Analyze oder andere Lösung

### 5. Implementierungsplanung

#### Rollout-Strategie

| Strategie | Beschreibung | Wann geeignet |
|-----------|--------------|---------------|
| **Big Bang** | Überall gleichzeitig | Einfache Änderungen, hohe Dringlichkeit |
| **Phasenweise** | Bereich für Bereich | Komplexe Änderungen, Lerneffekte nutzen |
| **Parallel** | Alt und Neu gleichzeitig | Hohes Risiko, Fallback nötig |

#### Implementierungsplan

| Phase | Aktivität | Wer | Wann | Status |
|-------|-----------|-----|------|--------|
| Vorbereitung | Schulungsunterlagen erstellen | Team | KW 45 | |
| Schulung | Mitarbeiter trainieren | Trainer | KW 46 | |
| Go-Live | Neue Prozesse starten | Alle | KW 47 | |
| Stabilisierung | Intensiv-Support | Team | KW 47-48 | |
| Übergabe | An Linie übergeben | MBB | KW 49 | |

#### Change Management

**ADKAR-Modell:**
- **A**wareness: Bewusstsein für Notwendigkeit
- **D**esire: Wunsch nach Veränderung
- **K**nowledge: Wissen wie
- **A**bility: Fähigkeit umzusetzen
- **R**einforcement: Verstärkung der Veränderung

**Widerstand adressieren:**
- Früh einbinden (nicht überraschen)
- Quick Wins zeigen
- Champions identifizieren
- Bedenken ernst nehmen
- Erfolge feiern

## Tollgate-Kriterien Improve

Die Improve-Phase gilt als abgeschlossen, wenn:

- [ ] Lösungen für alle Grundursachen entwickelt
- [ ] Lösungen bewertet und priorisiert
- [ ] FMEA für Top-Lösungen durchgeführt
- [ ] Pilot erfolgreich abgeschlossen
- [ ] Pilot-Ergebnisse dokumentiert
- [ ] Implementierungsplan erstellt
- [ ] Schulungskonzept vorhanden
- [ ] Management-Freigabe für Rollout

## PRINCE2 Integration

| Improve-Element | PRINCE2-Äquivalent |
|-----------------|-------------------|
| Lösungsentwicklung | Arbeitspaket |
| Pilot | Stage (separate Phase) |
| Implementierungsplan | Phasenplan |
| Risikobewertung (FMEA) | Risikoregister |
| Change Management | Kommunikationsplan |

## Scrum Integration

| Improve-Element | Scrum-Äquivalent |
|-----------------|-----------------|
| Lösungen | User Stories / Product Backlog Items |
| Priorisierung | Backlog Refinement |
| Pilot | Sprint(s) für MVP |
| Implementierung | Weitere Sprints |
| Feedback | Sprint Review + Retrospektive |
