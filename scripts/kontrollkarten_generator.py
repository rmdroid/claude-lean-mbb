#!/usr/bin/env python3
"""
Lean Six Sigma - Kontrollkarten Generator
X-bar/R, I-MR, p-Chart, c-Chart
"""

import numpy as np
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass


# Kontrollkarten-Konstanten
CONTROL_CHART_CONSTANTS = {
    2: {'A2': 1.880, 'D3': 0, 'D4': 3.267, 'd2': 1.128},
    3: {'A2': 1.023, 'D3': 0, 'D4': 2.574, 'd2': 1.693},
    4: {'A2': 0.729, 'D3': 0, 'D4': 2.282, 'd2': 2.059},
    5: {'A2': 0.577, 'D3': 0, 'D4': 2.114, 'd2': 2.326},
    6: {'A2': 0.483, 'D3': 0, 'D4': 2.004, 'd2': 2.534},
    7: {'A2': 0.419, 'D3': 0.076, 'D4': 1.924, 'd2': 2.704},
    8: {'A2': 0.373, 'D3': 0.136, 'D4': 1.864, 'd2': 2.847},
    9: {'A2': 0.337, 'D3': 0.184, 'D4': 1.816, 'd2': 2.970},
    10: {'A2': 0.308, 'D3': 0.223, 'D4': 1.777, 'd2': 3.078},
}


@dataclass
class KontrollkarteErgebnis:
    """Ergebnis einer Kontrollkarten-Analyse."""
    typ: str
    daten: List[float]
    cl: float
    ucl: float
    lcl: float
    ooc_punkte: List[int]  # Out of Control Punkte (Index)
    regeln_verletzt: Dict[str, List[int]]
    
    def ist_in_kontrolle(self) -> bool:
        return len(self.ooc_punkte) == 0
    
    def zusammenfassung(self) -> str:
        if self.ist_in_kontrolle():
            return f"Prozess ist IN KONTROLLE (CL={self.cl:.4f}, UCL={self.ucl:.4f}, LCL={self.lcl:.4f})"
        else:
            return f"Prozess ist OUT OF CONTROL! {len(self.ooc_punkte)} Punkte außerhalb der Grenzen. Indizes: {self.ooc_punkte}"


def western_electric_rules(daten: List[float], cl: float, ucl: float, lcl: float) -> Dict[str, List[int]]:
    """
    Prüft Western Electric Rules für Out-of-Control-Signale.
    
    Returns:
        Dictionary mit Regelverletzungen und betroffenen Indizes
    """
    arr = np.array(daten)
    n = len(arr)
    sigma = (ucl - cl) / 3
    
    verletzungen = {}
    
    # Regel 1: 1 Punkt außerhalb 3σ
    regel1 = [i for i in range(n) if arr[i] > ucl or arr[i] < lcl]
    if regel1:
        verletzungen['Regel 1 (außerhalb 3σ)'] = regel1
    
    # Regel 2: 9 aufeinanderfolgende Punkte auf einer Seite der CL
    regel2 = []
    for i in range(n - 8):
        fenster = arr[i:i+9]
        if all(x > cl for x in fenster) or all(x < cl for x in fenster):
            regel2.extend(range(i, i+9))
    regel2 = list(set(regel2))
    if regel2:
        verletzungen['Regel 2 (9 Punkte auf einer Seite)'] = regel2
    
    # Regel 3: 6 aufeinanderfolgende steigende oder fallende Punkte
    regel3 = []
    for i in range(n - 5):
        fenster = arr[i:i+6]
        steigend = all(fenster[j] < fenster[j+1] for j in range(5))
        fallend = all(fenster[j] > fenster[j+1] for j in range(5))
        if steigend or fallend:
            regel3.extend(range(i, i+6))
    regel3 = list(set(regel3))
    if regel3:
        verletzungen['Regel 3 (6 Punkte Trend)'] = regel3
    
    # Regel 4: 14 aufeinanderfolgende alternierende Punkte
    regel4 = []
    for i in range(n - 13):
        fenster = arr[i:i+14]
        alternierend = True
        for j in range(13):
            if j % 2 == 0 and fenster[j] >= fenster[j+1]:
                alternierend = False
                break
            if j % 2 == 1 and fenster[j] <= fenster[j+1]:
                alternierend = False
                break
        if alternierend:
            regel4.extend(range(i, i+14))
    regel4 = list(set(regel4))
    if regel4:
        verletzungen['Regel 4 (14 alternierende Punkte)'] = regel4
    
    # Regel 5: 2 von 3 Punkten außerhalb 2σ
    sigma2_upper = cl + 2 * sigma
    sigma2_lower = cl - 2 * sigma
    regel5 = []
    for i in range(n - 2):
        fenster = arr[i:i+3]
        ausserhalb = sum(1 for x in fenster if x > sigma2_upper or x < sigma2_lower)
        if ausserhalb >= 2:
            regel5.extend(range(i, i+3))
    regel5 = list(set(regel5))
    if regel5:
        verletzungen['Regel 5 (2 von 3 außerhalb 2σ)'] = regel5
    
    # Regel 6: 4 von 5 Punkten außerhalb 1σ
    sigma1_upper = cl + sigma
    sigma1_lower = cl - sigma
    regel6 = []
    for i in range(n - 4):
        fenster = arr[i:i+5]
        ausserhalb = sum(1 for x in fenster if x > sigma1_upper or x < sigma1_lower)
        if ausserhalb >= 4:
            regel6.extend(range(i, i+5))
    regel6 = list(set(regel6))
    if regel6:
        verletzungen['Regel 6 (4 von 5 außerhalb 1σ)'] = regel6
    
    return verletzungen


