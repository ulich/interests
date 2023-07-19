import unittest
from interests import calculate_interests

class TestCalculateDailyInterest(unittest.TestCase):

    def test_positive_transactions(self):
        transactions = [
            {'date': "21.02.2023", 'amount': 10_000},
            {'date': "23.02.2023", 'amount': 10_000},
            {'date': "26.05.2023", 'amount': -5_000},
            {'date': "17.07.2023", 'amount': -15_000},
        ]
        annual_interest_rate = 3.7 / 100.0
        end_date = "17.09.2023"

        interests = calculate_interests(transactions, annual_interest_rate, end_date)
        self.assertAlmostEqual(interests, 271.85, 2)

    def test_no_transactions(self):
        transactions = []
        annual_interest_rate = 3.7 / 100.0
        end_date = "17.07.2023"

        interest = calculate_interests(transactions, annual_interest_rate, end_date)
        self.assertEqual(interest, 0)

    def test_single_transaction(self):
        transactions = [
            {'date': "01.01.2023", 'amount': 10_000},
        ]
        annual_interest_rate = 5 / 100.0
        end_date = "01.07.2023"

        interest = calculate_interests(transactions, annual_interest_rate, end_date)
        self.assertAlmostEqual(interest, 250, places=2)

    def test_last_transaction_after_end_date(self):
        transactions = [
            {'date': "21.02.2023", 'amount': 10_000},
            {'date': "26.08.2023", 'amount': -5000},
        ]
        annual_interest_rate = 3.7 / 100.0
        end_date = "17.07.2023"

        with self.assertRaises(Exception) as context:
            calculate_interests(transactions, annual_interest_rate, end_date)
        
        self.assertEqual("Last transaction is after end date", str(context.exception))
            
    def test_negative_balance(self):
        transactions = [
            {'date': "21.02.2023", 'amount': 10_000},
            {'date': "23.02.2023", 'amount': -9_000},
            {'date': "26.05.2023", 'amount': -2_000},
        ]
        annual_interest_rate = 3.7 / 100.0
        end_date = "17.07.2023"

        with self.assertRaises(Exception) as context:
            calculate_interests(transactions, annual_interest_rate, end_date)
        
        self.assertEqual("Transaction 3 made balance negative, this is not supported", str(context.exception))

if __name__ == '__main__':
    unittest.main()
