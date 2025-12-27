# Adaptives Assessment – Fragenkatalog

Dieses Assessment ermittelt den Projektkontext und die fehlenden Informationen. Stelle nur Fragen, deren Antworten nicht bereits aus dem Kontext ersichtlich sind.

## Kontexterkennungs-Schema

Analysiere die Eingabe des Nutzers auf folgende Informationen:

| Dimension | Erkennungsmuster | Falls unklar → Frage |
|-----------|------------------|----------------------|
| **Branche** | IT, Software, Produktion, Verwaltung, Dienstleistung, Gesundheit | "In welcher Branche/welchem Bereich arbeitet ihr?" |
| **Problemtyp** | Qualität, Durchlaufzeit, Kosten, Fehlerquote, Compliance, Kundenzufriedenheit | "Was ist das Kernproblem – geht es um Qualität, Zeit, Kosten oder etwas anderes?" |
| **Scope** | Einzelprozess, Abteilung, Bereichsübergreifend, Unternehmensweit | "Wie groß ist der Scope – ein einzelner Prozess oder bereichsübergreifend?" |
| **Dringlichkeit** | Akut, Mittelfristig, Strategisch | "Wie dringend ist das Projekt – gibt es einen Zeitdruck?" |
| **Datenlage** | Daten vorhanden, Teilweise, Keine Daten | "Habt ihr bereits Daten zum Problem gesammelt?" |
| **Stakeholder** | Intern, Extern, Gemischt, Behörde | "Wer sind die wichtigsten Stakeholder?" |

## Projektkomplexitäts-Klassifizierung

Nach dem Assessment klassifiziere das Projekt:

### Quick Win (1-4 Wochen)
- Einzelner, klar abgegrenzter Prozess
- Problem und Ursache weitgehend bekannt
- Wenige Stakeholder
- Daten verfügbar
- → **Empfehlung:** Lean-Fokus, schlankes DMAIC

### Standard-Projekt (1-3 Monate)
- Definierter Prozess mit mehreren Schritten
- Ursache vermutet, aber nicht validiert
- Mehrere Stakeholder, eine Abteilung
- Daten teilweise vorhanden
- → **Empfehlung:** Volles DMAIC mit Statistik

### Transformation (3-12 Monate)
- Bereichsübergreifender Prozess
- Komplexe, unklare Ursachen
- Viele Stakeholder, politische Dimension
- Daten müssen erst erhoben werden
- → **Empfehlung:** Volles DMAIC + starkes PM-Framework

## PM-Framework Entscheidungslogik

Basierend auf dem Assessment empfehle das passende Framework:

### → PRINCE2 empfohlen wenn:
- Feste Budgets und Zeitrahmen existieren
- Klare Governance-Strukturen erforderlich (z.B. Behörden)
- Stakeholder erwarten formale Phasenübergänge (Tollgates)
- Projektumfang zu Beginn gut definierbar
- Externe Auftraggeber oder Compliance-Anforderungen
- Dokumentationspflichten bestehen

### → Scrum empfohlen wenn:
- Anforderungen sich während des Projekts ändern können
- Schnelle, iterative Verbesserungen möglich
- Cross-funktionales Team verfügbar
- Stakeholder regelmäßig eingebunden werden können
- IT/Software-Projekte oder agile Unternehmenskultur
- Experimentieren und Lernen im Fokus

### → Hybrid (PRINCE2 + Scrum) empfohlen wenn:
- Governance-Anforderungen UND Flexibilität benötigt
- Große Transformation mit iterativen Arbeitspaketen
- Formale Meilensteine, aber agile Umsetzung
- Mischung aus stabilen und dynamischen Projektteilen

## Standardisierte Einstiegsfragen

Falls aus dem Kontext wenig erkennbar ist, nutze diese Einstiegsfragen (max. 3-4 auf einmal):

**Block 1 – Problem verstehen:**
1. Was ist das konkrete Problem, das ihr lösen wollt?
2. Wie äußert sich das Problem? (Symptome, Auswirkungen)
3. Seit wann besteht das Problem?

**Block 2 – Kontext verstehen:**
4. Wer ist vom Problem betroffen? (Kunden, Mitarbeiter, Prozesse)
5. Wurde bereits versucht, das Problem zu lösen? Mit welchem Ergebnis?
6. Gibt es bereits Daten oder Messungen zum Problem?

**Block 3 – Ziele und Rahmenbedingungen:**
7. Was wäre das ideale Ergebnis des Projekts?
8. Welche Ressourcen (Zeit, Budget, Team) stehen zur Verfügung?
9. Gibt es Einschränkungen oder No-Gos?

## Ausgabe nach Assessment

Nach Abschluss des Assessments fasse zusammen:

```
## Projekt-Assessment Zusammenfassung

**Branche:** [X]
**Problemtyp:** [X]
**Scope:** [X]
**Komplexität:** [Quick Win / Standard / Transformation]
**Datenlage:** [X]

**Empfohlenes PM-Framework:** [PRINCE2 / Scrum / Hybrid]
**Begründung:** [2-3 Sätze]

**Nächster Schritt:** Starte mit der Define-Phase...
```