def xbar_r_karte(subgruppen: List[List[float]]) -> Tuple[KontrollkarteErgebnis, KontrollkarteErgebnis]:
    """
    Erstellt X-bar und R Kontrollkarten.
    
    Args:
        subgruppen: Liste von Subgruppen (jede Subgruppe ist eine Liste von Messwerten)
    
    Returns:
        Tuple von (X-bar Ergebnis, R Ergebnis)
    """
    subgruppen_arr = [np.array(sg) for sg in subgruppen]
    n = len(subgruppen_arr[0])  # Subgruppen-Größe
    
    if n not in CONTROL_CHART_CONSTANTS:
        raise ValueError(f"Subgruppen-Größe {n} nicht unterstützt. Erlaubt: 2-10")
    
    constants = CONTROL_CHART_CONSTANTS[n]
    A2, D3, D4 = constants['A2'], constants['D3'], constants['D4']
    
    # Berechne Mittelwerte und Spannweiten
    xbars = [np.mean(sg) for sg in subgruppen_arr]
    ranges = [np.max(sg) - np.min(sg) for sg in subgruppen_arr]
    
    # Zentrallinien
    xbar_bar = np.mean(xbars)
    r_bar = np.mean(ranges)
    
    # Kontrollgrenzen X-bar
    xbar_ucl = xbar_bar + A2 * r_bar
    xbar_lcl = xbar_bar - A2 * r_bar
    
    # Kontrollgrenzen R
    r_ucl = D4 * r_bar
    r_lcl = D3 * r_bar
    
    # Out of Control Punkte
    xbar_ooc = [i for i, x in enumerate(xbars) if x > xbar_ucl or x < xbar_lcl]
    r_ooc = [i for i, r in enumerate(ranges) if r > r_ucl or r < r_lcl]
    
    # Western Electric Rules
    xbar_regeln = western_electric_rules(xbars, xbar_bar, xbar_ucl, xbar_lcl)
    r_regeln = western_electric_rules(ranges, r_bar, r_ucl, r_lcl)
    
    xbar_ergebnis = KontrollkarteErgebnis(
        typ="X-bar",
        daten=xbars,
        cl=xbar_bar,
        ucl=xbar_ucl,
        lcl=xbar_lcl,
        ooc_punkte=xbar_ooc,
        regeln_verletzt=xbar_regeln
    )
    
    r_ergebnis = KontrollkarteErgebnis(
        typ="R",
        daten=ranges,
        cl=r_bar,
        ucl=r_ucl,
        lcl=r_lcl,
        ooc_punkte=r_ooc,
        regeln_verletzt=r_regeln
    )
    
    return xbar_ergebnis, r_ergebnis


