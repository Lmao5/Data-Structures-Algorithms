from credit_card import CreditCard
class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and
    fees."""

    def __init__(self, customer, bank, acnt, limit, apr):
        """Create a new predatory credit card instance."""
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
        self._count = 10
    def charge(self, price):
        success = super().charge(price)
        if not success:
            self._balance += 5
        else:
            self._count += 1
            if self._count > 10:
                self._balance += 1
        return success
    def process_month(self):
        self._balance *= pow(1 + self._apr, 1/12)
        self._balance += 1
        """Assess monthly interest on outstanding balance."""

apr = 0.0825
if __name__ == '__main__':
    wallet = []
    wallet.append(PredatoryCreditCard('John Lee', 'DBS',
    '5391 0375 9387 5309', 2500, apr) )
    wallet.append(PredatoryCreditCard('John Lee', 'OCBC',
    '3485 0399 3395 1954', 3500, apr) )
    wallet.append(PredatoryCreditCard('John Lee', 'Maybank',
    '5391 0375 9387 5309', 5000, apr) )
    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)
        
    for c in range(3):
        print('Customer =', wallet[c].get_customer())
        print('Bank =', wallet[c].get_bank())
        print('Account =', wallet[c].get_account())
        print('Limit =', wallet[c].get_limit())
        print('Balance =', wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New balance =', wallet[c].get_balance())
            wallet[c].process_month()
            print('New balance with interest=', wallet[c].get_balance())
        print()
