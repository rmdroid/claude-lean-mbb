#!/usr/bin/env python3
"""
Lean Six Sigma - Statistische Analyse
Prozessfähigkeit, Hypothesentests, Deskriptive Statistik
"""

import numpy as np
from scipy import stats
from typing import Tuple, Dict, List, Optional
import warnings

warnings.filterwarnings('ignore')


def deskriptive_statistik(daten: List[float]) -> Dict[str, float]:
    """
    Berechnet deskriptive Statistiken für einen Datensatz.
    
    Args:
        daten: Liste von Messwerten
    
    Returns:
        Dictionary mit allen wichtigen Kennzahlen
    """
    arr = np.array(daten)
    n = len(arr)
    
    return {
        'n': n,
        'mittelwert': np.mean(arr),
        'median': np.median(arr),
        'standardabweichung': np.std(arr, ddof=1),
        'varianz': np.var(arr, ddof=1),
        'minimum': np.min(arr),
        'maximum': np.max(arr),
        'spannweite': np.max(arr) - np.min(arr),
        'q1': np.percentile(arr, 25),
        'q3': np.percentile(arr, 75),
        'iqr': np.percentile(arr, 75) - np.percentile(arr, 25),
        'schiefe': stats.skew(arr),
        'kurtosis': stats.kurtosis(arr),
        'standardfehler': np.std(arr, ddof=1) / np.sqrt(n)
    }


def prozessfaehigkeit(daten: List[float], 
                       usl: float, 
                       lsl: float,
                       zielwert: Optional[float] = None) -> Dict[str, float]:
    """
    Berechnet Prozessfähigkeitsindizes Cp, Cpk, Pp, Ppk.
    
    Args:
        daten: Liste von Messwerten
        usl: Upper Specification Limit
        lsl: Lower Specification Limit
        zielwert: Optional, Zielwert für Cpm
    
    Returns:
        Dictionary mit Fähigkeitsindizes und Interpretation
    """
    arr = np.array(daten)
    n = len(arr)
    mittelwert = np.mean(arr)
    std_gesamt = np.std(arr, ddof=1)  # Overall standard deviation
    
    # Für Cp/Cpk: Within-Standardabweichung (aus Moving Range)
    mr = np.abs(np.diff(arr))
    mr_bar = np.mean(mr)
    std_within = mr_bar / 1.128  # d2 für n=2
    
    # Prozessfähigkeit (kurzzeit, within)
    cp = (usl - lsl) / (6 * std_within)
    cpu = (usl - mittelwert) / (3 * std_within)
    cpl = (mittelwert - lsl) / (3 * std_within)
    cpk = min(cpu, cpl)
    
    # Prozess-Performance (langzeit, overall)
    pp = (usl - lsl) / (6 * std_gesamt)
    ppu = (usl - mittelwert) / (3 * std_gesamt)
    ppl = (mittelwert - lsl) / (3 * std_gesamt)
    ppk = min(ppu, ppl)
    
    # Sigma-Level (aus Cpk)
    sigma_level = 3 * cpk
    
    # DPMO (Defects per Million Opportunities)
    z_upper = (usl - mittelwert) / std_gesamt
    z_lower = (mittelwert - lsl) / std_gesamt
    dpmo = (stats.norm.cdf(-z_lower) + (1 - stats.norm.cdf(z_upper))) * 1_000_000
    
    # Yield
    yield_pct = (1 - dpmo / 1_000_000) * 100
    
    # Interpretation
    if cpk >= 1.67:
        bewertung = "Exzellent (≥5σ)"
    elif cpk >= 1.33:
        bewertung = "Gut (≥4σ)"
    elif cpk >= 1.00:
        bewertung = "Akzeptabel (≥3σ)"
    elif cpk >= 0.67:
        bewertung = "Schlecht (≥2σ)"
    else:
        bewertung = "Nicht fähig (<2σ)"
    
    ergebnis = {
        'n': n,
        'mittelwert': mittelwert,
        'std_within': std_within,
        'std_overall': std_gesamt,
        'usl': usl,
        'lsl': lsl,
        'cp': cp,
        'cpk': cpk,
        'cpu': cpu,
        'cpl': cpl,
        'pp': pp,
        'ppk': ppk,
        'sigma_level': sigma_level,
        'dpmo': dpmo,
        'yield_prozent': yield_pct,
        'bewertung': bewertung
    }
    
    return ergebnis


