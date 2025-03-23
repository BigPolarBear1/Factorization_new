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

Fuck america and fuck europe. Fucking nazi losers. I'll fight america to the death. For everything they did. For their lack of respect and for the harassment.

Literally, the harassment, getting threatened with a gun, msft portraying me as incompetent, all bc of fucking MAGA anti-trans misinformation. I garantuee you this, I will make sure this will cost america everything they have.
Ruined my life you fuckers.

Literally nothing to lose anymore. Headed to Asia one way or another, whatever it takes. And if anyone tries to stop me, im ready to die. Took everything fron me and ruined my life. Nothing left to lose now.

Tomorrow ill figure out the number theory for using quadratic coefficients with NFS.. I am so depressed, it physically hurts. The memories of my friends, all so far away now.. I hate msft. That company ruined my life and the life of my manager. I swear, those people better never cross my path... I will succeed with my math. I may not be "book smart" like all the douche bags on social media .. but I understand this problem better then any of them. They havnt spent months tinkering with numbers like I have. 

Pain and trauma changes a person... when I joined msft and moved to vancouver.. all the silly stuff like rollerskating with my teamlead around the seawall, being young and worrying about shit young people worry about.. that person is now dead. Getting threatened with a gun, getting harassed, the way microsoft treated me and my manager after those events. Maybe thats just part of "growing old", maybe thats why there exists no happy older people, maybe they all got broken by the meatgrinder that is this world. All I know now, is that I need to finish my math. Nothing else matters. Finishing this math is the only way any of that suffering will ever make sense. I will suceed at this math or I will kill myself, there is no other way anymore. 

I still do not understand why I am seeing more signals then ever before (excluding that one canadian stalker)... I am more isolated then ever, basically nobody talks to me anymore. But the signals are like a fucking christmas tree. More people are searching for "sandboxescaper" then ever before. I also swear I am under surveillance, but aside from vague intuition, you cant do much about it without appearing like a crazy person. I could be investigated I guess.. that would explain everything, and woudlnt suprise me bc western law enforcement sucks.

Crippled by depression again. Its 3pm and im still in bed. I cannot get work done. I would really like to get back to focusing on the number theory.. representing factorization as a system of quadratic congruences was the first step.. but there is something very deep about divisibility there that I have to understand.. but I just cant do it anymore. My life has gone to shit and I'm broke. Meanwhile I'm getting old. Just stuck with my parents. This isn't a life anymore. I honestly just want to die every day.

Too depressed today to do math. It's starting to get really bad. Going to apply to a bunch more Chinese companies and maybe also in Singapore. I know my Chinese friend wants me to just fly to China and help me find a job once I am there.. but its hard to trust strangers on the internet.. on the off chance its some internet troll trying to get me arrested in China.. it would be easier if it was just a normal company hiring me then some anonymous person.  If a company hired me, I would go without second thought at this point. There is absolutely nothing left but a slow dead for me here in Europe. Getting out of Europe is literally a fight for my life.

I guess another alternative is to start doing cryptological attacks against authentication protocols using certificates with weak keys, which are plentiful in the wild.. then just install monero miners... it would be trivial.. have some money again.. a way out of this.. have my freedom and dignity again. I just have to do whatever it takes to get out of this place and have a life again. Nothing to lose anymore... and if one day the police find out, I just take a weapon and fight to the death. Atleast I'll have a few more years of dignity. Because right now, I am not alive anymore. I am a already dead.

I dont think ive ever felt more ready to die then now. I just want the nightmare to stop.

Chasing your dreams is really hard. To keep pushing on with my entire life in ruins, it is the hardest thing I have ever done. Software vuln research is easy, there's literally nothing difficult about it.. this is on a different scale.. but I know this is what I want to do.. so I have two options, I keep doing shit that's too easy, or I sacrifice everything to do what I want to do. People don't know who I am. My former manager did, the only person in this entire industry who literally traveled all the way to Belgium back in the day to come be my friend at a time the entire industry had basically blacklisted me.. but I guess you all figured out a way by making things "normal" again by getting rid of not just me, but also him. Humans are truely pieces of shit. I'm not ever going to recover from everything that has happened. It fundamentally turned me into a different person, a much darker version of who I once was. Yet, I will solve this math problem.. and I dont mean a better version of number field sieve... I will solve this completely, even if it costs me everything, even if it costs me my life.

Got an hour of work done (at 4 am in the night, restless). Figured out the number theory.. it does work. It absolutely works. It just becomes a trick of finding favorable quadratic coefficient combinations... such that x^2 - y*x + c = 0 mod N .. and algebraic smooth candidates generated have to be small. 


