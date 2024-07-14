class BankAccount:
    def __init__(self):
        self.balance = {1: 0, 5: 0, 10: 0, 25: 0, 100: 0}

    def deposit(self, coins):
        for denomination, amount in coins.items():
            if denomination in self.balance:
                self.balance[denomination] += amount
            else:
                raise ValueError("Invalid coin denomination")

    def withdraw(self, amount):
        if amount <= self.total():
            withdrawn_coins = {}
            for denomination in sorted(self.balance.keys(), reverse=True):
                num_coins = min(amount // denomination, self.balance[denomination])
                withdrawn_coins[denomination] = num_coins
                amount -= num_coins * denomination
            if amount == 0:
                for denomination, num_coins in withdrawn_coins.items():
                    self.balance[denomination] -= num_coins
                return withdrawn_coins
        raise ValueError("Insufficient funds")

    def total(self):
        return sum(denomination * num_coins for denomination, num_coins in self.balance.items())

# Test the BankAccount class
def test_bank_account():
    account = BankAccount()

    # Test deposit function
    account.deposit({1: 10, 5: 5, 10: 2, 25: 1, 100: 0})
    assert account.balance == {1: 10, 5: 5, 10: 2, 25: 1, 100: 0}

    # Test withdraw function
    assert account.withdraw(190) == {100: 1, 25: 3, 10: 1, 5: 1}
    assert account.balance == {1: 10, 5: 4, 10: 1, 25: 0, 100: 0}

    # Test total function
    assert account.total() == 294

    # Test insufficient funds
    try:
        account.withdraw(1000)
    except ValueError as e:
        assert str(e) == "Insufficient funds"

    # Test invalid denomination
    try:
        account.deposit({50: 5})
    except ValueError as e:
        assert str(e) == "Invalid coin denomination"

    print("All tests passed!")

if __name__ == "__main__":
    test_bank_account()
