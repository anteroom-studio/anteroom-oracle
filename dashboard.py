"""
ZAI Oracle — Dashboard v2.0
by Zawwar (github.com/Zawwarsami16)

Full Bloomberg-grade terminal output.
Every section has a purpose, every number is sourced.
"""

import os
from datetime import datetime
from config import DATA_PATH

class C:
    RESET = "\033[0m"; BOLD = "\033[1m"; DIM = "\033[2m"
    GREEN = "\033[92m"; CYAN = "\033[96m"; YELLOW = "\033[93m"
    RED = "\033[91m"; MAGENTA = "\033[95m"; WHITE = "\033[97m"
    GRAY = "\033[90m"; ORANGE = "\033[38;5;208m"; BRED = "\033[91m\033[1m"

def g(text, color): return f"{color}{text}{C.RESET}"
def clr(): os.system("cls" if os.name == "nt" else "clear")
def sec(title, col=C.CYAN):
    print(g(f"  {title}", col + C.BOLD))
    print(g("  " + "─"*58, C.GRAY))

def wrap(text, width=60, indent="    "):
    words = str(text).split()
    line, lines = indent, []
    for w in words:
        if len(line) + len(w) > width:
            lines.append(line)
            line = indent + w + " "
        else:
            line += w + " "
    if line.strip(): lines.append(line)
    return lines


def print_header(ai_source):
    now = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
    print(g("╔══════════════════════════════════════════════════════════════╗", C.GREEN))
    print(g("║", C.GREEN) + g("          ZAI ORACLE  —  THE ALL-SEEING EYE                  ", C.BOLD + C.WHITE) + g("║", C.GREEN))
    print(g("║", C.GREEN) + g(f"          {now}                              ", C.GRAY) + g("║", C.GREEN))
    print(g("║", C.GREEN) + g("          by Zawwar · github.com/Zawwarsami16               ", C.GRAY) + g("║", C.GREEN))
    print(g("╚══════════════════════════════════════════════════════════════╝", C.GREEN))
    if ai_source:
        print(g(f"  AI: {ai_source}", C.GREEN))
    print()


