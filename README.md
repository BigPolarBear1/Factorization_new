!!!Work in progress!!!!

Uploaded a new version (15 march):

Will factor 150 bit in a couple of minutes on a laptop.
Still trying to figure out how to fix the code in try_sm, right now it will ignore numbers that are too big. 
But I believe I have an idea how to resolve that. I'll upload a better version soon. #roadto200bit

Use: python3 QS.py -keysize 150

Much better version will be published in the coming days.

TO DO: I will upload a newer version tomorrow. It will factor 200-bit on a laptop. I just really quickly skimmed through a paper on GNFS, it has a much better smooth finding method.. so if this beats standard QS... and I implement GNFS's way of smooth finding, will it beat standard GNFS too? Now THAT would be something... I'm so fucking broke, but my intuition is telling me there is something here.. hence I must push on. Always trust your intuition.. the universe works in mysterious ways. 

Update: Ok. Tomorrow I'll upload a slightly improved PoC. It will find smooths for 200-bit, but slowly. It's written in python after all. Reading about number field sieve, and finding smooths in mod p...  I have to focus on that, stop wasting time on this QS stuff and figure out how that works exactly. Because if I can get a similar approach working with quadratic coefficients... then we eliminate so many of the issues this PoC is having... the sky would be the limit. And understanding that will also give me a better understanding wether or not there is anything novel about my approach. Feeling optimistic that the coming weeks will reveal a true breakthrough finally. Now that we're moving on the GNFS, the best factoring algorithm in the world, any improvements we manage to make there, would be akin to literally moving the bar, pushing out into the uknown... which is very exciting. And after two years, the number theory used for GNFS suddenly looks much less daunting, it's very similar to QS.. just more abstract algebra (i.e doing shit mod p like I was also doing).
