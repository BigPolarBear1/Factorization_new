!!!Work in progress!!!!

Uploaded a new version (14 march):

Will factor 100 bit moduli in about 10 seconds.

Use: python3 QS.py -keysize 100

Increase base (and potentially sieve_interval) for higher bits when smooth finding gets too slow. I will improve the smooth finding code soon.

To do: This is a work in progress. I need to do some optimizations this weekend in try_sm, to create even smaller numbers. As the heuristic for this is very sloppy right now. And also create more combinations there as we're skipping a lot of them. I hope to get it all done this weekend.

Heavily modified version of (to use quadratic coefficients instead): https://github.com/NachiketUN/Quadratic-Sieve-Algorithm/blob/master/src/main.py

Update: Oh I just realized a quick fix in try_sm() to make it work many times faster... If we add a bunch of quadratic coefficients together.. and the number ends up being too big, we can subtract some quadratic coefficients again.. as long as the square is above x*N... its still a bit sloppy.. ideally I want to come up with a way better heuristic there... but that should already massively increase the odds of hitting smooths.. let me fix that tomorrow.. I got headache right now.
