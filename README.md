# Factorization_new

Publishing my work-in-progress.

This demonstrates using quadratic coefficients to generate smooth numbers.
Current version run with: python3 QS.py -keysize 30 

Will only factor small semi-primes for now, this is a work in progress.
TO DO: When we generate smooth candidates, if the remainder is not 1 or -1, we can continue sieving this easily and find smooths a lot faster. I will try to finish this before the end of next weekend. Aside from that, everything else works as expected. Just the smooth generation is a bit sloppy.

It is supposed to still be slow. Because the smooth generation logic isn't implemented yet. It just generates numbers divisible by the factor base right now, that is all, there's no sieving or anything taking place. But the number theory works, and this already demonstrates that. Next is to implement this part... one step at a time. Making it public already, because I juts don't care anymore, like none of it matters anyway. Can't get a job. Been unemployed for over a year. No income. Nothing.

I only realized I could use my work to plug into QS a few days ago, so this is just all quickly put together in just a couple of days. I was exploring a different route before, but I think this one has more potential once I finish the smooth finding portion.. which should really just be a matter of solving linear congruences.

I'm fairly confident this is now the right direction to take my research. My previous mistake was not realizing that ANY valid coefficient combination has an infinite amount of matching squares mod n. Restricting myself to finding those two squares with 4N inbetween was my big mistakes. I hope to finish everything in the coming days. Tomorrow I'll take one day off to gather my thoughts, after that, I'll do one final push to finish this. I'm nearly there.. and you can see the code already, I'm not bluffing.

People are probably still laughing at everything I do. But I know I am nearly there now, this lets me hunt for smooths in ways that wasnt possible before. Its literally solving linear congruences now.. I just got to write the code. Just one day to take a break today, and then I continue full speed to the finish line.

Update 28/2: I think I have one way to do the sieving. Just a series of linear congruences. First generate a number divisible by the factor base. Secondly, see what remains. Then solve linear congruences to see the fewest amount of times N needs to be added/subtracted to get another factor within the factor base (or multiple factors in the factor base, I'll have to run some tests to see whats most efficient), then keep repeating that process until hopefully it turns into a smooth. Its not ideal, but should greatly improve the odds. And any factors that fall in our factor base we can ignore and only work with whats left, so if what remains is a very small number, then we can compute this process very quickly. Or some type of algorithm where we do congruences, and then only proceed if we can shrink the number outside the factor base. If I had more time, I could probably spent months on finding the best way to find smooths, Im certain a nice algorithm for this can be found. Also I think we should probably have very small factors like 2,3,5 also in our factor base (which are currently skipped in the PoC).. since these factors are the most commonly found, thus improving the odds of finding a smooth. I'll write the code tomorrow, for some reason I am feeling unfocused today.