def i_mr_karte(einzelwerte: List[float]) -> Tuple[KontrollkarteErgebnis, KontrollkarteErgebnis]:
    """
    Erstellt I (Individual) und MR (Moving Range) Kontrollkarten.
    
    Args:
        einzelwerte: Liste von Einzelmesswerten
    
    Returns:
        Tuple von (I Ergebnis, MR Ergebnis)
    """
    arr = np.array(einzelwerte)
    
    # Moving Ranges
    mr = np.abs(np.diff(arr))
    
    # Zentrallinien
    x_bar = np.mean(arr)
    mr_bar = np.mean(mr)
    
    # Kontrollgrenzen I-Karte (E2 = 2.66 für n=2)
    i_ucl = x_bar + 2.66 * mr_bar
    i_lcl = x_bar - 2.66 * mr_bar
    
    # Kontrollgrenzen MR-Karte (D4 = 3.267 für n=2)
    mr_ucl = 3.267 * mr_bar
    mr_lcl = 0  # D3 = 0 für n=2
    
    # Out of Control
    i_ooc = [i for i, x in enumerate(arr) if x > i_ucl or x < i_lcl]
    mr_ooc = [i for i, m in enumerate(mr) if m > mr_ucl]
    
    # Western Electric Rules
    i_regeln = western_electric_rules(arr.tolist(), x_bar, i_ucl, i_lcl)
    mr_regeln = western_electric_rules(mr.tolist(), mr_bar, mr_ucl, mr_lcl)
    
    i_ergebnis = KontrollkarteErgebnis(
        typ="I (Individual)",
        daten=arr.tolist(),
        cl=x_bar,
        ucl=i_ucl,
        lcl=i_lcl,
        ooc_punkte=i_ooc,
        regeln_verletzt=i_regeln
    )
    
    mr_ergebnis = KontrollkarteErgebnis(
        typ="MR (Moving Range)",
        daten=mr.tolist(),
        cl=mr_bar,
        ucl=mr_ucl,
        lcl=mr_lcl,
        ooc_punkte=mr_ooc,
        regeln_verletzt=mr_regeln
    )
    
    return i_ergebnis, mr_ergebnis


def p_karte(fehlerhafte: List[int], stichproben: List[int]) -> KontrollkarteErgebnis:
    """
    Erstellt p-Kontrollkarte für Anteil fehlerhafter Einheiten.
    
    Args:
        fehlerhafte: Anzahl fehlerhafter Einheiten pro Stichprobe
        stichproben: Stichprobengröße pro Periode
    
    Returns:
        KontrollkarteErgebnis
    """
    np_arr = np.array(fehlerhafte)
    n_arr = np.array(stichproben)
    
    # Anteile
    p_arr = np_arr / n_arr
    
    # Durchschnittlicher Anteil
    p_bar = np.sum(np_arr) / np.sum(n_arr)
    
    # Variable Kontrollgrenzen (abhängig von Stichprobengröße)
    ucl_arr = p_bar + 3 * np.sqrt(p_bar * (1 - p_bar) / n_arr)
    lcl_arr = p_bar - 3 * np.sqrt(p_bar * (1 - p_bar) / n_arr)
    lcl_arr = np.maximum(lcl_arr, 0)  # LCL kann nicht negativ sein
    
    # Durchschnittliche Grenzen für Ausgabe
    n_avg = np.mean(n_arr)
    ucl_avg = p_bar + 3 * np.sqrt(p_bar * (1 - p_bar) / n_avg)
    lcl_avg = max(0, p_bar - 3 * np.sqrt(p_bar * (1 - p_bar) / n_avg))
    
    # Out of Control (mit variablen Grenzen)
    ooc = [i for i, (p, u, l) in enumerate(zip(p_arr, ucl_arr, lcl_arr)) if p > u or p < l]
    
    return KontrollkarteErgebnis(
        typ="p (Anteil fehlerhaft)",
        daten=p_arr.tolist(),
        cl=p_bar,
        ucl=ucl_avg,
        lcl=lcl_avg,
        ooc_punkte=ooc,
        regeln_verletzt=western_electric_rules(p_arr.tolist(), p_bar, ucl_avg, lcl_avg)
    )


def c_karte(fehler_anzahl: List[int]) -> KontrollkarteErgebnis:
    """
    Erstellt c-Kontrollkarte für Anzahl Fehler pro Einheit.
    
    Args:
        fehler_anzahl: Anzahl Fehler pro Prüfeinheit
    
    Returns:
        KontrollkarteErgebnis
    """
    c_arr = np.array(fehler_anzahl)
    
    # Durchschnitt
    c_bar = np.mean(c_arr)
    
    # Kontrollgrenzen
    ucl = c_bar + 3 * np.sqrt(c_bar)
    lcl = max(0, c_bar - 3 * np.sqrt(c_bar))
    
    # Out of Control
    ooc = [i for i, c in enumerate(c_arr) if c > ucl or c < lcl]
    
    return KontrollkarteErgebnis(
        typ="c (Fehleranzahl)",
        daten=c_arr.tolist(),
        cl=c_bar,
        ucl=ucl,
        lcl=lcl,
        ooc_punkte=ooc,
        regeln_verletzt=western_electric_rules(c_arr.tolist(), c_bar, ucl, lcl)
    )


