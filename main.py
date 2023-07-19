from interests.interests import calculate_interests

transactions = [
    {'date': "21.02.2023", 'amount': 10_000},
    {'date': "23.02.2023", 'amount': 10_000},
    {'date': "26.05.2023", 'amount': -5000},
]
annual_interest_rate = 3.7 / 100.0
end_date = "17.07.2023"
exemption_order = 50  # Freistellungsauftrag

total_interest_earned = calculate_interests(transactions, annual_interest_rate, end_date)
print(f"Total interest earned: {total_interest_earned:.2f}")

taxable_amount = max(total_interest_earned - exemption_order, 0)
print(f"Taxable amount: {taxable_amount:.2f}")

tax = taxable_amount * 0.25
print(f"Tax: {tax:.2f}")

soli = tax * 0.055
print(f"Solidarity surcharge: {soli:.2f}")

net_interest_earned = total_interest_earned - tax - soli
print(f"Net interest earned: {net_interest_earned:.2f}")
