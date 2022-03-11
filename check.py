
class Operations:

    def __init__(self):
        self.a = 5
        self.b = 5

    def mul(self):

        self.a += 1
        self.b += 1
        return self.a*self.b

    def div(self):

        self.a += 1
        self.b += 1
        return self.a//self.b

if __name__ == "__main__":

    opr = Operations()
    aDiv = opr.div()
    aMul = opr.mul()
    print(aDiv)
    print(aMul)

    