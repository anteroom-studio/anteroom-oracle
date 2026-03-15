<div align="center">

# ZAI ORACLE 🔮
### The All-Seeing Eye — Markets · Wars · Politics · Geopolitics

**by Zawwar | https://github.com/Zawwarsami16**

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![AI](https://img.shields.io/badge/AI-Groq%20%7C%20Gemini%20%7C%20Claude-purple?style=for-the-badge)
![Markets](https://img.shields.io/badge/System-Macro%20Intelligence-green?style=for-the-badge)
![Interface](https://img.shields.io/badge/Interface-Terminal-black?style=for-the-badge)

</div>

---

## What Is ZAI Oracle?

Most tools show **price charts**.  
Most news tools show **headlines**.

ZAI Oracle watches **the world system**.

It combines:

• global markets  
• wars and conflicts  
• geopolitical risk  
• energy shocks  
• political signals  
• crypto intelligence  
• historical crisis patterns  

Then it asks:

**“Given everything happening right now, what is most likely to happen next?”**

---

## Terminal Preview

## Oracle Output Example

```bash
╔══════════════════════════════════════════════════════════════╗
║              ZAI ORACLE — THE ALL-SEEING EYE                ║
║           2026-03-14  18:57:37                              ║
║           by Zawwar · github.com/Zawwarsami16               ║
╚══════════════════════════════════════════════════════════════╝

AI: groq:llama-3.3-70b-versatile

DATA HEALTH
──────────────────────────────────────────────────────────────
Market feeds:    20/20 verified
Overall trust:   ██████████ 110%

LIVE MARKETS
──────────────────────────────────────────────────────────────
S&P 500        6,632  ▼ -0.61%
NASDAQ        22,105  ▼ -0.93%
Gold           5,020  ▼ -1.06%
Oil WTI         98.71 ▲ +3.11%
Nat Gas          3.13 ▼ -3.15%
Silver          80.69 ▼ -2.93%
VIX             27.19 ▼ -0.37%
DXY            100.50 ▲ +0.76%
Bitcoin        70,723 ▼ -0.10%
Ethereum        2,084 ▼ -0.26%
Solana            87 ▼ -0.77%

GEOPOLITICAL RISK INDEX
──────────────────────────────────────────────────────────────
Global Risk: ████████████ 86.5 / 100  → EXTREME
Fastest rising factor: War Escalation

War Escalation        ██████████████ 25/25
Energy Chokepoint     ████████████   20/20
Sanctions Trade       ███████        9/15
Political Instability ███████████    15/15
Financial Stress      ███████████    15/15
Tech Disruption       ██             2/10

MARKET REGIME
──────────────────────────────────────────────────────────────
RISK-OFF / WAR PREMIUM   (High confidence)

Drivers:
• Active conflict headlines (54 articles)
• Oil elevated near $99
• VIX elevated → risk aversion

Asset behavior in this regime:
Gold   → BULLISH  (safe haven demand)
Oil    → BULLISH  (supply shock)
Stocks → BEARISH  (risk-off selling)
Bonds  → BULLISH  (flight to safety)
Crypto → BEARISH  (liquidation risk)

WORLD SIGNALS
──────────────────────────────────────────────────────────────
Risk Level: CRITICAL
Sources scanned: 184 articles from 23 sources

War / Conflict        ███████████ 54
Oil / Energy          ██████████  51
Crypto Regulation     ████        20
Politics              ███         13
Recession Economy     ██           8
Geopolitics           ██           6
Tech / AI             ██           5

CAUSAL CHAINS
──────────────────────────────────────────────────────────────
Energy Shock
Oil +3.1% → inflation pressure → yields rise → stock compression

War Risk Premium
War headlines → oil bid → gold safe haven → equities risk-off

Dollar Wrecking Ball
DXY rising → EM pressure → crypto headwind

WHALE INTELLIGENCE
──────────────────────────────────────────────────────────────
Overall: MIXED SIGNALS

BTC whales:  Source not connected
ETH whales:  Data unavailable
Congress:    NEUTRAL

HISTORICAL PARALLELS
──────────────────────────────────────────────────────────────
23 events in database · 6-dimension similarity

1. Russia-Ukraine Full Invasion (2022)
   Similarity: 78.8%

2. Gulf War (1990)
   Similarity: 78.2%

3. World War I (1914)
   Similarity: 77.0%

SCENARIO ENGINE
──────────────────────────────────────────────────────────────

Bear Case   ██████████ 50%
Oil spike → equities dump
S&P500 -10% to -20%

Base Case   ███████    35%
Range-bound markets
Oil 99-109

Bull Case   ███        15%
Oil drops
Risk-on rally

TACTICAL READ
──────────────────────────────────────────────────────────────
Stance: DEFENSIVE

Watch:
• VIX > 35
• Oil > $110
• S&P500 < 6400

ORACLE PREDICTION
──────────────────────────────────────────────────────────────
Outlook: BEARISH
Confidence: 72%

Summary:
Global macro risk is elevated due to war escalation,
energy stress, and political uncertainty.
Markets remain vulnerable to downside shocks.
```

## Quick Start

Clone repository

```bash
git clone https://github.com/Zawwarsami16/ZAI-Oracle
cd ZAI-Oracle
```

Create environment file

```bash
cp .env.example .env
nano .env
```

Add API key

```
GROQ_KEY=gsk_your_key_here
```

Run Oracle

```bash
python3 zai_oracle.py
```

---

## Command Modes

### Live Analysis

```bash
python3 zai_oracle.py
```

Runs full world analysis.

---

### Crisis Replay Mode

```bash
python3 zai_oracle.py --replay gulf-war
python3 zai_oracle.py --replay 2008-gfc
python3 zai_oracle.py --replay ukraine-invasion
python3 zai_oracle.py --replay covid-crash
python3 zai_oracle.py --replay 1973-oil-shock
python3 zai_oracle.py --replay dotcom-peak
```

Shows:

• historical signals  
• detected regime  
• oracle prediction  
• real outcome  

---

### Scenario Engine

```bash
python3 zai_oracle.py --scenario oil=115,vix=36
```

Creates:

• Bear case  
• Base case  
• Bull case  

---

### Crisis List

```bash
python3 zai_oracle.py --list-crises
```

Lists all replayable crises.

---

## Data Coverage

| System | Coverage |
|------|------|
Markets | S&P500, NASDAQ, Oil, Gold, BTC, ETH, VIX |
Geopolitics | Reuters, Crisis Group, Foreign Policy |
Energy | OPEC + supply shocks |
Crypto | Whale wallets |
Politics | Congress trades |
Disasters | Earthquakes, outbreaks |
History | 20+ global crises |

---

## Architecture

```text
zai_oracle.py
│
├── world_scanner.py
├── history_engine.py
├── crisis_replay.py
├── scenario_engine.py
├── regime_detector.py
├── oracle_brain.py
├── whale_tracker.py
├── dashboard.py
├── oracle_memory.py
├── sanity_validator.py
└── config.py
```

---

## Philosophy

Markets move because of **systems**:

• war  
• energy  
• policy  
• inflation  
• geopolitics  

History doesn't repeat exactly.

But it **rhymes**.

Oracle tries to detect those rhymes.

---

## Disclaimer

Research tool only.  
Not financial advice.

---

**Created by Zawwar**
