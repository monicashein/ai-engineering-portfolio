"""P1a lab: variables, numbers, strings and f-strings using synthetic meter data."""

# Raw input (messy, as it often arrives from source systems)
raw_meter_id = "  mtr-00123 "
customer = "tan ah kow"
previous_kwh = 10234.5
current_kwh = 10598.25
days = 31
rate_per_kwh = 0.2985      # synthetic tariff (SGD)
tax_rate = 0.09

# TODO 1: clean the meter id -> "MTR-00123" (remove spaces, uppercase)
meter_id = raw_meter_id.strip().upper()

# TODO 2: format the customer name in title case -> "Tan Ah Kow"
customer_name = customer.title()

# TODO 3: compute usage, cost before tax, tax amount and total
usage_kwh = current_kwh - previous_kwh
cost = usage_kwh * rate_per_kwh
tax = cost * tax_rate
total = cost + tax

# TODO 4: average kWh per day (float) and number of full weeks in the period (int)
avg_per_day = usage_kwh / days
full_weeks = days // 7

# TODO 5: print the summary using f-strings so the output matches the expected
print("==============================")
print("       UTILITY BILL SUMMARY   ")
print("==============================")
print(f"Meter ID:     {meter_id}")
print(f"Customer:     {customer_name}")
print(f"Usage:        {usage_kwh:.2f} kWh")
print(f"Daily Avg:    {avg_per_day:.2f} kWh/day")
print(f"Billing Days: {days} days ({full_weeks} full weeks)")
print("------------------------------")
print(f"Cost (subtotal): ${cost:.2f}")
print(f"Tax ({tax_rate * 100:.0f}%):       ${tax:.2f}")
print(f"Total Due:    ${total:.2f}")
print("==============================")

label = 11
print(f"{'Meter':<{label}}: {meter_id}")
print(f"{'Customer':<{label}}: {customer_name}")
print(f"{'Usage':<{label}}: {usage_kwh:.2f} kWh over {days} days ({full_weeks} full weeks)")
print(f"{'Avg/day':<{label}}: {avg_per_day:.2f} kWh")
print(f"{'Cost':<{label}}: ${cost:.2f}")
print(f"{f'Tax ({tax_rate:.0%})':<{label}}: ${tax:.2f}")
print(f"{'Total':<{label}}: ${total:.2f}")
