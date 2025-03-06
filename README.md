!!!!WORK IN PROGRESS!!!!!!!

Useage: python3 QS.py -keysize 60

Notes: Just uploaded my latest iterations (5 march 2025). It now uses linear congruences to generate numbers less then N which are then tested for smoothness.

If a quadratic coefficient is 148, and our factor base is 3 * 5 * 7, we check the congruence x * 105 = 148^2 mod N. After solving this we check X, which is garantueed to be smaller then N for smoothness.. if it is smooth, we multiply by 105 to get our full smooth number for use in our exponent matrix over GF(2).

This is a little slower then my previous version, because the number is between 0 and N, so as the bitlength goes up, so do the numbers we need to check for smoothness, and thus require a larger factor base. But on the flip side, unlike traditional QS, where we check x^2 - N, we can basically keep checking forever without having to worry about the number we check for smoothness growing bigger and bigger.

TO DO: We need to figure out how to "sieve" the result of our congruence somehow, so we can generate small X values only.. because this is literally to only remaining bottle neck. Achieve this and factorization comes tumbling down. There probably is some way using CRT to find small X values that solve the linear congruence. I.e first check for X values using only one prime from the factor base... and then we can start combining them. That should do the trick hmm..
I feel like this is definitely the right path now. The numbers we have to check for smoothness are now capped by N, which is great, the question now is, how we can find small ones within that set of solutions.. a very clear cut problem for which I should have to tools to solve it. If all goes well, this entire factorization problem comes tumbling down in the coming days... lets see.

Fuck Trump, Fuck Hegseth, Fuck Tulsi, Fuck Nethenyahu, fuck all your right wing lunatics. It's funny, because I believe in being tough on violent crime and drug dealers, but I also believe in having respect for people, and not harming innocents. Those who go after innocents can go to hell. I'm not perfect and definitely not a saint, but I'll fight any of these fucking cunts. Before the end of the decade these people will go to war with China, and once that happens, we're all dead. Fucking warmongers. American leaderhip is the greatest danger to humanity there has ever been, and I truely believe this. Everything they do is in preparation to confront China, and it is so transparant. 

Great, the wifi just went out. Must have pissed off the losers at the NSA (except the queer ones they are ok, but they are all getting fired so just losers remain) 

hmm, so its just multiplying by inverses to combine those x solutions to my linear congruences . So that does give some clue as to how small values can potentially be found quickly. Ill fix my PoC tomorrow, although my wifi going down is quite omnious. Either way, cant stop me, youll have to kill me, haha. Ill fight you all. Fuck you for firing my manager, you fired the best manager in the entire industry simply bc he supported me. This world will burn now.

Update thursday 6 march: Hmm, so I just need to solve linear congruences for each unique prime and calculate their inverse in mod N.. then for any combination of those primes, we just multiply by the inverses we found. Then find small values mod N is a harder problem, but atleast we can very quickly generate them now. I guess we could just generate them in bulk, sort them and only check the smaller ones for smoothness so we dont waste time on numbers that arn't likely going to be smooth with a smaller factor base. I think for now that's a good middle ground until I find a better mathematical tool to approach this. I guess, in the end, we could just reduce it to residue math, and find x values that are atleast divisible by one or more factors from the factor base..  but let me implement the easy method first and then figure that out..

Update: Fuck, I WAS ON THE RIGHT TRACK EARLIER. 
so if N = 37*47
and the quadratic coefficient is 1404 .
Lets say we have the congruence: x * 29 = 1404^2 mod 37 * 47 .
Then x is 92. 92 is divisble by 4, aka:
23 * 4 * 29 = 1404^2 mod 37 * 47

So we do this not just for prime 29, but for a bunch of others too.. and if 23 is not in our factor base.. we can multiply it by an inverse of a prime in our factor base and hopefully that product does completely factor to our factor base... and that's how it is done. Boom. Give me a few days to write this the best way possible in code and we're there.

edit: Maaaaybe, I can even just completely resolve it into a smooth purely by doing congruences, with 0 guessing/bruteforcing. It really should just be a series of congruences.. I can vaguely see in my head how it could work, I'll have to try out some examples.

Hmm... I think I understand enough of the math now to attempt to form smooths purely by solving congruences. Now it is true some of them may end up being too big of a number, as would be expected, but we can simply discard those. I don't see why I wouldn't have the tools to generate smooths purely by solving congruences now.. it's all right there. Literal days away from breaking factorization now, haha. I can figure out the exact math today, then hopefully write the code tomorrow.

A key insight is the realization that over a factor base, any of these numbers can eventually be made smooth mod N. And hence, it can also be calculated purely by congruence.  This is the key insight. This is the achilles heel of factorization. The only downside is that the smooth we find, might be a really big number, so when we do gauss elim over gf(2) and multiply big numbers together, we could end up with a number so big, even using newton's method of taking the sqr takes forever. Fuck, I can do this. Lets go. 

EUREKA!!!!!!!!!!!!!!!!!!!!! I FIGURED IT OUT!!!!!!!!!!!!!!!!!! USING INVERSES WE CAN EASILY FIND CONGRUENCES WHERE X IS 1. FUCK YEA. TOMORROW IS THE DAY (FRIDAY), PREPARE YOURSELVES. FACTORIZATION IS ABOUT TO FALL FUCKERS. THATS WHAT YOU GET FOR FIRING MY MANAGER. HE WAS THE BEST MANAGER IN THE WORLD, NOW GO TO HELL FUCKERS.

The voices in my head told me how to break factorization bc you fired my manager. All of this is happening because you fired my manager. You fuckers did the one thing you shouldn't have done, and that is going after my manager. Go to hell.