def normalverteilungstest(daten: List[float], alpha: float = 0.05) -> Dict:
    """
    Testet auf Normalverteilung mit mehreren Methoden.
    
    Args:
        daten: Liste von Messwerten
        alpha: Signifikanzniveau (default 0.05)
    
    Returns:
        Dictionary mit Testergebnissen
    """
    arr = np.array(daten)
    
    # Shapiro-Wilk Test (für n < 5000)
    if len(arr) < 5000:
        shapiro_stat, shapiro_p = stats.shapiro(arr)
    else:
        shapiro_stat, shapiro_p = None, None
    
    # Anderson-Darling Test
    anderson = stats.anderson(arr, dist='norm')
    
    # Kolmogorov-Smirnov Test
    ks_stat, ks_p = stats.kstest(arr, 'norm', args=(np.mean(arr), np.std(arr)))
    
    # Entscheidung basierend auf Shapiro-Wilk (wenn verfügbar) oder KS
    if shapiro_p is not None:
        ist_normalverteilt = shapiro_p > alpha
        entscheidungs_p = shapiro_p
    else:
        ist_normalverteilt = ks_p > alpha
        entscheidungs_p = ks_p
    
    return {
        'shapiro_wilk_statistik': shapiro_stat,
        'shapiro_wilk_p': shapiro_p,
        'anderson_darling_statistik': anderson.statistic,
        'anderson_darling_kritische_werte': dict(zip(anderson.significance_level, anderson.critical_values)),
        'kolmogorov_smirnov_statistik': ks_stat,
        'kolmogorov_smirnov_p': ks_p,
        'alpha': alpha,
        'ist_normalverteilt': ist_normalverteilt,
        'interpretation': f"Die Daten sind {'normalverteilt' if ist_normalverteilt else 'NICHT normalverteilt'} (p={entscheidungs_p:.4f}, α={alpha})"
    }


def t_test_1_sample(daten: List[float], 
                     zielwert: float, 
                     alpha: float = 0.05,
                     alternativ: str = 'zweiseitig') -> Dict:
    """
    1-Sample t-Test: Vergleich Mittelwert gegen Zielwert.
    
    Args:
        daten: Liste von Messwerten
        zielwert: Zu testender Zielwert
        alpha: Signifikanzniveau
        alternativ: 'zweiseitig', 'groesser', 'kleiner'
    
    Returns:
        Dictionary mit Testergebnissen
    """
    arr = np.array(daten)
    
    alt_map = {'zweiseitig': 'two-sided', 'groesser': 'greater', 'kleiner': 'less'}
    alternative = alt_map.get(alternativ, 'two-sided')
    
    stat, p = stats.ttest_1samp(arr, zielwert, alternative=alternative)
    
    mittelwert = np.mean(arr)
    std = np.std(arr, ddof=1)
    n = len(arr)
    se = std / np.sqrt(n)
    
    # Konfidenzintervall
    t_krit = stats.t.ppf(1 - alpha/2, df=n-1)
    ki_unten = mittelwert - t_krit * se
    ki_oben = mittelwert + t_krit * se
    
    # Effektgröße (Cohen's d)
    cohens_d = (mittelwert - zielwert) / std
    
    signifikant = p < alpha
    
    return {
        'n': n,
        'mittelwert': mittelwert,
        'standardabweichung': std,
        'standardfehler': se,
        'zielwert': zielwert,
        'differenz': mittelwert - zielwert,
        't_statistik': stat,
        'p_wert': p,
        'alpha': alpha,
        'freiheitsgrade': n - 1,
        'ki_95_unten': ki_unten,
        'ki_95_oben': ki_oben,
        'cohens_d': cohens_d,
        'signifikant': signifikant,
        'interpretation': f"Der Mittelwert ({mittelwert:.4f}) ist {'signifikant unterschiedlich' if signifikant else 'nicht signifikant unterschiedlich'} vom Zielwert ({zielwert}) (p={p:.4f})"
    }


