
rem=3

def hadd(a,b):
    # sum of two bits expressed as boolean
    # Parameters:
    #a--boolean:The first bit
    #b--boolean:The second bit

    return ((a or b) and not (a and b), a and b)
    #returns tuple (s0,s1)= s1s0 where s1 and s0 are boolean

def add(a,b,c):
    #sum of three bits expressed as boolean
    # Parameters:
    #a--boolean:The first bit
    #b--boolean:The second bit
    #c--boolean:The third bit
    (x0,x1)=hadd(a,b)
    (x2,x3)=hadd(x0,c)
    return (x2, x1 or x3)
    #returns (s0,s1) which is equal to s1s0 in boolean

def add4(a0,a1,a2,a3,b0,b1,b2,b3,c):
    #sum of 2 4-bit numerals a3a2a1a0 and b3b2b1b0 expressed as booleans
    #a3a2a1a0+b3b2b1b0
    (s0,s1)=add(a0,b0,c)
    (s2,s3)=add(a1,b1,s1)
    (s4,s5)=add(a2,b2,s3)
    (s6,s7)=add(a3,b3,s5)
    return (s0,s2,s4,s6,s7)
    #returns a 5-bit numeral expressed in boolean

def hcmp(a,b):
    #if a!=b then to find if a>b or b<a
    #a--boolean:the first bit
    #b--boolean:the second bit
    if a==False:
        return False
    else:
        return True

def cmp(a0,a1,a2,a3, b0,b1,b2,b3):
    #compare 2 4-bit numerals a3a2a1a0 and b3b2b1b0 expressed in booleans
    # if a3a2a1a0>=b3b2b1b0 returns True otherwise False
    x=(a0,a1,a2,a3)
    y=(b0,b1,b2,b3)
    (a0,a1,a2,a3)=x
    (b0,b1,b2,b3)=y
    if x==y:
        return True
    elif a3!=b3:
        return hcmp(a3,b3)
    elif a2!=b2:
        return hcmp(a2,b2)
    elif a1!=b1:
        return hcmp(a1,b1)
    elif a0!=b0:
        return hcmp(a0,b0)

def hsub(a,b):
    #subtraction of 2 bits expressed in booleans and taken in order
    #a-b
    #a--boolean:the first bit
    #b--boolean:the second bit
    return ((a or b) and not(a and b),(not a)and b)
    #returns difference and borrow bit as a tuple whose elements are in boolean

def fsub(a,b,c):
    #subtraction of 2 bits and one borrow bit
    #a--boolean:The first bit
    #b--boolean:The second bit
    #c--boolean:The third bit
    (s0,s1)=hsub(a,b)
    (s2,s3)=hsub(s0,c)
    return (s2, s1 or s3)
    #returns tuple with elements who are in boolean

def sub4(a0,a1,a2,a3, b0,b1,b2,b3):
    #subtraction of 2 4-bit numerals a0a1a2a3 and b0b1b2b3 expressed as booleans
    #a0a1a2a3 - b0b1b2b3
    # returns tuple --4 bit difference along with one bit for sign which are in boolean
    if cmp(a0,a1,a2,a3, b0,b1,b2,b3)==True:

        (s0,s1)=fsub(a0,b0,False)
        (s2,s3)=fsub(a1,b1,s1)
        (s4,s5)=fsub(a2,b2,s3)
        (s6,s7)=fsub(a3,b3,s5)
        return (s0,s2,s4,s6,False)

    elif cmp(a0,a1,a2,a3, b0,b1,b2,b3)==False:

        (s0,s1)=fsub(b0,a0,False)
        (s2,s3)=fsub(b1,a1,s1)
        (s4,s5)=fsub(b2,a2,s3)
        (s6,s7)=fsub(b3,a3,s5)
        return (s0,s2,s4,s6,True)

def add8(a,b,c):
    #addition of 2 8-bit numerals and a carry bit expressed as booleans
    (a0,a1,a2,a3,a4,a5,a6,a7) = a
    (b0,b1,b2,b3,b4,b5,b6,b7) = b
    (d0,d1,d2,d3,d4) = add4(a0,a1,a2,a3,b0,b1,b2,b3,c)
    (d5,d6,d7,d8,cout)=add4(a4,a5,a6,a7,b4,b5,b6,b7,d4)
    s=(d0,d1,d2,d3,d5,d6,d7,d8)
    return (s,cout)
    # returns tuple--9 bit numeral where cout is carry bit ,in booleans

def mul4(a,b):
    #product of 2 4-bit numerals a0a1a2a3 and b0b1b2b3 expressed in booleans
    #a0a1a2a3*b0b1b2b3
    (a0,a1,a2,a3)=a
    (b0,b1,b2,b3)=b
    if(b0,b1,b2,b3) ==(False,False,False,False):
        return (False,False,False,False,False,False,False,False)
    else:
        (x1,x2,x3,x4,x5)=sub4(b0,b1,b2,b3,True,False,False,False)
        (y0,y1,y2,y3,y4,y5,y6,y7)=mul4((a0,a1,a2,a3),(x1,x2,x3,x4))
        (A1,A2,A3,A4,A5,A6,A7,A8),A9=add8((a0,a1,a2,a3,False,False,False,False),(y0,y1,y2,y3,y4,y5,y6,y7),False)
        return (A1,A2,A3,A4,A5,A6,A7,A8)
    # returns 8 bit numeral product in booleans
