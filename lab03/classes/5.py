class Account :
    def __init__(self, owner, balance = 0) :
        self.owner = owner
        self.balance = balance 
        
    def __str__(self):
        print('Account owner: {} \nAccount balance {}'.format(self.owner, self.balance))
        
    def deposit(self, deposit) :
        self.balance = self.balance + deposit
        print('Your current balance is {}'.format(self.balance))
        
    def withdraw(self, withdraw):
            if withdraw > self.balance:
                print('You dont have enough money. You have only {} in your account'.format(self.balance))
            else:
                self.balance = self.balance - withdraw
                print('Withdrawal Accepted. Your current balance is {}'.format(self.balance))

mtstr = Account("Aboa", 555)

mtstr.deposit(155)
mtstr.__str__()
mtstr.withdraw(720)
