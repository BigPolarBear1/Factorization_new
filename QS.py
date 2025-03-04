##Author: Essbee Vanhoutte
##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!WORK IN PROGRESS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
##Modified version of: https://github.com/Maosef/Quadratic-Sieve
##Added my own number theoretical results to use Quadratic coefficients

from math import fabs, ceil, sqrt, exp, log, log2
import random
from itertools import chain
import sympy
from bisect import bisect_left
import itertools
import sys
import argparse
import multiprocessing
import time
import copy
from timeit import default_timer
key=0                 #Define a custom modulus to factor
keysize=12            #Generate a random modulus of specified bit length
workers=8           #max amount of parallel processes to use
sieve_interval=100000
g_enable_custom_factors=0
g_p=107
g_q=41
base=5 #Used for generating quadratic coefficients.. need to increase this or sieve_interval if we cant construct a big enough matrix and increasing the factor base is not an option.
bit_tol=-5 #Needs to be adjusted based on base value.... uncomment print("psmooth_cands: ",len(psmooth_cands)) in gen_smooths to help adjust it... function should return sufficient candidates.
second_base=1000 #factor base, at size 2000 gauss elim will take about a minute.

##Key gen function##
def power(x, y, p):
    res = 1;
    x = x % p;
    while (y > 0):
        if (y & 1):
            res = (res * x) % p;
        y = y>>1; # y = y/2
        x = (x * x) % p;
    return res;

def miillerTest(d, n):
    a = 2 + random.randint(1, n - 4);
    x = power(a, d, n);
    if (x == 1 or x == n - 1):
        return True;
    while (d != n - 1):
        x = (x * x) % n;
        d *= 2;
        if (x == 1):
            return False;
        if (x == n - 1):
            return True;
    # Return composite
    return False;

def isPrime( n, k):
    if (n <= 1 or n == 4):
        return False;
    if (n <= 3):
        return True;
    d = n - 1;
    while (d % 2 == 0):
        d //= 2;
    for i in range(k):
        if (miillerTest(d, n) == False):
            return False;
    return True;

def generateLargePrime(keysize = 1024):
    while True:
        num = random.randrange(2**(keysize-1), 2**(keysize))
        if isPrime(num,4):
            return num

def findModInverse(a, m):
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

def generateKey(keySize):
    while True:
        p = generateLargePrime(keySize)
        print("[i]Prime p: "+str(p))
        q=p
        while q==p:
            q = generateLargePrime(keySize)
        print("[i]Prime q: "+str(q))
        n = p * q
        print("[i]Modulus (p*q): "+str(n))
        count=65537
        e =count
        if gcd(e, (p - 1) * (q - 1)) == 1:
            break

    phi=(p - 1) * (q - 1)
    d = findModInverse(e, (p - 1) * (q - 1))
    publicKey = (n, e)
    privateKey = (n, d)
    print('[i]Public key - modulus: '+str(publicKey[0])+' public exponent: '+str(publicKey[1]))
    print('[i]Private key - modulus: '+str(privateKey[0])+' private exponent: '+str(privateKey[1]))
    return (publicKey, privateKey,phi,p,q)
##END KEY GEN##

def bitlen(int_type):
    length=0
    while(int_type):
        int_type>>=1
        length+=1
    return length   

def gcd(a,b): # Euclid's algorithm
    if b == 0:
        return a
    elif a >= b:
        return gcd(b,a % b)
    else:
        return gcd(b,a)

def solve_lin_con(a,b,m):
    ##ax=b mod m
    g=gcd(a,m)
    a,b,m = a//g,b//g,m//g
    return pow(a,-1,m)*b%m  

def isqrt(n): # Newton's method, returns exact int for large squares
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def build_matrix(factor_base, smooth_nums, factors):
    M = []
    factor_base.insert(0, -1)
        
    for i in range(len(smooth_nums)):
        
        exp_vector = make_vector(factors[i],factor_base)
        M.append(exp_vector)

    M = transpose(M)
    return (False, M)

def formal_deriv(y,x):
    result=(2*x)+(y)
    return result

def find_r(mod,total):
    mo,i=mod,0
    while (total%mod)==0:
        mod=mod*mo
        i+=1
    return i

