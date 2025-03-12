!!!!WORK IN PROGRESS!!!!!!!

Useage: python3 QS.py -keysize 60

Notes: Just uploaded my latest iterations (5 march 2025). It now uses linear congruences to generate numbers less then N which are then tested for smoothness.

Better version will be released soon...



update: Hmmm... I need to just look at quadratic coefficients mod P, and subtract N mod P from them.. when they get to 0 they form a relation.. and I can use that information to construct smooths. That's how it should be done I believe... god fucking damnit. So fucking mentally exhausted.

I.e if a quadratic coefficient mod 11 is 5, then the squared one is 5^2 mod 11, 5^2 - 4*4387 = 0 mod 11. So I know there is a relation there with 4N inbetween. I got to start generalizing this ...  I just need to find multiple relations like this... then multiply them together .... i cant think clearly in this place with all the stress going on. 

Wasted atleast 2 weeks going down wrong rabbit holes when the real answer was infront of me all along... I tried to mimic traditional QS... while in reality I had to zero in on finding relations in quadratic coefficients mod P in isolation.. there's no point in pivoting my findings into normal QS.. that is conveluted and nullifies any of its strengths... ergh. FUCK. AND FUCK MICROSOFT. 


FFFFFUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUCK. I wasted so much time. I CAN BUILD SMOOTHS AFTER ALL. JUST HAVE TO FIND RELATIONS MOD P. FUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUCK!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
GO TO HELL. I guess I gave my enemies extra time. But now, I will be done in a matter of days for real. Now it finally clicked. FUUUUCK. These assholes stalking my github commits must think I'm some idiot who can't do math. Yea, well, I just get lost going down wrong rabbit holes sometimes... it happens. Only been doing math for less then 2 years. Now, this mistake I wont make in the future again, it's how I get stronger every day, hahahaha.

OK OK.... so create an outline for the (proper) algorithm tonight. Then begin writing it tomorrow.. and we should be done somewhere this week. Calculate relations mod P, multiply them together. EASY, haha. FUCK, it was so easy all the time. I dont understand where my head is sometimes. It doesn't matter. Eventually I always arrive at the correct solution, because I never stop and I never give up, haha. Until my last dying breath you fuckers.

My brain is like a quantum computer, incoherent until it collapses into the right solution, haha.. something like that, I don't know anything about quantum lol. one year and 10 months I have been working on factorization now. My entire life has been ruined. But nothing in life comes for free, and the greater the prize, the greater the sacrifice has to be. And even when I finish this "chapter" of my work on factorization, it is but the first chapter of many.. because I will not rest or stop until the factorization problem is completely broken. And with those insights, perhaps even other problems can be broken too.. and thus the wheel of time keeps turning as we march into the future hahaha. 

EUREKA! I was right!!!!! I was fucking right! As long as the number of times N is subtracted is a square in the factor base, we end up with a smooth. So when we multiply relations together, ALL we need to do is maintain a square and we are garantueed to have a smooth. I can do this tomorrow. Come  on, final stretch now, final effort to victory. Fuck yea. About to prove everyone wrong haha.

Should be easy now. Fuck man, I was about to kill myself out of desperation. Its always in the darkest moments the solution finally comes. Never give up folks.

I got it. I finally got it. After nearly 2 years. I got it for real now. I can definitely code this within a day. Just solve linear congruence mod primes from the factor base.. and the amount of times N gets subtracted needs to be a square inside the factor base, so using that, we can very easily determine which relations we need to multiply together. Its a simple as that!!!!!!! FUCK. Finally. I don't think I could have endured one more day of this desperation. Just the right time for it to finally come to me.
