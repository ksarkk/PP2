class Account :
    def __init__(self, owner, balance = 0) :
        self.owner = owner
        self.balance = balance 
        
    def __str__(self):
        print('Account owner: {} \nAccount balance {}'.format(self.owner, self.balance))
        
    def deposit(self, deposit_amt) :
        self.balance = self.balance + deposit_amt
        print('Your current balance is {}'.format(self.balance))
        
    def withdraw(self, withdraw_amt):
            if withdraw_amt > self.balance:
                print('You dont have enough money. You have only {} in your account'.format(self.balance))
            else:
                self.balance = self.balance - withdraw_amt
                print('Withdrawal Accepted. Your current balance is {}'.format(self.balance))

mtstr = Account("Aboa", 555)

mtstr.deposit(155)
mtstr.__str__()
mtstr.withdraw(720)
