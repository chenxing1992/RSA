import ContinuedFractions, Arithmetic
import sys
from binascii import *
e=217356749319385698521929657544628507680950813122965981036139317973675569442588326220293299168756490163223201593446006249622787212268918299733683908813777695992195006830244088685311059537057855442978678020950265617092637544349098729925492477391076560770615398034890984685084288600014953201593750327846808762513
n=413514550275673527863957027545525175432824699510881864021105557583918890022061739148026915990124447164572528944722263717357237476264481036272236727160588284145055425035045871562541038353702292714978768468806464985590036061328334595717970895975121788928626837881214128786266719801269965024179019247618967408217
c=337907824405966440030495671003069758278111764297629248609638912154235544001123799434176915113308593275372838266739188034566867280295804636556069233774555055521212823481663542294565892061947925909547184805760988117713501561339405677394457210062631040728412334490054091265643226842490973415231820626551757008360


def hack_RSA(e,n):
    '''
    Finds d knowing (e,n)
    applying the Wiener continued fraction attack
    '''
    frac = ContinuedFractions.rational_to_contfrac(e, n)
    convergents = ContinuedFractions.convergents_from_contfrac(frac)
    
    for (k,d) in convergents:
        
        #check if d is actually the key
        if k!=0 and (e*d-1)%k == 0:
            phi = (e*d-1)//k
            s = n - phi + 1
            # check if the equation x^2 - s*x + n = 0
            # has integer roots
            discr = s*s - 4*n
            if(discr>=0):
                t = Arithmetic.is_perfect_square(discr)
                if t!=-1 and (s+t)%2==0:
                    print("Hacked!")
                    return d

# TEST functions

def test_hack_RSA():
    print("Testing Wiener Attack")
    print(" e = " );
    print (e)
    print(" n = " );
    print(n)
    print("d = ")
    print(hack_RSA(e, n))    
    print("m =")
    m = pow ( c , hack_RSA(e, n) , n )
    print unhexlify(format(m,'x'))
    
if __name__ == "__main__":
	test_hack_RSA()
	#print hack_RSA(e,n)
