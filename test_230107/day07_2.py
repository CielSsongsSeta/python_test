
def AbsSum(n1,n2) :
    result = 0
    if n1 < 0 :
        n1 = n1 * -1
    if n2 < 0 :
        n2 = n2 * -1
    result = n1 + n2
    return result

result1 = AbsSum(-1,3)
print(result1)

class c1 :
    def AbsSum(self, n1,n2) :
        result = 0
        if n1 < 0 :
            n1 = n1 * -1
        if n2 < 0 :
            n2 = n2 * -1
        self.n1 = n1
        self.n2 = n2
        result = n1 + n2
        return result
    def Last(self) :
        print(self.n1+self.n2)


c = c1()
c.AbsSum(3,5)
c.Last()
