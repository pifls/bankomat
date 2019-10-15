class Card:
  def __init__(self, idCode, pinCode, balance):
    self.idCode = idCode
    self.pinCode = pinCode
    self.balance = balance

  def getId(self):
    return self.idCode

  def getPin(self):
    return self.pinCode
    
  def getBalance(self):
    return self.balance

  def withdrawMoney(self, money):
    money = int(money)
    if money <= self.balance:
      self.balance = self.balance - money
      return 'New account balance: ' + str(self.balance)
    else:
      return 'Not enough money on account'

  def putMoney(self, money):
    money = int(money)
    self.balance = self.balance + money
    return 'New account balance: ' + str(self.balance)