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
