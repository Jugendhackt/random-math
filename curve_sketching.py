from random import randint
import random, copy, JsonGenerator

print "works!"


# this code is supposed to do curve sketching (German: Kurvendiskussion) for you

# factorlist = [0.5, 0.5, 0.5, 0.75, 0.75, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6 ]



# 'typeclass' Show
class Show:
    def show(self):
        pass


# This is part of a bigger term, it represents one (x + n) in a polynom
class TermPart(Show):
    zero = None

    def __init__(self, zero, mult = 1):
        self.zero = zero

    # returns the value which would cause this term to become Zero
    def getZero(self):
        return -self.zero

    # show-instance for TermPart
    def show(self):
        if self.zero == 0:
            return "x"
        if self.zero < 0 :
            return "(x %s)" % self.zero
        return "(x + %s)" % self.zero


# This is part of a Polynome, especially the part a * x ^ b
# (in this case: mult * x ^ tiex, where tiex is short for 'tier of x')
class Mult(Show):
    mult = 1
    tiex = 0

    def __init__(self, mult = 1, tiex = 0):
        self.mult = mult
        self.tiex = tiex

    # returns the mu
    def getMult(self):
        return self.mult

    # returns the tier of X
    def getX(self):
        return self.tiex

    # increases the tier of x by one
    def incX(self):
        self.tiex += 1

    # decreases the tier of x by one
    def decX(self):
        self.tiex -= 1

    # show-instance for Mult
    def show(self):
        if self.mult == 0:
            return ""
        return ("%sx^%s" % (self.mult, self.tiex) )


# This represents a Zero-Term of the form a * (b + x) * (c + x) * ... + d
class ZeroTerm(Show):
    tier = None
    a = None
    d = None
    termList = []

    # For constructing you need the tier of the term, everything else es generated if required
    def __init__(self, tier, a = randint(1,5), d = 0):
        self.tier     = tier
        self.a        = a
        self.d        = d
        self.termList = copy.deepcopy(generateTerm(tier) )

    # show-instance for ZeroTerm
    def show(self):
        res = str(self.a) + ' * '
        for term in self.termList:
            res += term.show()
        return res

    # returns the zero-values of this particular term
    def getZeros(self):
        zeros = []
        for term in self.termList:
            zeros.append(term.getZero())
        return zeros

    # showing this Zero-Based-Term as a Polynome, meaning in the form: a * x ^ n + b * x ^ n-1 + ... + d
    def showAsPolynome(self):
        return fold(lambda x, y: y.show() + ' + ' + x, getPolynome(self), '')


# noZero as well as prefZero are numbers
def generateTermPart(noZero = None, prefZero = None):
    if prefZero != None:
        res = TermPart(prefZero)
    else:
        zero = randint(0,10) * random.choice ([-1, 1])
        if zero == noZero:
            res = generateTermPart(noZero)
        else:
            res = TermPart(zero)
    return res


# Generates a Term of tier (German: grad) n
def generateTerm(tier):
    terms = []
    for i in range(tier):
        terms.append(generateTermPart() )
    return terms


# fold without a first accumulator, same as mappend?
def fold1(f, l): # :: (a -> a -> a) -> [a] -> a
    if len(l) < 2:
        return l
    return fold(f, l[1:], l[0])


# fold ... self-describing :P
def fold(f, l, a): # :: (a -> b -> a) -> a -> [b] -> a
    """
    f: the function to apply
    l: the list to fold
    a: the accumulator, who is also the 'zero' on the first call
    """
    return a if(len(l) == 0) else fold(f, l[1:], f(a, l[0]))


# returns the list of monome-terms
def getPolynome(zeroTerm): # ZeroTerm -> [Mult]
    # schritt:
    #  - alle mults mit erstem Term multiplizieren, dann naechster schritt.
    m1 = [Mult(zeroTerm.a)]
    lists = zeroTerm.termList
    return fold(multStep, zeroTerm.termList, m1)

