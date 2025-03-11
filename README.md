!!!!WORK IN PROGRESS!!!!!!!

Useage: python3 QS.py -keysize 60

Notes: Just uploaded my latest iterations (5 march 2025). It now uses linear congruences to generate numbers less then N which are then tested for smoothness.

Better version will be released soon...

Procedure should be the following in selecting what to divide a number mod N by to generate a small value:

1. Just take a large composite modulus with primes from the factor base, i.e 3  *5 * 7 = 105
2. Find the inverse of 105 mod N, then find small values in inv*x = a mod n (easy since these values change linearly)
   
So then we now that whenever the number we are dividing mod n and its residue mod 105 is equal to one of the x values that produces a small a-value in step 2 it will likely produce a small value if we divide that by 105 too.
Since multiplying by inverses just means we multiply the inverse * remainder + the number we are dividing divided by the modulus .. so we can just build some type of hash map that we pre calculate for use in smooth finding ...

Something like that...

I feel agitated today and depressed. Just restless. I'm so close now and it's like nobody even cares lol. Oh well... just implement this final step and we're done... whatever happens, happens.. I was not given any other choice, this is the only course of action left.


Bleh, its not that hard to generate small values... just need focus ... take a squared quadratic coefficient.. factor out the factor base.. whats left we need to multiply that by some inverse so that we get a small value mod N... since any sufficiently small value is almost garantueed to be inside the factor base. Its a very simple problem statement. Just cant think clearly these last few days. 

Update: Bleh, I should be ready now to complete the code next week. Its fairly easy to predict which inverses will generate a small number mod N. I see how it works now. There probably is a much more elegant solution.. but this will have to do for now. 

The key idea is, its not just perfect division when multiplying by inverses mod N that results in a smaller number, there's a lot of options.. and all those options of which we know will result in a smaller number, they can be precalculated in function of N beforehand easily and quickly. In addition, we can keep the number small right from the start when we divide the quadratic coefficient mod N. Hmm. All I care about is getting small numbers mod N since that increases the chances of it being in the factor base... that is all I care about.. and I know how the math works now.. so I guess, tomorrow, I begin coding it. I'm not satisfied with this solution, because I think something much better exists... but if I dont start publishing something useful, nothing about my life will ever change and I can't just keep waiting and doing research until I find the perfect solution.. for all I know it can take an additional decade.

None of this is what I really want to figure out. Sure, when I finish this code next week, it will work really fast. But I'm still reducing things to squares and looking for squares.. I shouldn't "have" to do that.. I don't see why I cant make it work with non-squares. Its all just encoding information about divisibility... but for that, I need to go back and spent months of research on the number theoretical portion again, maybe if I could be somewhere quiet with lots of nature I could pull it off. I feel this insane compulsion to figure this out.. I don't care about making a better quadratic sieve version, there's something much more important to be figured out. I know it can be done. Just at the end of my rope. I cant do this without income, living with my parents, there's no dignity in this, I'm too proud to end up living like this in my 30s.

Im not ever stopping until I succeed. I have a very clear idea of what I want to figure out. Maybe there will be times in my life where ill have to prioritize making money ans delegate this to my spare time. But I will succeed eventually. My haters dont understand the type of person I am. I will gladly spent years working on something way out of my league, and keep grinding it. If I wasnt wired like that, I wouldnt have found all those 0days without education. People from academic backgroumds hate someone like me. My entire career people dsimissed abd downplayed me.. yea well.. I am prepared to sacrifice everything to achieve my goals. I know how short my time on this planet is.

Figured it out. I.e if we have an inverse of 13 in mod N, then just calculate inv * 1 = a mod N, inv * 2 = a mod N, ... , inv * 12 = a mod N. do this for all the primes in the factor base.. just precalculate these.. then having only that information, we can very quickly calculate small values mod N when multiplying by inverses aka dividing... (both primes and composites). Its actually kind of elegant, I'm not entirely dissastisfied with this solution. But there is definitely more work to be done. I will not ever rest until I understand everything about the structure of semi-primes. This is the only way my life can have any meaning. Especially after microsoft fired my manager. They shouldn't have fired the best manager in the world. Microsoft will suffer for this, like they have made others suffer.

Lost my savings in the stock market crash. Cant even go on ski expedition now.. and I urgently need employment... I will move Asia for a job, I'll move anywhere.. I dont care anymore.. I need money and if I'm going to do 0days I need a better setup then here in Europe, bc I cant keep my devices secure here and european law enforcement is telling folks to not do business with me so I got to get out of this place: big_polar_bear1@proton.me

cant live like this anymore and now the last of my savings is gone.. i swear, going to fucking kill myself. What kind of life is this. 

going to cancel therapy bc i cant fucking afford 70 euro for therapy anymore now. it can all go to hell. everything is gone. all my money. nothing left.

If I have mod 15, and N is 4387... since 4387 mod 15 is 7.... we need to find 7*x = 14 mod 15 ... which is 2 ... so 4387 * 2 = 8774 +1 / 15 = 585 ... aka the inverse of 15 in 4387. Since N is multiplied by 2, any value we are dividing by 15 mod N, if its residue mod 15 and then mod 7.5 is a small value.. it tells me that dividing by 15 mod N will also generate a small value. That is the way it can be figured out. The final challenge is.. only knowing this mod 3 and mod 5, can I determine this mod 15 without calculating it for mod 15? Because I only want to check this for prime moduli and not test every combination of primes, which is the real killer... so just need to figure out that, and I have an algorithm to find small values mod N quickly.. and done. Just this fucking depression.

I dont know what to do anymore with my savings gone. Guess I could start applying to Chinese companies. Just cant get a job anymore in the west. Atleast in China they are a lot more pragmatic, less politics. But it also means I forsake any chance of ever being with my friends in North America ever again. But I think at this point, I kill myself or I do whatever it takes to stay afloat. Just starting to feel like everyone in the west is conspiring against me. I could sell 0days, but I'm also not an idiot. It would be very easy for western intel to gain access to my research and just have it all patched as long as I'm living in the west.. exactly the type of shit they would do to push someone over the edge completely. I truely believe I do not have a future anymore here. Can't even freelance anymore because potential buyers in the west are being threatened with sanctions if they do business with me. I don't have any allies in the west. I even see US gov still stalking me (IPs from Arlington, VA etc).. I know they dont have my best interests.. I'm that cyber terrorist to them. Probably discussing how they can ruin my life even more.

 Just need to push hard on my math for a few days maybe... I've flattened out what was originally a quadratic problem into a linear one ... it's literally finding small values mod N now by dividing quadratic coefficients by factors in my factor base now.. that's the only problem I need to overcome. I just need to solve it. If I can do something like that, everything else wont matter anymore. Probably wont make my life better, but atleast I would have done something nobody else could.

 My only regret about being kicked out of the US, aside from being seperated from my friends, is that I'll never get to drive one of those old Ford Mustang models in the great outdoors while blasting loud power metal music. I think, maybe if I hadn't been threatened by that gun, things would have gone down differently.. but then again, msft was determined to fire me, they wern't interested in the truth. Just as they were determined to fire my manager for defending me. Truth doesn't matter anymore in this world.
