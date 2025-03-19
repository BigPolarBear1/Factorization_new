!!!Work in progress!!!!

Uploaded a new version (18 march):

Will factor 150 bit in a couple of minutes on a laptop.

Use: python3 QS.py -keysize 150

To do: After reading about number field sieve, I realized I can use quadratic coefficients as algebraic factor base. This makes a lot more sense and would overcome many of the shortcomings of the uploaded PoC. I will upload a version using number field sieve's approach shortly.. my hope is that it not only improves this PoC but also improves existing number field sieve methods.

Note: I have been unemployed for over a year and am also still looking for work: big_polar_bear1@proton.me 

New york fbi and Belgian feds are too noisy. Good thing ill be in Asia soon, not going to wait for those fuckers to harass me.

They can close my bank account, freeze my money, but I'll simply make more money and get the hell out of this place. Can't stop me from going to Asia. There is nothing for me here in the west. Fuckers have literally put me on a sanctions list and are threatening folks who want to do business with me. There's no life nor future for me in the west. I'm getting the hell out of here asap. 

Anyway, i've managed to implement the sieving logic used in number field sieve in python (i.e finding smooths in a rational and algebraic base) ... just got to adjust it to work with my own findings... should be all done this week... then either one of two things will happen: It outperforms NFS since we don't have to worry about polynomial selection... or I find out that all I have been doing is a weaker version of what NFS is doing. But my bets are on the first one. Either way, once I understand this NFS stuff at a deep level like I do quadratic sieve now ... I will be situated at the cutting edge...and from there it will only be a matter of time until a real breakthrough happens. None of this has been lost time. I started with 0 math knowledge, couldn't even do highschool algebra, and I'm proud how far I've gotten now.

The more I read about NFS, and the more I understand about it.. the more I am convinced using quadratic coefficients is much better. That whole polynomial selection step is conveluted. Just use quadratic coefficients, it has those exact same properties....

Shit day, not very productive. Maybe one or two hours of work. Atleast I figured out the number field sieve stuff I guess..... it's not as daunting as I had feared. Feeling very optimistic about it. Now truely entering the final stage of this project.. I should probably hurry and work hard, everyone in my life seems sad I'm doing this math now for 2 years and not focused on making a living.. but something tells me, I have to push on, something tells me all my findings wern't as bad as people told me they were, that I was actually on the right path all along... and that if I don't see it through now, I miss my one chance to do something important. I'm just so stressed and depressed. My financial situation is very dire now.. cant even take a vacation... had to cancel my ski expedition too.. something I really wanted to do. Oh well. 

If those quadratic coefficients work for quadratic sieve, then they will also work for GNFS. I really cant see or understand why it wouldn't work. Its so much better then just generating some polynomial of higher degree with roots and coefficient and all those moving parts... just use quadratic coefficients...  well... it shouldn't be long now... before the end of the month a working PoC will come online. I am so horribly depressed, but I know western intel wants nothing more then for me to take my own life, but they dont know how determined I am, they'll have to come kill me instead. Ofcourse even at that they wouldn't succeed, bc western intel is all weak little people, haha. 

Watching some movies, and slowly processing the stuff about NFS in my head.... it will work with quadratic coefficients. Why would you use polynomials if you can just use quadratic coefficients (fuck the roots too, we dont care) ... its just looking for the same type of homomorphism or whatever the fancy math word is. I've spent 2 years on this problem. It only took me a minute of reading about NFS for me to immediatly recognize this... people must have known.. there is no way people wouldn't have known. But if they had known, then why has nobody told me? That is the part I don't understand. People must think im some kind of fool. Always just showing me disrespect. Before the end of the month, I will finish this and put it online. Perhaps had I not been disrespected like this, a different outcome would have been possible.
