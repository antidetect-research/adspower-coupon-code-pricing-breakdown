#!/usr/bin/env python3
"""
AdsPower Anti-Detect Browser Pricing & Long-Term Prepaid Discount Calculator 2026.
Calculates effective monthly fees and annual realized savings across Base and Pro tiers.
"""
import argparse

def calculate_discount(monthly_rate, months, discount_pct):
    base_total = monthly_rate * months
    discount_multiplier = (100.0 - discount_pct) / 100.0
    prepaid_total = base_total * discount_multiplier
    effective_monthly = prepaid_total / months if months > 0 else 0.0
    savings = base_total - prepaid_total
    return {
        "monthly_rate": monthly_rate,
        "months": months,
        "discount_pct": discount_pct,
        "base_total": base_total,
        "prepaid_total": prepaid_total,
        "effective_monthly": effective_monthly,
        "savings": savings
    }

def main():
    parser = argparse.ArgumentParser(description="AdsPower Plan & Annual Discount Calculator")
    parser.add_argument("--monthly-rate", type=float, default=50.0, help="Monthly base price in USD (default: $50.00 for 100 profiles)")
    parser.add_argument("--months", type=int, default=12, help="Subscription commitment duration in months (default: 12)")
    parser.add_argument("--discount-pct", type=float, default=40.0, help="Prepaid discount percentage (default: 40.0%)")
    args = parser.parse_args()

    res = calculate_discount(args.monthly_rate, args.months, args.discount_pct)
    print(f"Monthly Base Cost:       ${res['monthly_rate']:.2f}")
    print(f"Commitment Period:       {res['months']} months")
    print(f"Prepaid Discount:        {res['discount_pct']:.1f}%")
    print(f"Annual Prepaid Total:    ${res['prepaid_total']:.2f}")
    print(f"Effective Monthly:       ${res['effective_monthly']:.2f}/mo")
    print(f"Annual Realized Savings: ${res['savings']:.2f}/year")

if __name__ == "__main__":
    main()
