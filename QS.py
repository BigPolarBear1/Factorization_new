###Note: Modified https://github.com/NachiketUN/Quadratic-Sieve-Algorithm/blob/master/src/main.py with my own number theoretical findings.


from math import fabs, ceil, sqrt, exp, log
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
key=0                 #Define a custom modulus to factor
keysize=12            #Generate a random modulus of specified bit length
workers=8           #max amount of parallel processes to use

g_enable_custom_factors=0
g_p=107
g_q=41
sieve_interval=10
base=5
second_base=50
max_sieve=10 #Quit worker after this amount is found. Need to change this logic later and just loop workers until smooth_stop is reached.
smooth_stop=50  #Should be atleast the size of second_base
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


 


def build_matrix(smooth_nums,factor_base):
# generates exponent vectors mod 2 from previously obtained smooth numbers, then builds matrix

    def factor(n,factor_base):#trial division from factor base
       # print(n)
        factors = []
        if n < 0:
            factors.append(-1)
        for p in factor_base:
            if p == -1:
                pass
            else:
                while n % p == 0:# and n > 0:
                    factors.append(p)
                    n //= p
      #  print("factors: ",factors)               
        return factors

    M = []
    factor_base.insert(0,-1)

    for n in smooth_nums:
        exp_vector = [0]*(len(factor_base))
        n_factors = factor(n,factor_base)
      #  print(n,n_factors)
        for i in range(len(factor_base)):
            if factor_base[i] in n_factors:
                exp_vector[i] = (exp_vector[i] + n_factors.count(factor_base[i])) % 2


        
        M.append(exp_vector)
        
    return(False, transpose(M))
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
    #mprint(M)
    #M = optimize(M)
    marks = [False]*len(M[0])
    
    for i in range(len(M)): #do for all rows
        row = M[i]
        #print(row)
        
        for num in row: #search for pivot
            if num == 1:
                #print("found pivot at column " + str(row.index(num)+1))
                j = row.index(num) # column index
                marks[j] = True
                
                for k in chain(range(0,i),range(i+1,len(M))): #search for other 1s in the same column
                    if M[k][j] == 1:
                        for i in range(len(M[k])):
                            M[k][i] = (M[k][i] + row[i])%2
                break
            
   # print(marks)
    M = transpose(M)
    #mprint(M)
    
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
    print(str(a)+"^2 = "+str(b)+"^2 mod "+str(N))
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

def gen_seq_sub(start,p,n,mod2):
    global sieve_interval
    i=0
    ret=solve_lin_con(n,start%mod2,mod2)
    p=mod2
    start-=n*ret 
    seq=[]
    if start == 0:
        start-=n*p
    while i < sieve_interval:
        seq.append(start)
        start-=n*p
        i+=1 
    return seq

def gen_seq_add(start,p,n,mod2):
    global sieve_interval
    i=0
    ret=solve_lin_con(n,start%mod2,mod2)
    p=mod2
    start-=n*ret 
    if start == 0:
        start+=n*p
    seq=[]
    while i < sieve_interval:
        seq.append(start)
        start+=n*p
        i+=1
    return seq    
def gen_smooths(sol,mod,factor_list,n,mod2):#,primeslist2):
    global sieve_interval
    global max_sieve
    smooths=[]
    found=[]
    start=sol**2
    i=0
    seq=[]
    seq.extend(gen_seq_sub(start,factor_list[i],n,mod2))
    seq.extend(gen_seq_add(start,factor_list[i],n,mod2))
      #  i+=1
    i=0
    while i < len(seq):
        rem=seq[i]
        j=0
        while j < len(factor_list):
            while rem%mod2 == 0:
                rem=rem//mod2
                if rem ==0: #Dunno?
                    break
            while rem%factor_list[j]==0:
               rem=rem//factor_list[j]
               if rem ==0: #Dunno?
                    break 
            j+=1
            if rem==1 or rem==-1:
                if seq[i] not in found:
                    found.append(seq[i])
                break
        i+=1
    return found

def generate_smooths(procnum,return_dict,n,enum,flist,mod,primeslist2):
    sm=[]
    xlist=[]
    mod2=1
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
        s=gen_smooths(sols,mod,factor_list,n,mod2)
        sm.extend(s)
        for it2 in s:
            xlist.append(sols)
        if len(s) > 0:
            print("["+str(procnum)+"]Found smooths: "+str(len(sm))+"/"+str(max_sieve))    
        if len(sm)>max_sieve-1:
            break
    test=[]
    test.append(sm)
    test.append(xlist)
    return_dict[procnum]=test
    return 0         


def launch(lists,n,primeslist2):
    global smooth_stop
    sr=round(n**0.5)
    allsols,allbigsums=[],[]
    bigsums,bigmodulus=[],[]
    i=0
    while i < len(lists):
        sums,modulus=normalize_sols(n,lists[i])  
        bigsums.append(sums)
        bigmodulus.append(modulus)
        i+=1
    print(bigsums)
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
        if balive == 0 or tlen > smooth_stop:
            for proc in jobs:
                proc.terminate()
            fres=check
            i=0
            fsm=[]
            fxlist=[]
            while i < len(fres):
                fsm.extend(fres[i][0])
                fxlist.extend(fres[i][1])
                i+=1
            QS(n,primeslist2,fsm,fxlist)
            print("All procs exited")
            return 0    
    return 

def equation(y,x,n,mod):
    rem=(x**2)+y*-x+n
    rem2=rem%mod
    return rem2,rem  

def QS(n,factor_list,sm,xlist):
    if len(xlist)!=len(sm):
        print("BLASDHASDS")
        time.sleep(100000)
    if len(sm) < len(factor_list):
        print("Not enough smooth numbers found")
        return 0
    is_square, t_matrix = build_matrix(sm,factor_list)
    sol_rows,marks,M = gauss_elim(t_matrix) 
    if sol_rows == 0:
        return 0

    solution_vec = solve_row(sol_rows,M,marks,0)
    factor = solve(solution_vec,sm,n,xlist) 

    for K in range(1,len(sol_rows)):
        if (factor == 1 or factor == n):
            solution_vec = solve_row(sol_rows,M,marks,K)
            factor = solve(solution_vec,sm,n,xlist)
        else:
            print("Found factors!")
            print(factor)
            print(n/factor)
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
        #primeslist1.pop(0)
        lists[i%workers],mods[i%workers]=build_sols_list(prime1,n,lists[i%workers],mods[i%workers])
        i+=1          
    print(lists)
    launch(lists,n,primeslist2)
    return 

def get_primes(start,stop):
    return list(sympy.sieve.primerange(start,stop))



def main():
    global key
    global base
    global workers
 #   while 1:
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


    n=p*q   
    bits=bitlen(n)
    primeslist=[]
    primeslist1=[]
    primeslist2=[]

    print("[i]Modulus length: ",bitlen(n))
    primeslist.extend(get_primes(2,100000))
    i=0
    while i < base*workers:
        primeslist1.append(primeslist[0])
        i+=1
        primeslist.pop(0)    
    print("primeslist1: ",primeslist1)
    i=0
    while i < second_base:
        primeslist2.append(primeslist[0]) 
        i+=1 
        primeslist.pop(0) 
    print("primelist2: ",primeslist2)          
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
