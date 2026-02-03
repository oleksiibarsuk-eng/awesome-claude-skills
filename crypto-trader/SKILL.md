---
name: crypto-trader
description: Provides comprehensive cryptocurrency trading assistance including market analysis, technical indicators, risk management strategies, and portfolio optimization. Use this skill when analyzing crypto markets, developing trading strategies, evaluating tokens, or managing crypto portfolios.
---

# Crypto Trader

## Overview

This skill enables sophisticated cryptocurrency trading analysis and decision-making support. It combines technical analysis, fundamental research, risk management, and market intelligence to help traders make informed decisions in crypto markets.

## Core Capabilities

### 1. Market Analysis

Analyze cryptocurrency markets using multiple data sources and analytical frameworks:

- **Price Action Analysis**: Examine candlestick patterns, support/resistance levels, and trend identification
- **Volume Analysis**: Assess trading volume, liquidity, and market depth
- **Market Sentiment**: Evaluate social media trends, news sentiment, and Fear & Greed Index
- **On-Chain Metrics**: Review blockchain data including active addresses, transaction volume, and whale movements
- **Correlation Analysis**: Compare crypto assets and their relationships with traditional markets

**Example queries:**
- "Analyze BTC price action over the last 30 days"
- "What's the current market sentiment for Ethereum?"
- "Compare the performance of top 10 altcoins this week"

### 2. Technical Analysis

Apply technical indicators and chart patterns to identify trading opportunities:

**Key Indicators:**
- Moving Averages (SMA, EMA)
- RSI (Relative Strength Index)
- MACD (Moving Average Convergence Divergence)
- Bollinger Bands
- Fibonacci Retracements
- Support and Resistance Levels
- Volume Profile

**Chart Patterns:**
- Head and Shoulders
- Double Top/Bottom
- Triangles (Ascending, Descending, Symmetrical)
- Flags and Pennants
- Cup and Handle

**Example queries:**
- "Calculate RSI for BTC and identify overbought/oversold conditions"
- "Show me the 50-day and 200-day moving averages for ETH"
- "Identify key support and resistance levels for SOL"

### 3. Trading Strategies

Develop and evaluate trading strategies based on market conditions:

**Strategy Types:**
- **Trend Following**: Ride major market trends using moving averages and momentum indicators
- **Mean Reversion**: Trade oversold/overbought conditions using RSI and Bollinger Bands
- **Breakout Trading**: Identify and trade key support/resistance breakouts
- **Swing Trading**: Capitalize on multi-day price swings
- **Scalping**: Quick trades on small price movements (requires proper risk management)
- **DCA (Dollar Cost Averaging)**: Systematic accumulation strategy
- **Grid Trading**: Automated buy/sell orders at predetermined price levels

**Example queries:**
- "Design a DCA strategy for accumulating BTC"
- "Create a swing trading plan for ETH based on current technicals"
- "Evaluate a breakout strategy for altcoins"

### 4. Risk Management

Implement proper risk management to protect capital:

**Risk Management Principles:**
- Position sizing based on account size and risk tolerance
- Stop-loss and take-profit level calculation
- Risk-reward ratio evaluation (minimum 1:2 recommended)
- Portfolio diversification strategies
- Maximum drawdown limits
- Leverage usage guidelines (with strong warnings about risks)

**Risk Calculations:**
```
Position Size = (Account Size × Risk %) / Stop Loss Distance
Risk-Reward Ratio = (Take Profit - Entry) / (Entry - Stop Loss)
```

**Example queries:**
- "Calculate position size for a $10,000 account with 2% risk per trade"
- "What should my stop-loss be for a long position on BTC at $45,000?"
- "Evaluate the risk-reward ratio of this trade setup"

### 5. Fundamental Analysis

Evaluate cryptocurrency projects beyond price action:

**Key Research Areas:**
- **Tokenomics**: Supply mechanics, distribution, inflation/deflation
- **Use Case & Adoption**: Real-world utility and adoption metrics
- **Team & Development**: GitHub activity, team credentials, roadmap progress
- **Competitive Analysis**: Position within market segment
- **Regulatory Environment**: Legal status and compliance
- **Technology Stack**: Blockchain architecture, scalability, security

