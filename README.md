hi!!!Work in progress!!!!

Uploaded a new version (18 march):

Will factor 150 bit in a couple of minutes on a laptop.

Use: python3 QS.py -keysize 150

To do: Final version will be released soon. It borrows number field's smooth finding strategy together with everything I have learned using quadratic coefficients. It will allow you to find smooths using small polynomials of the second degree... 

Still looking for work, will relocate: big_polar_bear1@proton.me

Bleh... cant sleep. I know I can build smooths like number field sieve does. I know I have all the pieces. I don't need to combine coefficients first like I'm doing in my quadratic sieve PoC... *sigh*
So depressed. I cant believe my fucking life anymore. Im so angry at everything that has happened. Just treated like complete trash, after so many years of hard work.

Fuck it. a^2 = b^2 mod N, both side can be represented seperately in an exponent matrix... number field sieve shows how. I know one side can be constructed by combining quadratic coefficients and squaring them...  that is EASY. However, I don't want to combine them above a certain threshold, I want to find smooths with coefficients mod p ideally and plug that into my square finding matrix...... so let me figure out the number theory for that first ... and I know how the other side is derived from that, so once I figure this out, then figuring that out should be straight forward. One step at a time... 

I swear, someone knows. Someone knows I am right about my approach. And damn you all to hell for treating me like the enemy. If I act the way I do, its exactly for these reasons. You all deserve to burn in hell. After all I have done in my career, bugs in OpenSsl, Secure Channel, IKE, kerberos ... etc etc... this is how I get treated lol. You're all going to burn for this.

I dont even know what people are thinking. That i'm just going to stop? Give up? Youre only hope of me giving up is if I kill myself. And honestly, there were days lately, where that almost happend... but I know I am right. And I know I can do it. And I will do it. And go to hell.

Just thinking out loud..

148^2 = 0 mod 37   ... so any 0 quadratic coefficients... if I combine them we will have a multiple of those moduli .. easy way to construct smooths on one side.
if we have 148^2 = 66^2 mod 4387 ... 66^2 mod 37 = 27  ... which is equal to 148^2 - 4*4387 = 27 mod 37 .. hmm.. now if we look at all quadratic coefficients mod p1, p2, p3, p4 ... and we see which one reaches 0 when subtracted 4N ... then we know which factors will be generated on the other side!!!!!!!!!!!!!!!!!!!!!!!!!!! Aha. Now I need to figure out a way to figure out if they will be smooth or not... I can do that... shouldnt be hard. God damnit, I was so close already with my uploaded PoC. One more adjustment... dont want to brute force combine coefficients and test for smoothness... I should be able to determine which combinations will be smooth with the power of ABSTRACT ALGEBRA AND NUMBER THEORY!!!!!!!!!!!! Yes. Its not that hard. Hell, I doubt I'll even have to make it as complicated as number field sieve's approach. 

Burn in hell. All you people think youre so much better at me. You think me finding this was luck, yes? You dont know how hard I worked. How much I sacrificed. I kept going, despite being threatened with a gun, harassed, fired from my job. Kicked out of the country away from my friends. My fucking manager fired. Tried really hard to ruin my life (and that of my manager). But I kept going. I'll never stop. You'll have to kill me..and good luck with that, because even at that you'll all fucking fail because I'm a polar bear and I'll fucking devour you fuckers alive.


Aaaand booom.... I just figured out how to find smooths by looking ath quadratic coefficients mod p...... probably should have realized this weeks ago... feeling a bit slow... reminds me of highschool when I sucked at math. Anyway... give me a few good days of a better mood and some sleep... and a much much much much much better PoC is about to come online. Its actually ver simple. Don't need to do complicated stuff like number field sieve.

FUCK. FUCK. Its kind of trivial to set up a^2 = b^2 mod N if I know the values of quadratic coefficients mod p, together with all the other stuff I worked out so far. Don't need to do all this retarded shit. Just build it on both side... its fucking easy. Just abstract algebra. AH FUCK. GO TO HELL. Maybe me being slow and retarded in my final days of my math project is fate. Maybe fate wants you fuckers to have a couple more day. But go to hell. GO TO HELL.

Using that entire xN trick, I know how much N should be inbetween. Hence, on both side, within my factor base, I know what factors I can use to build a congruence mod N. Fuck algebraic factor base... fuck polynomial roots... fuck am I overcomplicating shit when its literally linear shit. I guess learning about NFS and how it builds both sides of the congruence seperately was needed to have this insight, but it still doesn't make me feel less stupid that it took this fucking long.

New PoC before the end of the week.. this should be my final version... instead of bruteforcing coefficients it will build smooths on both sides of the congruence... I know how to do it...

This math shit is going to kill me eventually. But at the same time, I don't think I can stop until factorization is completely broken... and I don't mean broken as in RSA broken... I mean, make factorization as easy as multiplication. Or close to. I don't think its a sacrifice worth making. I think being happy is more important. I think its just all the trauma. It just put me on a path, where I have to do this now.. almost like it was fate... or madness, or both. Definitely some weird shit going on I can't explain. Like someone, or something, from a different world, or time, reaching out, encouraging me to devote my life to this... I think its just the isolation and trauma.. trying to find meaning in a meaningless world. I dont care if I go completely mad. Before I lose it all, I will solve factorization. 
