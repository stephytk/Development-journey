
from csv import DictReader

class Transcationanalyser:
   
    def __init__(self):
       
       fr = open("ABSTRACTION\\bankanalyzer\\bank_transactions_500_records.csv")

       self.transactions =list(DictReader(fr))

       print((self.transactions),"records found")
    

    def debit_transactions(self):


        for t in  self.transactions:

            if t.get("type")=="debit":

                print(t)

    def credit_transaction(self):

        for t in self.transactions:

            if t.get("type")=="credit":

                print(t)


    def high_value_transcation(self): #amount>75000
    
        for t in self.transactions:

            if int(t.get ("amount"))>75000:

                print(t)

    def highest_debit(self): 

        high_deb = 0

        for t in self.transactions:

            if t.get("type")=="debit":

                amount = int(t.get("amount"))

                if amount > high_deb:

                    high_deb = amount

        print("Highest debit amount is ",high_deb)

    def highest_credit(self):

        high_credit = 0

        for t in self.transactions:

            if t.get("type") == "credit":

                amount = int(t.get("amount"))

                if amount > high_credit:

                    high_credit = amount

        print("Highest credit amount is ",high_credit)

    
analysis = Transcationanalyser()

analysis.debit_transactions()

analysis.credit_transaction()

analysis.high_value_transcation()

analysis.highest_debit()

analysis.highest_credit()
       


       








    
        
      

   