def u_karte(fehler_anzahl: List[int], einheiten: List[int]) -> KontrollkarteErgebnis:
    """
    Erstellt u-Kontrollkarte für Fehler pro Einheit (variable Einheitengröße).
    
    Args:
        fehler_anzahl: Anzahl Fehler pro Periode
        einheiten: Anzahl geprüfter Einheiten pro Periode
    
    Returns:
        KontrollkarteErgebnis
    """
    c_arr = np.array(fehler_anzahl)
    n_arr = np.array(einheiten)
    
    # Fehler pro Einheit
    u_arr = c_arr / n_arr
    
    # Durchschnitt
    u_bar = np.sum(c_arr) / np.sum(n_arr)
    
    # Variable Kontrollgrenzen
    ucl_arr = u_bar + 3 * np.sqrt(u_bar / n_arr)
    lcl_arr = u_bar - 3 * np.sqrt(u_bar / n_arr)
    lcl_arr = np.maximum(lcl_arr, 0)
    
    # Durchschnittliche Grenzen
    n_avg = np.mean(n_arr)
    ucl_avg = u_bar + 3 * np.sqrt(u_bar / n_avg)
    lcl_avg = max(0, u_bar - 3 * np.sqrt(u_bar / n_avg))
    
    # Out of Control
    ooc = [i for i, (u, uc, lc) in enumerate(zip(u_arr, ucl_arr, lcl_arr)) if u > uc or u < lc]
    
    return KontrollkarteErgebnis(
        typ="u (Fehler pro Einheit)",
        daten=u_arr.tolist(),
        cl=u_bar,
        ucl=ucl_avg,
        lcl=lcl_avg,
        ooc_punkte=ooc,
        regeln_verletzt=western_electric_rules(u_arr.tolist(), u_bar, ucl_avg, lcl_avg)
    )


def kontrollkarte_bericht(ergebnis: KontrollkarteErgebnis) -> str:
    """Erstellt einen formatierten Bericht für eine Kontrollkarte."""
    lines = [
        f"\n{'='*60}",
        f"KONTROLLKARTE: {ergebnis.typ}",
        f"{'='*60}",
        f"Zentrallinie (CL):           {ergebnis.cl:.4f}",
        f"Obere Kontrollgrenze (UCL):  {ergebnis.ucl:.4f}",
        f"Untere Kontrollgrenze (LCL): {ergebnis.lcl:.4f}",
        f"Anzahl Datenpunkte:          {len(ergebnis.daten)}",
        "",
        f"STATUS: {'IN KONTROLLE ✓' if ergebnis.ist_in_kontrolle() else 'OUT OF CONTROL ✗'}",
    ]
    
    if ergebnis.ooc_punkte:
        lines.append(f"\nPunkte außerhalb der Grenzen: {ergebnis.ooc_punkte}")
    
    if ergebnis.regeln_verletzt:
        lines.append("\nVerletzte Regeln:")
        for regel, punkte in ergebnis.regeln_verletzt.items():
            lines.append(f"  - {regel}: Punkte {punkte}")
    
    lines.append(f"{'='*60}\n")
    return '\n'.join(lines)


# Beispiel-Nutzung
if __name__ == "__main__":
    # Beispiel: X-bar/R Karte
    print("=== X-bar/R Karte ===")
    subgruppen = [
        [10.2, 10.4, 10.1, 10.3],
        [10.0, 10.2, 10.1, 10.0],
        [10.3, 10.5, 10.2, 10.4],
        [10.1, 10.0, 10.2, 10.1],
        [10.4, 10.3, 10.5, 10.2],
        [10.2, 10.1, 10.3, 10.2],
        [10.0, 10.1, 10.0, 10.2],
        [10.3, 10.4, 10.2, 10.3],
        [10.1, 10.2, 10.1, 10.0],
        [10.2, 10.3, 10.1, 10.2],
    ]
    
    xbar_erg, r_erg = xbar_r_karte(subgruppen)
    print(kontrollkarte_bericht(xbar_erg))
    print(kontrollkarte_bericht(r_erg))
    
    # Beispiel: I-MR Karte
    print("\n=== I-MR Karte ===")
    einzelwerte = [10.2, 10.5, 10.1, 10.3, 10.0, 10.4, 10.2, 10.1, 10.3, 10.2,
                   10.0, 10.1, 10.4, 10.2, 10.3, 10.1, 10.2, 10.0, 10.3, 10.1]
    
    i_erg, mr_erg = i_mr_karte(einzelwerte)
    print(kontrollkarte_bericht(i_erg))
    print(kontrollkarte_bericht(mr_erg))
    
    # Beispiel: p-Karte
    print("\n=== p-Karte ===")
    fehlerhafte = [3, 5, 2, 4, 6, 3, 2, 4, 5, 3]
    stichproben = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
    
    p_erg = p_karte(fehlerhafte, stichproben)
    print(kontrollkarte_bericht(p_erg))
