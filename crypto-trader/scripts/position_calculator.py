#!/usr/bin/env python3
"""
Position Size Calculator for Crypto Trading

Calculates optimal position size based on:
- Account size
- Risk percentage per trade
- Stop-loss distance
- Risk-reward ratio

Usage:
    python position_calculator.py --account 10000 --risk 2 --stop 5
    python position_calculator.py --account 10000 --risk 1.5 --entry 45000 --stop 43500
"""

import sys


def calculate_position_size(account_size, risk_percent, stop_loss_percent):
    """
    Calculate position size based on account risk.

    Args:
        account_size: Total account size in USD
        risk_percent: Risk percentage per trade (e.g., 2 for 2%)
        stop_loss_percent: Stop loss distance in percentage (e.g., 5 for 5%)

    Returns:
        Position size in USD
    """
    risk_amount = account_size * (risk_percent / 100)
    position_size = risk_amount / (stop_loss_percent / 100)

    return position_size, risk_amount


def calculate_position_from_prices(account_size, risk_percent, entry_price, stop_price):
    """
    Calculate position size from specific entry and stop prices.

    Args:
        account_size: Total account size in USD
        risk_percent: Risk percentage per trade
        entry_price: Entry price
        stop_price: Stop loss price

    Returns:
        Position size and number of units
    """
    risk_amount = account_size * (risk_percent / 100)
    stop_distance = abs(entry_price - stop_price)
    stop_percent = (stop_distance / entry_price) * 100

    position_size = risk_amount / (stop_distance / entry_price)
    units = position_size / entry_price

    return position_size, units, risk_amount, stop_percent


def calculate_risk_reward(entry_price, stop_price, take_profit_price):
    """Calculate risk-reward ratio."""
    risk = abs(entry_price - stop_price)
    reward = abs(take_profit_price - entry_price)

    if risk == 0:
        return None

    return reward / risk


def calculate_take_profit_targets(entry_price, stop_price, ratios=[2, 3, 5]):
    """Calculate take-profit targets for given risk-reward ratios."""
    risk = abs(entry_price - stop_price)
    direction = "long" if entry_price > stop_price else "short"

    targets = []
    for ratio in ratios:
        if direction == "long":
            target = entry_price + (risk * ratio)
        else:
            target = entry_price - (risk * ratio)

        targets.append({
            "ratio": ratio,
            "price": target,
            "gain_percent": ((target - entry_price) / entry_price) * 100
        })

    return targets


def print_position_analysis(account_size, risk_percent, position_size, risk_amount,
                            stop_percent, entry_price=None, stop_price=None,
                            units=None, leverage=1):
    """Print detailed position analysis."""
    print("\n" + "="*80)
    print("POSITION SIZE CALCULATOR")
    print("="*80 + "\n")

    print("📊 ACCOUNT INFORMATION")
    print(f"   Total Account Size: ${account_size:,.2f}")
    print(f"   Risk per Trade: {risk_percent}%")
    print(f"   Maximum Risk Amount: ${risk_amount:,.2f}")
    print()

    print("🎯 POSITION DETAILS")
    print(f"   Recommended Position Size: ${position_size:,.2f}")
    print(f"   Position as % of Account: {(position_size/account_size)*100:.2f}%")

    if leverage > 1:
        required_margin = position_size / leverage
        print(f"   Leverage: {leverage}x")
        print(f"   Required Margin: ${required_margin:,.2f}")

    if entry_price and units:
        print(f"   Entry Price: ${entry_price:,.2f}")
        print(f"   Units to Buy: {units:.6f}")

    print()

    print("🛡️ RISK MANAGEMENT")
    if stop_price:
        print(f"   Stop Loss Price: ${stop_price:,.2f}")
    print(f"   Stop Loss Distance: {stop_percent:.2f}%")
    print(f"   Maximum Loss if Stopped Out: ${risk_amount:,.2f} ({risk_percent}% of account)")
    print()

    # Risk warnings based on position size
    position_percent = (position_size / account_size) * 100

    if risk_percent > 2:
        print("⚠️  WARNING: Risk per trade exceeds 2% - considered aggressive")
    if position_percent > 50:
        print("⚠️  WARNING: Position size exceeds 50% of account - high concentration risk")
    if leverage > 1:
        print("⚠️  WARNING: Using leverage amplifies both gains and losses")

    print()


def print_take_profit_targets(entry_price, stop_price, targets):
    """Print take-profit target recommendations."""
    print("🎯 TAKE PROFIT TARGETS")
    print(f"   Based on Entry: ${entry_price:,.2f} | Stop: ${stop_price:,.2f}")
    print()

    for target in targets:
        print(f"   Target {target['ratio']}:1 R:R")
        print(f"      Price: ${target['price']:,.2f}")
        print(f"      Gain: {target['gain_percent']:+.2f}%")
        print()

    print("💡 Scaling Out Strategy:")
    print("   - Take 30-40% profit at 2:1 R:R")
    print("   - Take 30-40% profit at 3:1 R:R")
    print("   - Let remaining 20-30% run to 5:1+ with trailing stop")
    print()