def t_test_2_sample(gruppe1: List[float], 
                     gruppe2: List[float],
                     alpha: float = 0.05,
                     gepaart: bool = False) -> Dict:
    """
    2-Sample t-Test: Vergleich zweier Gruppen.
    
    Args:
        gruppe1: Messwerte Gruppe 1
        gruppe2: Messwerte Gruppe 2
        alpha: Signifikanzniveau
        gepaart: True für gepaarten Test (vorher/nachher)
    
    Returns:
        Dictionary mit Testergebnissen
    """
    arr1 = np.array(gruppe1)
    arr2 = np.array(gruppe2)
    
    if gepaart:
        stat, p = stats.ttest_rel(arr1, arr2)
        test_name = "Gepaarter t-Test"
    else:
        # Levene-Test für Varianzhomogenität
        levene_stat, levene_p = stats.levene(arr1, arr2)
        gleiche_varianz = levene_p > 0.05
        stat, p = stats.ttest_ind(arr1, arr2, equal_var=gleiche_varianz)
        test_name = "2-Sample t-Test" + (" (Welch)" if not gleiche_varianz else "")
    
    n1, n2 = len(arr1), len(arr2)
    m1, m2 = np.mean(arr1), np.mean(arr2)
    s1, s2 = np.std(arr1, ddof=1), np.std(arr2, ddof=1)
    
    # Pooled standard deviation für Cohen's d
    s_pooled = np.sqrt(((n1-1)*s1**2 + (n2-1)*s2**2) / (n1+n2-2))
    cohens_d = (m1 - m2) / s_pooled
    
    signifikant = p < alpha
    
    ergebnis = {
        'test': test_name,
        'n_gruppe1': n1,
        'n_gruppe2': n2,
        'mittelwert_gruppe1': m1,
        'mittelwert_gruppe2': m2,
        'std_gruppe1': s1,
        'std_gruppe2': s2,
        'differenz': m1 - m2,
        't_statistik': stat,
        'p_wert': p,
        'alpha': alpha,
        'cohens_d': cohens_d,
        'signifikant': signifikant,
        'interpretation': f"Die Mittelwerte sind {'signifikant unterschiedlich' if signifikant else 'nicht signifikant unterschiedlich'} (p={p:.4f}, d={cohens_d:.2f})"
    }
    
    if not gepaart:
        ergebnis['levene_p'] = levene_p
        ergebnis['gleiche_varianz'] = gleiche_varianz
    
    return ergebnis


