class Loan:
    
    def __init__(self, annualInterestRate=2.5, numberOfYears=1, loanAmount=1000):

        if annualInterestRate <= 0 :
         raise ValueError("Invalid annualInterestRate")
 
        if numberOfYears <= 0 :
         raise ValueError("Invalid numberOfYears")
       
        if loanAmount <= 0 :
         raise ValueError("Invalid loanAmount")
      
        self.__annualInterestRate = annualInterestRate
        self.__numberOfYears = numberOfYears
        self.__loanAmount = loanAmount
     
  
    def getAnnualInterestRate(self):
        return self.__annualInterestRate
    

    def setAnnualInterestRate(self, annualInterestRate):
        if annualInterestRate <= 0 :
         raise ValueError("Invalid annualInterestRate")
        self.__annualInterestRate = annualInterestRate

    def getNumberOfYears(self): 
        return self.__numberOfYears


    def setNumberOfYears(self, numberOfYears):
        if numberOfYears <= 0 :
         raise ValueError("Invalid numberOfYears")
        self.__numberOfYears = numberOfYears
     
    def getLoanAmount(self):
        return self.__loanAmount
     
    def setLoanAmount(self, loanAmount):
        if loanAmount <= 0 :
         raise ValueError("Invalid loanAmount")
        self.__loanAmount = loanAmount
     
     
    def getMonthlyPayment(self):
        monthlyInterestRate = self.__annualInterestRate / 1200
        numberOfPayments = self.__numberOfYears*12
        monthlyPayment = self.__loanAmount * monthlyInterestRate * (1+ monthlyInterestRate) * numberOfPayments \
    / ((1 + monthlyInterestRate) * numberOfPayments -1)

        return monthlyPayment
   

    def getTotalPayment(self):
        totalPayment = self.getMonthlyPayment() * self.__numberOfYears * 12
        return totalPayment
   
try:
 l =  Loan(7.5, 30, 100000)
 print("Total payment: " + str(l.getTotalPayment()))
except ValueError as e:
 print(e)

try:
 m = Loan(-1, 3, 3)
 print("Total payment: " + str(m.getTotalPayment())) 
except ValueError as e:
 print(e)