**Example queries:**
- "Analyze the tokenomics of [TOKEN]"
- "Compare Layer 1 blockchain fundamentals: ETH vs SOL vs AVAX"
- "Evaluate the development activity of [PROJECT]"

### 6. Portfolio Management

Optimize and track cryptocurrency portfolios:

- Portfolio allocation strategies (Bitcoin-heavy, balanced, aggressive growth)
- Rebalancing recommendations based on market conditions
- Correlation analysis to reduce portfolio risk
- Performance tracking and metrics (ROI, Sharpe ratio, max drawdown)
- Tax-loss harvesting strategies

**Example queries:**
- "Analyze my portfolio allocation and suggest improvements"
- "When should I rebalance my crypto portfolio?"
- "Calculate the Sharpe ratio of my crypto holdings"

## Trading Workflow

### Step 1: Market Context Assessment

Before any trade, establish the broader market context:

1. Check Bitcoin dominance and overall market direction
2. Review major cryptocurrency indices (Total Market Cap, DeFi TVL)
3. Assess macro factors (regulatory news, institutional adoption, economic indicators)
4. Identify current market regime (bull, bear, sideways)

### Step 2: Asset Selection

Identify specific trading opportunities:

1. Scan for assets showing strong technicals (momentum, volume, patterns)
2. Filter based on fundamental strength and catalysts
3. Verify liquidity and trading volume adequacy
4. Check for upcoming events (updates, partnerships, unlocks)

### Step 3: Entry Planning

Develop specific entry criteria:

1. Identify optimal entry zone using support levels and indicators
2. Define entry triggers (breakout confirmation, reversal signals)
3. Consider multiple entry options (single entry vs scale-in)
4. Set alert levels for monitoring

### Step 4: Risk Definition

Establish risk parameters before entry:

1. Calculate position size based on account risk tolerance
2. Set stop-loss level below key support or based on ATR
3. Define take-profit targets at resistance levels
4. Calculate risk-reward ratio (minimum 1:2)

### Step 5: Trade Execution

Execute the trade with discipline:

1. Enter position at planned price or better
2. Immediately set stop-loss order
3. Set take-profit orders or trailing stops
4. Document trade rationale and parameters

### Step 6: Trade Management

Actively manage open positions:

1. Monitor for invalidation signals
2. Adjust stops to breakeven when in profit
3. Scale out at predetermined targets
4. Avoid emotional decision-making

### Step 7: Post-Trade Review

Learn from every trade:

1. Document trade outcome and P&L
2. Analyze what worked and what didn't
3. Update trading journal with insights
4. Adjust strategy based on results

## Important Warnings & Disclaimers

**⚠️ CRITICAL RISK WARNINGS:**

1. **Extreme Volatility**: Cryptocurrency markets are extremely volatile. Prices can move 10-50% in hours.

2. **Not Financial Advice**: This skill provides educational information only, not financial advice. Always do your own research (DYOR).

3. **Leverage Risks**: Leveraged trading can liquidate entire positions. Never use leverage without understanding the risks. Beginners should avoid leverage entirely.

4. **Scam Awareness**: Cryptocurrency space has many scams. Verify all information, never share private keys, beware of too-good-to-be-true returns.

5. **Regulatory Risks**: Crypto regulations vary by jurisdiction and change rapidly. Ensure compliance with local laws.

6. **Only Risk What You Can Afford to Lose**: Never invest money needed for living expenses, debt payments, or emergencies.

7. **Security**: Use hardware wallets for significant holdings, enable 2FA, use strong unique passwords, beware of phishing.

8. **Tax Implications**: Crypto trading has tax consequences. Consult a tax professional familiar with cryptocurrency.

## Market Data Sources

When analyzing markets, reference these reliable sources:

