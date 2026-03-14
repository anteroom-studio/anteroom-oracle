# ZAI ORACLE 🔮
### The All-Seeing Eye — Markets · Wars · Politics · Geopolitics

**by Zawwar | [github.com/Zawwarsami16](https://github.com/Zawwarsami16)**

---

## What Is This?

Most market tools look at price charts.  
Most news tools show headlines.  
ZAI Oracle looks at **everything simultaneously** — and connects the dots.

It answers one question:  
**"Given everything happening in the world right now, what is most likely to happen next — and what does history say about it?"**

---

## What It Covers

| Domain | Data Sources |
|--------|-------------|
| Markets | S&P500, NASDAQ, Gold, Oil, BTC, ETH, VIX, 17 assets |
| Geopolitics | Reuters, Al Jazeera, Foreign Policy, Crisis Group, 10+ feeds |
| Wars + Conflicts | Live conflict tracking, 500+ news sources |
| Energy | Oil price, EIA data, OPEC news |
| Politics | US Congress trades, election news, policy feeds |
| Crypto | CoinDesk, CoinTelegraph, whale wallet tracking |
| Natural Disasters | USGS earthquakes, NOAA, WHO outbreaks |
| Sanctions | OFAC actions, SEC enforcement, BIS |
| Whale Tracking | BTC top wallets, ETH known addresses, Congress trades |
| History | 20+ historical crises from 1914 to 2022 |

---

## One Command

```bash
python3 zai_oracle.py
```

That's it. Everything else is automatic.

---

## Setup

**1. Clone**
```bash
git clone https://github.com/Zawwarsami16/ZAI-Oracle
cd ZAI-Oracle
```

**2. Create .env file**
```bash
cp .env.example .env
nano .env
```

**3. Add your Groq key (free)**
```
GROQ_KEY=gsk_your_key_here
```
Get it free at: groq.com → sign up → API Keys

**4. Run**
```bash
python3 zai_oracle.py
```

---

## AI Modes — Auto-Selected

| What's in .env | AI Used | Speed |
|----------------|---------|-------|
| GROQ_KEY | Groq llama3-70b — FREE | 3-5 sec |
| GEMINI_KEY | Google Gemini — FREE tier | 5-10 sec |
| ANTHROPIC_KEY | Claude — paid, most accurate | 5-10 sec |
| Ollama installed | Local LLM — FREE, offline | 2-4 min CPU |
| Nothing | Rule-based logic | Instant |

System auto-detects GPU and asks if you want local vs API when both are available.

---

## Historical Crisis Database

ZAI Oracle compares today to 20+ historical events:

- WW1 (1914), WW2 (1939)
- Korean War (1950), Vietnam War (1965)
- Gulf War (1990), Iraq War (2003)
- Ukraine War (2022)
- Great Depression (1929)
- Oil Crisis (1973)
- Black Monday (1987)
- Asian Financial Crisis (1997)
- Dot-com Crash (2000)
- Financial Crisis (2008)
- COVID Crash (2020)
- Crypto Winter (2022)
- Volcker Shock (1980)
- Post-COVID Inflation (2021-2023)

---

## Files

| File | Purpose |
|------|---------|
| `.env` | Your API keys — only file you edit |
| `zai_oracle.py` | Main launcher — run this |
| `hardware_detector.py` | GPU/RAM scan + AI mode selection |
| `world_scanner.py` | Live prices + 500+ news feeds |
| `whale_tracker.py` | BTC/ETH wallets + Congress trades |
| `history_engine.py` | Historical crisis database + matching |
| `oracle_brain.py` | AI prediction engine |
| `dashboard.py` | Dark terminal output |
| `config.py` | Loads .env, wallet addresses |

---

*Research tool. Not financial advice.*
