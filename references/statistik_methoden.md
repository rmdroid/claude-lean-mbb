# Statistische Methoden – MBB Niveau

Diese Referenz beschreibt die wichtigsten statistischen Methoden für Lean Six Sigma mit Interpretationshilfen.

## Deskriptive Statistik

### Lagemaße

| Maß | Berechnung | Wann nutzen |
|-----|------------|-------------|
| **Mittelwert (x̄)** | Summe / Anzahl | Normalverteilte Daten |
| **Median** | Mittlerer Wert (sortiert) | Schiefe Verteilung, Ausreißer |
| **Modus** | Häufigster Wert | Kategoriale Daten |

### Streuungsmaße

| Maß | Berechnung | Interpretation |
|-----|------------|----------------|
| **Spannweite (R)** | Max - Min | Einfach, aber ausreißerempfindlich |
| **Varianz (s²)** | Σ(x - x̄)² / (n-1) | Mittlere quadratische Abweichung |
| **Standardabweichung (s)** | √Varianz | Streuung in Originaleinheit |
| **Variationskoeffizient (CV)** | s / x̄ × 100% | Relative Streuung, vergleichbar |

### Verteilungsform

| Kennzahl | Interpretation |
|----------|----------------|
| **Schiefe = 0** | Symmetrisch |
| **Schiefe > 0** | Rechtsschiefe (Ausreißer nach oben) |
| **Schiefe < 0** | Linksschiefe (Ausreißer nach unten) |
| **Kurtosis = 3** | Normalverteilt |
| **Kurtosis > 3** | Spitzer, mehr Ausreißer |
| **Kurtosis < 3** | Flacher, weniger Ausreißer |

## Prozessfähigkeit

### Fähigkeitsindizes

| Index | Formel | Interpretation |
|-------|--------|----------------|
| **Cp** | (USL - LSL) / (6σ) | Potenzielle Fähigkeit (ignoriert Zentrierung) |
| **Cpk** | min[(USL - μ) / (3σ), (μ - LSL) / (3σ)] | Tatsächliche Fähigkeit (berücksichtigt Zentrierung) |
| **Pp** | (USL - LSL) / (6s) | Langzeit-Performance (potentiell) |
| **Ppk** | min[(USL - μ) / (3s), (μ - LSL) / (3s)] | Langzeit-Performance (tatsächlich) |

**Unterschied Cp/Cpk vs. Pp/Ppk:**
- Cp/Cpk: Kurzzeit, nutzt σ aus Subgruppen-Variation (within)
- Pp/Ppk: Langzeit, nutzt s aus Gesamtvariation (overall)

### Interpretation

| Wert | Bewertung | Sigma-Level | DPMO |
|------|-----------|-------------|------|
| < 0,67 | Nicht fähig | < 2σ | > 308.537 |
| 0,67 - 1,00 | Schlecht | 2-3σ | 66.807 - 308.537 |
| 1,00 - 1,33 | Akzeptabel | 3-4σ | 6.210 - 66.807 |
| 1,33 - 1,67 | Gut | 4-5σ | 233 - 6.210 |
| > 1,67 | Exzellent | > 5σ | < 233 |

**Zielwert:** Cpk ≥ 1,33 (entspricht ~4σ)

### Voraussetzungen

- Daten normalverteilt (Test mit Anderson-Darling, Shapiro-Wilk)
- Prozess stabil (keine Trends, Shifts in Kontrollkarte)
- Ausreichende Stichprobe (n ≥ 30, besser n ≥ 50)

## Hypothesentests

### Allgemeines Framework

**Schritte:**
1. Hypothesen formulieren (H₀, H₁)
2. Signifikanzniveau festlegen (α = 0,05)
3. Test durchführen, p-Wert berechnen
4. Entscheidung: p < α → H₀ ablehnen

**Fehlerarten:**

