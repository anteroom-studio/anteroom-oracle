ZAI ORACLE 🔮
The All-Seeing Eye — Markets · Wars · Politics · Geopolitics

Created by Zawwar
github.com/Zawwarsami16

What Is ZAI Oracle?

Most tools show price charts.
Most news tools show headlines.

ZAI Oracle does something different.

It scans:

• global markets
• wars and conflicts
• geopolitical risk
• energy supply shocks
• political instability
• crypto signals
• historical crisis patterns

Then it asks:

Given everything happening in the world right now, what is the most likely outcome?

Oracle combines real-time data + historical pattern recognition + AI reasoning to produce a macro outlook and tactical market stance.

What Oracle Actually Does

Oracle continuously analyzes multiple global systems simultaneously.

System	Description
Market Scanner	Tracks stocks, commodities, crypto and volatility
Geopolitical Scanner	Detects wars, sanctions, diplomatic shifts
Energy Monitor	Oil, natural gas, supply route disruption
Political Signals	Elections, policy, Congress trading
Crypto Intelligence	Whale wallets, ETF flows, regulation news
Historical Engine	Compares today with past crises
Scenario Engine	Simulates possible market outcomes
Risk Index	Calculates global instability score
What Data It Uses
Domain	Sources
Markets	S&P500, NASDAQ, Oil, Gold, Silver, BTC, ETH, VIX, DXY, yields
Geopolitics	Reuters, Al Jazeera, Crisis Group, Foreign Policy
Wars	Live conflict headlines + war escalation signals
Energy	Oil price feeds, OPEC news, energy supply routes
Crypto	CoinDesk, CoinTelegraph, whale wallets
Politics	Congress trades, elections, regulation
Natural Disasters	WHO outbreaks, earthquakes, weather
Sanctions	OFAC actions, SEC enforcement
History	20+ major crises from 1914 → 2022
One Command

Running Oracle requires only one command.

python3 zai_oracle.py


Oracle will automatically:

• scan markets
• analyze geopolitical risk
• compare with history
• generate scenarios
• produce a tactical outlook

Setup
1 Clone the Repository
git clone https://github.com/Zawwarsami16/ZAI-Oracle
cd ZAI-Oracle

2 Create Environment File
cp .env.example .env
nano .env

3 Add AI Key (Recommended)
GROQ_KEY=gsk_your_key_here


Free key available at:

groq.com → API Keys

4 Run Oracle
python3 zai_oracle.py

Command Examples

These commands allow deeper analysis and historical simulation.

Command	Description
python3 zai_oracle.py	Full live world analysis
python3 zai_oracle.py --replay gulf-war	Gulf War 1990 replay
python3 zai_oracle.py --replay 2008-gfc	Global Financial Crisis 2008
python3 zai_oracle.py --replay ukraine-invasion	Russia-Ukraine War 2022
python3 zai_oracle.py --replay covid-crash	COVID crash 2020
python3 zai_oracle.py --replay 1973-oil-shock	OPEC oil embargo 1973
python3 zai_oracle.py --replay dotcom-peak	Dot-com bubble 2000
python3 zai_oracle.py --scenario oil=115,vix=36	Custom macro scenario
python3 zai_oracle.py --list-crises	List historical events
Crisis Replay Engine

Oracle can simulate historical events and compare them to today.

Example:

python3 zai_oracle.py --replay gulf-war


Oracle will show:

• market reaction on that day
• signals active during the crisis
• predicted regime
• what actually happened later
• accuracy assessment

This allows pattern recognition across history.

Scenario Engine

You can test custom macro scenarios.

Example:

python3 zai_oracle.py --scenario oil=115,vix=36


Oracle will calculate:

• Bear case
• Base case
• Bull case

Then generate a probability weighted outlook.

AI Modes

Oracle automatically selects the best AI available.

Condition	AI Used
GROQ_KEY present	Groq llama3-70B
GEMINI_KEY present	Google Gemini
ANTHROPIC_KEY present	Claude
Ollama installed	Local LLM
No AI available	Rule-based prediction
Historical Crisis Database

Oracle contains a database of major global crises including:

• World War I
• World War II
• 1973 Oil Crisis
• Black Monday 1987
• Dot-Com Bubble 2000
• Global Financial Crisis 2008
• COVID Crash 2020
• Russia-Ukraine War 2022

And many more.

Each crisis contains:

• trigger event
• market reaction
• signal breakdown
• recovery timeline

File Structure
File	Purpose
zai_oracle.py	Main launcher
world_scanner.py	Live market + news scanning
history_engine.py	Historical crisis database
crisis_replay.py	Crisis replay simulation
scenario_engine.py	Scenario generator
oracle_brain.py	AI reasoning
whale_tracker.py	Crypto + Congress signals
dashboard.py	Terminal UI
oracle_memory.py	Data tracking
sanity_validator.py	Data validation
config.py	Environment loader
Screenshots

Live Oracle output:

Crisis replay:

Scenario analysis:

Philosophy Behind Oracle

Oracle was built around a simple idea:

Markets are not random.

They respond to:

• wars
• energy shocks
• policy changes
• systemic crises

History does not repeat exactly — but it often rhymes.

Oracle tries to detect those rhymes.

Disclaimer

This project is a research and analysis tool only.

It is not financial advice.

Markets are unpredictable and historical patterns do not guarantee future outcomes.
