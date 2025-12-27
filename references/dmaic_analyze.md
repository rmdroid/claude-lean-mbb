# DMAIC Analyze Phase – MBB Niveau

Die Analyze-Phase identifiziert und validiert die Grundursachen des Problems durch qualitative und quantitative Methoden.

## Werkzeuge der Analyze-Phase

### 1. Ursachenanalyse-Framework

**Strategie:** Von breit nach fokussiert

```
Viele mögliche Ursachen
        │
        ▼
Ishikawa / Brainstorming (generieren)
        │
        ▼
Pareto-Analyse (priorisieren)
        │
        ▼
5-Why (tiefere Ursachen)
        │
        ▼
Statistische Validierung (bestätigen)
        │
        ▼
Wenige validierte Grundursachen
```

### 2. Ishikawa-Diagramm (Fischgräte)

**6M-Kategorien für Produktion:**
- **Mensch:** Qualifikation, Motivation, Fehler
- **Maschine:** Ausrüstung, Werkzeuge, Software
- **Material:** Rohmaterial, Qualität, Verfügbarkeit
- **Methode:** Prozesse, Verfahren, Arbeitsanweisungen
- **Milieu:** Umgebung, Arbeitsplatz, Klima
- **Messung:** Messfehler, Kalibrierung, Datenqualität

**Alternative für Dienstleistung (5P + 1P):**
- **People:** Mitarbeiter, Kunden
- **Process:** Arbeitsabläufe
- **Policies:** Regeln, Vorgaben
- **Place:** Standort, Arbeitsumgebung
- **Product:** Dienstleistung, Deliverables
- **Proof:** Dokumentation, Nachweise

**Erstellungsschritte:**
1. Problem (Effekt) rechts als Kopf
2. Hauptkategorien als Gräten
3. Brainstorming: Ursachen an Gräten
4. Tiefere Ursachen als Nebengräten
5. Priorisieren: Top 3-5 markieren

### 3. 5-Why-Analyse

Die 5-Why-Methode gräbt zur Grundursache durch wiederholtes "Warum?".

**Regeln:**
- Mind. 5× "Warum?" fragen
- Jede Antwort muss faktisch sein (nicht spekulativ)
- Bei Verzweigungen: alle Pfade verfolgen
- Stopp wenn: Grundursache beeinflussbar ist

**Beispiel:**
```
Problem: Kunde erhielt falsche Lieferung

Warum 1: Falsches Produkt wurde verpackt
Warum 2: Mitarbeiter hat falsches Regal angesteuert
Warum 3: Regalbeschriftung war fehlerhaft
Warum 4: Nach Umräumaktion wurde nicht aktualisiert
Warum 5: Es gibt keinen Prozess für Beschriftungsupdates
         ↓
Grundursache: Fehlender Prozess für Lagerbeschriftung
```

**Qualitätsprüfung:**
- Ist die Grundursache beeinflussbar?
- Ist sie spezifisch genug für Maßnahmen?
- Erklärt sie das Problem vollständig?

### 4. Pareto-Analyse

Die Pareto-Analyse priorisiert nach dem 80/20-Prinzip.

**Schritte:**
1. Kategorien der Fehler/Probleme sammeln
2. Häufigkeit oder Kosten pro Kategorie zählen
3. Absteigend sortieren
4. Kumulative Prozente berechnen
5. Fokus auf Kategorien bis 80% kumulativ

**Beispiel:**

| Fehlerart | Anzahl | % | Kumulativ |
|-----------|--------|---|-----------|
| Falsche Menge | 45 | 36% | 36% |
| Falsches Produkt | 32 | 26% | 62% |
| Beschädigung | 23 | 18% | 80% |
| Verspätung | 12 | 10% | 90% |
| Sonstige | 13 | 10% | 100% |

→ Fokus auf: Falsche Menge, Falsches Produkt, Beschädigung

### 5. Statistische Analyse

#### 5.1 Hypothesentests – Entscheidungsbaum

```
Was wird verglichen?
        │
        ├── Mittelwerte
        │   ├── 1 Gruppe vs. Zielwert → 1-Sample t-Test
        │   ├── 2 Gruppen (unabhängig) → 2-Sample t-Test
        │   ├── 2 Gruppen (verbunden) → Paired t-Test
        │   └── >2 Gruppen → ANOVA
        │
        ├── Anteile/Häufigkeiten
        │   ├── 1 Anteil vs. Zielwert → 1-Proportion Test
        │   ├── 2 Anteile → 2-Proportion Test
        │   └── Kategorien vs. erwartet → Chi²-Test
        │
        └── Zusammenhänge
            ├── 2 kontinuierliche → Korrelation
            └── X→Y Beziehung → Regression
```

#### 5.2 Interpretation der Ergebnisse