| | H₀ wahr | H₀ falsch |
|--|---------|-----------|
| **H₀ beibehalten** | Richtig (1-α) | Fehler 2. Art (β) |
| **H₀ ablehnen** | Fehler 1. Art (α) | Richtig (Power = 1-β) |

### Test-Auswahl

```
Welche Daten?
    │
    ├── Kontinuierlich (Messwerte)
    │   │
    │   ├── 1 Gruppe vs. Sollwert
    │   │   └── 1-Sample t-Test
    │   │
    │   ├── 2 unabhängige Gruppen
    │   │   └── 2-Sample t-Test
    │   │
    │   ├── 2 verbundene Gruppen (vorher/nachher)
    │   │   └── Paired t-Test
    │   │
    │   └── >2 Gruppen
    │       └── One-Way ANOVA
    │
    └── Diskret/Attributiv (Zähldaten)
        │
        ├── 1 Anteil vs. Sollwert
        │   └── 1-Proportion Test
        │
        ├── 2 Anteile vergleichen
        │   └── 2-Proportion Test
        │
        └── Häufigkeiten vs. Erwartung
            └── Chi²-Test
```

### 1-Sample t-Test

**Hypothesen:**
- H₀: μ = μ₀ (Mittelwert = Zielwert)
- H₁: μ ≠ μ₀ (zweiseitig) oder μ > μ₀ / μ < μ₀ (einseitig)

**Voraussetzungen:**
- Daten normalverteilt (oder n > 30)
- Unabhängige Beobachtungen

**Beispiel:**
"Ist die mittlere Durchlaufzeit signifikant anders als der Zielwert von 2 Tagen?"

### 2-Sample t-Test

**Hypothesen:**
- H₀: μ₁ = μ₂ (Mittelwerte gleich)
- H₁: μ₁ ≠ μ₂

**Voraussetzungen:**
- Beide Gruppen normalverteilt
- Varianzen gleich (oder Welch-t-Test verwenden)
- Unabhängige Stichproben

**Beispiel:**
"Gibt es einen signifikanten Unterschied in der Fehlerquote zwischen Schicht A und Schicht B?"

### Paired t-Test

**Hypothesen:**
- H₀: μd = 0 (Mittlere Differenz = 0)
- H₁: μd ≠ 0

**Voraussetzungen:**
- Differenzen normalverteilt
- Gepaarte Beobachtungen (vorher/nachher am gleichen Objekt)

**Beispiel:**
"Hat die Schulung die Bearbeitungszeit signifikant verändert? (Messung vor und nach Schulung bei denselben Mitarbeitern)"

### One-Way ANOVA

**Hypothesen:**
- H₀: μ₁ = μ₂ = ... = μk (alle Mittelwerte gleich)
- H₁: Mindestens ein Mittelwert unterscheidet sich

**Voraussetzungen:**
- Normalverteilung in allen Gruppen
- Varianzhomogenität (Levene-Test)
- Unabhängige Stichproben

**Beispiel:**
"Gibt es signifikante Unterschiede in der Zykluszeit zwischen den 4 Produktionslinien?"

**Post-hoc Tests:**
Bei signifikantem ANOVA-Ergebnis: Tukey HSD oder Bonferroni für paarweise Vergleiche.

### Chi²-Test

**Hypothesen:**
- H₀: Beobachtete = Erwartete Häufigkeiten
- H₁: Signifikante Abweichung

**Voraussetzungen:**
- Erwartete Häufigkeiten ≥ 5 pro Zelle
- Unabhängige Beobachtungen

**Beispiel:**
"Ist die Fehlerverteilung nach Fehlerart (A, B, C) zufällig oder gibt es signifikante Häufungen?"

## Korrelation und Regression

### Korrelation

**Pearson-Korrelation (r):**
- Misst linearen Zusammenhang
- Wertebereich: -1 bis +1

