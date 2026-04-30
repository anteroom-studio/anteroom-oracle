# Anteroom Oracle

**Geopolitical and macro intelligence terminal for market-regime research.**

Anteroom Oracle is a Python-based research system that combines live market data, world-event signals, geopolitical risk scoring, historical crisis comparison, whale-activity context, and scenario modeling into one terminal intelligence interface.

> Built by **Anteroom Studio** as part of its research systems and intelligence tooling.

---

## Overview

Most market tools focus on price charts or headline streams. Anteroom Oracle is designed to evaluate the wider system around markets: conflict, energy shocks, policy signals, macro stress, crypto flows, historical parallels, and regime behavior.

It helps explore questions such as:

- What market regime appears most consistent with current conditions?
- Which world-event categories are driving risk?
- Which historical crises share similar signal patterns?
- How do scenario probabilities shift under different inputs?
- What should researchers monitor next?

This is a research tool, not a trading signal service.

---

## Core Capabilities

- Live market scanning across equities, commodities, volatility, rates, and crypto
- World-news and geopolitical signal extraction
- Geopolitical risk index generation
- Market-regime detection
- Historical crisis comparison and replay mode
- Scenario modeling for custom macro assumptions
- Whale-activity and public-flow context
- Terminal dashboard rendering
- Local storage for snapshots and run history

---

## Quick Start

Install dependencies:

```bash
pip install -r requirements.txt
```

Create local environment settings:

```bash
cp .env.example .env
```

Optional keys can be added to `.env`:

```env
GROQ_KEY=
GEMINI_KEY=
ANTHROPIC_KEY=
ETHERSCAN_KEY=
TELEGRAM_BOT_TOKEN=
TELEGRAM_CHAT_ID=
DATA_PATH=./oracle_data
```

Run a full scan:

```bash
python3 zai_oracle.py
```

> The launcher filename is retained for compatibility. It can be renamed after repository migration.

---

## Command Modes

Run live analysis:

```bash
python3 zai_oracle.py
```

List replayable crises:

```bash
python3 zai_oracle.py --list-crises
```

Run historical replay mode:

```bash
python3 zai_oracle.py --replay gulf-war
python3 zai_oracle.py --replay 2008-gfc
python3 zai_oracle.py --replay ukraine-invasion
python3 zai_oracle.py --replay covid-crash
python3 zai_oracle.py --replay 1973-oil-shock
python3 zai_oracle.py --replay dotcom-peak
```

Run scenario mode:

```bash
python3 zai_oracle.py --scenario oil=115,vix=36,war_headlines=30
```

---

## Data Coverage

| System | Coverage |
|---|---|
| Markets | S&P 500, NASDAQ, oil, gold, silver, VIX, DXY, rates, crypto |
| World signals | Conflict, energy, policy, geopolitics, macro stress, technology |
| Historical library | Crisis snapshots and historical regime comparisons |
| Crypto context | Public whale-wallet and flow indicators where available |
| Scenarios | Bear/base/bull research paths and custom input assumptions |

---

## System Architecture

```text
Anteroom Oracle
├── zai_oracle.py          Main CLI entry point
├── world_scanner.py       Market and world-signal collection
├── data_collector.py      Data aggregation and normalization
├── news_brain.py          News and geopolitical signal extraction
├── whale_tracker.py       Public whale-activity context
├── correlation_engine.py  Cross-asset and stress-signal logic
├── regime_detector.py     Market-regime detection
├── sanity_validator.py    Data quality and confidence scoring
├── history_engine.py      Historical crisis comparison
├── crisis_replay.py       Replay and scenario lab modes
├── scenario_engine.py     Scenario and geo-risk modeling
├── oracle_brain.py        Rule/model-assisted scenario summary
├── oracle_memory.py       Snapshot and delta memory
├── dashboard.py           Terminal renderer
├── config.py              Environment and runtime settings
└── .env.example           Safe local configuration template
```

---

## Safety and Scope

Anteroom Oracle is intended for research, education, and internal experimentation. Its outputs may be incomplete, stale, or incorrect depending on data-source availability, model behavior, API limits, and market conditions.

This project does not provide financial, investment, legal, or professional advice. Always verify outputs independently before using them in any real-world decision.

---

## Studio

**Anteroom Studio**  
Research systems, intelligence interfaces, and experimental software.