def print_data_health(val_report):
    if not val_report: return
    total  = val_report.get("total_assets", 0)
    errors = val_report.get("errors_count", 0)
    fixed  = val_report.get("fixed_count", 0)
    trust  = max(0, 100 - errors * 12 + fixed * 5)
    tc     = C.GREEN if trust >= 80 else C.YELLOW if trust >= 60 else C.RED
    bar    = g("█" * (trust // 10), tc) + g("░" * (10 - trust // 10), C.GRAY)
    sec("DATA HEALTH", C.CYAN)
    print(f"  Market feeds:    {g(str(total - errors) + '/' + str(total) + ' verified', C.GREEN if not errors else C.YELLOW)}")
    print(f"  Overall trust:   [{bar}] {g(str(trust) + '%', tc)}")
    for f in val_report.get("fixed", []):
        print(f"  {g('Fixed:', C.YELLOW)} {f}")
    for w in val_report.get("warnings", [])[:2]:
        print(f"  {g('Warning:', C.YELLOW)} {w}")
    for e in val_report.get("errors", []):
        print(f"  {g('Conflict:', C.RED)} {e}")
    print()


def print_markets(prices):
    sec("LIVE MARKETS", C.CYAN)
    assets = [
        ("S&P 500",    "sp500", "$"),
        ("NASDAQ",     "nasdaq","$"),
        ("Gold",       "gold",  "$"),
        ("Oil WTI",    "oil",   "$"),
        ("Nat. Gas",   "naturalgas", "$"),
        ("Silver",     "silver","$"),
        ("VIX Fear",   "vix",   ""),
        ("DXY Dollar", "dxy",   ""),
        ("10Y Yield",  "tnx",   "%"),
        ("Bitcoin",    "btc",   "$"),
        ("Ethereum",   "eth",   "$"),
        ("Solana",     "sol",   "$"),
    ]
    for label, key, pfx in assets:
        d = prices.get(key)
        if not d: continue
        price = d.get("price", 0)
        chg   = d.get("change_pct", 0)
        warns = d.get("warnings", [])
        src   = d.get("source", "")
        arr   = g("↑", C.GREEN) if chg >= 0 else g("↓", C.RED)
        cc    = C.GREEN if chg >= 0 else C.RED
        if pfx == "$":
            p_str = f"${price:>10,.0f}" if price > 999 else f"${price:>10,.2f}"
        else:
            p_str = f" {price:>10,.2f}{'%' if pfx == '%' else ''}"
        w_str = g(" ⚠", C.YELLOW) if warns else ""
        w_str += g("  ► WATCH $100", C.YELLOW) if key == "oil" and price >= 95 and not warns else ""
        w_str += g("  ► FEAR", C.RED) if key == "vix" and price >= 28 and not warns else ""
        s_str = g(f" [{src}]", C.GRAY) if src else ""
        print(f"  {g(label, C.WHITE):<16}  {g(p_str, C.YELLOW)}   {arr} {g(f'{chg:+.2f}%', cc)}{w_str}{s_str}")
    print()


def print_geo_risk_index(geo_index):
    if not geo_index: return
    total = geo_index.get("total", 0)
    label = geo_index.get("label", "?")
    comps = geo_index.get("components", {})
    fast  = geo_index.get("fastest_rising", "")
    lc = {"EXTREME": C.BRED, "CRITICAL": C.RED, "HIGH": C.RED,
          "ELEVATED": C.ORANGE, "MODERATE": C.YELLOW, "LOW": C.GREEN}
    sec("GEOPOLITICAL RISK INDEX", C.MAGENTA)
    bar = g("█" * int(total / 10), lc.get(label, C.YELLOW)) + g("░" * (10 - int(total / 10)), C.GRAY)
    print(f"  Global Risk:     [{bar}] {g(str(total) + '/100', C.WHITE)}  {g(label, lc.get(label, C.YELLOW) + C.BOLD)}")
    if fast:
        print(f"  Fastest rising:  {g(fast, C.ORANGE)}")
    print()
    for name, comp in comps.items():
        s   = comp.get("score", 0)
        mx  = comp.get("max", 1)
        note= comp.get("note", "")
        trend=comp.get("trend", "")
        pct = s / mx if mx else 0
        mb  = g("█" * int(pct * 5), C.RED if pct > 0.7 else C.ORANGE if pct > 0.4 else C.CYAN)
        mb += g("░" * (5 - int(pct * 5)), C.GRAY)
        lbl = name.replace("_", " ").title()
        tc  = C.RED if trend in ["critical","rising","stressed"] else C.YELLOW if trend in ["elevated","uncertain"] else C.GREEN
        print(f"  {g(lbl, C.GRAY):<26} [{mb}] {s:.0f}/{mx}  {g(trend, tc)}")
    print()


def print_regime(regime_data):
    if not regime_data: return
    regime  = regime_data.get("regime", "UNKNOWN")
    color   = regime_data.get("color", "YELLOW")
    drivers = regime_data.get("drivers", [])
    behav   = regime_data.get("asset_behavior", {})
    conf    = regime_data.get("confidence", "LOW")
    ends    = regime_data.get("what_ends_it", "")
    cm = {"RED": C.RED, "RED_BOLD": C.BRED, "ORANGE": C.ORANGE,
          "YELLOW": C.YELLOW, "GREEN": C.GREEN, "CYAN": C.CYAN}
    sec("MARKET REGIME", C.MAGENTA)
    print(f"  {g(regime, cm.get(color, C.YELLOW) + C.BOLD)}  {g('(' + conf + ' confidence)', C.GRAY)}")
    print()
    if drivers:
        print(g("  Drivers:", C.WHITE))
        for d in drivers: print(f"    {g('-', C.GRAY)} {d}")
        print()
    if behav:
        print(g("  Asset behavior in this regime:", C.WHITE))
        for asset, beh in list(behav.items())[:5]:
            bc = C.GREEN if "BULL" in beh else C.RED if any(x in beh for x in ["BEAR","SEVERE"]) else C.YELLOW
            print(f"    {g(asset.capitalize() + ':', C.GRAY):<14} {g(beh, bc)}")
        print()
    if ends:
        print(g(f"  Ends when: {ends}", C.GRAY))
    print()


def print_world_signals(news_data, world_situation):
    risk    = news_data.get("risk_level", "UNKNOWN")
    total   = news_data.get("total_articles", 0)
    unique  = news_data.get("unique_articles", total)
    sources = news_data.get("total_sources", 0)
    sigs    = news_data.get("signals", {})
    rc = {"CRITICAL": C.BRED, "HIGH": C.RED, "ELEVATED": C.ORANGE, "MODERATE": C.YELLOW, "LOW": C.GREEN}
    sec("WORLD SIGNALS", C.MAGENTA)
    print(f"  Risk Level:  {g(risk, rc.get(risk, C.YELLOW) + C.BOLD)}  "
          f"{g('(' + str(unique) + ' unique articles · ' + str(sources) + ' sources)', C.GRAY)}")
    stresses = world_situation.get("market_stress", [])
    if stresses:
        print()
        for s in stresses[:3]: print(f"  {g('►', C.RED)} {s}")
    print()
    for cat, data in list(sigs.items())[:7]:
        count   = data.get("count", 0)
        usrcs   = data.get("unique_sources", 0)
        srcbd   = data.get("source_breakdown", {})
        consens = data.get("consensus", "LOW")
        t1      = data.get("tier_breakdown", {}).get("tier1", 0)
        bc      = C.RED if count > 12 else C.ORANGE if count > 6 else C.CYAN
        bar     = g("█" * min(count, 15), bc) + g("░" * (15 - min(count, 15)), C.GRAY)
        cc      = C.GREEN if consens == "HIGH" else C.YELLOW if consens == "MEDIUM" else C.GRAY
        print(f"  {g(cat, C.WHITE):<26} {bar} {g(str(count), bc)}")
        if srcbd:
            top = sorted(srcbd.items(), key=lambda x: x[1], reverse=True)[:4]
            src_str = " · ".join(f"{s[0].replace('_',' ').title()} ({s[1]})" for s in top)
            print(f"  {'':<26}  {g(str(usrcs) + ' sources', C.GRAY)} · "
                  f"Consensus: {g(consens, cc)} · "
                  f"{g('Tier-1: ' + str(t1), C.CYAN)}")
            print(f"  {'':<26}  {g(src_str[:52], C.DIM)}")
        if count > 8 and data.get("headlines"):
            h = data["headlines"][0]
            print(f"  {'':<26}  {g('→ ' + h.get('title', '')[:52], C.GRAY)}")
        print()


def print_causal_chains(chains):
    if not chains: return
    sec("CAUSAL CHAINS", C.CYAN)
    for chain in chains:
        sev = chain.get("severity", "MODERATE")
        sc  = C.RED if sev == "HIGH" else C.ORANGE
        print(f"  {g(chain['name'], sc + C.BOLD)}")
        print(f"    {g(chain['chain'], C.GRAY)}")
        print()


def print_oracle_memory(delta):
    sec("ORACLE MEMORY", C.CYAN)
    if not delta or not delta.get("has_previous"):
        print(g("  First run — baseline established. Next run will show delta.", C.GRAY))
        print()
        return
    prev  = delta.get("previous_scan", "unknown")
    rchg  = delta.get("risk_change", "")
    trend = delta.get("risk_trend", "STABLE")
    cdelta= delta.get("confidence_delta", 0)
    tc    = C.RED if trend == "DETERIORATING" else C.GREEN if trend == "IMPROVING" else C.YELLOW
    ta    = "↑ DETERIORATING" if trend == "DETERIORATING" else "↓ IMPROVING" if trend == "IMPROVING" else "→ STABLE"
    print(f"  Previous scan:   {g(prev, C.GRAY)}")
    print(f"  Risk:            {g(rchg, C.WHITE)}  {g(ta, tc + C.BOLD)}")
    if cdelta:
        print(f"  Confidence:      {g(f'{cdelta:+.1f}%', C.RED if cdelta < -5 else C.GREEN if cdelta > 5 else C.YELLOW)}")
    print()
    news = delta.get("new_signals",   [])
    drop = delta.get("dropped_signals",[])
    intn = delta.get("intensified",   [])
    ease = delta.get("eased",         [])
    if any([news, drop, intn, ease]):
        print(g("  Signal changes since last scan:", C.WHITE))
        for s in news: print(f"    {g('+ ' + s, C.RED)}  {g('new', C.GRAY)}")
        for s in intn: print(f"    {g('↑ ' + s, C.ORANGE)}  {g('intensified', C.GRAY)}")
        for s in ease: print(f"    {g('↓ ' + s, C.GREEN)}  {g('easing', C.GRAY)}")
        for s in drop: print(f"    {g('- ' + s, C.GRAY)}  {g('dropped', C.GRAY)}")
    print()


def print_whale_intel(whale_data):
    if not whale_data: return
    summary  = whale_data.get("summary", {})
    btc      = whale_data.get("btc", {})
    eth      = whale_data.get("eth", {})
    congress = whale_data.get("congress", {})
    overall  = summary.get("overall_signal", "UNKNOWN")
    conf     = summary.get("confidence", "LOW")
    sc = C.RED if any(x in overall for x in ["EXIT","SELL"]) else C.GREEN if "ACCUM" in overall else C.YELLOW
    sec("WHALE INTELLIGENCE", C.CYAN)
    print(f"  Overall:   {g(overall, sc + C.BOLD)}  {g('Confidence: ' + conf, C.GRAY)}")
    print()
    btc_sig = btc.get("movement_signal", "UNKNOWN")
    btc_tot = btc.get("total_btc_tracked", 0)
    btc_w   = btc.get("wallets_checked", 0)
    btc_act = btc.get("active_wallets", 0)
    bc = C.GREEN if "ACCUM" in btc_sig else C.RED if "DISTRIB" in btc_sig else C.YELLOW
    if btc_w > 0:
        print(f"  BTC Whales   {g(btc_sig, bc)}")
        print(f"  {g('  Tracked:', C.GRAY)} {btc_w} wallets · {g(f'{btc_tot:,.0f} BTC', C.WHITE)} · {g(str(btc_act) + ' active', C.CYAN)}")
    else:
        print(f"  BTC Whales   {g('Source not connected', C.GRAY)}")
        print(f"  {g('  blockchain.info API limiting — confidence penalty applied', C.GRAY)}")
    eth_sig = eth.get("signal", "UNKNOWN")
    eth_w   = eth.get("wallets_checked", 0)
    if eth.get("status") == "no_key":
        print(f"  ETH Whales   {g('Add ETHERSCAN_KEY to .env to enable', C.GRAY)}")
    elif eth_w > 0:
        ec = C.RED if "MAJOR" in eth_sig else C.YELLOW if "SOME" in eth_sig else C.GREEN
        print(f"  ETH Whales   {g(eth_sig[:40], ec)}  {g(str(eth_w) + ' wallets tracked', C.GRAY)}")
    else:
        print(f"  ETH Whales   {g('Data unavailable', C.GRAY)}")
    cs = congress.get("signal", "NEUTRAL")
    ct = congress.get("total_trades", 0)
    cb = congress.get("buys", 0)
    cs2= congress.get("sells", 0)
    cc = C.RED if any(x in cs for x in ["BEAR","DEFEN"]) else C.GREEN if "BULL" in cs else C.YELLOW
    print(f"  Congress     {g(cs[:45], cc)}")
    if ct > 0:
        print(f"  {g('  Trades:', C.GRAY)} {ct} · {g(str(cb) + ' buys', C.GREEN)} · {g(str(cs2) + ' sells', C.RED)}")
        if congress.get("tickers_bought"):
            print(f"  {g('  Buying: ', C.GRAY)}{', '.join(congress['tickers_bought'][:5])}")
        if congress.get("tickers_sold"):
            print(f"  {g('  Selling:', C.GRAY)}{', '.join(congress['tickers_sold'][:5])}")
    print()


def print_historical_parallels(hist_data):
    matches = hist_data.get("top_matches", [])
    if not matches: return
    sec("HISTORICAL PARALLELS", C.YELLOW)
    print(g(f"  {hist_data.get('total_events_in_db', 0)} events in database · 6-dimension similarity analysis", C.GRAY))
    print()
    for i, m in enumerate(matches[:3]):
        sim    = m.get("similarity", 0)
        name   = m.get("name", "")
        per    = m.get("period", "")
        les    = m.get("lesson", "")
        bd     = m.get("breakdown", {})
        imp    = m.get("impact", {})
        ttb    = m.get("time_to_bottom", "?")
        rec    = m.get("recovery_time", "?")
        trigger= m.get("trigger", "")
        sc     = C.RED if sim >= 80 else C.ORANGE if sim >= 60 else C.YELLOW
        bar    = g("█" * int(sim / 10), sc) + g("░" * (10 - int(sim / 10)), C.GRAY)
        print(f"  {g(str(i+1) + '.', C.GRAY)} {g(name, C.WHITE)}  {g('(' + per + ')', C.GRAY)}")
        if trigger:
            print(f"     {g('Trigger: ' + trigger[:60], C.GRAY)}")
        print(f"     Similarity  [{bar}] {g(str(sim) + '%', sc)}")
        strongest = m.get("strongest_match", "")
        if bd:
            print(f"     {g('Match breakdown:', C.GRAY)}", end="")
            if strongest:
                print(f"  {g('Strongest: ' + strongest.replace('_match','').replace('_',' '), C.YELLOW)}")
            else:
                print()
            for dim, pct in sorted(bd.items(), key=lambda x: x[1], reverse=True):
                lbl    = dim.replace("_match","").replace("_"," ")
                mb     = g("█" * int(pct / 20), sc) + g("░" * (5 - int(pct / 20)), C.GRAY)
                is_str = " ◄" if dim == strongest else ""
                print(f"       • {g(lbl, C.GRAY):<22} [{mb}] {pct:.0f}%{g(is_str, C.YELLOW)}")
        if imp:
            print(f"     {g('Historical impact:', C.GRAY)}")
            for asset, move in list(imp.items())[:3]:
                print(f"       {g(asset + ':', C.GRAY):<12} {move}")
        print(f"     {g('Time to bottom: ' + ttb, C.GRAY)}  ·  {g('Recovery: ' + rec, C.GRAY)}")
        if les:
            print(f"     {g('Lesson:', C.GRAY)} {g(les[:60], C.DIM)}")
        print()


def print_scenarios(scenarios):
    if not scenarios: return
    sec("SCENARIO ENGINE", C.GREEN)
    hist_note = scenarios.get("historical_note", "")
    if hist_note:
        print(g(f"  Context: {hist_note[:70]}", C.GRAY))
        print()
    for key in ["bear", "base", "bull"]:
        s   = scenarios.get(key, {})
        lbl = s.get("label", "")
        pct = s.get("probability", 0)
        out = s.get("outlook", "")
        mp  = s.get("market_path", "")
        w4  = s.get("4_weeks", "")
        trg = s.get("triggers", [])
        inv = s.get("invalidated_if", [])
        col = C.RED if key == "bear" else C.GREEN if key == "bull" else C.YELLOW
        bar = g("█" * (pct // 5), col) + g("░" * (20 - pct // 5), C.GRAY)
        print(f"  {g(lbl, col + C.BOLD):<32} [{bar}] {g(str(pct) + '%', col)}")
        print(f"    {g(mp, C.GRAY)}")
        print(f"    {g('4 weeks: ' + w4, C.WHITE)}")
        if trg:
            print(f"    {g('Triggers:', C.CYAN)}")
            for t in trg[:2]: print(f"      {g('→ ' + t, C.GRAY)}")
        if inv:
            print(f"    {g('Invalidated if:', C.GRAY)}")
            for v in inv[:2]: print(f"      {g('✗ ' + v, C.DIM)}")
        print()


def print_explainability(explain):
    if not explain: return
    sec("WHY ORACLE THINKS THIS", C.CYAN)
    sup  = explain.get("supporting", [])
    con  = explain.get("contradicting", [])
    weak = explain.get("weakest_link", "")
    wpct = explain.get("weakest_pct", 0)
    miss = explain.get("missing_data", [])
    if sup:
        print(g("  Supporting evidence:", C.WHITE))
        for s in sup: print(f"    {g('✓', C.GREEN)} {s}")
        print()
    if con:
        print(g("  Contradicting signals:", C.YELLOW))
        for c in con: print(f"    {g('⚠', C.YELLOW)} {c}")
        print()
    if weak:
        print(f"  {g('Weakest component:', C.GRAY)} {weak} ({wpct:.0f}%)")
    if miss:
        for m in miss: print(f"  {g('Missing:', C.RED)} {m}")
    print()


def print_tactical_read(prediction):
    """Prints the tactical read — actionable, operator-grade."""
    if not prediction: return
    tactical = prediction.get("tactical_read", {})
    if not tactical: return
    sec("TACTICAL READ", C.YELLOW)
    stance = tactical.get("stance", "NEUTRAL")
    sc = C.RED if stance == "DEFENSIVE" else C.GREEN if stance == "OPPORTUNISTIC" else C.YELLOW
    print(f"  Stance:    {g(stance, sc + C.BOLD)}")
    levels = tactical.get("key_levels", [])
    if levels:
        print(g("  Key levels:", C.WHITE))
        for lv in levels[:3]:
            print(f"    {g('►', C.CYAN)} {lv}")
    avoid = tactical.get("avoid", "")
    watch = tactical.get("watch_for", "")
    if avoid:
        print(f"  {g('Avoid:', C.RED):<12} {avoid[:65]}")
    if watch:
        print(f"  {g('Watch for:', C.GREEN):<12} {watch[:65]}")
    print()


def print_prediction(prediction, conf_breakdown):
    if not prediction: return
    outlook = prediction.get("overall_outlook", "NEUTRAL")
    conf    = prediction.get("confidence", 0)
    source  = prediction.get("ai_source", "unknown")
    summary = prediction.get("summary", "")
    gentime = prediction.get("generated_at", "")[:19]
    oc = {"BULLISH": C.GREEN, "MILDLY BULLISH": C.GREEN, "BEARISH": C.RED,
          "VOLATILE": C.ORANGE, "CRITICAL": C.BRED, "NEUTRAL": C.YELLOW}
    sec("ORACLE PREDICTION", C.GREEN)
    sit = prediction.get("current_situation_summary", "")
    if sit:
        print(g("  Situation:", C.WHITE))
        for line in wrap(sit, 62): print(g(line, C.GRAY))
        print()
    ci  = int(conf)
    cb  = g("█" * (ci // 10), C.GREEN) + g("░" * (10 - ci // 10), C.GRAY)
    cl  = conf_breakdown.get("interpretation", "") if conf_breakdown else ""
    print(f"  Outlook:         {g(outlook, oc.get(outlook, C.YELLOW) + C.BOLD)}")
    print(f"  Confidence:      [{cb}] {g(str(ci) + '%', C.CYAN)}  {g('(' + cl + ')', C.GRAY) if cl else ''}")
    if conf_breakdown:
        comps    = conf_breakdown.get("components", {})
        penalties= conf_breakdown.get("penalties", {})
        if comps:
            print(g("  Confidence components:", C.GRAY))
            for name, comp in comps.items():
                s  = comp.get("score", 0)
                mx = comp.get("max", 1)
                mb = g("█" * int((s/mx)*5 if mx else 0), C.GREEN) + g("░" * (5 - int((s/mx)*5 if mx else 0)), C.GRAY)
                print(f"    {g(name.replace('_',' '), C.GRAY):<30} [{mb}] {s:.0f}/{mx}")
        if penalties:
            print(g("  Confidence penalties:", C.GRAY))
            for name, note in penalties.items():
                print(f"    {g('⬇ ' + note, C.RED)}")
        print()
    domains = prediction.get("domain_outlooks", {})
    if domains:
        print(g("  Domain outlook:", C.WHITE))
        for dom, txt in domains.items():
            dc = C.RED if any(x in txt.upper() for x in ["BEAR","DANGER"]) else C.GREEN if any(x in txt.upper() for x in ["BULL","POSITIVE"]) else C.GRAY
            print(f"    {g(dom.capitalize() + ':', C.CYAN):<16} {g(txt[:55], dc)}")
        print()
    watch = prediction.get("what_to_watch", [])
    if watch:
        print(g("  Watch:", C.CYAN))
        for w in watch[:3]: print(f"    {g('►', C.GREEN)} {w}")
        print()
    risk = prediction.get("biggest_risk", "")
    opp  = prediction.get("biggest_opportunity", "")
    if risk: print(f"  {g('⚠ Risk:', C.RED):<12} {risk[:60]}")
    if opp:  print(f"  {g('★ Opp:', C.GREEN):<12} {opp[:60]}")
    if risk or opp: print()
    if summary:
        print(g("  Summary:", C.WHITE))
        for line in wrap(summary, 62): print(g(line, C.GRAY))
        print()
    print(g(f"  Source: {source}  ·  Generated: {gentime}", C.GRAY))


def print_accuracy(acc):
    if not acc: return
    sec("FORECAST SCOREBOARD", C.CYAN)
    hr  = acc.get("hit_rate", 0)
    l10 = acc.get("last_10_rate", 0)
    hc  = C.GREEN if hr >= 60 else C.YELLOW if hr >= 45 else C.RED
    print(f"  Total predictions:   {acc.get('total_predictions', 0)}")
    print(f"  Overall hit rate:    {g(str(hr) + '%', hc)}")
    print(f"  Last 10 hit rate:    {g(str(l10) + '%', hc)}")
    print()


def print_footer():
    print()
    print(g("  " + "─"*58, C.GRAY))
    print(g("  ZAI Oracle v2.0  ·  by Zawwar  ·  github.com/Zawwarsami16", C.GRAY))
    print(g("  All data saved to oracle_data/  ·  Run again for fresh scan", C.GRAY))
    print()


def render(hw, prices, news_data, world_situation, whale_data, hist_data,
           prediction, val_report, conf_breakdown, delta, regime_data,
           accuracy_stats, geo_index, scenarios, explain, causal_chains):
    clr()
    ai_source = prediction.get("ai_source", "") if prediction else ""
    print_header(ai_source)
    print_data_health(val_report)
    print_markets(prices)
    print_geo_risk_index(geo_index)
    print_regime(regime_data)
    print_world_signals(news_data, world_situation)
    print_causal_chains(causal_chains)
    print_oracle_memory(delta)
    print_whale_intel(whale_data)
    print_historical_parallels(hist_data)
    print_scenarios(scenarios)
    print_explainability(explain)
    print_tactical_read(prediction)
    print_prediction(prediction, conf_breakdown)
    print_accuracy(accuracy_stats)
    print_footer()