| r-Wert | Interpretation |
|--------|----------------|
| 0,0 - 0,3 | Schwach |
| 0,3 - 0,5 | Moderat |
| 0,5 - 0,7 | Stark |
| 0,7 - 1,0 | Sehr stark |

**Achtung:** Korrelation ≠ Kausalität!

**Beispiel:**
"Gibt es einen Zusammenhang zwischen Maschinenalter und Fehlerquote?"

### Lineare Regression

**Modell:** y = β₀ + β₁x + ε

| Kennzahl | Interpretation |
|----------|----------------|
| **R²** | Anteil erklärter Varianz (0-1) |
| **p-Wert (Steigung)** | Ist β₁ signifikant von 0 verschieden? |
| **Konfidenzintervall** | Unsicherheitsbereich für Vorhersage |

**Residuenanalyse:**
- Normalverteilt (Histogramm, Q-Q-Plot)
- Homoskedastisch (konstante Streuung)
- Unabhängig (keine Muster)

**Beispiel:**
"Wie stark beeinflusst die Temperatur die Ausschussrate? (Vorhersagemodell)"

## Kontrollkarten (SPC)

### X̄/R-Karte

**Anwendung:** Kontinuierliche Daten, Subgruppen (n = 2-10)

**Berechnung:**
- X̄̄ = Mittelwert aller Subgruppen-Mittelwerte
- R̄ = Mittelwert aller Spannweiten

**Kontrollgrenzen X̄-Karte:**
- UCL = X̄̄ + A₂ × R̄
- LCL = X̄̄ - A₂ × R̄

**Kontrollgrenzen R-Karte:**
- UCL = D₄ × R̄
- LCL = D₃ × R̄

### I-MR-Karte

**Anwendung:** Einzelwerte (n = 1), z.B. tägliche Kennzahlen

**Berechnung:**
- MR = |x_i - x_{i-1}| (Moving Range)
- MR̄ = Mittelwert der Moving Ranges

**Kontrollgrenzen I-Karte:**
- UCL = X̄ + 2,66 × MR̄
- LCL = X̄ - 2,66 × MR̄

### p-Karte

**Anwendung:** Anteil fehlerhafter Einheiten, variable Stichprobengröße

**Berechnung:**
- p̄ = Gesamt-Fehleranzahl / Gesamt-Stichprobe

**Kontrollgrenzen:**
- UCL = p̄ + 3 × √(p̄(1-p̄)/n)
- LCL = p̄ - 3 × √(p̄(1-p̄)/n)

(LCL = 0 wenn negativ berechnet)

### Interpretation

**In Control:** Alle Punkte innerhalb der Grenzen, keine Muster
**Out of Control:** Punkt außerhalb oder Muster erkannt

**Muster erkennen:**
- 1 Punkt > 3σ: Ausreißer, Sonderursache
- 7+ Punkte auf einer Seite: Shift
- 7+ Punkte steigend/fallend: Trend
- 14+ Punkte alternierend: Überreaktion

## Praktische Tipps

### Stichprobengröße

| Analyse | Minimum | Empfohlen |
|---------|---------|-----------|
| Deskriptive Statistik | 10 | 30+ |
| Prozessfähigkeit | 30 | 50-100 |
| t-Test | 15/Gruppe | 30/Gruppe |
| ANOVA | 15/Gruppe | 20/Gruppe |
| Regression | 30 | 10 pro Prädiktor |
| Kontrollkarte | 20 Subgruppen | 25+ Subgruppen |

### Häufige Fehler

| Fehler | Vermeidung |
|--------|------------|
| Normalverteilung nicht geprüft | Immer Verteilungstest vor Analyse |
| Ausreißer nicht behandelt | Box-Plot prüfen, entscheiden ob entfernen |
| Kleine Stichprobe überinterpretiert | Konfidenzintervalle beachten |
| Korrelation als Kausalität | Prozesswissen einbeziehen |
| p < 0,05 als einziges Kriterium | Auch Effektgröße betrachten |