def find_all_solp(n,start,limit):
    ##This code is shit, if lifting takes too long, blame this function.
    rlist=[]    
    if start == 2:
        rlist=[[0,1]]
    else:
        i=0
        while i<start:
            if squareRootExists(n,start,i):
                temp=find_solution_x(n,start,i)
                rlist.append(temp[0])
            i+=1
    newlist=[]
    mod=start**2
    g=0
    while g<limit-1:
        rlist2=[]
        for i in rlist:
            if i[1]== -1:
                rlist2.append([i[0],-1,i[2]])
                continue
            j=0
            while j<len(i)-1:
                j+=1
                x=i[j]
                y=i[0]
                while 1:
                    xo=x    
                    while 1:
                        test,test2=equation(y,x,n,mod)
                        if test == 0:
                            b=0
                            while b<len(rlist2):
                                if rlist2[b][0] == y and rlist2[b][1] != -1:
                                    rlist2[b].append(x)
                                    b=-1
                                    break
                                b+=1    
                            if b!=-1:       
                                rlist2.append([y,x])
                        x+=mod//start
                        if x>mod-1:
                            break
                    x=xo    
                    y+=mod//start   
                    if y>mod-1:
                        break
            b=0
            while b<len(rlist2):
                if rlist2[b][1] != -1:
                    x=rlist2[b][1]
                    y=rlist2[b][0]
                    re=formal_deriv(y,x)
                    r=find_r(start,re)
                    ceiling=(start*r)+1
                    ceiling=start**ceiling
                    if mod < ceiling:
                        b+=1
                        continue    
                    rlist2[b]=[]
                    rlist2[b].append(y)
                    rlist2[b].append(-1)
                    rlist2[b].append(ceiling)
                b+=1    
        rlist=rlist2.copy() 
        mod*=start
        g+=1
    fe=[]
    
    for i in rlist2:
        if i[0] not in fe:
            fe.append(i[0])
            if i[1]==-1:
                y=i[0]
                while 1:
                    y+=i[2]
                    if y<(mod//start):
                        fe.append(y)
                    else:
                        break   
    newlist.append(mod//start)
    fe.sort()
    newlist.append(fe)  
    return newlist
    
def transpose(matrix):
#transpose matrix so columns become rows, makes list comp easier to work with
    new_matrix = []
    for i in range(len(matrix[0])):
        new_row = []
        for row in matrix:
            new_row.append(row[i])
        new_matrix.append(new_row)
    return(new_matrix)

        
def gauss_elim(M):
#reduced form of gaussian elimination, finds rref and reads off the nullspace
#https://www.cs.umd.edu/~gasarch/TOPICS/factoring/fastgauss.pdf
    marks = [False]*len(M[0])
    
    for i in range(len(M)): #do for all rows
        row = M[i]
        for num in row: #search for pivot
            if num == 1:
                j = row.index(num) # column index
                marks[j] = True
                
                for k in chain(range(0,i),range(i+1,len(M))): #search for other 1s in the same column
                    if M[k][j] == 1:
                        for i in range(len(M[k])):
                            M[k][i] = (M[k][i] + row[i])%2
                break
    M = transpose(M)
    sol_rows = []
    for i in range(len(marks)): #find free columns (which have now become rows)
        if marks[i]== False:
            free_row = [M[i],i]
            sol_rows.append(free_row)
    
    if not sol_rows:
        return 0,0,0#("No solution found. Need more smooth numbers.")
    return sol_rows,marks,M

def solve_row(sol_rows,M,marks,K=0):
    solution_vec, indices = [],[]
    free_row = sol_rows[K][0] # may be multiple K
    for i in range(len(free_row)):
        if free_row[i] == 1: 
            indices.append(i)
    
    for r in range(len(M)): #rows with 1 in the same column will be dependent
        for i in indices:
            if M[r][i] == 1 and marks[r]:
                solution_vec.append(r)
                break
               
    solution_vec.append(sol_rows[K][1]) 
    return(solution_vec)
    
def solve(solution_vec,smooth_nums,N,xlist):
    solution_nums = [smooth_nums[i] for i in solution_vec]
    x_nums = [xlist[i] for i in solution_vec]
    Asquare = 1
    for n in solution_nums:
        Asquare *= n

    b=1
    for n in x_nums:
        b *= n
    a = isqrt(Asquare)
   # print(str(a)+"^2 = "+str(b)+"^2 mod "+str(N))
    if b > a:
        temp=a
        a=b
        b=temp
    factor = gcd(a-b,N)
    return factor


def create_partial_results(sols):
    new=[]
    i=0
    while i < len(sols):
        j=0
        new.append(sols[i])
        new.append([])
        while j < len(sols[i+1]):
            k=0
            temp=sols[i+1][j]
            tot=sols[i]
            while k < len(sols):
                if sols[k] != sols[i]:
                    inv=inverse(sols[k],sols[i])
                    temp=temp*inv*sols[k]
                    tot*=sols[k]
                k+=2
            new[-1].append(temp%tot)    
            j+=1
        i+=2    
    return new,tot    

def verify_smooth(factor_base, smooth_cands, x_cands):
    '''verifies smooth relations from candidates'''
    def factor(n, factor_base): # trial division from factor base
        factors = []
        if n < 0:
            factors.append(-1)
            n //= -1
                
        for p in factor_base:

            while n % p == 0:
                factors.append(p)
                n //= p
        if n == 1 or n == -1:
            return factors
            
        else:
            return None

    smooth_nums = []
    factors = []
    x_list = []
        
    for i in range(len(smooth_cands)):
            
        fac = factor(smooth_cands[i], factor_base)
            
        if fac:
            smooth_nums.append(smooth_cands[i])
            factors.append(fac)
            x_list.append(x_cands[i])
    return (smooth_nums, x_list, factors)
def gen_smooths(sol,mod,factor_list,n,mod2):
    global sieve_interval
    start=sol**2
    n_bits = [0 for x in range(sieve_interval)]
    p_bits = [0 for x in range(sieve_interval)]
    i=0
    n_indices=[]
    p_indices=[]
    smooth_nums=[]
    x_list=[]
    factors=[]
    while i < len(factor_list):
        ret=solve_lin_con(n,start%factor_list[i],factor_list[i])
        n_indices.append(ret)
        p_indices.append(factor_list[i]-ret)
        i+=1
    

   
    n_indices, n_bits=sieve(n_indices, n_bits,factor_list)
    p_indices, p_bits=sieve(p_indices, p_bits,factor_list)
        
    nsmooth_cands, nx_cands, psmooth_cands, px_cands=find_candidates(n_bits,p_bits,0,sol,n)
    n_smooths, n_xs, n_factors = verify_smooth(factor_list, nsmooth_cands, nx_cands)
    p_smooths, p_xs, p_factors = verify_smooth(factor_list, psmooth_cands, px_cands)
    #print("psmooth_cands: ",len(psmooth_cands))
    smooth_nums += p_smooths
    x_list += p_xs
    factors += p_factors

    smooth_nums = n_smooths + smooth_nums 
    x_list = n_xs + x_list
    factors = n_factors + factors


    return smooth_nums, x_list, factors

def generate_smooths(procnum,return_dict,n,enum,flist,mod,primeslist2):
    sm=[]
    xlist=[]
    flist=[]
    mod2=1
    test=[[],[],[]]
    for p in primeslist2:
        mod2*=p
    for comb in itertools.product(*enum):
        sols=0
        for l in comb:  
            sols+=l
            del l
        del comb
        factor_list=primeslist2
        sols=sols%mod
        smooth_nums, x_list, factors=gen_smooths(sols,mod,factor_list,n,mod2)
        sm.extend(smooth_nums)
        xlist.extend(x_list)
        flist.extend(factors)
        test[0]=sm
        test[1]=xlist
        test[2]=flist
        return_dict[procnum]=test
    return 0         

def sieve(indices, bits, base_list):
    global sieve_interval
    base_bits = [round(log2(p)) for p in base_list]
    I=sieve_interval
    new_indices = []
    k=0
    while k<len(indices):
        p=base_list[k]
        starts = indices[k]
        if starts >= I:
            indices[k]=starts-I #For next round
            continue
        for j in range(starts, len(bits), p):
            bits[j] += base_bits[k] 
        indices[k] = j + p - I
        k+=1
    new_indices.append(starts)
    return new_indices, bits
    
def find_candidates(n_bits,p_bits,dis_from_center,sol,n):
    global sieve_interval
    I=sieve_interval
    nx_cands = []  
    nsmooth_cands = []
    px_cands = []  
    psmooth_cands = []

    if sol == 0:
        sol+=n
    start=sol**2
    for i in range(I-1, 1, -1):  # going backwards to preserve order
        x = sol
        thres = int(log2(abs(x**2))) - bit_tol  # threshold
        if abs(n_bits[i]) >= thres and abs(p_bits[i])>1:  # found B-smooth candidate
            nsmooth_cands.append(start-i*n)
            nx_cands.append(x)

    for i in range(1,I):
        x = sol
        thres = int(log2(abs(x**2))) - bit_tol  
        if abs(p_bits[i]) >= thres and abs(p_bits[i])>1 :  # found B-smooth candidate
            psmooth_cands.append(start+i*n)
            px_cands.append(x)
    #print("psmooth_cands: ",psmooth_cands)        
    return nsmooth_cands, nx_cands, psmooth_cands, px_cands

def launch(lists,n,primeslist2):
    sr=round(n**0.5)
    allsols,allbigsums=[],[]
    bigsums,bigmodulus=[],[]
    i=0
    while i < len(lists):
        sums,modulus=normalize_sols(n,lists[i])  
        bigsums.append(sums)
        bigmodulus.append(modulus)
        i+=1
    enum=[]
    i=0
    factor_list=[]
    cores=1
    j=0
    while j < len(bigsums):
        i=0
        enum.append([])
        factor_list.append([])
        while i < len(bigsums[j]):
            enum[-1].append(bigsums[j][i+1])
            factor_list[-1].append(bigsums[j][i])
            i+=2
        j+=1    

    manager=multiprocessing.Manager()
    return_dict=manager.dict()
    jobs=[]
    procnum=0
    print("[*]Launching attack")
    z=0
    while z < len(bigsums):
        p=multiprocessing.Process(target=generate_smooths, args=(procnum,return_dict,n,enum[z],factor_list[z],bigmodulus[z],primeslist2))
        jobs.append(p)
        p.start()
        procnum+=1
        z+=1            
    
    for proc in jobs:
        proc.join(timeout=0)        
    lastlen=0
    start=default_timer()
    while 1:
        time.sleep(1)
        z=0
        balive=0
        while z < len(jobs):
            if jobs[z].is_alive():
                balive=1
            z+=1
        check=return_dict.values()
        tlen=0
        for item in check:
            tlen+=len(item[0])
        if tlen > lastlen:
            print("[i]Smooths found: "+str(tlen)+"/"+str(second_base))
            lastlen=tlen
        if balive == 0 or tlen > second_base:
            for proc in jobs:
                proc.terminate()
            fres=check
            i=0
            fsm=[]
            fxlist=[]
            flist=[]
            while i < len(fres):
                fsm.extend(fres[i][0])
                fxlist.extend(fres[i][1])
                flist.extend(fres[i][2])
                i+=1
            duration = default_timer() - start
                        
            print("[i]Smooth finding took: "+str(duration)+" (seconds)")     
            QS(n,primeslist2,fsm,fxlist,flist)
            print("[i]All procs exited")
            return 0    
    return 

def equation(y,x,n,mod):
    rem=(x**2)+y*-x+n
    rem2=rem%mod
    return rem2,rem  
def make_vector(n_factors,factor_base): 
    '''turns factorization into an exponent vector mod 2'''
    
    exp_vector = [0] * (len(factor_base))
    # print(n,n_factors)
    for j in range(len(factor_base)):
        if factor_base[j] in n_factors:
            exp_vector[j] = (exp_vector[j] + n_factors.count(factor_base[j])) % 2
    return exp_vector
def QS(n,factor_list,sm,xlist,flist):
    if len(sm) < len(factor_list):
        print("[i]Not enough smooth numbers found")
        return 0

    if len(sm)-100 > len(factor_list): #reduce for smaller matrix
        print('[*]trimming smooth relations...')
        del sm[len(factor_list):]
        del xlist[len(factor_list):]
        del flist[len(factor_list):]  
    is_square, t_matrix = is_square, t_matrix = build_matrix(factor_list, sm, flist)#build_matrix(sm,factor_list)
    print("[*]Starting Gaussian elimination")
    start=default_timer()
    sol_rows,marks,M = gauss_elim(t_matrix) 
    if sol_rows == 0:
        return 0
    duration = default_timer() - start
                        
    print("[i]Gauss_elim took: "+str(duration)+" (seconds)") 
    solution_vec = solve_row(sol_rows,M,marks,0)
    print("[*]Checking solutions")
    start=default_timer()
    factor = solve(solution_vec,sm,n,xlist) 

    for K in range(1,len(sol_rows)):
        if (factor == 1 or factor == n):
            solution_vec = solve_row(sol_rows,M,marks,K)
            factor = solve(solution_vec,sm,n,xlist)
        else:
            print("[i]Found factors of: "+str(n))
            print("P: ",factor)
            print("Q: ",n//factor)
            duration = default_timer() - start
                        
            print("[i]Found factors in: "+str(duration)+" (seconds)") 
            return factor, n/factor     
    return 0
def legendre(a, p):
    return pow_mod(a,(p-1)//2,p) 

def squareRootExists(n,p,b):
    b=b%p
    c=n%p
    bdiv = (b*inverse(2,p))%p
    alpha = (pow_mod(bdiv,2,p)-c)%p
    if alpha == 0:
        return 1
    
    if legendre(alpha,p)==1:
        return 1
    return 0

def inverse(a, m):
    if gcd(a, m) != 1:
        return None
    u1,u2,u3 = 1,0,a
    v1,v2,v3 = 0,1,m
    while v3 != 0:
        q = u3//v3
        v1,v2,v3,u1,u2,u3=(u1-q*v1),(u2-q*v2),(u3-q*v3),v1,v2,v3
    return u1%m

def pow_mod(base, exponent, modulus):
    return pow(base,exponent,modulus)  

def find_sol_for_p(n,p):
    rlist=[]
    y=0
    while y<p:
            if squareRootExists(n,p,y):
                rlist.append(y)
            y+=1
    return rlist

def find_solution_x(n,mod,y):
    ##to do: can use tonelli if this ends up taking too long
    rlist=[]
    x=0
    while x<mod:
        test,test2=equation(y,x,n,mod)
        if test == 0:
            rlist.append([y,x])     
        x+=1
    return rlist


def normalize_sols(n,sum1):  
    sum1,total=create_partial_results(sum1)

    return sum1,total    

def build_sols_list(prime1,n,test1,mod1):
    found1=0
    mult1=[]
    mult1=[]
    mult1.append(prime1)
    if prime1==2:
        mult1=[2,[1]]
    else:   
        mult1.append(find_sol_for_p(n,mult1[0]))
    lift=2
    liftlim=1
    if prime1==2:
        liftlim=6
    elif prime1==3:
        liftlim=1
    elif prime1 < 1:
        liftlim=1
    if prime1 < 3:
        while 1:
            oldmult1=copy.deepcopy(mult1)
            mult1=find_all_solp(n,prime1,lift)
            if(len(mult1[1])-len(oldmult1[1])>prime1-1):
                if lift > liftlim:
                    mult1=oldmult1
                    break
            if lift > liftlim:
                mult1=oldmult1
                break       
            lift+=1 
    test1.append(mult1[0])
    test1.append(mult1[1])
                
    mod1*=mult1[0]
    return test1,mod1

def init(n,primeslist1,primeslist2):    
    global workers
    lists=[]
    mods=[]
    i=0
    while i < workers:
        lists.append([])
        mods.append(1)
        i+=1
    i=0
    while i < len(primeslist1):
        prime1=primeslist1[i]
        lists[i%workers],mods[i%workers]=build_sols_list(prime1,n,lists[i%workers],mods[i%workers])
        i+=1          
    launch(lists,n,primeslist2)
    return 

def get_primes(start,stop):
    return list(sympy.sieve.primerange(start,stop))

def main():
    global key
    global base
    global workers
    if g_p !=0 and g_q !=0 and g_enable_custom_factors == 1:
        p=g_p
        q=g_q
        key=p*q
    if key == 0:
        print("\n[*]Generating rsa key with a modulus of +/- size "+str(keysize)+" bits")
        publicKey, privateKey,phi,p,q = generateKey(keysize//2)
        n=p*q
        key=n
    else:
        print("[*]Attempting to break modulus: "+str(key))
        n=key

    sys.set_int_max_str_digits(1000000)
    sys.setrecursionlimit(1000000)
    bits=bitlen(n)
    primeslist=[]
    primeslist1=[]
    primeslist2=[]

    print("[i]Modulus length: ",bitlen(n))
    primeslist.extend(get_primes(2,10000000))
    sbaseprimes=[]
    i=0
    while i < base*workers:
        primeslist1.append(primeslist[0])
        i+=1
        primeslist.pop(0)    
    i=0
    sbaseprimes.extend(get_primes(2,10000000))
    while i < second_base:
        primeslist2.append(sbaseprimes[0]) 
        i+=1 
        sbaseprimes.pop(0)
        
    init(n,primeslist1,primeslist2)



def print_banner():
    print("Polar Bear was here       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                       ")
    print("⠀         ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣀⣀⣀⣤⣤⠶⠾⠟⠛⠛⠛⠛⠷⢶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⠶⠾⠛⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⢻⣿⣟ ⠀⠀⠀⠀      ")
    print("⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣶⠶⠶⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠳⣦⣄⠀⠀⠀⠀⠀   ")
    print("⠀⠀⠀⠀⠀⣠⡾⠟⠉⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠹⣿⡆⠀⠀⠀   ")
    print("⠀⠀⠀⣠⣾⠟⠀⠀⠀⠈⢉⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡀⠀⠀   ")
    print("⢀⣠⡾⠋⠀⢾⣧⡀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⠈⣷⠀⠀   ")
    print("⢿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⢹⡆⣿⡆⠀   ")
    print("⠈⢿⣿⣛⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣆⣸⠇⣿⡇⠀   ")
    print("⠀⠀⠉⠉⠙⠛⠛⠓⠶⠶⠿⠿⠿⣯⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠟⠀⣿⡇⠀   ")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠠⣦⢠⡄⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡞⠁⠀⠀⣿⡇⠀   ")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣶⠄⠀⠀⠀⠀⠀⠀⢸⣿⡇⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠇⣼⠋⠀⠀⠀⠀⣿⡇⠀   ")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⣿⣦⠀⠀⠀⠀⠀⠀⠀⣿⣧⣤⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⣿⣾⠃⠀⠀⠀⠀⠀⣿⠛⠀   ")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠀⠘⢿⣦⣀⠀⠀⠀⠀⠀⠸⣇⠀⠉⢻⡄⠀⠀⠀⠀⠀⠀⡘⣿⢿⣄⣠⠀⠀⠀⠀⠸⣧⡀   ")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠀⠀⠀⠙⣿⣿⡄⠀⠀⠀⠀⠹⣆⠀⠀⣿⡀⠀⠀⠀⠀⠀⣿⣿⠀⠙⢿⣇⠀⠀⠀⠀⠘⣷   ")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡏⠀⠀⢀⣿⡿⠻⢿⣷⣦⠀⠀⠀⠹⠷⣤⣾⡇⠀⠀⠀⠀⣤⣸⡏⠀⠀⠈⢻⣿⠀⠀⠀⠘⢿   ")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠿⠁⠀⠀⢸⡿⠁⠀⠀⠙⢿⣧⠀⠀⠀⠀⠠⣿⠇⠀⠀⠀⠀⣸⣿⠁⠀⠀⢀⣾⠇⠀⠀⠀⠀⣼   ")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⡁⠀⠀⠀⠀⣸⡇⠀⠀⠀⠀⠈⠿⣷⣤⣴⡶⠛⡋⠀⠀⠀⠀⢀⣿⡟⠀⠀⣴⠟⠁⠀⣀⣀⣀⣠⡿   ")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣤⣾⣧⣤⡿⠁⠀⠀⠀⠀⠀⠀⠀⠈⣿⣀⣾⣁⣴⣏⣠⣴⠟⠉⠀⠀⠀⠻⠶⠛⠛⠛⠛⠋⠉⠀   ")
    return

def parse_args():
    global keysize,key,workers,debug,show,printcols
    parser = argparse.ArgumentParser(description='Factor stuff')
    parser.add_argument('-key',type=int,help='Provide a key instead of generating one') 
    parser.add_argument('-keysize',type=int,help='Generate a key of input size')    
    parser.add_argument('-workers',type=int,help='# of cpu cores to use')
    parser.add_argument('-debug',type=int,help='1 to enable more verbose output')
    parser.add_argument('-show',type=int,help='1 to render input matrix. 2 to render input+ouput matrix. -1 to render input matrix truncated by --printcols. -2 to render input+output matrix truncated by --printcols')
    parser.add_argument('--printcols',type=int,help='Truncate matrix output if enabled')

    args = parser.parse_args()
    if args.keysize != None:    
        keysize = args.keysize
    if args.key != None:    
        key=args.key
    if args.workers != None:  
        workers=args.workers
    if args.debug != None:
        debug=args.debug    
    if args.show != None:
        show=args.show
        if show < 0 and args.printcols  != None:
            printcols=args.printcols    
    return

if __name__ == "__main__":
    parse_args()
    print_banner()
    main()
