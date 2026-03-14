"""
ZAI Oracle v3.0 — Main Launcher
by Zawwar (github.com/Zawwarsami16)

Usage:
  python3 zai_oracle.py                         # Full analysis
  python3 zai_oracle.py --replay gulf-war       # Crisis replay
  python3 zai_oracle.py --replay 2008-gfc
  python3 zai_oracle.py --replay ukraine-invasion
  python3 zai_oracle.py --replay covid-crash
  python3 zai_oracle.py --replay 1973-oil-shock
  python3 zai_oracle.py --replay dotcom-peak
  python3 zai_oracle.py --scenario oil=115,vix=36,war_headlines=30
  python3 zai_oracle.py --list-crises
"""

import os
import sys
import subprocess
import json
from datetime import datetime


def print_banner():
    os.system("cls" if os.name == "nt" else "clear")
    print("""
\033[92m
  ╔══════════════════════════════════════════════════════════╗
  ║                                                          ║
  ║      ███████╗ █████╗ ██╗      ██████╗ ██████╗ █████╗    ║
  ║      ╚══███╔╝██╔══██╗██║     ██╔═══██╗██╔══██╗██╔══██╗  ║
  ║        ███╔╝ ███████║██║     ██║   ██║██████╔╝███████║  ║
  ║       ███╔╝  ██╔══██║██║     ██║   ██║██╔══██╗██╔══██║  ║
  ║      ███████╗██║  ██║███████╗╚██████╔╝██║  ██║██║  ██║  ║
  ║      ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝  ║
  ║                                                          ║
  ║           O R A C L E  v 3 . 0                          ║
  ║      Geopolitical & Macro Intelligence Engine            ║
  ║      by Zawwar · github.com/Zawwarsami16                 ║
  ║                                                          ║
  ╚══════════════════════════════════════════════════════════╝
\033[0m""")


REQUIRED = [("requests","requests"),("pandas","pandas"),
            ("numpy","numpy"),("yfinance","yfinance"),("psutil","psutil")]

def ensure_packages():
    print("\033[96m  Checking dependencies...\033[0m")
    missing = [p for p,i in REQUIRED if not _ok(i)]
    if not missing:
        print("\033[92m  All packages ready.\033[0m\n")
        return
    print(f"\033[93m  Installing: {', '.join(missing)}...\033[0m")
    for p in missing:
        subprocess.check_call([sys.executable,"-m","pip","install",p,
                               "--break-system-packages","-q"])
    print("\033[92m  Packages installed.\033[0m\n")

def _ok(name):
    try: __import__(name); return True
    except ImportError: return False

def setup_folders():
    from config import DATA_PATH
    for f in [DATA_PATH,f"{DATA_PATH}/live",f"{DATA_PATH}/news",
              f"{DATA_PATH}/whales",f"{DATA_PATH}/history",
              f"{DATA_PATH}/predictions",f"{DATA_PATH}/screenshots",
              f"{DATA_PATH}/memory"]:
        os.makedirs(f, exist_ok=True)

def step(n, t, msg):
    print(f"\033[96m  [{n}/{t}] {msg}...\033[0m")


def run_replay_mode(crisis_key):
    from crisis_replay import replay_crisis, print_replay, CRISIS_SNAPSHOTS
    if crisis_key == "list" or crisis_key not in CRISIS_SNAPSHOTS:
        print("\033[92m  Available crisis replays:\033[0m\n")
        for key, snap in CRISIS_SNAPSHOTS.items():
            print(f"  \033[96m{key:<25}\033[0m  {snap['name']}  ({snap['date']})")
        print(f"\n  Usage: python3 zai_oracle.py --replay gulf-war\n")
        return
    print(f"\033[96m  Loading crisis replay: {crisis_key}...\033[0m")
    current_prices = None
    try:
        from world_scanner import fetch_live_prices
        print("\033[96m  Fetching current prices for comparison...\033[0m")
        current_prices = fetch_live_prices()
    except Exception:
        pass
    replay_data = replay_crisis(crisis_key, current_prices)
    print_replay(crisis_key, replay_data, current_prices)