def print_position_examples(account_size, risk_percent):
    """Print example positions with different stop losses."""
    print("📋 POSITION SIZE EXAMPLES FOR DIFFERENT STOP LOSSES")
    print()

    stop_examples = [2, 3, 5, 7, 10]

    print(f"{'Stop Loss':<12} {'Position Size':<20} {'% of Account':<15}")
    print("-" * 47)

    for stop in stop_examples:
        pos_size, _ = calculate_position_size(account_size, risk_percent, stop)
        pos_percent = (pos_size / account_size) * 100

        print(f"{stop}%{'':<10} ${pos_size:>12,.2f}{'':<6} {pos_percent:>5.1f}%")

    print()


def main():
    if len(sys.argv) < 2 or "--help" in sys.argv or "-h" in sys.argv:
        print("Usage:")
        print("\nOption 1: Calculate from percentages")
        print("  python position_calculator.py --account 10000 --risk 2 --stop 5")
        print("\nOption 2: Calculate from specific prices")
        print("  python position_calculator.py --account 10000 --risk 2 --entry 45000 --stop 43500")
        print("\nOption 3: Include take-profit targets")
        print("  python position_calculator.py --account 10000 --risk 2 --entry 45000 --stop 43500 --tp 48000")
        print("\nOption 4: Include leverage")
        print("  python position_calculator.py --account 10000 --risk 2 --stop 5 --leverage 3")
        print("\nParameters:")
        print("  --account: Total account size in USD (required)")
        print("  --risk: Risk percentage per trade, e.g., 2 for 2% (required)")
        print("  --stop: Stop loss percentage OR --entry/--stop for specific prices (required)")
        print("  --entry: Entry price (optional, use with --stop price)")
        print("  --tp: Take profit price (optional)")
        print("  --leverage: Leverage multiplier (default: 1)")
        print("  --examples: Show position examples for different stop losses")
        sys.exit(0)

    # Parse arguments
    account_size = None
    risk_percent = None
    stop_percent = None
    entry_price = None
    stop_price = None
    take_profit = None
    leverage = 1
    show_examples = False

    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == "--account" and i + 1 < len(sys.argv):
            account_size = float(sys.argv[i + 1])
            i += 2
        elif sys.argv[i] == "--risk" and i + 1 < len(sys.argv):
            risk_percent = float(sys.argv[i + 1])
            i += 2
        elif sys.argv[i] == "--stop" and i + 1 < len(sys.argv):
            value = float(sys.argv[i + 1])
            if value < 100:  # Assume percentage
                stop_percent = value
            else:  # Assume price
                stop_price = value
            i += 2
        elif sys.argv[i] == "--entry" and i + 1 < len(sys.argv):
            entry_price = float(sys.argv[i + 1])
            i += 2
        elif sys.argv[i] == "--tp" and i + 1 < len(sys.argv):
            take_profit = float(sys.argv[i + 1])
            i += 2
        elif sys.argv[i] == "--leverage" and i + 1 < len(sys.argv):
            leverage = float(sys.argv[i + 1])
            i += 2
        elif sys.argv[i] == "--examples":
            show_examples = True
            i += 1
        else:
            print(f"Unknown argument: {sys.argv[i]}")
            sys.exit(1)

    # Validate required parameters
    if not account_size or not risk_percent:
        print("❌ Error: --account and --risk are required")
        print("Use --help for usage information")
        sys.exit(1)

    # Calculate position size
    if entry_price and stop_price:
        # Calculate from specific prices
        position_size, units, risk_amount, stop_percent = calculate_position_from_prices(
            account_size, risk_percent, entry_price, stop_price
        )

        print_position_analysis(account_size, risk_percent, position_size, risk_amount,
                               stop_percent, entry_price, stop_price, units, leverage)

        # Calculate take-profit targets
        targets = calculate_take_profit_targets(entry_price, stop_price)
        print_take_profit_targets(entry_price, stop_price, targets)

        # If specific take-profit provided, calculate R:R
        if take_profit:
            rr = calculate_risk_reward(entry_price, stop_price, take_profit)
            if rr:
                print(f"💰 CUSTOM TAKE PROFIT")
                print(f"   Take Profit Price: ${take_profit:,.2f}")
                print(f"   Risk-Reward Ratio: {rr:.2f}:1")
                gain_percent = ((take_profit - entry_price) / entry_price) * 100
                gain_amount = (take_profit - entry_price) * units
                print(f"   Potential Gain: {gain_percent:+.2f}% (${gain_amount:,.2f})")
                print()

    elif stop_percent:
        # Calculate from percentages
        position_size, risk_amount = calculate_position_size(
            account_size, risk_percent, stop_percent
        )

        print_position_analysis(account_size, risk_percent, position_size, risk_amount,
                               stop_percent, leverage=leverage)

    else:
        print("❌ Error: Provide either --stop percentage OR --entry and --stop prices")
        sys.exit(1)

    # Show examples if requested
    if show_examples:
        print_position_examples(account_size, risk_percent)

    print("="*80)
    print("⚠️  RISK DISCLAIMER")
    print("="*80)
    print("This calculator is for educational purposes only.")
    print("Always:")
    print("  • Risk only what you can afford to lose")
    print("  • Never risk more than 1-2% per trade for conservative approach")
    print("  • Use stop losses on every trade")
    print("  • Be cautious with leverage - it amplifies both gains and losses")
    print("  • Consult with a financial advisor before making investment decisions")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()
