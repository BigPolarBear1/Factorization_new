!!!!WORK IN PROGRESS!!!!!!!

Useage: python3 QS.py -keysize 60

Notes: Just uploaded my latest iterations (5 march 2025). It now uses linear congruences to generate numbers less then N which are then tested for smoothness.

Better version will be released soon...

Damnit, I got basically everything figured out. We start with a squared quadratic coefficient, and we start dividing it mod N until we get something in the factor base (but it has to loop around N atleast once). 
Which can be reformulated as a weaker version of the discrete log problem.. since we don't need an exact residue, just a small one mod N, as that almost garantuees it to be in the factor base.
I know the math of it, and having a bunch of inverses to choose from, it should allow me to figure out how to choose a combination of inverses to get a small residue mod N. I know the exact math, how multiplying by inverses changes the residue .. I should be able to construct some kind of heuristic from that. Just hard to focus. I feel really depressed and I miss my friends. It's been a year now. And two years since I lived in Vancouver. Slowly the faces of the friends I had known fading out of memory, and time just relentlessly progressing. Stuck here, with months flying by and nothing good happening. Just the hate because of what Microsoft did to my Manager, portraying me as incompetent and fabricating lies so they could fire my manager without a severance. It makes me feel violent and angry. I hate these people. They will pay the price for what they have done.
