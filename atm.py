class Atm:
  def __init__(self, cards):
    self.cards = cards

  def isInt(self, s):
    try: 
      int(s)
      return True
    except ValueError:
        return False
  
  def exit(self):
    print('Thank you for using our service.')

  def validateCard(self, cardId):
    valid = False
    if not self.isInt(cardId):
      return False
    cardId = int(cardId)
    for card in self.cards:
      if cardId == card.getId():
        valid = True
    return valid
  
  def validatePin(self, cardId, pinCode):
    valid = False
    if not self.isInt(pinCode):
      return False
    pinCode = int(pinCode)
    for card in self.cards:
      if cardId == card.getId() and pinCode == card.getPin():
        valid = True
    return valid
  
  def performAction(self, action, cardId, money):
    for card in self.cards:
      if cardId == card.getId():
        correctCard = card

    if action == '1':
      print(correctCard.getBalance())
    elif action == '2':
      print(correctCard.withdrawMoney(money))
    elif action == '3':
      print(correctCard.putMoney(money))
    else:
      print("Invalid action")
  
  def ifPinValid(self, cardId):
    while True:
      print("Please perform action: \n 1 - account balance\n 2 - withdraw money\n 3 - put money\n 0 - exit")
      action = input()
      if action == '1':
        self.performAction(action, cardId, 0)
      elif action == '2':
        print("Enter amount to withdraw:")
        money = input()
        if not self.isInt(money):
          print("Invalid input")
        else:
          self.performAction(action, cardId, money)
      elif action == '3':
        print("Enter amount to put into account:")
        money = input()
        if not self.isInt(money):
          print("Invalid input")
        else:
          self.performAction(action, cardId, money)
      elif action == '0':
        self.exit()
        break
      else:
        print("Incorrect action")
  
  def ifCardValid(self, cardId):
    pinChances = 3
    while pinChances > 0:
      pinCode = input()
      if pinCode == '0':
        self.exit()
        break
      pinValid = self.validatePin(cardId, pinCode)
      if pinValid:
        print("PIN Correct")
        self.ifPinValid(cardId)
        break
      else:
        print("PIN Incorrect.")
      pinChances = pinChances - 1
    if pinChances == 0:
      print("Wrong PIN for third time. Please contact customer service")

  def runAtm(self):
    print('Please put your card into ATM.           / 0 to exit')
    while True:
      cardId = input()
      if cardId == '0':
        self.exit()
        break
      cardValid = self.validateCard(cardId)
      if cardValid:
        print("Card is valid. Please give PIN code.     / 0 to exit")
        self.ifCardValid(int(cardId))
        break
      else:
        print("Card invalid. Try again.                 / 0 to exit")