!!!!WORK IN PROGRESS!!!!!!!

Useage: python3 QS.py -keysize 60

Notes: Just uploaded my latest iterations (5 march 2025). It now uses linear congruences to generate numbers less then N which are then tested for smoothness.

If a quadratic coefficient is 148, and our factor base is 3 * 5 * 7, we check the congruence x * 105 = 148^2 mod N. After solving this we check X, which is garantueed to be smaller then N for smoothness.. if it is smooth, we multiply by 105 to get our full smooth number for use in our exponent matrix over GF(2).

This is a little slower then my previous version, because the number is between 0 and N, so as the bitlength goes up, so do the numbers we need to check for smoothness, and thus require a larger factor base. But on the flip side, unlike traditional QS, where we check x^2 - N, we can basically keep checking forever without having to worry about the number we check for smoothness growing bigger and bigger.

TO DO: We need to figure out how to "sieve" the result of our congruence somehow, so we can generate small X values only.. because this is literally to only remaining bottle neck. Achieve this and factorization comes tumbling down. There probably is some way using CRT to find small X values that solve the linear congruence. I.e first check for X values using only one prime from the factor base... and then we can start combining them. That should do the trick hmm..
I feel like this is definitely the right path now. The numbers we have to check for smoothness are now capped by N, which is great, the question now is, how we can find small ones within that set of solutions.. a very clear cut problem for which I should have to tools to solve it. If all goes well, this entire factorization problem comes tumbling down in the coming days... lets see.

Fuck Trump, Fuck Hegseth, Fuck Tulsi, Fuck Nethenyahu, fuck all your right wing lunatics. It's funny, because I believe in being tough on violent crime and drug dealers, but I also believe in having respect for people, and not harming innocents. Those who go after innocents can go to hell. I'm not perfect and definitely not a saint, but I'll fight any of these fucking cunts. Before the end of the decade these people will go to war with China, and once that happens, we're all dead. Fucking warmongers. American leaderhip is the greatest danger to humanity there has ever been, and I truely believe this. Everything they do is in preparation to confront China, and it is so transparant. 