# multiplies one term with all of the 'Mult's up until now
def multStep(lmults, head): # :: [Mult] -> Term -> [Mult]
    res = []
    for m in lmults:
        res.append(multXTerm(m,head) )
    re = simplify(concat(res))[:]
    return re

# the concat-function ....
def concat(l): # :: [[a]] -> [a]
    return [item for sublist in l for item in sublist]


"""
# not-working version of simplify ...

def split(f, l):
    tr = filter(f,l)
    fa = filter(lambda x: not (f(x) ), l)
    return (tr, fa)

def simplify(mults): # :: [Mult] -> [Mult]
    def doWork(n, other):
        start = other[0]
        (ol, rest) = split(lambda x:isAddable(start, x), other)
        result = fold1(add, ol)
        if len(rest) < 1:
            return [result]
        return [result] + doWork(n+1, rest)
    return doWork(0, mults)
"""



# returns True if both of the Mults are of the same tier, meaning simply addable
def isAddable(m1, m2): # :: Mult -> Mult -> Bool .... required ?!
    return m1.tiex == m2.tiex


# adding two Mults if possible
def add(m1, m2): # :: Mult -> Mult -> 'Maybe Mult'
    if isAddable(m1, m2):
        return Mult(m1.mult + m2.mult, m1.tiex)
    return None

# multiplying a Mult with a Term, which results in a list of Mults
# e.g. a * x ^ b * (c + x) = c * a * x ^ b + a * x ^ b+1
def multXTerm(mult, term): # :: Mult -> Term -> [Mult]
    mult2 = copy.copy(mult)
    mult.mult *= term.zero
    mult2.incX()
    return [mult, mult2]

# working version of simplify, adding together all of those terms that are addable
def simplify(mults): # :: [Mult] -> [Mult]
    maxn = len(mults)
    newaccum = []
    for i in range(maxn):
        monome = filter(lambda x: isAddable(Mult(3,i), x), mults )
        if len(monome) > 1:
            newaccum.append(fold1(add, monome))
        if len(monome) == 1:
            newaccum.append(monome[0])
    return newaccum[:]







# Generating a Random Exercise asking for the zero-resulting values
def generatePolynomeExercise(n):
    zeroterm = ZeroTerm(n)
    zeros    = zeroterm.getZeros()
    aufgabe  = zeroterm.showAsPolynome() + "\n" + random.choice(["Berechne die nullstellen!", "Wo schneidet die Funktion die x-Achse?"])
    tipp     = random.choice(['Newton-Formel! xn+1 = xn - f(xn) / f\'(xn)', 'Polynomdivision!'])
    schritte = map( (lambda z: 'Nullstelle bei ' + str(z) ), zeros)
    return JsonGenerator.generateJsonDatei("Polynom_Nullstellen", aufgabe, zeros, tipp, schritte)




















"""

from random import randint
import random

for i in range (0, 10):
    # random int between 1 and 20
    x = randint(1, 19) * random.choice ([-1, 1])
    # randint (1, 19)
    factorlist = [0.5, 0.5, 0.5, 0.75, 0.75, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6 ]
    random.shuffle(factorlist)
    factor = factorlist[i] * random.choice([-1, 1])
    summand = randint (2, 20)

    result = factor * x + summand

    factorlist2 = [0.5, 0.5, 2, 2, 3, 3, 4, 4, 5, 5]
    random.shuffle (factorlist2)
    factor2 = factorList2[i] * random.choice ([-1, 1])

    summand2 = result - factor2 * x

#    if summand > 0:
#        line = "%sx + %s = %sx + %s    x = %s" % (factor, summand, factor2, summand2, x)
    if summand == 0:
        line = "%sx = %sx + %s    x = %s" % (factor, factor2, summand2, x)
    else:
        line = "%sx + %s = %sx + %s    x = %s" % (factor, summand, factor2, summand2, x)

    print line

"""






