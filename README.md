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
I guess in my greatest moments of despair.. clarity finally comes... it was the same when I was hunting OpenSsl.. the days before I found that high sev bug.. I was ready to end it all.

So what I need to do... take a squared quadratic coefficient mod p, subtract N, see if that too is a squared quadratic coefficient mod p. If yes... we save this information... subtract N again... repeat. Do this for all.. and from that information, we multiply things together and try to keep that N subtraction small... so we end up with a small number that we then check for smoothness.. that's it right? I believe thats the most gas I'm going to get out of my current findings without doing more intensive research. So tomorrow.. I finish this... and either it works, or its over.. and then I don't care anymore.. if it doens't work, I don't think I can keep going, i'm too old and I cant stand all the pain and loss anymore.

Life probably would have been easier if they hadn't fired my manager with accusations of unfairly promoting me (only made it to SE II after nearly 4 years, and I have the CVEs to prove I deserverd those promotions) ... they just portrayed me as incompetent and someone who should have never been there. And didn't just ruined my life, but also the life of one of my best friends (my manager), one of the only people in this entire industry who supported me. That in combination of all those things happening right after I was threatened with a gun outside my apartment.. it did a type of damage I don't think I will ever recover from. Just painful memories of all the good times with my teamlead in vancouver. Memories of places and people I can't ever go back to. The best time I had in my life. Just isolation now, and this math problem. Now with most of my savings gone in the stock market crash.. I don't know. One last attempt at my math tomrrow.. after that.. yea well.. fuck this world. Its the world's loss, because they'll never know the things I could have done. Let them choke in their own stupidity.

What if  I just calculate quadratic coefficients for every prime in my factor base. Then it just becomes, finding small values of N that have to be subtracted to reach 0 and multiplying them together until that coefficient squared is bigger then N...  I guess that would be my most simple and elegant approach yet. Plus, I can probably code this in about an hour tomorrow. Ok... lets do that.. 



And it doesn't really matter how we calculate quadratic coefficients. Right now they are calculated for 4N inbetween. But if we subtract 3N from all the coefficients, then it becomes the textbook one they talk about in QS papers. But it truely does not matter. Because all the other combinations also get increased or subtracted... so its all kind of relative. Its just finding those relations where we end up with small numbers that factor over the factor base. So just calculate coefficients for all primes in the factor base... calculate how much N needs to be subtracted to reach 0 (aka a multiple) and make sure that total when we square the coefficient and subtract the amount of N we found, it creates a small number that is garantueed to be divisible by the factor base. Its more about that ratio really then anything else. One final effort tomorrow...time to try and sleep now I guess..


Ok I have worked out the details in my head. Calculate all the quadratic coefficients for every prime in my factor base. Calculate how much N needs to be subtracted to reach 0 for each squared coefficient. Now with that.... take all those with 1N difference, multiply permutations of those together such that the squared coefficient - 1N is near 0. Those are basically garantueed to be in the factor base. Not enough smooths? No problem, now repeat for 2N... and so on. Thats the best I can do for now. Publish that, fix that paper too.. and take a break for a few months from math until I'm in a better place to resume it again.

Great, my belgian bank ended their relationship with me and is closing my accounts. Getting treated like a criminal by everyome. And I havnt even done crime. But maybe its a wake up call to finally get out of europe and head to Asia..
Its like in this movie, enemy of the state... all these gov people just jealous because I found more 0days then them. Easier to just portray me as a cyber criminal and ruin my life rather then proof any cyber crime actually happened. 
Fuck man... its really time to go to Asia. What kind of life can I build here? I cant do anything here.
