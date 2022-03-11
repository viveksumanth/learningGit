
class Operations:

    def __init__(self):
        self.x = 5
        self.y = 5

    def mul(self):

        self.a += 1
        self.b += 1
        return self.a*self.b

    def div(self):

        self.x += 1
        self.y += 1
        return self.x//self.y

if __name__ == "__main__":

    opr = Operations()
    aDiv = opr.div()
    aMul = opr.mul()
    print(aDiv)
    print(aMul)

    