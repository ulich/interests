# interests

A small python script that calulates earning of interests on a savings account using the 360 day-year which is used by european banks.

You can provide multiple transactions that happen throughout the year with deposits and withdrawals:

```python
from interests import calculate_interests

transactions = [
    {'date': "21.02.2023", 'amount': 10_000},
    {'date': "23.02.2023", 'amount': 10_000},
    {'date': "26.05.2023", 'amount': -5000},
]
annual_interest_rate = 3.7 / 100.0
end_date = "17.07.2023"

total_interest_earned = calculate_interests(transactions, annual_interest_rate, end_date)
print(f"Total interest earned: {total_interest_earned:.2f}")
```

prints:
```
21.02.2023 - 23.02.2023: Days[  2] Balance[  10,000.0] Interests[   1.28]
21.02.2023 - 23.02.2023: Days[  2] Balance[  10,000.0] Interests[   2.06]
23.02.2023 - 26.05.2023: Days[ 93] Balance[  20,000.0] Interests[ 191.17]
26.05.2023 - 17.07.2023: Days[ 51] Balance[  15,000.0] Interests[  78.63]
Total interest earned: 271.85
```

## Running locally

Edit the values in main.py, then:

```
virtualenv venv
. ./venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Running tests

```
python -m unittest discover -s interests
```
