# Factorization_new

Work in progress.

Uses Quadratic coefficients, this makes it easier to paralellize and we don't have the issue where x^2-n becomes bigger and bigger as x increases.
But since at every sieve interval step this subtracts N, we do need a larger factor base.
I'm going to dig in some more if that issue can somehow be managed. Maybe just subtract N mod m or something.. I'll try some things tomorrow.

Current PoC use: python3 QS.py -keysize 70  (current settings will work well up to 80 bits)
