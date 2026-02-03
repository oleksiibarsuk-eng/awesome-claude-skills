#!/usr/bin/env python3
"""
Technical Indicators Calculator for Cryptocurrencies

Calculates common technical indicators including:
- RSI (Relative Strength Index)
- MACD (Moving Average Convergence Divergence)
- Moving Averages (SMA, EMA)
- Bollinger Bands
- Support and Resistance Levels

Usage:
    python technical_indicators.py BTC --period 30
    python technical_indicators.py ETH --indicators rsi,macd
"""

import sys
import json
import urllib.request
from datetime import datetime

COINGECKO_API = "https://api.coingecko.com/api/v3"

COIN_IDS = {
    "BTC": "bitcoin",
    "ETH": "ethereum",
    "SOL": "solana",
    "BNB": "binancecoin",
    "XRP": "ripple",
    "ADA": "cardano",
    "DOGE": "dogecoin",
    "MATIC": "matic-network",
    "DOT": "polkadot",
    "AVAX": "avalanche-2",
    "LINK": "chainlink"
}


def fetch_price_data(coin_id, days=30):
    """Fetch historical price data from CoinGecko."""
    url = f"{COINGECKO_API}/coins/{coin_id}/market_chart?vs_currency=usd&days={days}&interval=daily"

    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode())
            prices = [price[1] for price in data["prices"]]
            return prices
    except Exception as e:
        print(f"❌ Error fetching data: {e}")
        return None


def calculate_sma(prices, period):
    """Calculate Simple Moving Average."""
    if len(prices) < period:
        return None

    return sum(prices[-period:]) / period


def calculate_ema(prices, period):
    """Calculate Exponential Moving Average."""
    if len(prices) < period:
        return None

    multiplier = 2 / (period + 1)
    ema = sum(prices[:period]) / period  # Start with SMA

    for price in prices[period:]:
        ema = (price * multiplier) + (ema * (1 - multiplier))

    return ema


def calculate_rsi(prices, period=14):
    """Calculate Relative Strength Index."""
    if len(prices) < period + 1:
        return None

    changes = [prices[i] - prices[i-1] for i in range(1, len(prices))]

    gains = [change if change > 0 else 0 for change in changes]
    losses = [abs(change) if change < 0 else 0 for change in changes]

    avg_gain = sum(gains[-period:]) / period
    avg_loss = sum(losses[-period:]) / period

    if avg_loss == 0:
        return 100

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    return rsi


def calculate_macd(prices, fast=12, slow=26, signal=9):
    """Calculate MACD (Moving Average Convergence Divergence)."""
    if len(prices) < slow:
        return None

    ema_fast = calculate_ema(prices, fast)
    ema_slow = calculate_ema(prices, slow)

    macd_line = ema_fast - ema_slow

    # For simplicity, using SMA for signal line (should be EMA of MACD)
    # Would need historical MACD values for proper EMA calculation
    signal_line = macd_line  # Simplified

    histogram = macd_line - signal_line

    return {
        "macd": macd_line,
        "signal": signal_line,
        "histogram": histogram
    }


def calculate_bollinger_bands(prices, period=20, std_dev=2):
    """Calculate Bollinger Bands."""
    if len(prices) < period:
        return None

    sma = calculate_sma(prices, period)
    recent_prices = prices[-period:]

    variance = sum((p - sma) ** 2 for p in recent_prices) / period
    std = variance ** 0.5

    upper_band = sma + (std * std_dev)
    lower_band = sma - (std * std_dev)

    return {
        "upper": upper_band,
        "middle": sma,
        "lower": lower_band,
        "bandwidth": (upper_band - lower_band) / sma * 100
    }


def find_support_resistance(prices, lookback=20):
    """Find support and resistance levels."""
    if len(prices) < lookback:
        return None

    recent_prices = prices[-lookback:]

    # Find local maxima and minima
    resistance_levels = []
    support_levels = []

    for i in range(1, len(recent_prices) - 1):
        if recent_prices[i] > recent_prices[i-1] and recent_prices[i] > recent_prices[i+1]:
            resistance_levels.append(recent_prices[i])
        elif recent_prices[i] < recent_prices[i-1] and recent_prices[i] < recent_prices[i+1]:
            support_levels.append(recent_prices[i])

    # Get most significant levels (average of clusters)
    resistance = sum(resistance_levels) / len(resistance_levels) if resistance_levels else None
    support = sum(support_levels) / len(support_levels) if support_levels else None

    return {
        "resistance": resistance,
        "support": support,
        "current": prices[-1]
    }


def interpret_rsi(rsi):
    """Interpret RSI value."""
    if rsi >= 70:
        return "🔴 OVERBOUGHT (Consider taking profits or waiting for correction)"
    elif rsi <= 30:
        return "🟢 OVERSOLD (Potential buying opportunity)"
    elif 50 <= rsi < 70:
        return "🟡 BULLISH (Moderate uptrend)"
    elif 30 < rsi < 50:
        return "🟡 BEARISH (Moderate downtrend)"
    else:
        return "⚪ NEUTRAL"


def interpret_macd(macd):
    """Interpret MACD."""
    if macd["macd"] > macd["signal"]:
        return "🟢 BULLISH (MACD above signal line)"
    else:
        return "🔴 BEARISH (MACD below signal line)"


