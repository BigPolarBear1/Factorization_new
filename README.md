!!!Work in progress!!!!

Uploaded a new version (15 march):

Will factor 150 bit in a couple of minutes on a laptop.
Still trying to figure out how to fix the code in try_sm, right now it will ignore numbers that are too big. 
But I believe I have an idea how to resolve that. I'll upload a better version soon. #roadto200bit

Use: python3 QS.py -keysize 150

Increase base (and potentially sieve_interval) for higher bits when smooth finding gets too slow. I will improve the smooth finding code soon.

To do: This is a work in progress. I need to do some optimizations this weekend in try_sm, to create even smaller numbers. As the heuristic for this is very sloppy right now. And also create more combinations there as we're skipping a lot of them. I hope to get it all done this weekend.

Heavily modified version of (to use quadratic coefficients instead): https://github.com/NachiketUN/Quadratic-Sieve-Algorithm/blob/master/src/main.py

Update: Oh I just realized a quick fix in try_sm() to make it work many times faster... If we add a bunch of quadratic coefficients together.. and the number ends up being too big, we can subtract some quadratic coefficients again.. as long as the square is above x*N... its still a bit sloppy.. ideally I want to come up with a way better heuristic there... but that should already massively increase the odds of hitting smooths.. let me fix that tomorrow.. I got headache right now.

The thing is, this current way of doing this, it can already compete with existing QS PoCs.. despite being incredibly sloppy. I really need to fix that code in try_sm to generate as small as possible values. It's kind of doing it, but just using very wild estimates right now. Once I get this fine tuned.. I suspect it will blast past 200 bits with ease on a laptop in python. And I know, if I don't get past 200 bit atleast (on a laptop) nobody is going to take me seriously. But I know I can do it, and this weekend, I will prove it.

You know. With everything that has happened. Getting threatened with gun, getting fired, losing my work visa and having to leave behind all the friends I had known for years, them also firing my manager bc he stood up for me. All the bullshit here in Europe, with law enforcement telling people to not do business with me on threat of sanctions. Now my bank account getting closed down, and the last of my savings for whatever reason being frozen. I can see why people go into crime. Like honestly, I understand the psychology behind it now. I'm ready to dissappear and do cybercrime. The irony is, people have been portraying me like this my entire career.. despite all the sacrifices and hard work.. I think the last of my morals has gone out of the window, because this world, it doesn't play by the rules, and the people who do, they just end up broke and hopeless. Even in "civil society", the people who are succesful are sociopaths who have ruined atleast as many, if not more lifes then the real criminals.. atleast the criminals don't pretend to be anything they arn't ... atleast got to respect that.
I don't get it. It all start when I started finding all these bugs in TLS protocols and whatnot... like someone actively trying to ruin my life. I wouldn't be suprised if there's some jealous shithead intel folks doing this. All these people are jealous bc they are no skill losers. Yea, fuck you all.

Going to quit therapy. I have 5k EUR left, half of that is frozen by my bank, which is also closing my account. Cant afford it. Finish this math, and prepare to depart Europe to go and find a way to make a living elsewhere. Not going to die here in Europe like this. 

Just really starting to despise this world and people. I made so much sacrifices, and I have nothing, broke, living with my parents at age 35. All my friends half a world away thanks to msft. Just fundamentally beginning to change me. Especially the pain of having had to leave behind my friends. That more then anything. I can do cybercrime now, might aswell become the person everyone wants me to be.

Looking at that try_sm() function, right now, I'm just multiplying moduli together until its square is higher then x*N, but when summing coefficients, they can be anywhere from 0 to the modulus... and if we then square them.. it creates too much variance, there is no garantuee it will be close to x*N, which is what the end goal is. So need a better approach there. There is still literal exponential speed gains to be made there.. this is definitely unexplored territory.. I don't get it man. Throwing my work on github, honestly, its the last thing I want (and wanted) to do... but what other choice do I have? I have nothing, I can't find employment, I can't sell my work. Just nothing. What other choice do I have anymore? Anyway.. once I figure out how to sort out that function.. I guess my work is done. If I can get it done near perfectly, I estimate that the performance gains are going to push it well beyond anything else out there.
