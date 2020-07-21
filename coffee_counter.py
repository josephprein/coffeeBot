class CoffeeCounter:

    def __init__(self, member, count):
        self.member = member
        self.count = count

    def getCount(self):
        return self.count

    def increment(self):
        self.count +=1

    def message(self):
        if self.count < 2:
            message = self.member.mention + " you have had " + str(self.count) + " cup of coffee."
        else:
            message = self.member.mention + " you have had " + str(self.count) + " cups of coffee."
        return message

    def reset(self):
        self.count = 0
