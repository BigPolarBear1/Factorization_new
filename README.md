!!!!WORK IN PROGRESS!!!!!!!

Useage: python3 QS.py -keysize 60

Notes: Just uploaded my latest iterations (5 march 2025). It now uses linear congruences to generate numbers less then N which are then tested for smoothness.

Better version will be released soon...

Ergh... now I see how it works. 
Its actually very simple.

Get rid of quadratic coefficients. 

Just calculate multiples of N. 
Take the square root and ceil it (like in standard QS).
From there we can do logarithmic sieving as is standard. 
After the values start becoming too big, move to the next multiple of N... and repeat.

That's really all there is too it. lol. 
*sigh* feeling suicidal. 

The way I calculated those quadratic coefficients, they are just for 4*N. 
I guess I could start subtracting 4*N from those coefficients and see where they become 0... which means they form a relation. 
I wonder what the quadratic coefficients for 5*N look like.. is it just the residues of N added to the quadratic coefficients of 4*N? 

I had been misunderstanding my findings this entire time. Maybe not all is lost. Perhaps this new insight will lead to a much better solution.

update: Hmmm... I need to just look at quadratic coefficients mod P, and subtract N mod P from them.. when they get to 0 they form a relation.. and I can use that information to construct smooths. That's how it should be done I believe... god fucking damnit. So fucking mentally exhausted.

I.e if a quadratic coefficient mod 11 is 5, then the squared one is 5^2 mod 11, 5^2 - 4*4387 = 0 mod 11. So I know there is a relation there with 4N inbetween. I got to start generalizing this ...  I just need to find multiple relations like this... then multiply them together .... i cant think clearly in this place with all the stress going on. 

Wasted atleast 2 weeks going down wrong rabbit holes when the real answer was infront of me all along... I tried to mimic traditional QS... while in reality I had to zero in on finding relations in quadratic coefficients mod P in isolation.. there's no point in pivoting my findings into normal QS.. that is conveluted and nullifies any of its strengths... ergh. FUCK. AND FUCK MICROSOFT. 