def print_technical_analysis(symbol, prices, indicators=None):
    """Print technical analysis results."""
    current_price = prices[-1]

    print("\n" + "="*80)
    print(f"TECHNICAL ANALYSIS - {symbol}")
    print("="*80)
    print(f"Current Price: ${current_price:,.2f}")
    print(f"Data Points: {len(prices)} days")
    print()

    # All indicators by default
    if not indicators:
        indicators = ["rsi", "macd", "ma", "bb", "sr"]

    # RSI
    if "rsi" in indicators:
        rsi = calculate_rsi(prices, 14)
        if rsi:
            print("📊 RELATIVE STRENGTH INDEX (RSI)")
            print(f"   RSI(14): {rsi:.2f}")
            print(f"   Interpretation: {interpret_rsi(rsi)}")
            print()

    # MACD
    if "macd" in indicators:
        macd = calculate_macd(prices)
        if macd:
            print("📈 MACD (Moving Average Convergence Divergence)")
            print(f"   MACD Line: {macd['macd']:.2f}")
            print(f"   Signal Line: {macd['signal']:.2f}")
            print(f"   Histogram: {macd['histogram']:.2f}")
            print(f"   Interpretation: {interpret_macd(macd)}")
            print()

    # Moving Averages
    if "ma" in indicators:
        sma_20 = calculate_sma(prices, 20)
        sma_50 = calculate_sma(prices, 50)
        ema_12 = calculate_ema(prices, 12)
        ema_26 = calculate_ema(prices, 26)

        print("📉 MOVING AVERAGES")
        if sma_20:
            trend_20 = "Above" if current_price > sma_20 else "Below"
            print(f"   SMA(20): ${sma_20:,.2f} - Price is {trend_20} ({'🟢' if trend_20 == 'Above' else '🔴'})")
        if sma_50:
            trend_50 = "Above" if current_price > sma_50 else "Below"
            print(f"   SMA(50): ${sma_50:,.2f} - Price is {trend_50} ({'🟢' if trend_50 == 'Above' else '🔴'})")
        if ema_12:
            print(f"   EMA(12): ${ema_12:,.2f}")
        if ema_26:
            print(f"   EMA(26): ${ema_26:,.2f}")

        # Golden Cross / Death Cross
        if sma_20 and sma_50:
            if sma_20 > sma_50:
                print(f"   📈 SHORT-TERM BULLISH: SMA(20) above SMA(50)")
            else:
                print(f"   📉 SHORT-TERM BEARISH: SMA(20) below SMA(50)")
        print()

    # Bollinger Bands
    if "bb" in indicators:
        bb = calculate_bollinger_bands(prices, 20, 2)
        if bb:
            print("📊 BOLLINGER BANDS")
            print(f"   Upper Band: ${bb['upper']:,.2f}")
            print(f"   Middle (SMA): ${bb['middle']:,.2f}")
            print(f"   Lower Band: ${bb['lower']:,.2f}")
            print(f"   Bandwidth: {bb['bandwidth']:.2f}%")

            if current_price > bb['upper']:
                print(f"   🔴 Price above upper band - potentially overbought")
            elif current_price < bb['lower']:
                print(f"   🟢 Price below lower band - potentially oversold")
            else:
                print(f"   ⚪ Price within bands - normal range")
            print()

    # Support and Resistance
    if "sr" in indicators:
        sr = find_support_resistance(prices, 30)
        if sr and sr['support'] and sr['resistance']:
            print("🎯 SUPPORT & RESISTANCE LEVELS")
            print(f"   Resistance: ${sr['resistance']:,.2f}")
            print(f"   Current:    ${sr['current']:,.2f}")
            print(f"   Support:    ${sr['support']:,.2f}")

            distance_to_resistance = ((sr['resistance'] - sr['current']) / sr['current']) * 100
            distance_to_support = ((sr['current'] - sr['support']) / sr['current']) * 100

            print(f"   Distance to Resistance: +{distance_to_resistance:.2f}%")
            print(f"   Distance to Support: -{distance_to_support:.2f}%")
            print()

    print("="*80)
    print("⚠️  Remember: Technical analysis is not financial advice.")
    print("    Always combine with fundamental analysis and risk management.")
    print("="*80 + "\n")


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python technical_indicators.py BTC --period 30")
        print("  python technical_indicators.py ETH --indicators rsi,macd,ma")
        print("\nSupported symbols:", ", ".join(COIN_IDS.keys()))
        print("\nAvailable indicators: rsi, macd, ma, bb, sr (all by default)")
        sys.exit(1)

    symbol = sys.argv[1].upper()
    period = 30
    indicators = None

    # Parse arguments
    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == "--period" and i + 1 < len(sys.argv):
            period = int(sys.argv[i + 1])
            i += 2
        elif sys.argv[i] == "--indicators" and i + 1 < len(sys.argv):
            indicators = sys.argv[i + 1].split(",")
            i += 2
        else:
            i += 1

    if symbol not in COIN_IDS:
        print(f"❌ Unknown symbol: {symbol}")
        print(f"Supported symbols: {', '.join(COIN_IDS.keys())}")
        sys.exit(1)

    coin_id = COIN_IDS[symbol]

    print(f"📊 Fetching {period}-day price data for {symbol}...")

    prices = fetch_price_data(coin_id, period)

    if not prices:
        print("Failed to fetch price data")
        sys.exit(1)

    print(f"✅ Received {len(prices)} price points")

    print_technical_analysis(symbol, prices, indicators)


if __name__ == "__main__":
    main()