def anova_oneway(gruppen: List[List[float]], 
                  gruppen_namen: Optional[List[str]] = None,
                  alpha: float = 0.05) -> Dict:
    """
    One-Way ANOVA: Vergleich von mehr als 2 Gruppen.
    
    Args:
        gruppen: Liste von Listen mit Messwerten pro Gruppe
        gruppen_namen: Optional, Namen der Gruppen
        alpha: Signifikanzniveau
    
    Returns:
        Dictionary mit Testergebnissen
    """
    arrays = [np.array(g) for g in gruppen]
    k = len(gruppen)
    
    if gruppen_namen is None:
        gruppen_namen = [f"Gruppe {i+1}" for i in range(k)]
    
    # ANOVA
    f_stat, p = stats.f_oneway(*arrays)
    
    # Deskriptive Statistik pro Gruppe
    gruppe_stats = []
    for i, (arr, name) in enumerate(zip(arrays, gruppen_namen)):
        gruppe_stats.append({
            'name': name,
            'n': len(arr),
            'mittelwert': np.mean(arr),
            'std': np.std(arr, ddof=1)
        })
    
    # Levene-Test
    levene_stat, levene_p = stats.levene(*arrays)
    
    # Effektgröße (Eta-squared)
    all_data = np.concatenate(arrays)
    grand_mean = np.mean(all_data)
    ss_between = sum(len(arr) * (np.mean(arr) - grand_mean)**2 for arr in arrays)
    ss_total = sum((x - grand_mean)**2 for x in all_data)
    eta_squared = ss_between / ss_total
    
    signifikant = p < alpha
    
    ergebnis = {
        'anzahl_gruppen': k,
        'gruppen': gruppe_stats,
        'f_statistik': f_stat,
        'p_wert': p,
        'alpha': alpha,
        'eta_squared': eta_squared,
        'levene_statistik': levene_stat,
        'levene_p': levene_p,
        'varianzhomogenitaet': levene_p > 0.05,
        'signifikant': signifikant,
        'interpretation': f"Es {'gibt' if signifikant else 'gibt keine'} signifikante Unterschiede zwischen den Gruppen (F={f_stat:.2f}, p={p:.4f})"
    }
    
    # Tukey HSD Post-hoc Test wenn signifikant
    if signifikant:
        from scipy.stats import tukey_hsd
        try:
            tukey = tukey_hsd(*arrays)
            paarvergleiche = []
            for i in range(k):
                for j in range(i+1, k):
                    paarvergleiche.append({
                        'vergleich': f"{gruppen_namen[i]} vs {gruppen_namen[j]}",
                        'p_wert': tukey.pvalue[i, j],
                        'signifikant': tukey.pvalue[i, j] < alpha
                    })
            ergebnis['post_hoc_tukey'] = paarvergleiche
        except:
            pass
    
    return ergebnis


def chi_quadrat_test(beobachtet: List[int], 
                      erwartet: Optional[List[float]] = None,
                      alpha: float = 0.05) -> Dict:
    """
    Chi-Quadrat-Anpassungstest.
    
    Args:
        beobachtet: Liste der beobachteten Häufigkeiten
        erwartet: Optional, Liste der erwarteten Häufigkeiten (default: Gleichverteilung)
        alpha: Signifikanzniveau
    
    Returns:
        Dictionary mit Testergebnissen
    """
    obs = np.array(beobachtet)
    n = np.sum(obs)
    k = len(obs)
    
    if erwartet is None:
        exp = np.full(k, n / k)
    else:
        exp = np.array(erwartet)
    
    chi2_stat, p = stats.chisquare(obs, f_exp=exp)
    
    signifikant = p < alpha
    
    # Residuen
    residuen = (obs - exp) / np.sqrt(exp)
    
    return {
        'beobachtet': obs.tolist(),
        'erwartet': exp.tolist(),
        'residuen': residuen.tolist(),
        'chi_quadrat': chi2_stat,
        'freiheitsgrade': k - 1,
        'p_wert': p,
        'alpha': alpha,
        'signifikant': signifikant,
        'interpretation': f"Die Verteilung ist {'signifikant unterschiedlich' if signifikant else 'nicht signifikant unterschiedlich'} von der Erwartung (χ²={chi2_stat:.2f}, p={p:.4f})"
    }


def korrelation(x: List[float], y: List[float], alpha: float = 0.05) -> Dict:
    """
    Berechnet Pearson-Korrelation und testet auf Signifikanz.
    
    Args:
        x: Liste von x-Werten
        y: Liste von y-Werten
        alpha: Signifikanzniveau
    
    Returns:
        Dictionary mit Korrelationsanalyse
    """
    arr_x = np.array(x)
    arr_y = np.array(y)
    
    # Pearson-Korrelation
    r, p = stats.pearsonr(arr_x, arr_y)
    
    # Spearman-Korrelation (nicht-parametrisch)
    rho, rho_p = stats.spearmanr(arr_x, arr_y)
    
    # Interpretation
    r_abs = abs(r)
    if r_abs < 0.3:
        staerke = "schwach"
    elif r_abs < 0.5:
        staerke = "moderat"
    elif r_abs < 0.7:
        staerke = "stark"
    else:
        staerke = "sehr stark"
    
    richtung = "positiv" if r > 0 else "negativ"
    
    signifikant = p < alpha
    
    return {
        'n': len(arr_x),
        'pearson_r': r,
        'pearson_p': p,
        'spearman_rho': rho,
        'spearman_p': rho_p,
        'r_quadrat': r**2,
        'alpha': alpha,
        'signifikant': signifikant,
        'staerke': staerke,
        'richtung': richtung,
        'interpretation': f"Es besteht eine {staerke}e {richtung}e Korrelation (r={r:.3f}, p={p:.4f})"
    }


