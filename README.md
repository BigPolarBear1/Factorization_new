# Factorization_new

Work in progress.

Uses Quadratic coefficients, this makes it easier to paralellize and we don't have the issue where x^2-n becomes bigger and bigger as x increases.
But since at every sieve interval step this subtracts N, we do need a larger factor base.
I'm going to dig in some more if that issue can somehow be managed. Maybe just subtract N mod m or something.. I'll try some things tomorrow. Probably some way to just subtract N mod the factor_base... hmm, I can see a solution in my head, but I'll need to run the numbers if it actually works like I think it might.

Current PoC use: python3 QS.py -keysize 70  (current settings will work well up to 80 bit)

Update: Subtracting n mod the factorbase instead of the full n at each sieve step should work much better.. thinking about it in my head, I dont see why it wouldnt work. I can now conjure solutions in my head to math problems without doing the math on paper, haha, every day I grow stronger. Ill fix the PoC tomorrow.. that should allow us to easily blaze past 100 bit.

Update2: OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOH. So the above works.. but that got me thinking. Why not just take the factor base as start (i.e p1 * p2 * p3 * p4), and from there just do congruences over mod N using the factor base so we maintain smoothness ... and then we can get two values on both sides with the same value mod N quickly. No need for sieving at all. But that would really break factorization really hard... it can't be that easy, can it?

Wait wait, it can't be this easy. I.e if we the quadratic coefficient 148.. so one square is 148^2 ... then we can just take 3*5*7, aka 105 .. and figure out the congruence where x*105 = 148^2 mod N???????????? 
So as long as the x solution to that congruence is in the factor base, we have a smooth? So just complete congruence to find smooths instead of logarithmic sieving and shit? hmm 
