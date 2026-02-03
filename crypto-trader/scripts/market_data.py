#!/usr/bin/env python3
"""
Cryptocurrency Market Data Fetcher

Fetches real-time cryptocurrency market data from CoinGecko API including:
- Current price in USD
- 24h price change
- Market cap
- Trading volume
- Price history

Usage:
    python market_data.py BTC ETH SOL
    python market_data.py BTC --days 7
    python market_data.py --top 10
"""

import sys
import json
import urllib.request
import urllib.error
from datetime import datetime

COINGECKO_API = "https://api.coingecko.com/api/v3"

# Common coin ID mappings
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
    "LINK": "chainlink",
    "UNI": "uniswap",
    "ATOM": "cosmos",
    "LTC": "litecoin",
    "BCH": "bitcoin-cash"
}


def fetch_json(url):
    """Fetch JSON data from URL with error handling."""
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as e:
        print(f"❌ HTTP Error {e.code}: {e.reason}")
        return None
    except urllib.error.URLError as e:
        print(f"❌ Connection Error: {e.reason}")
        return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None


def get_coin_id(symbol):
    """Convert symbol to CoinGecko coin ID."""
    symbol = symbol.upper()
    return COIN_IDS.get(symbol, symbol.lower())


def fetch_market_data(coin_ids):
    """Fetch market data for multiple coins."""
    ids_str = ",".join(coin_ids)
    url = f"{COINGECKO_API}/coins/markets?vs_currency=usd&ids={ids_str}&order=market_cap_desc&sparkline=false"

    data = fetch_json(url)
    if not data:
        return None

    results = []
    for coin in data:
        results.append({
            "symbol": coin["symbol"].upper(),
            "name": coin["name"],
            "price": coin["current_price"],
            "price_change_24h": coin["price_change_percentage_24h"],
            "market_cap": coin["market_cap"],
            "volume_24h": coin["total_volume"],
            "circulating_supply": coin.get("circulating_supply", 0),
            "market_cap_rank": coin.get("market_cap_rank", "N/A")
        })

    return results


def fetch_price_history(coin_id, days=7):
    """Fetch historical price data."""
    url = f"{COINGECKO_API}/coins/{coin_id}/market_chart?vs_currency=usd&days={days}"

    data = fetch_json(url)
    if not data or "prices" not in data:
        return None

    prices = []
    for timestamp, price in data["prices"]:
        dt = datetime.fromtimestamp(timestamp / 1000)
        prices.append({
            "date": dt.strftime("%Y-%m-%d %H:%M"),
            "price": price
        })

    return prices


def fetch_top_coins(limit=10):
    """Fetch top coins by market cap."""
    url = f"{COINGECKO_API}/coins/markets?vs_currency=usd&order=market_cap_desc&per_page={limit}&page=1&sparkline=false"

    data = fetch_json(url)
    if not data:
        return None

    results = []
    for coin in data:
        results.append({
            "rank": coin["market_cap_rank"],
            "symbol": coin["symbol"].upper(),
            "name": coin["name"],
            "price": coin["current_price"],
            "price_change_24h": coin["price_change_percentage_24h"],
            "market_cap": coin["market_cap"],
            "volume_24h": coin["total_volume"]
        })

    return results


def format_number(num):
    """Format large numbers with suffixes."""
    if num >= 1_000_000_000:
        return f"${num/1_000_000_000:.2f}B"
    elif num >= 1_000_000:
        return f"${num/1_000_000:.2f}M"
    elif num >= 1_000:
        return f"${num/1_000:.2f}K"
    else:
        return f"${num:.2f}"


def print_market_data(results):
    """Pretty print market data."""
    print("\n" + "="*80)
    print("CRYPTOCURRENCY MARKET DATA")
    print("="*80 + "\n")

    for coin in results:
        change_emoji = "📈" if coin["price_change_24h"] >= 0 else "📉"
        change_color = "+" if coin["price_change_24h"] >= 0 else ""

        print(f"🪙 {coin['name']} ({coin['symbol']})")
        print(f"   Rank: #{coin['market_cap_rank']}")
        print(f"   Price: ${coin['price']:,.2f}")
        print(f"   24h Change: {change_emoji} {change_color}{coin['price_change_24h']:.2f}%")
        print(f"   Market Cap: {format_number(coin['market_cap'])}")
        print(f"   24h Volume: {format_number(coin['volume_24h'])}")
        print()


def print_top_coins(results):
    """Pretty print top coins table."""
    print("\n" + "="*100)
    print("TOP CRYPTOCURRENCIES BY MARKET CAP")
    print("="*100)
    print(f"{'Rank':<6} {'Symbol':<8} {'Name':<20} {'Price':<15} {'24h Change':<12} {'Market Cap':<15}")
    print("-"*100)

    for coin in results:
        change_emoji = "📈" if coin["price_change_24h"] >= 0 else "📉"
        change_str = f"{coin['price_change_24h']:+.2f}%"

        print(f"#{coin['rank']:<5} {coin['symbol']:<8} {coin['name']:<20} "
              f"${coin['price']:>12,.2f} {change_emoji} {change_str:<10} "
              f"{format_number(coin['market_cap']):<15}")

    print()


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python market_data.py BTC ETH SOL")
        print("  python market_data.py BTC --days 7")
        print("  python market_data.py --top 10")
        print("\nSupported symbols:", ", ".join(COIN_IDS.keys()))
        sys.exit(1)

    # Check if fetching top coins
    if sys.argv[1] == "--top":
        limit = int(sys.argv[2]) if len(sys.argv) > 2 else 10
        print(f"📊 Fetching top {limit} cryptocurrencies...")

        results = fetch_top_coins(limit)
        if results:
            print_top_coins(results)
        else:
            print("Failed to fetch data")
        return

    # Parse coin symbols
    symbols = []
    days = None

    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == "--days":
            days = int(sys.argv[i + 1])
            i += 2
        else:
            symbols.append(sys.argv[i])
            i += 1

    if not symbols:
        print("❌ No coin symbols provided")
        sys.exit(1)

    # Convert symbols to coin IDs
    coin_ids = [get_coin_id(s) for s in symbols]

    print(f"📊 Fetching market data for: {', '.join(symbols)}...")

    # Fetch and display market data
    results = fetch_market_data(coin_ids)
    if results:
        print_market_data(results)
    else:
        print("Failed to fetch market data")
        return

    # Fetch price history if requested
    if days and len(symbols) == 1:
        print(f"📈 Fetching {days}-day price history for {symbols[0]}...")
        history = fetch_price_history(coin_ids[0], days)

        if history:
            print("\n" + "="*60)
            print(f"PRICE HISTORY - {symbols[0]} (Last {days} days)")
            print("="*60)

            # Show sample of history (first and last few entries)
            sample_size = min(5, len(history) // 2)
            for entry in history[:sample_size]:
                print(f"{entry['date']}: ${entry['price']:,.2f}")

            if len(history) > sample_size * 2:
                print("...")

            for entry in history[-sample_size:]:
                print(f"{entry['date']}: ${entry['price']:,.2f}")

            print(f"\nTotal data points: {len(history)}")

            # Calculate price change
            start_price = history[0]["price"]
            end_price = history[-1]["price"]
            change_pct = ((end_price - start_price) / start_price) * 100
            change_emoji = "📈" if change_pct >= 0 else "📉"

            print(f"\n{days}-day change: {change_emoji} {change_pct:+.2f}%")
            print(f"Start: ${start_price:,.2f} → End: ${end_price:,.2f}")


if __name__ == "__main__":
    main()
