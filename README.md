!!!!WORK IN PROGRESS!!!!!!!

Useage: python3 QS.py -keysize 60

Notes: Just uploaded my latest iterations (5 march 2025). It now uses linear congruences to generate numbers less then N which are then tested for smoothness.

Better version will be released soon...

Procedure should be the following in selecting what to divide a number mod N by to generate a small value:

1. Just take a large composite modulus with primes from the factor base, i.e 3  *5 * 7 = 105
2. Find the inverse of 105 mod N, then find small values in inv*x = a mod n (easy since these values change linearly)
   
So then we now that whenever the number we are dividing mod n and its residue mod 105 is equal to one of the x values that produces a small a-value in step 2 it will likely produce a small value if we divide that by 105 too.
Since multiplying by inverses just means we multiply the inverse * remainder + the number we are dividing divided by the modulus .. so we can just build some type of hash map that we pre calculate for use in smooth finding ...

Something like that...

I feel agitated today and depressed. Just restless. I'm so close now and it's like nobody even cares lol. Oh well... just implement this final step and we're done... whatever happens, happens.. I was not given any other choice, this is the only course of action left.
