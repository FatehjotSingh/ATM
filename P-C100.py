class ATM(object):
    def __init__(self,card,pin):
        self.card= card
        self.pin=pin

    def Balance(self):
        print('your balance is nonexistent')
    def Withdrawal(self,amount,removal):
        newamount=amount-removal
        print(newamount)

def New():
 Cardno = input('enter card no. ')
 Pin = input('enter pin ')
 NewUser=ATM(Cardno,Pin)
 print('Choose your activity')
 print('1.balance Enquiry ; 2.Withdrawal')
 dat=int(input('your choice '))
 if(dat==1):
     NewUser.Balance()
 elif(dat==2):
     am= int(input('enter amount '))
     rm = int(input('enter removal '))
     NewUser.Withdrawal(am,rm)
 else:
     print('please enter a number between 1 and 2 only ')

New()