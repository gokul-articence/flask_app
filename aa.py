# create a class for banking application, function
    # - statement, account open, deposit, balance check

class Account:
    def __init__(self,name,age,addre,pan,balance):
        self.statement=[]
        self.name=name
        self.age=age
        self.addre=addre
        self.pan=pan
        self.balance=balance
        self.statement.append(('deposit',balance,self.balance))

    def deposit(self,amt):
        self.balance+=amt
        self.statement.append(('deposit',amt,self.balance))


    def withdraw(self,amt):
        self.balance-=amt
        self.statement.append(('withdraw',amt,self.balance))
    
    def get_statement(self):
        for i in self.statement:
            print(i)
        
    def current_balance(self):
        print(self.balance)

person_1=Account("trisha",19,"vellore","terla",100000)
person_2=Account("thiru",19,"vellore","terla",100000)
person_3=Account("kalai",19,"tanjaore","terla",200)
person_4=Account("srinivas",19,"vellore","terla",100000000)

person_1.deposit(49000)
# person_2.withdraw(2000)
# person_3.get_statement()
# person_4.withdraw(30000)
person_1.withdraw(30000)
person_1.current_balance()
person_1.deposit(10000)
person_1.current_balance()
person_1.get_statement()