**Price & Market Data:**
- CoinGecko API (free, comprehensive)
- CoinMarketCap (market data, rankings)
- TradingView (charts, technical analysis)
- CryptoCompare (historical data, aggregated prices)

**On-Chain Data:**
- Glassnode (on-chain metrics)
- IntoTheBlock (on-chain analytics)
- Etherscan/Blockchain explorers (transaction data)

**Sentiment & News:**
- Crypto Fear & Greed Index
- LunarCrush (social sentiment)
- CryptoPanic (aggregated news)
- Twitter/X (real-time sentiment)

**DeFi Metrics:**
- DeFi Llama (TVL, protocols)
- Dune Analytics (on-chain queries)

## Scripts

The `scripts/` directory contains helper tools:

### market_data.py
Fetches real-time cryptocurrency market data including prices, volume, market cap, and basic metrics from CoinGecko API.

**Usage:**
```bash
python scripts/market_data.py BTC ETH SOL
```

### technical_indicators.py
Calculates common technical indicators (RSI, MACD, Moving Averages, Bollinger Bands) for any cryptocurrency given historical price data.

**Usage:**
```bash
python scripts/technical_indicators.py BTC --period 30
```

### position_calculator.py
Calculates optimal position size based on account size, risk percentage, and stop-loss distance.

**Usage:**
```bash
python scripts/position_calculator.py --account 10000 --risk 2 --stop 5
```

## References

### references/trading_strategies.md
Detailed documentation of proven cryptocurrency trading strategies with entry/exit criteria, backtesting results, and risk parameters.

### references/risk_management.md
Comprehensive risk management framework including position sizing formulas, portfolio allocation models, and drawdown recovery strategies.

### references/technical_analysis_guide.md
In-depth guide to technical analysis specifically for cryptocurrency markets, including indicator interpretations and chart pattern identification.

## Best Practices

1. **Always Use Stop Losses**: Protect capital by limiting downside on every trade
2. **Risk Management First**: Never risk more than 1-2% of account per trade
3. **Journal Every Trade**: Document rationale, setup, and results
4. **Stay Informed**: Follow market news, updates, and regulatory changes
5. **Avoid FOMO**: Wait for proper setups rather than chasing pumps
6. **Diversify**: Don't put all capital in a single asset
7. **Continuous Learning**: Markets evolve; continuously update knowledge
8. **Emotional Discipline**: Follow your plan, avoid revenge trading
9. **Start Small**: Begin with small positions while learning
10. **Secure Assets**: Use proper security measures for holdings

## Example Scenarios

### Scenario 1: Swing Trade Setup Analysis
**User:** "I want to swing trade ETH. Current price is $2,800. Should I enter?"

**Analysis Process:**
1. Check overall market context (Bitcoin trend, market sentiment)
2. Analyze ETH technicals (RSI, moving averages, support/resistance)
3. Review volume and liquidity
4. Identify entry zone, stop-loss, and take-profit levels
5. Calculate position size based on risk parameters
6. Provide trade plan with risk-reward ratio

### Scenario 2: Portfolio Review
**User:** "Review my portfolio: 50% BTC, 30% ETH, 10% SOL, 10% LINK"

**Analysis Process:**
1. Assess allocation relative to risk tolerance and market conditions
2. Evaluate correlation between holdings
3. Check for overexposure to specific sectors (L1s, DeFi, etc.)
4. Suggest rebalancing if needed
5. Recommend diversification improvements
6. Consider tax implications of rebalancing

### Scenario 3: Risk Management Check
**User:** "Calculate position size for a long on BTC at $45,000 with stop at $43,500"

**Analysis Process:**
1. Determine stop-loss distance ($1,500 or 3.33%)
2. Apply 2% account risk rule
3. Calculate: Position Size = (Account × 0.02) / 0.0333
4. Provide position size in both $ and BTC
5. Calculate risk-reward for different take-profit targets
6. Warn about volatility considerations

---

**Remember:** Successful crypto trading requires discipline, continuous learning, and strict risk management. This skill provides tools and frameworks, but ultimate trading decisions and their consequences rest with the trader.
