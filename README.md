!!!!WORK IN PROGRESS!!!!!!!

Useage: python3 QS.py -keysize 60

Notes: Just uploaded my latest iterations (5 march 2025). It now uses linear congruences to generate numbers less then N which are then tested for smoothness.

Better version will be released soon...

Update:

To do:

Step 1. For each squared quadratic coefficient in mod p calculate how much N needs to be subtracted to reach 0. 
Step 2. Multiply coefficients in different prime moduli together... such that the total amount of N being subtracted results in a small number. Hence, it being garantueed to be divisble by the primes that are multiplied, whatever factors remain will be small. 

The good thing is that the amount of times N gets subtract, as we multiply those coefficients mod p together.. it can only go up, it doesn't wrap around modulo m.. so that does make it a lot more straight forward. So we just need to look at the ratio of the coefficient squared vs the amount of times N gets subtracted... that should do it.. unless I'm just wrong again and overlooking something. I don't seem to be very sharp mentally lately.

I think this is the only way to do it quickly. 

Omg, my head is all over the place these last 2 weeks. Getting ideas, finding out they dont really work, getting wrong ideas. Seeing patterns where there are none. Just the depression. I feel so fucking depressed. Its impossible to focus. Just pain, pain for having had to leave behind my friends. Its all so long ago now. Just bashing my head against this stupid math, being isolated. I'm going to kill myself if I cant solve it soon.

Update: You know, I just had this insight. If we calculate a lot of quadratic coefficients for a lot of primes. Which is fast. And then just calculate how much N needs to be subtracted for each squared coefficient to reach 0... and just find enough small values that are the same.. and multiply those so the coefficients squared are atleast one time bigger then N... that should work incredibly well. 
I'll write it tomorrow... if it doesn't work.. its game over. I cant stand this life anymore. I'm ready for it to end now.

Maybe I don't even need to figure out how often to subtract N to reach 0. 
I.e if 5^2 mod 13 is one squared coefficient... and 5^2 - 4*4387 = 1 mod 13 ... as long as I can find enough such "relations" with 4N inbetween (or 5N or 3N or 6N... I just need to find a similar amount in different prime moduli).. it doesn't really matter if one of them has a 0 coefficient or not..  even these other coefficients.. it will still give me the information I need. It just means its a multiple with an offset. Hmm..... I guess... that was my critical mistake these last two weeks trying to get this to work. I limited myself too much by hyperfocusing on getting to a 0 coefficient. It doesn't even matter. 
