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


Bleh, its not that hard to generate small values... just need focus ... take a squared quadratic coefficient.. factor out the factor base.. whats left we need to multiply that by some inverse so that we get a small value mod N... since any sufficiently small value is almost garantueed to be inside the factor base. Its a very simple problem statement. Just cant think clearly these last few days. 

Update: Bleh, I should be ready now to complete the code next week. Its fairly easy to predict which inverses will generate a small number mod N. I see how it works now. There probably is a much more elegant solution.. but this will have to do for now. 

The key idea is, its not just perfect division when multiplying by inverses mod N that results in a smaller number, there's a lot of options.. and all those options of which we know will result in a smaller number, they can be precalculated in function of N beforehand easily and quickly. In addition, we can keep the number small right from the start when we divide the quadratic coefficient mod N. Hmm. All I care about is getting small numbers mod N since that increases the chances of it being in the factor base... that is all I care about.. and I know how the math works now.. so I guess, tomorrow, I begin coding it. I'm not satisfied with this solution, because I think something much better exists... but if I dont start publishing something useful, nothing about my life will ever change and I can't just keep waiting and doing research until I find the perfect solution.. for all I know it can take an additional decade.

None of this is what I really want to figure out. Sure, when I finish this code next week, it will work really fast. But I'm still reducing things to squares and looking for squares.. I shouldn't "have" to do that.. I don't see why I cant make it work with non-squares. Its all just encoding information about divisibility... but for that, I need to go back and spent months of research on the number theoretical portion again, maybe if I could be somewhere quiet with lots of nature I could pull it off. I feel this insane compulsion to figure this out.. I don't care about making a better quadratic sieve version, there's something much more important to be figured out. I know it can be done. Just at the end of my rope. I cant do this without income, living with my parents, there's no dignity in this, I'm too proud to end up living like this in my 30s.
