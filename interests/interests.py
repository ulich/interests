from datetime import datetime
from days360 import days360

def calculate_interests(transactions, annual_interest_rate, end_date):
    daily_interest_rate = annual_interest_rate / 360.0
    
    transactions.sort(key=lambda x: _parse_date(x['date']))
    
    if len(transactions) == 0:
        return 0
    
    if _parse_date(transactions[-1]['date']) > _parse_date(end_date):
        raise Exception("Last transaction is after end date")
    
    transactions.append({'date': end_date, 'amount': 0})
    
    current_balance = 0.0
    total_interest = 0.0
    
    for i in range(len(transactions)):
        if i == 0:
            current_balance += transactions[i]['amount']
            continue

        transaction = transactions[i]
        prev_transaction = transactions[i - 1]
        
        days = days360(_parse_date(prev_transaction['date']), _parse_date(transaction['date']), method="EU")
        
        interests = current_balance * daily_interest_rate * days
        total_interest += interests
        
        print(f"{prev_transaction['date']} - {transaction['date']}: Days[{days:3}] Balance[{current_balance:10,}] Interests[{interests:7.2f}]")

        current_balance += transaction['amount']
        if current_balance < 0:
            raise Exception(f"Transaction {i + 1} made balance negative, this is not supported")

    return total_interest


def _parse_date(date_str):
    return datetime.strptime(date_str, "%d.%m.%Y")
