# Factorization_new

Publishing my work-in-progress.

This demonstrates using quadratic coefficients to generate smooth numbers.
Current version run with: python3 QS.py -keysize 30 

Will only factor small semi-primes for now, this is a work in progress.
TO DO: When we generate smooth candidates, if the remainder is not 1 or -1, we can continue sieving this easily and find smooths a lot faster. I will try to finish this before the end of next weekend. Aside from that, everything else works as expected. Just the smooth generation is a bit sloppy.

It is supposed to still be slow. Because the smooth generation logic isn't implemented yet. It just generates numbers divisible by the factor base right now, that is all, there's no sieving or anything taking place. But the number theory works, and this already demonstrates that. Next is to implement this part... one step at a time. Making it public already, because I juts don't care anymore, like none of it matters anyway. Can't get a job. Been unemployed for over a year. No income. Nothing.

I only realized I could use my work to plug into QS a few days ago, so this is just all quickly put together in just a couple of days. I was exploring a different route before, but I think this one has more potential once I finish the smooth finding portion.. which should really just be a matter of solving linear congruences.
