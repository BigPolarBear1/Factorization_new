!!!!WORK IN PROGRESS!!!!!!!

Useage: python3 QS.py -keysize 60

Notes: Just uploaded my latest iterations (5 march 2025). It now uses linear congruences to generate numbers less then N which are then tested for smoothness.

Better version will be released soon...

When summing quadratic coefficients, we just need to find sums, which are atleast bigger then N, but as small as possible mod N. That is definitely something I can do by means of heuristic or "weights". Then test if its in the factor base.. and move on. Then we dont need to worry about division mod N. My PoC already works, it generates numbers less then N... and we can keep generating them basically for eternity.. its just zero-ing in on small numbers mod N now.. because there is no point in testing large numbers for smoothness. Depressed. Nothing good is happenning in life. Lost my savings now. People in the west being told not to do business with me. I've been unemployed for over a year, without income.  All because some fuckers pointed a gun at me and shouted insults at me in Redmond. Anyone would become extremely agitated. I had told my manager about the harassment, and when he tried to protest them firing me, they also fired my manager. Just 0 respect for people at Microsoft. Doesn't matter how hard you work. Guess I'm turning 35 this week. Unemployed living with my parents. I'm either going to kill myself, move to China or turn to cyber crime. There isn't any other alternatives. Mostly sad, that the memories of all the friends I had are fading from memory..  I didn't think life would ever become like this again. Rollerblading around the seawall with my teamlead, that was some cool shit.. places and people I'll never see again thanks to microsoft. I dont know what im supposed to do.

Update: OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOH. So if N is 4387. And the square root of N is +/- 66. Hence any quadratic coefficient which is a 66*x + 1 (or +2, +3, whatever) will result in a small squared coefficient mod N!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Then when summing non-squared partial results together (see paper), we should attempt to have it close to a multiple of 66. Which is EASY! If we just make a selection, see how far we are from a multiple of 66, then we can quickly "shift" the selection to a small one. Or simply assign "weights" to each selection to help guide which ones we should sum together. And as long as the square is larger then N, we will have a small value mod N, and thus, if it divides by the factor base... we WIN. That is how you do it! I got it! I found it! Haha. Tomorrow I'll write the code. Tired tonight. The guys at the pentagon gonna be so mad, haha.