**p-Wert:**
- p < 0,05: Statistisch signifikant (Nullhypothese ablehnen)
- p ≥ 0,05: Nicht signifikant (Nullhypothese nicht ablehnen)

**Praktische Signifikanz:**
- Statistische Signifikanz ≠ praktische Relevanz
- Immer Effektgröße betrachten
- Frage: Ist der Unterschied groß genug für Handlung?

**Konfidenzintervalle:**
- 95% KI zeigt Bereich plausibler Werte
- Überlappen KIs nicht: signifikanter Unterschied
- Breites KI: hohe Unsicherheit (mehr Daten nötig)

#### 5.3 Korrelation und Regression

**Korrelation (r):**
- r = 0: Kein linearer Zusammenhang
- r = ±0,3: Schwach
- r = ±0,5: Mittel
- r = ±0,7: Stark
- r = ±1: Perfekt

**Achtung:** Korrelation ≠ Kausalität!

**Regression:**
- R² (Bestimmtheitsmaß): Anteil erklärter Varianz
- R² > 0,7: Gutes Modell
- Residuen prüfen (Normalverteilung, Homoskedastizität)

### 6. Prozessanalyse

#### Wertschöpfungsanalyse (VA/NVA)

Klassifiziere jeden Prozessschritt:

| Kategorie | Definition | Beispiele |
|-----------|------------|-----------|
| **Value Added (VA)** | Kunde würde dafür bezahlen | Produktion, Beratung |
| **Non-Value Added but Necessary (NVAN)** | Nicht wertschöpfend, aber erforderlich | Compliance, Qualitätsprüfung |
| **Non-Value Added (NVA)** | Verschwendung, eliminierbar | Warten, Nacharbeit, Transport |

**Ziel:** NVA eliminieren, NVAN minimieren, VA optimieren.

#### 8 Arten der Verschwendung (TIMWOODS)

| Verschwendung | Erklärung | Indikatoren |
|---------------|-----------|-------------|
| **T**ransport | Unnötiges Bewegen von Material | Lange Wege, häufige Transporte |
| **I**nventar | Überschüssige Bestände | Hohe Lagerkosten, Obsoleszenz |
| **M**ovement | Unnötige Bewegung von Menschen | Ergonomie-Probleme, Suchzeiten |
| **W**aiting | Warten auf Material, Information, Entscheidung | Leerlauf, Bottlenecks |
| **O**verproduction | Mehr produzieren als benötigt | Lageraufbau, vorzeitige Produktion |
| **O**verprocessing | Mehr tun als der Kunde verlangt | Überqualität, unnötige Features |
| **D**efects | Fehler, Nacharbeit, Ausschuss | Reklamationen, Ausschussquote |
| **S**kills | Ungenutztes Mitarbeiterpotenzial | Demotivation, keine Einbindung |

### 7. Ursachen-Validierung

Bevor Ursachen als bestätigt gelten:

**Validierungs-Checkliste:**
- [ ] Ursache durch Daten belegt (nicht nur Vermutung)
- [ ] Statistischer Test signifikant (p < 0,05)
- [ ] Effektgröße praktisch relevant
- [ ] Ursache ist beeinflussbar (nicht extern)
- [ ] Prozessexperten bestätigen Plausibilität

**Dokumentation:**

| Vermutete Ursache | Validierungsmethode | Ergebnis | Status |
|-------------------|---------------------|----------|--------|
| Schicht A macht mehr Fehler | 2-Sample t-Test | p=0,003, Δ=2,3% | ✓ Bestätigt |
| Alte Maschine langsamer | Korrelation Alter-Zeit | r=0,12 | ✗ Nicht bestätigt |

## Tollgate-Kriterien Analyze

Die Analyze-Phase gilt als abgeschlossen, wenn:

- [ ] Ishikawa/Brainstorming durchgeführt (alle möglichen Ursachen)
- [ ] Pareto-Analyse für Priorisierung
- [ ] 5-Why für Top-Ursachen
- [ ] Statistische Validierung der Hypothesen
- [ ] Grundursachen quantifiziert und dokumentiert
- [ ] Prozessanalyse (VA/NVA, Verschwendung) abgeschlossen
- [ ] Management-Buy-in für identifizierte Ursachen

## PRINCE2 Integration

| Analyze-Element | PRINCE2-Äquivalent |
|-----------------|-------------------|
| Ursachenanalyse | Issue-Analyse |
| Validierte Ursachen | Business Case Update |
| Empfehlungen | Exception Report (bei Abweichung) |

## Scrum Integration

| Analyze-Element | Scrum-Äquivalent |
|-----------------|-----------------|
| Ishikawa/5-Why | Sprint-Workshop |
| Statistische Analyse | Sprint(s) für Analyse |
| Ergebnisse | Sprint Review |
| Learnings | Retrospektive |
