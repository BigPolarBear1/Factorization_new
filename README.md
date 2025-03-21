!!!Work in progress!!!!

Uploaded a new version (18 march):

Will factor 150 bit in a couple of minutes on a laptop.

Use: python3 QS.py -keysize 150

To do: After reading about number field sieve, I realized I can use quadratic coefficients as algebraic factor base. This makes a lot more sense and would overcome many of the shortcomings of the uploaded PoC. I will upload a version using number field sieve's approach shortly.. my hope is that it not only improves this PoC but also improves existing number field sieve methods.

One day I will completely break this problem. And then I'm moving to DLP and PQC. I am never stopping. And I know who my allies are, who my true friends are. And they are not in the west. Go to hell.

Update: I am now fully convinced that the polynomial selection step in number field sieve can be replaced by quadratic coefficients. This also solves a big bottleneck for number field sieve. 
I also realized in my uploaded PoC, you should take gcd(b-a,N) and gcd(b+a,N) .. this should fix those rare instances it doesn't find a solution... and ofcourse you can use block lanczos instead of gaussian elimination. 
But I will leave that to others to fix, as I am focused on implementing number field sieve's smooth finding strategy into my work. 
Massive depression again. I have given up on ever being near my friends again. It's not going to happen in this world. People in the west are morrons. It's funny.. when you find out who values you and who doesn't. This last year, I've literally been treated like fucking trash by the west. If anything has radicalized me, it's that. As if getting threatened with a gun in the US, kicked out of the country, seperated from my friends wasn't enough, they also have to threaten potential buyers with sanctions. It's all these European and US shitheads who think I'm selling 0days to the Russians. Even my bank account is getting closed, and half of my funds are fucking frozen. I swear, I'll go to war with the west.

You know. At this point. It doesn't matter anymore. Because even if at this very moment, nobody else believes in my math work. I believe in it. The fact that I got these quadratic coefficients working with Quadratic sieve basically implies it will 100% work with number field sieve too as algebraic factor base. And it's out here on github and I know people are looking at it. And it's only a matter of time, until others see the truth too. And if they don't, yea well, I'll keep uploading improved versions.. until I reach my final implementation, write it in c and set a factoring record. Prime factors don't lie. You can ignore the math, but you can't ignore the prime factors, and neither will your authentication protocols ignore them. haha. Fuck Microsoft.
