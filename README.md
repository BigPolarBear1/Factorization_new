# Factorization_new

Work in progress.

Uses Quadratic coefficients, this makes it easier to paralellize and we don't have the issue where x^2-n becomes bigger and bigger as x increases.
But since at every sieve interval step this subtracts N, we do need a larger factor base.
I'm going to dig in some more if that issue can somehow be managed. Maybe just subtract N mod m or something.. I'll try some things tomorrow. Probably some way to just subtract N mod the factor_base... hmm, I can see a solution in my head, but I'll need to run the numbers if it actually works like I think it might.

Current PoC use: python3 QS.py -keysize 70  (current settings will work well up to 80 bit)

Update: Subtracting n mod the factorbase instead of the full n at each sieve step should work much better.. thinking about it in my head, I dont see why it wouldnt work. I can now conjure solutions in my head to math problems without doing the math on paper, haha, every day I grow stronger. Ill fix the PoC tomorrow.. that should allow us to easily blaze past 100 bit.

Update2: OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOH. So the above works.. but that got me thinking. Why not just take the factor base as start (i.e p1 * p2 * p3 * p4), and from there just do congruences over mod N using the factor base so we maintain smoothness ... and then we can get two values on both sides with the same value mod N quickly. No need for sieving at all. But that would really break factorization really hard... it can't be that easy, can it?

Wait wait, it can't be this easy. I.e if we have the quadratic coefficient 148.. so one square is 148^2 ... then we can just take 3 * 5 * 7, aka 105 .. and figure out the congruence where x*105 = 148^2 mod N???????????? 
So as long as the x solution to that congruence is in the factor base, we have a smooth? So just complete congruence to find smooths instead of logarithmic sieving and shit? hmm 

AAAAAAAAAAAAAAAH. Why did I waste the entire weekend implementing logarithmic sieving when its a fucking linear problem that can be solved with linear congruences. aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaah. 
Oh well. Guess that buys people a few more extra days until shit hits the fan.

the NSA cryptologist reading this knows what is about to happen in a few days. Tick tock fuckers.

If you want to know why I am going to do what I am going to do, it is beause MSFT fired my manager simply because he stood up for me. Fired him for giving me a promotion, that I had earned, but MSFT claimed I hadn't despite all the bugs I found.
Because people made it impossible for me to stay with my friends. The only thing in life that mattered to me. I havn't seen my friends in almost a year. Everything I go outside running, I think about those days I was in Vancouver, with my friends, running around the seawall with my teamlead. You took away the best days of my life, and left nothing but ruin for me and my manager. A price has to be paid and a price will be paid, and I am stopping at nothing until this happens. Go to hell. I will destroy Microsoft for what they have done and I do not care who gets caught in the crossfire.

Ok... so  if a coefficient is 148 and we want to generate a number congruent to its square mod n with factors 3,5,7 we do this:

x*105 = 148^2 mod 4387 (n=4387 or whatever)

solving the linear congruence gives: 2423*105 = 148^2 mod 4387
BOOM. EASY. Then we only have to check 2423 against the factor base, a number always garantueed to be smaller then N.
Tick tock.........................hehehehhehehehehehehehehehehehehehehehe. Tomorrow I'll implement this and finish the PoC (wednessday 5 march). Go to hell for all you people have done.