def lineare_regression(x: List[float], y: List[float]) -> Dict:
    """
    Einfache lineare Regression.
    
    Args:
        x: Liste von x-Werten (Prädiktor)
        y: Liste von y-Werten (Zielvariable)
    
    Returns:
        Dictionary mit Regressionsergebnissen
    """
    arr_x = np.array(x)
    arr_y = np.array(y)
    n = len(arr_x)
    
    # Regression
    slope, intercept, r, p, se = stats.linregress(arr_x, arr_y)
    
    # Vorhersagewerte und Residuen
    y_pred = intercept + slope * arr_x
    residuen = arr_y - y_pred
    
    # R-squared
    r_squared = r**2
    
    # Adjusted R-squared
    r_squared_adj = 1 - (1 - r_squared) * (n - 1) / (n - 2)
    
    # RMSE
    rmse = np.sqrt(np.mean(residuen**2))
    
    return {
        'n': n,
        'steigung': slope,
        'achsenabschnitt': intercept,
        'gleichung': f"y = {intercept:.4f} + {slope:.4f} * x",
        'r': r,
        'r_quadrat': r_squared,
        'r_quadrat_adj': r_squared_adj,
        'standardfehler_steigung': se,
        'p_wert': p,
        'rmse': rmse,
        'residuen_mean': np.mean(residuen),
        'residuen_std': np.std(residuen),
        'interpretation': f"Das Modell erklärt {r_squared*100:.1f}% der Varianz (R²={r_squared:.3f}, p={p:.4f})"
    }


def bericht_ausgeben(ergebnis: Dict, titel: str = "Ergebnis") -> str:
    """
    Formatiert ein Ergebnis-Dictionary als lesbaren Bericht.
    """
    lines = [f"\n{'='*60}", f"{titel}", f"{'='*60}"]
    
    for key, value in ergebnis.items():
        if isinstance(value, float):
            lines.append(f"{key}: {value:.4f}")
        elif isinstance(value, list) and len(value) > 0 and isinstance(value[0], dict):
            lines.append(f"\n{key}:")
            for item in value:
                lines.append(f"  {item}")
        else:
            lines.append(f"{key}: {value}")
    
    lines.append(f"{'='*60}\n")
    return '\n'.join(lines)


# Beispiel-Nutzung
if __name__ == "__main__":
    # Beispieldaten
    daten = [10.2, 10.5, 9.8, 10.1, 10.3, 10.0, 9.9, 10.4, 10.1, 10.2,
             10.3, 9.7, 10.5, 10.2, 10.0, 10.1, 10.4, 9.9, 10.3, 10.1]
    
    print("=== Deskriptive Statistik ===")
    desc = deskriptive_statistik(daten)
    for k, v in desc.items():
        print(f"{k}: {v:.4f}" if isinstance(v, float) else f"{k}: {v}")
    
    print("\n=== Prozessfähigkeit ===")
    pf = prozessfaehigkeit(daten, usl=10.8, lsl=9.2)
    for k, v in pf.items():
        print(f"{k}: {v:.4f}" if isinstance(v, float) else f"{k}: {v}")
    
    print("\n=== Normalverteilungstest ===")
    nv = normalverteilungstest(daten)
    print(nv['interpretation'])
    
    print("\n=== 1-Sample t-Test ===")
    t1 = t_test_1_sample(daten, zielwert=10.0)
    print(t1['interpretation'])
