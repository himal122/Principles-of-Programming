class Loan:
    
    def __init__(self, annualInterestRate=2.5, numberOfYears=1, loanAmount=1000):

        self.__annualInterestRate = annualInterestRate
        self.__numberOfYears = numberOfYears
        self.__loanAmount = loanAmount
     
  
    def getAnnualInterestRate(self):
        return self.__annualInterestRate
    

    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate

    def getNumberOfYears(self): 
        return self.__numberOfYears


    def setNumberOfYears(self, numberOfYears):
        self.__numberOfYears = numberOfYears
     
    def getLoanAmount(self):
        return self.__loanAmount
     
    def setLoanAmount(self, loanAmount):
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
   

l =  Loan(7.5, 30, 100000)
print("Total payment: " + str(l.getTotalPayment()))

m = Loan(-1, 3, 3)
print("Total payment: " + str(m.getTotalPayment()))