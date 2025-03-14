!!!Work in progress!!!!

Uploaded a new version (14 march):

Will factor 100 bit moduli in about 10 seconds.

Use: python3 QS.py -keysize 100

Increase base (and potentially sieve_interval) for higher bits when smooth finding gets too slow. I will improve the smooth finding code soon.

To do: This is a work in progress. I need to do some optimizations this weekend in try_sm, to create even smaller numbers. As the heuristic for this is very sloppy right now. And also create more combinations there as we're skipping a lot of them. I hope to get it all done this weekend.

Heavily modified version of (to use quadratic coefficients instead): https://github.com/NachiketUN/Quadratic-Sieve-Algorithm/blob/master/src/main.py