def run_scenario_mode(scenario_str):
    from crisis_replay import run_scenario_lab, print_scenario_result
    inputs = {}
    for part in scenario_str.split(","):
        if "=" in part:
            k, v = part.split("=", 1)
            try:
                inputs[k.strip()] = float(v.strip())
            except ValueError:
                pass
    if not inputs:
        print("\033[91m  Invalid format. Example: --scenario oil=115,vix=36,war_headlines=30\033[0m\n")
        return
    print(f"\033[96m  Running scenario lab...\033[0m\n")
    result = run_scenario_lab(inputs)
    print_scenario_result(result)


def run_full_analysis():
    T = 9

    step(1, T, "Scanning hardware")
    from hardware_detector import detect, print_report
    hw = detect()
    print_report(hw)

    step(2, T, "Setting up data storage")
    setup_folders()

    step(3, T, "Fetching live prices (gold-api.com + yfinance + CoinGecko)")
    from world_scanner import fetch_live_prices, validate_prices, scan_world_news, assess_world_situation
    raw_prices         = fetch_live_prices()
    val_report         = validate_prices(raw_prices)
    prices             = raw_prices

    print(f"\033[92m  {len(prices)} assets  |  Trust: {val_report['trust_pct']}%  |  {val_report['fixed_count']} corrections\033[0m")
    for fix in val_report.get("fixed",[]): print(f"\033[93m  Source: {fix}\033[0m")
    for err in val_report.get("errors",[]): print(f"\033[91m  Warning: {err}\033[0m")
    for asset in ["oil","gold","silver","btc","sp500","vix"]:
        p = prices.get(asset,{})
        if p:
            chg  = p.get("change_pct",0)
            warn = " ⚠" if p.get("warnings") else ""
            src  = f" [{p.get('source','')}]" if p.get("source") else ""
            print(f"    {asset:<14} ${p['price']:>10,.2f}  {'↑' if chg>=0 else '↓'} {chg:+.2f}%{warn}{src}")

    step(4, T, "Scanning world news")
    news_data       = scan_world_news(max_feeds=30)
    world_situation = assess_world_situation(prices, news_data)
    risk            = news_data.get("risk_level","?")
    sigs            = list(news_data.get("signals",{}).keys())
    print(f"\033[92m  {news_data['unique_articles']} unique articles  |  Risk: {risk}  |  {news_data['total_sources']} sources\033[0m")

    step(5, T, "Tracking whale wallets")
    from whale_tracker import scan_all_whales
    whale_data = scan_all_whales()
    whale_sig  = whale_data.get("summary",{}).get("overall_signal","unknown")
    print(f"\033[92m  Whale signal: {whale_sig}\033[0m")

    step(6, T, "Historical comparison + scenarios + geo risk")
    from history_engine import compare_to_history
    from sanity_validator import calculate_confidence
    from scenario_engine import build_scenarios, calculate_geo_risk_index, build_causal_chain, build_explanation
    from regime_detector import detect_regime

    hist_data                  = compare_to_history(world_situation, news_data.get("signals",{}), prices)
    top                        = hist_data.get("top_matches",[{}])[0]
    conf_score, conf_breakdown = calculate_confidence(
        news_signals=news_data.get("signals",{}),
        hist_matches=hist_data,
        whale_data=whale_data,
        prices=prices,
    )
    geo_index     = calculate_geo_risk_index(news_data.get("signals",{}), prices)
    causal_chains = build_causal_chain(news_data.get("signals",{}), prices)
    regime_data   = detect_regime(news_data.get("signals",{}), prices)

    print(f"\033[92m  Best match: {top.get('name','?')} ({top.get('similarity',0)}%)\033[0m")
    for m in hist_data.get("top_matches",[])[:3]:
        print(f"    {m.get('similarity',0)}%  {m.get('name','')}  ({m.get('period','')})")
    print(f"\033[92m  Confidence: {conf_score}%  |  Geo Risk: {geo_index['total']}/100 ({geo_index['label']})\033[0m")

    step(7, T, "Generating Oracle prediction")
    from oracle_brain import get_oracle_prediction, save_prediction
    prediction = get_oracle_prediction(hw, world_situation, hist_data, whale_data, prices)
    if prediction and conf_score > 0:
        prediction["confidence"]           = conf_score
        prediction["confidence_breakdown"] = conf_breakdown

    save_prediction(prediction, {
        "risk_level":      news_data.get("risk_level"),
        "geo_risk_index":  geo_index["total"],
        "top_signal":      sigs[0] if sigs else None,
        "whale_signal":    whale_sig,
        "best_hist_match": top.get("name"),
    })

    scenarios = build_scenarios(world_situation, hist_data, news_data.get("signals",{}), prices, regime_data)
    explain   = build_explanation(news_data.get("signals",{}), prices, hist_data, whale_data, regime_data, conf_breakdown)

    print(f"\033[92m  Outlook: {prediction.get('overall_outlook','?')}  |  Confidence: {prediction.get('confidence',0)}%  |  AI: {prediction.get('ai_source','?')}\033[0m")

    step(8, T, "Memory + rendering")
    from oracle_memory import save_snapshot, get_delta, get_accuracy_stats
    from dashboard import render

    delta = get_delta(
        current_signals    = news_data.get("signals",{}),
        current_risk       = news_data.get("risk_level","MODERATE"),
        current_confidence = conf_score,
        current_whale      = whale_sig,
        current_hist       = top.get("name",""),
    )

    render(
        hw=hw, prices=prices, news_data=news_data,
        world_situation=world_situation, whale_data=whale_data,
        hist_data=hist_data, prediction=prediction,
        val_report=val_report, conf_breakdown=conf_breakdown,
        delta=delta, regime_data=regime_data,
        accuracy_stats=get_accuracy_stats(),
        geo_index=geo_index, scenarios=scenarios,
        explain=explain, causal_chains=causal_chains,
    )

    save_snapshot(
        risk_level=news_data.get("risk_level","MODERATE"),
        signals=news_data.get("signals",{}),
        confidence=conf_score,
        whale_signal=whale_sig,
        hist_match=top.get("name",""),
        prediction_outlook=prediction.get("overall_outlook","NEUTRAL"),
        prices=prices,
    )

    step(9, T, "Saving snapshot")
    from config import DATA_PATH
    ts   = datetime.now().strftime("%Y%m%d_%H%M%S")
    snap = {
        "timestamp":      datetime.now().isoformat(),
        "version":        "3.0",
        "risk_level":     news_data.get("risk_level"),
        "geo_risk_index": geo_index["total"],
        "outlook":        prediction.get("overall_outlook"),
        "confidence":     prediction.get("confidence"),
        "best_match":     top.get("name"),
        "regime":         regime_data.get("regime") if regime_data else None,
        "summary":        prediction.get("summary",""),
    }
    path = f"{DATA_PATH}/screenshots/oracle_{ts}.json"
    with open(path,"w") as f:
        json.dump(snap, f, indent=2)
    print(f"\033[92m  Saved: {path}\033[0m")
    print(f"\n\033[92m  Oracle v3.0 complete.\033[0m\n")
    print(f"\033[90m  Try: python3 zai_oracle.py --replay gulf-war\033[0m")
    print(f"\033[90m  Try: python3 zai_oracle.py --scenario oil=115,vix=36\033[0m\n")


def main():
    print_banner()
    ensure_packages()
    args = sys.argv[1:]
    if "--replay" in args:
        idx = args.index("--replay")
        run_replay_mode(args[idx+1] if idx+1 < len(args) else "list")
    elif "--list-crises" in args:
        run_replay_mode("list")
    elif "--scenario" in args:
        idx = args.index("--scenario")
        run_scenario_mode(args[idx+1] if idx+1 < len(args) else "")
    else:
        run_full_analysis()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n\033[92m  Stopped. — Zawwar\033[0m\n")
    except Exception as e:
        print(f"\n\033[91m  Fatal error: {e}\033[0m")
        import traceback
        traceback.print_exc()
