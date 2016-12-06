from itertools import chain
def jam(s):
    a = s.split('\n')
    a = [x.split(',') for x in a]
    shows = []
    names = []
    test = []
    for i in a:
        shows.append(i[len(i)-1])
        names.append([i[1].split(' with '),i[2].split(' and '),i[len(i)-2].split(' and ')])
    for i in names:
        test.append(list(chain(*i)))
    seen = set()
    names = []
    for e in test:
        for i in e:
             if i not in seen and not seen.add(i):
                 x = i.strip()
                 names.append(x)
    names.sort()
    final = {x: s.count(x) for x in names}
    return final
print (jam('''1/1/1 22 December 1967, Nicholas Parsons with Derek Nimmo, Clement Freud, Wilma Ewart and Beryl Reid, excuses for being late.
2/1/2 29 December 1967, Nicholas Parsons with Derek Nimmo, Clement Freud, Sheila Hancock and Carol Binstead, bedrooms.
3/1/3 5 January 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Betty Marsden and Elisabeth Beresford, ?
4/1/4 12 January 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Isobel Barnett and Bettine Le Beau, ?
5/1/5 20 January 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Andree Melly and Prunella Scales, the brownies
6/1/6 27 January 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Marjorie Proops and Millie Small, ?
7/1/7 2 February 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Aimi Macdonald and Una Stubbs, my honeymoon.
8/1/8 9 February 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Lucy Bartlett and Anona Winn, bloomer.
9/1/9 17 February 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Andree Melly and Charmian Innes, ?
10/1/10 23 February 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Barbara Blake and Renee Houston, my first grown-up dress.
11/1/11 1 March 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Andree Melly and Eleanor Summerfield, ?
12/1/12 8 March 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Andree Melly and Betty Marsden, ?
13/1/13 15 March 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Andree Melly and Charmian Innes, when I wear a top hat.
14/1/14 22 March 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Andree Melly and Betty Marsden, keeping wicket.
15/1/15 29 March 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Andree Melly and Charmian Innes, outdoor games.
16/1/16 5 April 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Andree Melly and Aimi Macdonald, how to stay lovely.
17/2/1 30 September 1968, Nicholas Parsons with Kenneth Williams, Clement Freud and Geraldine Jones, learning to fly.
18/2/2 7 October 1968, Clement Freud with Kenneth Williams, Nicholas Parsons and Geraldine Jones, making an entrance.
19/2/3 14 October 1968, Geraldine Jones with Kenneth Williams, Clement Freud and Nicholas Parsons, how to eat macaroni delicately and without cutting it.
20/2/4 21 October 1968, Kenneth Williams with Clement Freud, Nicholas Parsons and Geraldine Jones, the days of the week.
21/2/5 28 October 1968, Nicholas Parsons with Kenneth Williams, Clement Freud and Geraldine Jones, winter woollies.
22/2/6 4 November 1968, Nicholas Parsons with Kenneth Williams, Clement Freud and Geraldine Jones, Pythagoras.
23/3/1 31 December 1968, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Geraldine Jones, ?
24/3/2 7 January 1969, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Geraldine Jones, how to get a seat in a crowded train.
25/3/3 14 January 1969, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Andree Melly, doing nothing.
26/3/4 21 January 1969, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Andree Melly, what you see in the looking glass.
27/3/5 28 January 1969, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Betty Marsden, striking a fresh acquaintance.
28/3/6 4 February 1969, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Lucy Bartlett, dog watch.
29/3/7 11 February 1969, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Geraldine Jones, giving up smoking.
30/3/8 18 February 1969, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Geraldine Jones, the best hour of the week.
31/3/9 25 February 1969, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Andree Melly, gossipping.
32/3/10 4 March 1969, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Andree Melly, what to do with your vitality.
33/3/11 11 March 1969, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Aimi Macdonald, how to be good.
34/3/12 18 March 1969, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Juno Alexander, ?
35/3/13 25 March 1969, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Geraldine Jones, how best to colonise the Moon.
36/3/14 1 April 1969, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Geraldine Jones, ?
37/4/1 29 September 1969, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Andree Melly, what to reply to how to you do.
38/4/2 6 October 1969, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Miriam Karlin, where to draw the line.
39/4/3 13 October 1969, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Geraldine Jones, preventing long telephone conversations.
40/4/4 20 October 1969, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Juno Alexander, the function of a good waiter.
41/4/5 27 October 1969, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Teddie Beverley, the things I say.
42/4/6 3 November 1969, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Sheila Hancock, bloomers.
43/4/7 10 November 1969, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Geraldine Jones, interviewing a secretary.
44/4/8 17 November 1969, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Fenella Fielding, receiving compliments.
45/4/9 24 November 1969, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Sheila Hancock, appearing in public.
46/4/10 1 December 1969, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Andree Melly, what I most desire.
47/4/11 8 December 1969, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Sheila Hancock, watchdog.
48/4/12 15 December 1969, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Moira Lister, hot dogs.
49/4/13 22 December 1969, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Sheila Hancock, joy.
50/4/14 29 December 1969, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Miriam Karlin, makeup.
51/4/15 5 January 1970, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Sheila Hancock, Bacchus.
52/4/16 12 January 1970, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Aimi Macdonald, policemen.
53/4/17 19 January 1970, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Sheila Hancock, false teeth.
54/4/18 26 January 1970, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Diane Hart, astrology.
55/4/19 2 February 1970, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Aimi Macdonald, Oliver Cromwell.
56/4/20 9 February 1970, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Geraldine Jones, Constantinople.
57/4/21 16 February 1970, Clement Freud with Kenneth Williams, Derek Nimmo, Nicholas Parsons and Sheila Hancock, the Blarney stone.
58/4/22 23 February 1970, Kenneth Williams with Derek Nimmo, Clement Freud, Nicholas Parsons and Geraldine Jones, the alphabet.
59/4/23 2 March 1970, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Andree Melly, passing the buck.
60/4/24 9 March 1970, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Geraldine Jones, Hercules.
61/4/25 16 March 1970, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Andree Melly, Boswell.
62/4/26 23 March 1970, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Denise Coffey, breaking a code.
63/4/27 30 March 1970, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Geraldine Jones, Romulus and Remus.
64/5/1 8 September 1970, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Sheila Hancock, demonectomy.
65/5/2 15 September 1970, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Sheila Hancock, something for nothing.
66/5/3 22 September 1970, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Sheila Hancock, the little people.
67/5/4 29 September 1970, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Sheila Hancock, a nice cup of tea.
68/5/5 6 October 1970, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Denise Coffey, polystyrene.
69/5/6 13 October 1970, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Denise Coffey, ironing my smalls.
70/5/7 20 October 1970, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Denise Coffey, avoiding the bill in a restaurant.
71/5/8 27 October 1970, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Denise Coffey, thrills.
72/5/9 3 November 1970, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Andree Melly, admirable virtues.
73/5/10 10 November 1970, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Andree Melly, avoiding income tax.
74/5/11 17 November 1970, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Andree Melly, wine.
75/5/12 24 November 1970, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Andree Melly, what excites me.
76/5/13 1 December 1970, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Jacqueline MacKenzie, my cooker.
77/5/14 8 December 1970, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Jacqueline MacKenzie, panic.
78/5/15 15 December 1970, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Joan Turner, enjoying life.
79/5/16 22 December 1970, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Liz Fraser, stuffing your Christmas bird.
80/5/17 29 December 1970, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Katharine Whitehorn, panache.
81/5/18 5 January 1971, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Prunella Scales, astronomy.
82/5/19 12 January 1971, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Sheila Hancock, Christmas party games.
83/5/20 19 January 1971, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Sheila Hancock, modern art.
84/5/21 26 January 1971, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Sheila Hancock, snags of show business.
85/5/22 2 February 1971, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Sheila Hancock, demonstrating.
86/5/23 9 February 1971, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Andree Melly, unblocking the kitchen sink.
87/5/24 16 February 1971, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Andree Melly, jellyfish.
88/5/25 23 February 1971, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Barbara Castle, Frederick the Great.
89/5/26 2 March 1971, Nicholas Parsons with Kenneth Williams, Derek Nimmo and Clement Freud, Kenneth Williams.
90/6/1 12 October 1971, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Andree Melly, doing my own thing.
91/6/2 19 October 1971, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Andree Melly, playing with my yoyo.
92/6/3 26 October 1971, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Andree Melly, men.
93/6/4 2 November 1971, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Andree Melly, being tickled.
94/6/5 9 November 1971, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Sheila Hancock, the chairman.
95/6/6 16 November 1971, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Sheila Hancock, just a minute.
96/6/7 23 November 1971, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Sheila Hancock, lights.
97/6/8 30 November 1971, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Sheila Hancock, treachery.
98/6/9 7 December 1971, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Katharine Whitehorn, flamboyancy.
99/6/10 14 December 1971, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Katharine Whitehorn, essentials.
100/6/11 21 December 1971, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Aimi Macdonald, how to live to be a hundred years old.
101/6/12 28 December 1971, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Aimi Macdonald, optimism.
102/6/13 4 January 1972, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Andree Melly, impulses.
103/6/14 11 January 1972, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Andree Melly, cooking an octopus.
104/6/15 18 January 1972, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Andree Melly, sensible winter underwear.
105/6/16 25 January 1972, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Andree Melly, jazz.
106/6/17 1 February 1972, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Sheila Hancock, quince.
107/6/18 8 February 1972, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Sheila Hancock, noise.
108/6/19 15 February 1972, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Sheila Hancock, my life so far.
109/6/20 22 February 1972, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Sheila Hancock, frozen food.
110/6/21 29 February 1972, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Juno Alexander, fellow feeling.
111/6/22 7 March 1972, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Juno Alexander, hats.
112/6/23 14 March 1972, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Andree Melly, highways and byways.
113/6/24 21 March 1972, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Andree Melly, the abdabs.
114/6/25 28 March 1972, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Andree Melly, my socks.
115/6/26 4 April 1972, Andree Melly with Kenneth Williams, Clement Freud, Peter Jones and Nicholas Parsons, the position I now find myself in.
116/7/1 5 September 1972, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Aimi Macdonald, hairy legs.
117/7/2 12 September 1972, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Andree Melly, things I should never have done.
118/7/3 19 September 1972, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Sheila Hancock, sneakers.
119/7/4 26 September 1972, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, malapropisms.
120/7/5 3 October 1972, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Andree Melly, the Minute Waltz.
121/7/6 10 October 1972, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Aimi Macdonald, getting knotted.
122/7/7 17 October 1972, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Sheila Hancock, fiddlesticks.
123/7/8 24 October 1972, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Aimi Macdonald, my opinion.
124/7/9 31 October 1972, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Andree Melly, the multitude.
125/7/10 7 November 1972, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Sheila Hancock, empathy.
126/7/11 14 November 1972, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Aimi Macdonald, getting launched on the waters of oratory.
127/7/12 21 November 1972, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, nothing at all.
128/7/13 28 November 1972, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Sheila Hancock, piggy banks.
129/7/14 5 December 1972, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Aimi Macdonald, putting a bold face on it.
130/7/15 12 December 1972, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Andree Melly, what they say about me.
131/7/16 19 December 1972, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Sheila Hancock, traumatic experiences.
132/7/17 26 December 1972, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Aimi Macdonald, silent night.
133/7/18 2 January 1973, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Andree Melly, fan mail.
134/7/19 9 January 1973, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Sheila Hancock, what I stand for.
135/7/20 16 January 1973, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, reputation.
136/7/21 23 January 1973, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Sheila Hancock, idleness.
137/7/22 30 January 1973, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Aimi Macdonald, my exuberance.
138/7/23 6 February 1973, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Andree Melly, relativity.
139/7/24 13 February 1973, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Sheila Hancock, my favourite drink.
140/7/25 20 February 1973, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Aimi Macdonald, gross impertinence.
141/7/26 27 February 1973, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, aniseed balls.
142/8/1 30 July 1973, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, making a spectacular entrance.
143/8/2 6 August 1973, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Sheila Hancock, my foibles.
144/8/3 13 August 1973, Nicholas Parsons with Derek Nimmo, Clement Freud, Peter Jones and David Jacobs, my giddy aunt.
145/8/4 20 August 1973, Nicholas Parsons with Clement Freud, Peter Jones, Jean Marsh and Warren Mitchell, what I don't usually say.
146/8/5 27 August 1973, Nicholas Parsons with Clement Freud, Peter Jones, Aimi Macdonald and Ian Carmichael, checks.
147/8/6 3 September 1973, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Sheila Hancock, keeping prices down.
148/8/7 10 September 1973, Nicholas Parsons with Derek Nimmo, Clement Freud, Peter Jones and David Jacobs, a night on the tiles.
149/8/8 17 September 1973, Nicholas Parsons with Clement Freud, Peter Jones, Jean Marsh and Warren Mitchell, cobber.
150/8/9 24 September 1973, Nicholas Parsons with Clement Freud, Peter Jones, Aimi Macdonald and Ian Carmichael, steak and kidney pie.
151/8/10 1 October 1973, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Sheila Hancock, ecstasy.
152/8/11 8 October 1973, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Alfred Marks, how I restrain myself.
153/8/12 15 October 1973, Nicholas Parsons with Derek Nimmo, Clement Freud, Peter Jones and Barry Took, making notes.
154/8/13 22 October 1973, Nicholas Parsons with Derek Nimmo, Clement Freud, Peter Jones and Sheila Hancock, an appreciative audience.
155/8/14 29 October 1973, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Jean Marsh, exhortations.
156/8/15 5 November 1973, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Alfred Marks, being absolutely certain.
157/8/16 12 November 1973, Nicholas Parsons with Derek Nimmo, Clement Freud, Peter Jones and Barry Took, pate.
158/8/17 19 November 1973, Nicholas Parsons with Derek Nimmo, Clement Freud, Peter Jones and Sheila Hancock, diction.
159/8/18 26 November 1973, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Jean Marsh, rude words.
160/8/19 3 December 1973, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Andree Melly, Stephen Leacock.
161/8/20 10 December 1973, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Aimi Macdonald, my energy.
162/8/21 17 December 1973, Nicholas Parsons with Derek Nimmo, Clement Freud, Peter Jones and Andree Melly, my great-uncle Augustus.
163/8/22 24 December 1973, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Sheila Hancock, my dustbin.
164/8/23 31 December 1973, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Andree Melly, the wisest thing I ever heard.
165/8/24 7 January 1974, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Aimi Macdonald, how to think.
166/8/25 14 January 1974, Nicholas Parsons with Derek Nimmo, Clement Freud, Peter Jones and Andree Melly, peat.
167/8/26 21 January 1974, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, waiting.
168/9/1 16 September 1974, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, the first of a new series.
169/9/2 23 September 1974, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Jean Marsh, sparklers.
170/9/3 30 September 1974, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Sheila Hancock, my finest hour.
171/9/4 7 October 1974, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Jean Marsh, making a real fuss.
172/9/5 14 October 1974, Nicholas Parsons with Derek Nimmo, Clement Freud, Peter Jones and Barry Cryer, streaking.
173/9/6 21 October 1974, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Andree Melly, gettng wound up.
174/9/7 28 October 1974, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Barry Cryer, chambers.
175/9/8 4 November 1974, Nicholas Parsons with Derek Nimmo, Clement Freud, Peter Jones and Andree Melly, what I came here to say.
176/9/9 11 November 1974, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Sheila Hancock, waiting rooms.
177/9/10 18 November 1974, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Andree Melly, Niagara Falls.
178/9/11 25 November 1974, Nicholas Parsons with Derek Nimmo, Clement Freud, Peter Jones and Sheila Hancock, getting round people.
179/9/12 2 December 1974, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Alfred Marks, hedonism.
180/9/13 9 December 1974, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Andree Melly, my undoing.
181/9/14 16 December 1974, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Sheila Hancock, the Naismith steam hammer drop forging process.
182/9/15 23 December 1974, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Andree Melly, ?
183/9/16 30 December 1974, Nicholas Parsons with Derek Nimmo, Clement Freud, Peter Jones and Barry Cryer, distractions.
184/9/17 6 January 1975, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Sheila Hancock, a chairman's job.
185/9/18 13 January 1975, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Barry Cryer, how to celebrate.
186/9/19 20 January 1975, Nicholas Parsons with Derek Nimmo, Clement Freud, Peter Jones and Andree Melly, concealing the body.
187/9/20 27 January 1975, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Sheila Hancock, my muscles.
188/9/21 3 February 1975, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Andree Melly, getting carried away.
189/9/22 10 February 1975, Nicholas Parsons with Derek Nimmo, Clement Freud, Peter Jones and Sheila Hancock, getting pinched.
190/9/23 17 February 1975, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Alfred Marks, what I learn from this show.
191/9/24 24 February 1975, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Andree Melly, bill stickers.
192/9/25 3 March 1975, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Sheila Hancock, getting a lot of letters.
193/9/26 10 March 1975, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Aimi Macdonald, jury service.
194/9/27 17 March 1975, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, the way the wind blows.
195/10/1 23 September 1975, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Alfred Marks, starters.
196/10/2 30 September 1975, Nicholas Parsons with Derek Nimmo, Clement Freud, Peter Jones and Aimi Macdonald, standing up for my rights.
197/10/3 7 October 1975, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Aimi Macdonald, attack.
198/10/4 14 October 1975, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Alfred Marks, a commanding lead.
199/10/5 21 October 1975, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Patrick Moore, how I carry on.
200/10/6 28 October 1975, Nicholas Parsons with Clement Freud, Peter Jones, Sheila Hancock and Graeme Garden, hang gliding.
201/10/7 4 November 1975, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Aimi Macdonald, democracy.
202/10/8 11 November 1975, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Liz Fraser, the biggest laugh I ever had.
203/10/9 18 November 1975, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Michael Palin, a spree.
204/10/10 25 November 1975, Nicholas Parsons with Kenneth Williams, Peter Jones, Sheila Hancock and William Rushton, pleasure.
205/10/11 2 December 1975, Nicholas Parsons with Clement Freud, Peter Jones, Aimi Macdonald and Patrick Moore, sleep walking.
206/10/12 9 December 1975, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Sheila Hancock, what gives me the horrors.
207/10/13 16 December 1975, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Andree Melly, polo.
208/10/14 23 December 1975, Nicholas Parsons with Kenneth Williams, Peter Jones, Sheila Hancock and William Rushton, crackers.
209/10/15 30 December 1975, Nicholas Parsons with Derek Nimmo, Clement Freud, Peter Jones and Aimi Macdonald, awards.
210/10/16 6 January 1976, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Alfred Marks, the Parisian Latin quarter.
211/10/17 13 January 1976, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Alfred Marks, putting one over.
212/10/18 20 January 1976, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Patrick Moore, the fourth Earl Ross to say nothing of his 42 inch reflector.
213/10/19 27 January 1976, Nicholas Parsons with Clement Freud, Peter Jones, Sheila Hancock and Graeme Garden, puppets.
214/10/20 3 February 1976, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Liz Fraser, staying power.
215/10/21 10 February 1976, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Michael Palin, spanker.
216/10/22 17 February 1976, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Sheila Hancock, big game hunters.
217/10/23 24 February 1976, Nicholas Parsons with Clement Freud, Peter Jones, Aimi Macdonald and Patrick Moore, how to stop snoring.
218/10/24 2 March 1976, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Aimi Macdonald, pogo.
219/10/25 9 March 1976, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Andree Melly, fascinations.
220/11/1 3 November 1976, Nicholas Parsons with Kenneth Williams, Peter Jones, Sheila Hancock and Alfred Marks, what I put into life.
221/11/2 10 November 1976, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Graeme Garden, making my peace.
222/11/3 17 November 1976, Nicholas Parsons with Kenneth Williams, Peter Jones, Janet Brown and Magnus Pyke, keeping fit.
223/11/4 24 November 1976, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Patrick Moore, litterbugs.
224/11/5 1 December 1976, Nicholas Parsons with Derek Nimmo, Clement Freud, Peter Jones and Thora Hird, poverty.
225/11/6 8 December 1976, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Ray Alan, my plot.
226/11/7 15 December 1976, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Sheila Hancock, trolls.
227/11/8 22 December 1976, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Janet Brown, me.
228/11/9 29 December 1976, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Alfred Marks, the Moon.
229/11/10 5 January 1977, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, bath night.
230/11/11 12 January 1977, Ian Messiter with Kenneth Williams, Derek Nimmo, Peter Jones and Nicholas Parsons, bangs.
231/11/12 19 January 1977, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Magnus Pyke, burlesque.
232/11/13 26 January 1977, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, fun and games.
233/11/14 2 February 1977, Nicholas Parsons with Kenneth Williams, Peter Jones, Sheila Hancock and Alfred Marks, how to frighten this audience.
234/11/15 9 February 1977, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Graeme Garden, making my mark.
235/11/16 16 February 1977, Nicholas Parsons with Kenneth Williams, Peter Jones, Janet Brown and Magnus Pyke, show stoppers.
236/11/17 23 February 1977, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Patrick Moore, my impulses.
237/11/18 2 March 1977, Nicholas Parsons with Derek Nimmo, Clement Freud, Peter Jones and Thora Hird, knees.
238/11/19 9 March 1977, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Ray Alan, pride.
239/11/20 16 March 1977, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Sheila Hancock, peanuts.
240/11/21 23 March 1977, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Janet Brown, my ploy.
241/11/22 30 March 1977, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Alfred Marks, how I get going.
242/11/23 6 April 1977, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, the broads.
243/11/24 13 April 1977, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, the friendliest one I know.
244/11/25 20 April 1977, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Magnus Pyke, relaxation.
245/11/26 27 April 1977, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, plus Ian Messiter, my dignity.
246/12/1 21 February 1978, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Sheila Hancock and Bernard Cribbins, fools.
247/12/2 28 February 1978, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Patrick Moore, being scared.
248/12/3 7 March 1978, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Tommy Trinder, being scared.
249/12/4 14 March 1978, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Janet Brown, eccentrics.
250/12/5 21 March 1978, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and June Whitfield, what makes me burst with pride.
251/12/6 28 March 1978, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Sheila Hancock, making a good start.
252/12/7 4 April 1978, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, salesmen.
253/12/8 11 April 1978, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Sheila Hancock and Bernard Cribbins, customs.
254/12/9 18 April 1978, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Patrick Moore, how to become celebrated.
255/12/10 25 April 1978, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Tommy Trinder, why parrots don't sneeze.
256/12/11 2 May 1978, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Janet Brown, moose.
257/12/12 9 May 1978, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and June Whitfield, attack.
258/12/13 16 May 1978, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Sheila Hancock, making up.
259/12/14 23 May 1978, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, getting wound up.
260/13/1 23 January 1979, Nicholas Parsons with Kenneth Williams, Peter Jones, Aimi Macdonald and Patrick Moore, a grand opening.
261/13/2 30 January 1979, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, getting started.
262/13/3 6 February 1979, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Joan Bakewell, my ideal.
263/13/4 13 February 1979, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, excitement.
264/13/5 20 February 1979, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Ray Alan, simplicity.
265/13/6 27 February 1979, Nicholas Parsons with Kenneth Williams, Clement Freud, Tim Brooke-Taylor and Kenneth Robinson, why I should be knighted.
266/13/7 6 March 1979, Nicholas Parsons with Kenneth Williams, Clement Freud, Barry Took and Peter Cook, my other self.
267/13/8 13 March 1979, Nicholas Parsons with Kenneth Williams, Peter Jones, Aimi Macdonald and Patrick Moore, foolishness.
268/13/9 20 March 1979, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, customs.
269/13/10 27 March 1979, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Joan Bakewell, improvisation.
270/13/11 8 May 1979, Nicholas Parsons with Kenneth Williams, Clement Freud, Kenneth Robinson and Miriam Margolyes, hotch potch.
271/13/12 15 May 1979, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Ray Alan, if I were not a thespian.
272/13/13 22 May 1979, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, parbuckles.
273/13/14 29 May 1979, Nicholas Parsons with Kenneth Williams, Clement Freud, Barry Took and Peter Cook, the Loch Ness monster.
274/14/1 11 December 1979, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Peter Cook, how to get cracking.
275/14/2 18 December 1979, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Lorraine Chase, taking a diabolical liberty.
276/14/3 25 December 1979, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Lance Percival, exhibitionism.
277/14/4 1 January 1980, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Patrick Moore, overdoing it.
278/14/5 8 January 1980, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, looking ahead.
279/14/6 15 January 1980, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Tim Rice, rolls.
280/14/7 22 January 1980, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Rob Buckman, springing into action.
281/14/8 29 January 1980, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Aimi Macdonald, Aimi Macdonald.
282/14/9 5 February 1980, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Kenny Everett, the Mexican hat dance.
283/14/10 12 February 1980, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Sheila Hancock, bugling.
284/14/11 19 February 1980, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Barry Cryer, my resolution for this programme.
285/14/12 26 February 1980, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and John Junkin, getting a good start.
286/14/13 4 March 1980, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Bob Monkhouse, getting sent.
287/14/14 11 March 1980, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, my accolade.
288/15/1 7 March 1981, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Tim Rice, being forceful.
289/15/2 14 March 1981, Nicholas Parsons with Kenneth Williams, Clement Freud, Barry Cryer and Lance Percival, my following.
290/15/3 21 March 1981, Nicholas Parsons with Kenneth Williams, Peter Jones, Barry Took and Tim Brooke-Taylor, enough money.
291/15/4 28 March 1981, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Aimi Macdonald, having women in the show.
292/15/5 4 April 1981, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and John Junkin, parking meters.
293/15/6 11 April 1981, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Sheila Hancock, fruit.
294/15/7 18 April 1981, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, the best game.
295/15/8 25 April 1981, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Tim Rice, bliss.
296/15/9 2 May 1981, Nicholas Parsons with Clement Freud, Kenneth Williams, Barry Cryer and Graeme Garden, getting ice cubes out of the tray.
297/15/10 9 May 1981, Nicholas Parsons with Kenneth Williams, Peter Jones, Barry Took and Tim Brooke-Taylor, striving for perfection.
298/15/11 16 May 1981, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Aimi Macdonald, Irish humour.
299/15/12 23 May 1981, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and John Junkin, getting a shock.
300/15/13 30 May 1981, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Sheila Hancock, disreputable people.
301/15/14 6 June 1981, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, poor.
302/16/1 23 January 1982, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, the best way to lie.
303/16/2 30 January 1982, Nicholas Parsons with Kenneth Williams, Peter Jones, Sheila Hancock and Michael Wood, what amazes me.
304/16/3 6 February 1982, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Ian Messiter, the first time I appeared in public.
305/16/4 13 February 1982, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Graeme Garden, the strangest thing.
306/16/5 20 February 1982, Nicholas Parsons with Kenneth Williams, Tim Rice, John Junkin and Brian Johnston, moments of drama.
307/16/6 27 February 1982, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Denise Coffey, evasiveness.
308/16/7 6 March 1982, Nicholas Parsons with Kenneth Williams, Clement Freud, Barry Cryer and Libby Purves, laurel.
309/16/8 13 March 1982, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, blowing bubbles.
310/16/9 31 July 1982, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, what our audience loves.
311/16/10 7 August 1982, Nicholas Parsons with Kenneth Williams, Peter Jones, Sheila Hancock and Gyles Brandeth, the most outstanding personality in this show.
312/16/11 14 August 1982, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Victoria Wood, the most incredible thing I know.
313/16/12 21 August 1982, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Graeme Garden, what makes me excited.
314/16/13 28 August 1982, Nicholas Parsons with Kenneth Williams, Tim Rice, John Junkin and Maureen Lipman, my intellectual approach to the six pips of the Greenwich time signal.
315/16/14 4 September 1982, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Gyles Brandreth, being nosey.
316/16/15 11 September 1982, Nicholas Parsons with Kenneth Williams, Clement Freud, Barry Cryer and Elaine Stritch, kangaroo pie.
317/16/16 18 September 1982, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, things of mine refused by garbage collectors.
318/17/1 14 March 1983, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Sheila Hancock and Gyles Brandreth, the fun of bath night.
319/17/2 21 March 1983, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Jeremy Beadle, binge.
320/17/3 28 March 1983, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Liza Goddard, getting stung.
321/17/4 4 April 1983, Nicholas Parsons with Kenneth Williams, Clement Freud, Gyles Brandreth and Barry Cryer, good luck.
322/17/5 11 April 1983, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Miles Kington, trade tricks.
323/17/6 18 April 1983, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Sheila Hancock and Gyles Brandreth, the most loveable points of a rhinoceros.
324/17/7 25 April 1983, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Jan Ravens, getting at an itch in the middle of my back.
325/17/8 2 May 1983, Nicholas Parsons with Kenneth Williams, Clement Freud, Aimi Macdonald and Jeremy Beadle, early morning exercises.
326/17/9 9 May 1983, Clement Freud with Kenneth Williams, Derek Nimmo, Peter Jones and Nicholas Parsons, making a sausage roll.
327/17/10 16 May 1983, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Brian Johnston, telephone answering machines.
328/17/11 24 September 1983, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Victoria Wood, going off at the deep end.
329/17/12 1 October 1983, Nicholas Parsons with Kenneth Williams, Clement Freud, Aimi Macdonald and Jan Ravens, how to have fun in a public library.
330/17/13 8 October 1983, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and John Junkin, getting a good start.
331/17/14 15 October 1983, Kenneth Williams with Derek Nimmo, Clement Freud, Peter Jones and Nicholas Parsons, miller.
332/17/15 22 October 1983, Nicholas Parsons with Kenneth Williams, Peter Jones, Tim Rice and Libby Purves, magic.
333/17/16 29 October 1983, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Brian Johnston, getting dressed on the beach.
334/17/17 5 November 1983, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and John Junkin, paradise.
335/17/18 12 November 1983, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Victoria Wood, fun on the trampoline.
336/17/19 19 November 1983, Nicholas Parsons with Kenneth Williams, Peter Jones, Tim Rice and Libby Purves, plankton.
337/17/20 26 November 1983, Nicholas Parsons with Kenneth Williams, Clement Freud, Gyles Brandreth and Barry Cryer, a bad joke.
338/18/1 16 June 1984, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Tim Rice, the opening shot.
339/18/2 23 June 1984, Nicholas Parsons with Kenneth Williams, Clement Freud, Libby Purves and Henry Kelly, getting a thrill.
340/18/3 30 June 1984, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Gyles Brandreth and Martin Jarvis, a hoax.
341/18/4 7 July 1984, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and William Franklyn, my gambit.
342/18/5 14 July 1984, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and John Baddeley, the Marie Celeste.
343/18/6 21 July 1984, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Henry Kelly, encouragement.
344/18/7 28 July 1984, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Gyles Brandreth and Martin Jarvis, hide.
345/18/8 4 August 1984, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and John Baddeley, tongue twisters.
346/18/9 11 August 1984, Nicholas Parsons with Kenneth Williams, Peter Jones, Tim Rice and Barry Cryer, looking to the future.
347/18/10 18 August 1984, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, sparkle.
348/18/11 6 February 1985, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Martin Jarvis, taking command.
349/18/12 13 February 1985, Nicholas Parsons with Kenneth Williams, Clement Freud, Libby Purves and Toni Arthur, what I saw in a joke shop.
350/18/13 20 February 1985, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Tim Rice, punctuality.
351/18/14 27 February 1985, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Sheila Hancock, the Taj Mahal.
352/18/15 6 March 1985, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Martin Jarvis, a turn.
353/18/16 13 March 1985, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Henry Kelly, seals.
354/18/17 20 March 1985, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Sheila Hancock, milking a camel.
355/18/18 27 March 1985, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and William Franklyn, hail.
356/18/19 3 April 1985, Nicholas Parsons with Kenneth Williams, Peter Jones, Tim Rice and Barry Cryer, epics.
357/18/20 10 April 1985, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, the intellectual members of the audience.
358/19/1 14 December 1985, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, nightmares.
359/19/2 28 December 1985, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, the parson's nose.
360/19/3 4 January 1986, Nicholas Parsons with Kenneth Williams, Clement Freud, Gyles Brandreth and Tim Rice, doppelganger.
361/19/4 11 January 1986, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Simon Bates, slapstick.
362/19/5 18 January 1986, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Barry Cryer and Ian Hislop, trivia.
363/19/6 25 January 1986, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and William Franklyn, Arabian nights.
364/19/7 1 February 1986, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Simon Bates, luxury.
365/19/8 8 February 1986, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Barry Cryer and Ian Hislop, bubble baths.
366/19/9 15 February 1986, Nicholas Parsons with Kenneth Williams, Clement Freud, Gyles Brandreth and Tim Rice, lawyers.
367/19/10 22 February 1986, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and William Franklyn, green jellybabies.
368/19/11 1 March 1986, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, weather.
369/20/1 4 April 1987, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, customs.
370/20/2 11 April 1987, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Alfred Marks, talking to plants.
371/20/3 18 April 1987, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Tim Rice, will power.
372/20/4 25 April 1987, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Sheila Hancock and Tim Rice, fools.
373/20/5 2 May 1987, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, a grand occasion.
374/20/6 9 May 1987, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Stanley Unwin, winter pyjamas.
375/20/7 16 May 1987, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Tim Rice, habits.
376/20/8 23 May 1987, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Sheila Hancock and Tim Rice, ballooning.
377/20/9 30 May 1987, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Peter Jones and Alfred Marks, magic.
378/20/10 13 June 1987, Nicholas Parsons with Kenneth Williams, Clement Freud, Peter Jones and Eleanor Summerfield, getting animated.
379/20/11 20 June 1987, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, jersey.
380/20/12 27 June 1987, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, glory.
381/21/1 5 May 1988, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, fashionable bed attire.
382/21/2 12 May 1988, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Wendy Richard, going bananas.
383/21/3 19 May 1988, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Richard Murdoch, nappies.
384/21/4 26 May 1988, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Lance Percival, nuts.
385/21/5 2 June 1988, Nicholas Parsons with Clement Freud, Peter Jones, Lance Percival and Christopher Timothy, records.
386/21/6 9 June 1988, Nicholas Parsons with Clement Freud, Peter Jones, Lance Percival and Christopher Timothy, applause.
387/21/7 16 June 1988, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Wendy Richard, atlas.
388/21/8 23 June 1988, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, getting uptight.
389/22/1 28 March 1989, Nicholas Parsons with Clement Freud, Peter Jones, Wendy Richard and Barry Cryer, jams.
390/22/2 4 April 1989, Nicholas Parsons with Paul Merton, Derek Nimmo, Peter Jones and Richard Murdoch, coconut shies.
391/22/3 11 April 1989, Nicholas Parsons with Clement Freud, Wendy Richard, Richard Murdoch and Lance Percival, scales.
392/22/4 18 April 1989, Nicholas Parsons with Derek Nimmo, Clement Freud, Barry Cryer and Christopher Timothy, Manhattan.
393/22/5 25 April 1989, Nicholas Parsons with Paul Merton, Derek Nimmo, Peter Jones and Tim Rice, pinching.
394/22/6 2 May 1989, Nicholas Parsons with Derek Nimmo, Peter Jones, Tim Rice and Stanley Unwin, actors.
395/22/7 9 May 1989, Nicholas Parsons with Clement Freud, Wendy Richard, Richard Murdoch and Lance Percival, slang.
396/22/8 16 May 1989, Nicholas Parsons with Clement Freud, Peter Jones, Wendy Richard and Barry Cryer, gerry building.
397/22/9 23 May 1989, Nicholas Parsons with Derek Nimmo, Clement Freud, Barry Cryer and Christopher Timothy, keeping baby amused.
398/22/10 4 April 1989, Nicholas Parsons with Paul Merton, Derek Nimmo, Peter Jones and Richard Murdoch, poker.
399/23/1 17 March 1990, Nicholas Parsons with Paul Merton, Derek Nimmo, Clement Freud and Peter Jones, beauty contests.
400/23/2 24 March 1990, Nicholas Parsons with Paul Merton, Peter Jones, Wendy Richard and Richard Murdoch, garden worms.
401/23/3 31 March 1990, Nicholas Parsons with Derek Nimmo, Clement Freud, Tim Rice and Jimmy Mulville, package deals.
402/23/4 7 April 1990, Nicholas Parsons with Paul Merton, Derek Nimmo, Clement Freud and Peter Jones, sneezes.
403/23/5 14 April 1990, Nicholas Parsons with Derek Nimmo, Clement Freud, Tim Rice and Emma Freud, odds.
404/23/6 21 April 1990, Nicholas Parsons with Derek Nimmo, Clement Freud, Peter Jones and Wendy Richard, diaries.
405/23/7 28 April 1990, Nicholas Parsons with Paul Merton, Peter Jones, Wendy Richard and Richard Murdoch, defrosting the fridge.
406/23/8 5 May 1990, Nicholas Parsons with Derek Nimmo, Clement Freud, Peter Jones and Wendy Richard, health food shops.
407/24/1 5 January 1991, Nicholas Parsons with Paul Merton, Derek Nimmo, Clement Freud and Peter Jones, selling by telephone.
408/24/2 12 January 1991, Nicholas Parsons with Peter Jones, Tim Rice, Wendy Richard and Richard Stilgoe, chop suey.
409/24/3 19 January 1991, Nicholas Parsons with Paul Merton, Derek Nimmo, Clement Freud and Peter Jones, graffiti.
410/24/4 26 January 1991, Nicholas Parsons with Paul Merton, Derek Nimmo, Clement Freud and Sandi Toksvig, China.
411/24/5 2 February 1991, Nicholas Parsons with Derek Nimmo, Clement Freud, Peter Jones and Wendy Richard, telepathy.
412/24/6 9 February 1991, Nicholas Parsons with Paul Merton, Derek Nimmo, Clement Freud and Jimmy Mulville, bags.
413/24/7 16 February 1991, Nicholas Parsons with Derek Nimmo, Clement Freud, Peter Jones and Wendy Richard, a good part to play.
414/24/8 23 February 1991, Nicholas Parsons with Peter Jones, Tim Rice, Wendy Richard and Richard Stilgoe, biscuits in bed.
415/25/1 4 January 1992, Nicholas Parsons with Derek Nimmo, Clement Freud, Peter Jones and Maureen Lipman, jam.
416/25/2 11 January 1992, Nicholas Parsons with Paul Merton, Derek Nimmo, Wendy Richard and Stephen Fry, what to put on a muffin.
417/25/3 18 January 1992, Nicholas Parsons with Paul Merton, Clement Freud, Peter Jones and Helen Lederer, the boot.
418/25/4 25 January 1992, Nicholas Parsons with Derek Nimmo, Clement Freud, Peter Jones and Wendy Richard, this and that.
419/25/5 1 February 1992, Nicholas Parsons with Derek Nimmo, Clement Freud, Peter Jones and John Junkin, what.
420/25/6 8 February 1992, Nicholas Parsons with Paul Merton, Derek Nimmo, Wendy Richard and Stephen Fry, a good hand.
421/25/7 15 February 1992, Nicholas Parsons with Paul Merton, Clement Freud, Peter Jones and Tony Hawks, my silliest habit.
422/25/8 22 February 1992, Nicholas Parsons with Derek Nimmo, Clement Freud, Peter Jones and Wendy Richard, advertising.
423/25/9 20 July 1992 and 27 July 1992, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, plus Paul Merton, Tony Hawks, Sheila Hancock, Tim Rice, Wendy Richard, Stephen Fry, Barry Cryer, Richard Murdoch, Peter Cook, Ian Messiter, Victoria Wood, Jimmy Mulville, Elaine Stritch and Sandi Toksvig, Silver Minutes.
424/26/1 2 January 1993, Nicholas Parsons with Paul Merton, Clement Freud, Wendy Richard and Tony Slattery, briefs.
425/26/2 9 January 1993, Nicholas Parsons with Derek Nimmo, Clement Freud, Tony Hawks and Wendy Richard, bollards.
426/26/3 16 January 1993, Nicholas Parsons with Paul Merton, Derek Nimmo, Clement Freud and Peter Jones, Wales.
427/26/4 23 January 1993, Nicholas Parsons with Paul Merton, Clement Freud, Peter Jones and Caroline Quentin, the year ahead.
428/26/5 30 January 1993, Nicholas Parsons with Paul Merton, Derek Nimmo, Peter Jones and Richard Morton, custard pie humour.
429/26/6 6 February 1993, Nicholas Parsons with Paul Merton, Clement Freud, Wendy Richard and Tony Slattery, anyone in this show.
430/26/7 13 February 1993, Nicholas Parsons with Derek Nimmo, Clement Freud, Wendy Richard and Alistair McGowan, farmers.
431/26/8 20 February 1993, Nicholas Parsons with Paul Merton, Derek Nimmo, Clement Freud and Peter Jones, stocking.
432/26/9 27 February 1993, Nicholas Parsons with Paul Merton, Clement Freud, Peter Jones and Jim Sweeney, splits.
433/26/10 6 March 1993, Nicholas Parsons with Paul Merton, Derek Nimmo, Peter Jones and Craig Ferguson, reports.
434/27/1 1 January 1994, Nicholas Parsons with Derek Nimmo, Clement Freud, Peter Jones and Jenny Eclair, Scarborough.
TV1/1/1 6 January 1994, Nicholas Parsons with Tony Slattery, Tony Hawks, Kit Hesketh-Harvey and Helen Lederer, Eros.
435/27/2 8 January 1994, Nicholas Parsons with Paul Merton, Peter Jones, Stephen Fry and Pete McCarthy, pale.
TV2/1/2 13 January 1994, Nicholas Parsons with Tony Slattery, Arthur Smith, Jeremy Hardy and Mariella Frostrup, what the butler saw at 10 Downing Street.
436/27/3 15 January 1994, Nicholas Parsons with Paul Merton, Derek Nimmo, Clement Freud and Eddie Izzard, double whammy.
TV3/1/3 20 January 1994, Nicholas Parsons with Tony Slattery, Graham Norton, Arthur Smith and Ann Bryson, the House of Lords.
437/27/4 22 January 1994, Nicholas Parsons with Clement Freud, Tony Hawks, Kit Hesketh-Harvey and Hugh Dennis, Norwich.
TV4/1/4 27 January 1994, Nicholas Parsons with Tony Slattery, Clement Freud, Tony Hawks and Richard Vranch, double parking.
438/27/5 29 January 1994, Nicholas Parsons with Paul Merton, Clement Freud, Peter Jones and Arthur Smith, auld reekie.
TV5/1/5 3 February 1994, Nicholas Parsons with Tony Slattery, Tony Hawks, Kit Hesketh-Harvey and Helen Lederer, London pride.
439/27/6 5 February 1994, Nicholas Parsons with Paul Merton, Peter Jones, Wendy Richard and Lee Simpson, a great party.
TV6/1/6 10 February 1994, Nicholas Parsons with Tony Slattery, Jim Sweeney, Lee Simpson and Tony Blackburn, a try at Twickenham.
440/27/7 12 February 1994, Nicholas Parsons with Derek Nimmo, Peter Jones, Clement Freud and Jenny Eclair, what I don't talk about.
TV7/1/7 17 February 1994, Nicholas Parsons with Tony Slattery, Arthur Smith, Richard Vranch and Pete McCarthy, things to do on South End Pier.
441/27/8 19 February 1994, Nicholas Parsons with Paul Merton, Derek Nimmo, Clement Freud and Eddie Izzard, Edwin King of Northumberland.
TV8/1/8 24 February 1994, Nicholas Parsons with Tony Slattery, Derek Nimmo, Nick Revell and John Fortune, my elephant and castle.
442/27/9 26 February 1994, Nicholas Parsons with Paul Merton, Clement Freud, Peter Jones and Greg Proops, Princes Street.
TV9/1/9 3 March 1994, Nicholas Parsons with Tony Slattery, Neil Mullarkey, Tony Banks and Hattie Hayridge, Heathrow.
443/27/10 5 March 1994, Nicholas Parsons with Paul Merton, Peter Jones, Stephen Fry and Jan Ravens, metalwork.
TV10/1/10 2 August 1994, Nicholas Parsons with Tony Slattery, Clement Freud, Tony Hawks and Richard Vranch, London nightlife.
TV11/1/11 9 August 1994, Nicholas Parsons with Tony Slattery, Jim Sweeney, Lee Simpson and Jo Brand, the London Marathon.
TV12/1/12 16 August 1994, Nicholas Parsons with Tony Slattery, Derek Nimmo, Nick Revell and John Fortune, the scrubs.
TV13/1/13 23 August 1994, Nicholas Parsons with Tony Slattery, Arthur Smith, Richard Vranch and Ted Robbins, how we survived the Blitz.
TV14/1/14 30 August 1994, Nicholas Parsons with Tony Slattery, Neil Mullarkey, Tony Banks and Hattie Hayridge, why Oscar Wilde decided to live in Tight Street.
444/28/1 24 December 1994, Nicholas Parsons with Derek Nimmo, Clement Freud, Peter Jones and Stephen Fry, my favourite Christmas present.
445/28/2 31 December 1994, Nicholas Parsons with Paul Merton, Derek Nimmo, Clement Freud and Tony Hawks, tamoshanter.
446/28/3 7 January 1995, Nicholas Parsons with Derek Nimmo, Peter Jones, Tony Hawks and Jeremy Hardy, Glamorgan.
447/28/4 14 January 1995, Nicholas Parsons with Clement Freud, Tony Hawks, Kit Hesketh-Harvey and Hugh Dennis, jesters.
448/28/5 21 January 1995, Nicholas Parsons with Paul Merton, Derek Nimmo, Clement Freud and Tony Hawks, the firth of Forth.
449/28/6 28 January 1995, Nicholas Parsons with Paul Merton, Peter Jones, Kit Hesketh-Harvey and Jenny Eclair, mobile phones.
450/28/7 4 February 1995, Nicholas Parsons with Paul Merton, Derek Nimmo, Peter Jones and Steve Frost, a crash course.
451/28/8 11 February 1995, Nicholas Parsons with Derek Nimmo, Peter Jones, Tony Hawks and Jeremy Hardy, dragons.
452/28/9 18 February 1995, Nicholas Parsons with Paul Merton, Peter Jones, Wendy Richard and Lee Simpson, the third row of this audience.
453/28/10 25 February 1995, Nicholas Parsons with Paul Merton, Peter Jones, Kit Hesketh-Harvey and Jenny Eclair, playing the fool.
454/28/11 4 March 1995, Nicholas Parsons with Paul Merton, Derek Nimmo, Peter Jones and Steve Frost, odd surnames.
TV15/2/1 2 June 1995, Nicholas Parsons with Tony Slattery, Dale Winton, Clement Freud and Helen Lederer, wolves.
TV16/2/2 9 June 1995, Nicholas Parsons with Tony Slattery, Dale Winton, Richard Vranch and Tony Blackburn, having a double.
TV17/2/3 16 June 1995, Nicholas Parsons with Tony Slattery, Dale Winton, Mariella Frostrup and Carolyn Marshall, groceries in Grantham.
TV18/2/4 23 June 1995, Nicholas Parsons with Tony Slattery, Dale Winton, Graham Norton and Su Pollard, my first audition.
TV19/2/5 30 June 1995, Nicholas Parsons with Tony Slattery, Dale Winton, Kit Hesketh-Harvey and Jeremy Hardy, ?
TV20/2/6 7 July 1995, Nicholas Parsons with Tony Slattery, Dale Winton, Arthur Smith and Jim Sweeney, what I'm doing here.
TV21/2/7 14 July 1995, Nicholas Parsons with Tony Slattery, Dale Winton, Clement Freud and Helen Lederer, the M1.
TV22/2/8 21 July 1995, Nicholas Parsons with Tony Slattery, Dale Winton, Richard Vranch and Craig Charles, weekends.
TV23/2/9 28 July 1995, Nicholas Parsons with Tony Slattery, Dale Winton, Wendy Richard and Liza Goddard, Dale's diary.
TV24/2/10 4 August 1995, Nicholas Parsons with Tony Slattery, Dale Winton, Kit Hesketh-Harvey and Jeremy Hardy, the glamour of Solihull.
TV25/2/11 11 August 1995, Nicholas Parsons with Tony Slattery, Dale Winton, Tony Banks and Mariella Frostrup, down the tube.
TV26/2/12 18 August 1995, Nicholas Parsons with Tony Slattery, Dale Winton, Arthur Smith and Jim Sweeney, who is buried under Platform 10 at Waterloo Station.
TV27/2/13 25 August 1995, Nicholas Parsons with Tony Slattery, Dale Winton, Wendy Richard and Liza Goddard, ?
TV28/2/14 1 September 1995, Nicholas Parsons with Tony Slattery, Dale Winton, Graham Norton and Su Pollard, ?
455/29/1 6 January 1996, Nicholas Parsons with Paul Merton, Derek Nimmo, Clement Freud and Peter Jones, the capital of Scotland.
456/29/2 13 January 1996, Nicholas Parsons with Paul Merton, Clement Freud, Peter Jones and Kit Hesketh-Harvey, charisma.
457/29/3 20 January 1996, Nicholas Parsons with Derek Nimmo, Peter Jones, Tony Hawks and Fred MacAulay, Ayr.
458/29/4 27 January 1996, Nicholas Parsons with Paul Merton, Derek Nimmo, Clement Freud and Maria McErlane, Robin Hood.
459/29/5 3 February 1996, Nicholas Parsons with Derek Nimmo, Peter Jones, Graham Norton and Tony Hawks, castles.
460/29/6 10 February 1996, Nicholas Parsons with Paul Merton, Clement Freud, Peter Jones and Kit Hesketh-Harvey, big bang theory.
461/29/7 17 February 1996, Nicholas Parsons with Derek Nimmo, Peter Jones, Tony Hawks and Fred MacAulay, Burns.
462/29/8 24 February 1996, Nicholas Parsons with Paul Merton, Derek Nimmo, Clement Freud and Maria McErlane, goose.
463/29/9 2 March 1996, Nicholas Parsons with Derek Nimmo, Peter Jones, Graham Norton and Tony Hawks, Lindisfarne.
464/29/10 9 March 1996, Nicholas Parsons with Paul Merton, Derek Nimmo, Clement Freud and Peter Jones, tattoo.
465/30/1 4 January 1997, Nicholas Parsons with Paul Merton, Derek Nimmo, Clement Freud and Peter Jones, the Scotsman.
466/30/2 11 January 1997, Nicholas Parsons with Paul Merton, Derek Nimmo, Peter Jones and Neil Mullarkey, swan.
467/30/3 18 January 1997, Nicholas Parsons with Paul Merton, Clement Freud, Peter Jones and Graham Norton, pressing the flesh.
468/30/4 25 January 1997, Nicholas Parsons with Paul Merton, Derek Nimmo, Clement Freud and Julian Clary, jersey.
469/30/5 1 February 1997, Nicholas Parsons with Clement Freud, Peter Jones, Tony Hawks and Fred MacAulay, St Andrew's.
470/30/6 8 February 1997, Nicholas Parsons with Paul Merton, Derek Nimmo, Clement Freud and Peter Jones, the Highlands.
471/30/7 15 February 1997, Nicholas Parsons with Paul Merton, Derek Nimmo, Peter Jones and Neil Mullarkey, sauce.
472/30/8 22 February 1997, Nicholas Parsons with Paul Merton, Clement Freud, Peter Jones and Graham Norton, tripe.
473/30/9 1 March 1997, Nicholas Parsons with Clement Freud, Peter Jones, Tony Hawks and Fred MacAulay, greens.
474/30/10 8 March 1997, Nicholas Parsons with Paul Merton, Derek Nimmo, Clement Freud and Julian Clary, cows.
475/31/1 19 July 1997, Nicholas Parsons with Paul Merton, Clement Freud, Peter Jones and Arthur Smith, Manchester.
476/31/2 26 July 1997, Nicholas Parsons with Paul Merton, Clement Freud, Peter Jones and Kit Hesketh-Harvey, Leicestershire.
477/31/3 2 August 1997, Nicholas Parsons with Derek Nimmo, Clement Freud, Tony Hawks and Fred MacAulay, Glasgow.
478/31/4 9 August 1997, Nicholas Parsons with Paul Merton, Clement Freud, Peter Jones and Kit Hesketh-Harvey, flying by the seat of my pants.
479/31/5 16 August 1997, Nicholas Parsons with Derek Nimmo, Clement Freud, Tony Hawks and Fred MacAulay, citizens.
480/32/1 3 January 1998, Nicholas Parsons with Paul Merton, Derek Nimmo, Graham Norton and Greg Proops, getting in first.
481/32/2 10 January 1998, Nicholas Parsons with Paul Merton, Clement Freud, Peter Jones and Arthur Smith, the street.
482/32/3 17 January 1998, Nicholas Parsons with Paul Merton, Clement Freud, Tim Rice and Gerry Kelly, the crack.
483/32/4 8 September 1997 and 24 January 1998, Nicholas Parsons with Paul Merton, Derek Nimmo, Clement Freud and Peter Jones, logjam.
484/32/5 31 January 1998, Nicholas Parsons with Paul Merton, Derek Nimmo, Graham Norton and Greg Proops, forbidden fruit.
485/32/6 7 February 1998, Nicholas Parsons with Paul Merton, Clement Freud, Tim Rice and Gerry Kelly, pleasantries.
486/32/7 14 February 1998, Nicholas Parsons with Paul Merton, Derek Nimmo, Clement Freud and Peter Jones, Scottish widows.
487/33/1 8 June 1998, Nicholas Parsons with Paul Merton, Derek Nimmo, Clement Freud and Julian Clary, bath Oliver.
488/33/2 15 June 1998, Nicholas Parsons with Paul Merton, Clement Freud, Peter Jones and Maureen Lipman, where Just A Minute can be enjoyed.
489/33/3 22 June 1998, Nicholas Parsons with Paul Merton, Peter Jones, Steve Frost and Maria McErlane, what the actress said to the bishop.
490/33/4 29 June 1998, Nicholas Parsons with Derek Nimmo, Clement Freud, Peter Jones and Kit Hesketh-Harvey, palace.
491/33/5 6 July 1998, Nicholas Parsons with Paul Merton, Derek Nimmo, Tony Hawks and Blythe Duff, wee timorous beastie.
492/33/6 13 July 1998, Nicholas Parsons with Paul Merton, Peter Jones, Steve Frost and Maria McErlane, first words.
493/33/7 20 July 1998, Nicholas Parsons with Paul Merton, Clement Freud, Peter Jones and Maureen Lipman, white lies.
494/33/8 27 July 1998, Nicholas Parsons with Paul Merton, Derek Nimmo, Clement Freud and Julian Clary, service.
495/33/9 3 August 1998, Nicholas Parsons with Derek Nimmo, Clement Freud, Peter Jones and Kit Hesketh-Harvey, my favourite view.
496/33/10 10 August 1998, Nicholas Parsons with Paul Merton, Derek Nimmo, Tony Hawks and Blythe Duff, a university life.
497/34/1 18 January 1999, Nicholas Parsons with Derek Nimmo, Tony Hawks, Graham Norton and Linda Smith, the full monty.
498/34/2 25 January 1999, Nicholas Parsons with Paul Merton, Clement Freud, Peter Jones and Tony Hawks, the life and soul of the party.
499/34/3 1 February 1999, Nicholas Parsons with Peter Jones, Tim Rice, Jenny Eclair and Steve Frost, taking the sea air.
500/34/4 8 February 1999, Nicholas Parsons with Paul Merton, Clement Freud, Graham Norton and Fred MacAulay, breakfast in bed.
501/34/5 15 February 1999, Nicholas Parsons with Derek Nimmo, Clement Freud, Tony Slattery and Steve Frost, fast food.
502/34/6 22 February 1999, Nicholas Parsons with Paul Merton, Clement Freud, Peter Jones and Tony Hawks, the secret mission.
503/34/7 1 March 1999, Nicholas Parsons with Derek Nimmo, Tony Hawks, Graham Norton and Linda Smith, what makes me furious.
504/34/8 8 March 1999, Nicholas Parsons with Peter Jones, Tim Rice, Jenny Eclair and Steve Frost, giving your all.
505/34/9 15 March 1999, Nicholas Parsons with Paul Merton, Clement Freud, Graham Norton and Richard Morton, a can of worms.
506/34/10 22 March 1999, Nicholas Parsons with Derek Nimmo, Clement Freud, Tony Slattery and Steve Frost, the gatecrasher.
TV29/3/1 19 April 1999, Nicholas Parsons with Barry Cryer, John Sergeant, Su Pollard and Brian Sewell, ever decreasing circles.
TV30/3/2 20 April 1999, Nicholas Parsons with Tony Hawks, Wendy Richard, Steve Frost and Clare Balding, what I'd really like to talk about.
TV31/3/3 21 April 1999, Nicholas Parsons with Gyles Brandreth, Linda Smith, Isla Blair and Gary Wilmot, shrinking violet.
TV32/3/4 22 April 1999, Nicholas Parsons with Peter Jones, Linda Smith, Wendy Richard and Pam Ayres, Yorkshire pudding.
TV33/3/5 23 April 1999, Nicholas Parsons with Peter Jones, Tony Hawks, Gyles Brandreth and Jo Brand, St George's Day.
TV34/3/6 26 April 1999, Nicholas Parsons with Tony Hawks, Wendy Richard, Barry Cryer and Steve Frost, email.
TV35/3/7 27 April 1999, Nicholas Parsons with Peter Jones, Linda Smith, Maria McErlane and Michael Cashman, kitchen gadgets.
TV36/3/8 28 April 1999, Nicholas Parsons with Richard Vranch, Liza Goddard, Richard Morton and Tom O'Connor, rude words.
TV37/3/9 29 April 1999, Nicholas Parsons with Tony Hawks, Wendy Richard, Steve Frost and Clare Balding, duvets.
TV38/3/10 30 April 1999, Nicholas Parsons with Barry Cryer, John Sergeant, Su Pollard and Brian Sewell, shorthand.
TV39/3/11 3 May 1999, Nicholas Parsons with Gyles Brandreth, Linda Smith, Isla Blair and Gary Wilmot, if I ruled the world.
TV40/3/12 4 May 1999, Nicholas Parsons with Linda Smith, Wendy Richard, Maria McErlane and Steve Punt, virtual reality.
TV41/3/13 5 May 1999, Nicholas Parsons with Gyles Brandreth, Liza Goddard, Richard Morton and Ken Bruce, a bit on the side.
TV42/3/14 6 May 1999, Nicholas Parsons with Peter Jones, Linda Smith, Wendy Richard and Pam Ayres, mumbo jumbo.
TV43/3/15 10 May 1999, Nicholas Parsons with Tony Hawks, Wendy Richard, Barry Cryer and Steve Frost, garden gnomes.
TV44/3/16 11 May 1999, Nicholas Parsons with Peter Jones, Linda Smith, Maria McErlane and Michael Cashman, Niagara Falls.
TV45/3/17 12 May 1999, Nicholas Parsons with Peter Jones, Tony Hawks, Gyles Brandreth and Jo Brand, my greatest wish.
TV46/3/18 13 May 1999, Nicholas Parsons with Linda Smith, Wendy Richard, Maria McErlane and Steve Punt, the great British public.
TV47/3/19 14 May 1999, Nicholas Parsons with Gyles Brandreth, Liza Goddard, Richard Morton and Ken Bruce, flat feet.
TV48/3/20 26 May 1999, Nicholas Parsons with Richard Vranch, Liza Goddard, Richard Morton and Tom O'Connor, saying sorry.
507/35/1 5 July 1999, Nicholas Parsons with Paul Merton, Clement Freud, Peter Jones and Stephen Fry, flirting.
508/35/2 12 July 1999, Nicholas Parsons with Paul Merton, Clement Freud, Graham Norton and Fred MacAulay, breeding porcupines.
509/35/3 19 July 1999, Nicholas Parsons with Peter Jones, Kit Hesketh-Harvey, Jenny Eclair and Steve Frost, dreaming spires.
510/35/4 26 July 1999, Nicholas Parsons with Paul Merton, Clement Freud, Peter Jones and Tony Hawks, the wrong number.
511/35/5 2 August 1999, Nicholas Parsons with Peter Jones, Kit Hesketh-Harvey, Jenny Eclair and Steve Frost, mother tongue.
512/35/6 9 August 1999, Nicholas Parsons with Paul Merton, Clement Freud, Peter Jones and Stephen Fry, the novel inside me.
513/35/7 16 August 1999, Nicholas Parsons with Paul Merton, Clement Freud, Peter Jones and Greg Proops, the end of the century.
514/35/8 23 August 1999, Nicholas Parsons with Paul Merton, Clement Freud, Peter Jones and Richard Vranch, something I do only in Edinburgh.
515/35/9 30 August 1999, Nicholas Parsons with Paul Merton, Clement Freud, Peter Jones and Tony Hawks, York.
516/35/10 6 September 1999, Nicholas Parsons with Paul Merton, Clement Freud, Graham Norton and Fred MacAulay, speakeasy.
517/36/1 20 December 1999, Nicholas Parsons with Paul Merton, Clement Freud, Graham Norton and Linda Smith, Narcissus.
518/36/2 27 December 1999, Nicholas Parsons with Paul Merton, Clement Freud, Graham Norton and Linda Smith, the angel of the north.
519/36/3 3 January 2000, Nicholas Parsons with Clement Freud, Peter Jones, Tony Hawks and Kit Hesketh-Harvey, kicking off.
520/36/4 10 January 2000, Nicholas Parsons with Clement Freud, Peter Jones, Tony Hawks and Kit Hesketh-Harvey, milking laughs.
521/36/5 17 January 2000, Nicholas Parsons with Paul Merton, Peter Jones, Stephen Fry and Maria McErlane, laying it on with a trowel.
522/36/6 24 January 2000, Nicholas Parsons with Paul Merton, Peter Jones, Stephen Fry and Maria McErlane, miracles.
523/36/7 31 January 2000, Nicholas Parsons with Clement Freud, Graham Norton, Steve Frost and Martin Jarvis, hangovers.
524/36/8 7 February 2000, Nicholas Parsons with Clement Freud, Graham Norton, Steve Frost and Martin Jarvis, spice.
525/36/9 14 February 2000, Nicholas Parsons with Clement Freud, Julian Clary, Linda Smith and Simon Williams, casting off.
526/36/10 21 February 2000, Nicholas Parsons with Clement Freud, Julian Clary, Linda Smith and Simon Williams, powdering my nose.
527/37/1 3 July 2000, Nicholas Parsons with Clement Freud, Tony Hawks, Graham Norton and Linda Smith, smelling a rat.
528/37/2 10 July 2000, Nicholas Parsons with Paul Merton, Clement Freud, Linda Smith and Stephen Fry, what I wear in bed.
529/37/3 17 July 2000, Nicholas Parsons with Clement Freud, Tony Hawks, Sue Perkins and Jeremy Hardy, keeping your eye on the ball.
530/37/4 24 July 2000, Nicholas Parsons with Clement Freud, Tony Hawks, Graham Norton and Linda Smith, stuffing a chicken.
531/37/5 31 July 2000, Nicholas Parsons with Paul Merton, Clement Freud, Tim Rice and Annabel Giles, how I like to relax.
532/37/6 7 August 2000, Nicholas Parsons with Paul Merton, Clement Freud, Linda Smith and Stephen Fry, cats.
533/37/7 14 August 2000, Nicholas Parsons with Clement Freud, Tony Hawks, Sue Perkins and Jeremy Hardy, positive thinking.
534/37/8 21 August 2000, Nicholas Parsons with Paul Merton, Clement Freud, Tim Rice and Annabel Giles, chopsticks.
535/37/9 28 August 2000, Nicholas Parsons with Paul Merton, Clement Freud, Graham Norton and Ross Noble, the fringe.
536/37/10 4 September 2000, Nicholas Parsons with Paul Merton, Clement Freud, Graham Norton and Greg Proops, whiz kids.
537/38/1 1 January 2001, Nicholas Parsons with Clement Freud, Tony Hawks, Linda Smith and Ross Noble, taking the waters.
538/38/2 8 January 2001, Nicholas Parsons with Paul Merton, Clement Freud, Graham Norton and Sue Perkins, how to win friends and influence people.
539/38/3 15 January 2001, Nicholas Parsons with Paul Merton, Kit Hesketh-Harvey, Julian Clary and Linda Smith, a close shave.
540/38/4 22 January 2001, Nicholas Parsons with Paul Merton, Clement Freud, Graham Norton and Sue Perkins, the secret of eternal youth.
541/38/5 29 January 2001, Nicholas Parsons with Clement Freud, Tony Hawks, Linda Smith and Ross Noble, loyalty cards.
542/38/6 5 February 2001, Nicholas Parsons with Paul Merton, Kit Hesketh-Harvey, Julian Clary and Linda Smith, my first job.
543/38/7 12 February 2001, Nicholas Parsons with Tony Hawks, Graham Norton, Tim Rice and Jenny Eclair, bananas.
544/38/8 19 February 2001, Nicholas Parsons with Paul Merton, Clement Freud, Graham Norton and Barry Cryer, name dropping.
545/38/9 26 February 2001, Nicholas Parsons with Tony Hawks, Graham Norton, Tim Rice and Jenny Eclair, my philosophy of life.
546/38/10 5 March 2001, Nicholas Parsons with Paul Merton, Clement Freud, Graham Norton and Barry Cryer, a sore point.
547/39/1 9 July 2001, Nicholas Parsons with Paul Merton, Clement Freud, Julian Clary and Jenny Eclair, Brighton rock.
548/39/2 16 July 2001, Nicholas Parsons with Tony Hawks, Sue Perkins, Tim Rice and Ross Noble, the good old days.
549/39/3 23 July 2001, Nicholas Parsons with Paul Merton, Clement Freud, Liza Tarbuck and Steve Frost, rhubarb.
550/39/4 30 July 2001, Nicholas Parsons with Paul Merton, Clement Freud, Julian Clary and Jenny Eclair, how to annoy this audience.
551/39/5 6 August 2001, Nicholas Parsons with Tony Hawks, Sue Perkins, Tim Rice and Ross Noble, how to recognise a real Yorkshireman.
552/39/6 13 August 2001, Nicholas Parsons with Paul Merton, Clement Freud, Liza Tarbuck and Steve Frost, how to get rid of hiccups.
553/39/7 20 August 2001, Nicholas Parsons with Paul Merton, Clement Freud, Graham Norton and Linda Smith, keeping up with the Joneses.
554/39/8 27 August 2001, Nicholas Parsons with Clement Freud, Graham Norton, Jenny Eclair and Ross Noble, the cleverest person I know.
555/39/9 3 September 2001, Nicholas Parsons with Clement Freud, Graham Norton, Ross Noble and Charles Collingwood, how to remember people's names.
556/40/1 31 December 2001, Nicholas Parsons with Paul Merton, Clement Freud, Graham Norton and Linda Smith, the year ahead.
557/40/2 7 January 2002, Nicholas Parsons with Paul Merton, Clement Freud, Liza Tarbuck and Stephen Fry, crow's feet.
558/40/3 14 January 2002, Nicholas Parsons with Paul Merton, Kit Hesketh-Harvey, Linda Smith and Chris Neill, poetic licence.
559/40/4 21 January 2002, Nicholas Parsons with Paul Merton, Clement Freud, Sheila Hancock and Graham Norton, the magic of radio.
560/40/5 28 January 2002, Nicholas Parsons with Paul Merton, Clement Freud, Liza Tarbuck and Stephen Fry, blowing the whistle.
561/40/6 4 February 2002, Nicholas Parsons with Tony Hawks, Graham Norton, Tim Rice and Jenny Eclair, more haste less speed.
562/40/7 11 February 2002, Nicholas Parsons with Tony Hawks, Sue Perkins, Wendy Richard and Ross Noble, the wild west.
563/40/8 18 February 2002, Nicholas Parsons with Paul Merton, Kit Hesketh-Harvey, Linda Smith and Chris Neill, my idea of a perfect day.
564/40/9 25 February 2002, Nicholas Parsons with Tony Hawks, Graham Norton, Tim Rice and Jenny Eclair, how to complain in a restaurant.
565/40/10 4 March 2002, Nicholas Parsons with Tony Hawks, Sue Perkins, Wendy Richard and Ross Noble, the best advice I ever had.
566/40/11 11 March 2002, Nicholas Parsons with Paul Merton, Clement Freud, Sheila Hancock and Graham Norton, the Channel tunnel.
567/41/1 1 July 2002, Nicholas Parsons with Paul Merton, Clement Freud, Tony Hawks and Julian Clary, weather forecasters.
568/41/2 8 July 2002, Nicholas Parsons with Paul Merton, Clement Freud, Graham Norton and Liza Tarbuck, discos.
569/41/3 15 July 2002, Nicholas Parsons with Clement Freud, Gyles Brandreth, Jenny Eclair and Chris Neill, traffic wardens.
570/41/4 22 July 2002, Nicholas Parsons with Paul Merton, Clement Freud, Linda Smith and Ross Noble, Canterbury tales.
571/41/5 29 July 2002, Nicholas Parsons with Tony Hawks, Sue Perkins, Kit Hesketh-Harvey and Wendy Richard, the man on the Clapham omnibus.
572/41/6 5 August 2002, Nicholas Parsons with Paul Merton, Clement Freud, Tony Hawks and Julian Clary, how to make a Cornish pastie.
573/41/7 12 August 2002, Nicholas Parsons with Clement Freud, Gyles Brandreth, Jenny Eclair and Chris Neill, the Saxons.
574/41/8 19 August 2002, Nicholas Parsons with Tony Hawks, Sue Perkins, Kit Hesketh-Harvey and Wendy Richard, the changing of the guard.
575/41/9 26 August 2002, Nicholas Parsons with Paul Merton, Clement Freud, Ross Noble and Greg Proops, the chairman's darkest secret.
576/41/10 2 September 2002, Nicholas Parsons with Paul Merton, Clement Freud, Ross Noble and Sean Lock, how to play the bagpipes.
577/42/1 1 January 2003, Nicholas Parsons with Paul Merton, Clement Freud, Sheila Hancock and Graham Norton, plus Gyles Brandreth, Jenny Eclair, Ross Noble, Chris Neill, Steve Frost, Charles Collingwood, Pam Ayres, Helen Boaden and Malcolm Messiter, Just A Minute in 2050.
578/42/2 6 January 2003, Nicholas Parsons with Paul Merton, Clement Freud, Linda Smith and Ross Noble, how to hand in your resignation.
579/42/3 13 January 2003, Nicholas Parsons with Paul Merton, Clement Freud, Graham Norton and Liza Tarbuck, alternative medicine.
580/42/4 20 January 2003, Nicholas Parsons with Clement Freud, Tony Hawks, Graham Norton and Pam Ayres, upstaging people.
581/42/5 27 January 2003, Nicholas Parsons with Paul Merton, Kit Hesketh-Harvey, Ross Noble and Steve Frost, why I love queuing.
582/42/6 3 February 2003, Nicholas Parsons with Paul Merton, Clement Freud, Wendy Richard and Liza Tarbuck, why I don't use Cockney rhyming slang.
583/42/7 10 February 2003, Nicholas Parsons with Clement Freud, Tony Hawks, Graham Norton and Pam Ayres, being a rebel.
584/42/8 17 February 2003, Nicholas Parsons with Tony Hawks, Linda Smith, Chris Neill and Bill Bailey, growing old gracefully.
585/42/9 24 February 2003, Nicholas Parsons with Paul Merton, Kit Hesketh-Harvey, Ross Noble and Steve Frost, what goes on backstage.
586/42/10 3 March 2003, Nicholas Parsons with Paul Merton, Clement Freud, Wendy Richard and Liza Tarbuck, the butchers.
587/42/11 10 March 2003, Nicholas Parsons with Tony Hawks, Linda Smith, Chris Neill and Bill Bailey, what I dreamt about last night.
588/42/12 17 March 2003, Nicholas Parsons with Paul Merton, Clement Freud, Tony Hawks and Charles Collingwood, the wombles.
589/43/1 7 July 2003, Nicholas Parsons with Paul Merton, Clement Freud, Sheila Hancock and Kit Hesketh-Harvey, hogging the limelight.
590/43/2 14 July 2003, Nicholas Parsons with Paul Merton, Clement Freud, Tony Hawks and Charles Collingwood, ballroom dancing.
591/43/3 21 July 2003, Nicholas Parsons with Clement Freud, Tony Hawks, Jenny Eclair and Ross Noble, party poopers.
592/43/4 28 July 2003, Nicholas Parsons with Paul Merton, Clement Freud, Sheila Hancock and Kit Hesketh-Harvey, the perfect breakfast.
593/43/5 4 August 2003, Nicholas Parsons with Clement Freud, Tony Hawks, Linda Smith and Chris Neill, how to get rid of spots.
594/43/6 11 August 2003, Nicholas Parsons with Paul Merton, Clement Freud, Graham Norton and Linda Smith, the best dressed member of the panel.
595/43/7 18 August 2003, Nicholas Parsons with Clement Freud, Tony Hawks, Jenny Eclair and Ross Noble, something to write home about.
596/43/8 25 August 2003, Nicholas Parsons with Paul Merton, Clement Freud, Julian Clary and Ross Noble, breaking records.
597/43/9 1 September 2003, Nicholas Parsons with Paul Merton, Clement Freud, Greg Proops and Dara O'Briain, fringe benefits.
598/43/10 8 September 2003, Nicholas Parsons with Clement Freud, Tony Hawks, Linda Smith and Chris Neill, shorts.
599/44/1 5 January 2004, Nicholas Parsons with Paul Merton, Kit Hesketh-Harvey, Liza Tarbuck and Charles Collingwood, music hall.
600/44/2 12 January 2004, Nicholas Parsons with Clement Freud, Tony Hawks, Graham Norton and Ross Noble, chewing the fat.
601/44/3 19 January 2004, Nicholas Parsons with Paul Merton, Clement Freud, Graham Norton and Linda Smith, my favourite words.
602/44/4 26 January 2004, Nicholas Parsons with Gyles Brandreth, Fred MacAulay, Maria McErlane and Nick Revell, doing two things at once.
603/44/5 2 February 2004, Nicholas Parsons with Gyles Brandreth, Fred MacAulay, Maria McErlane and Nick Revell, cold turkey.
604/44/6 9 February 2004, Nicholas Parsons with Paul Merton, Kit Hesketh-Harvey, Liza Tarbuck and Charles Collingwood, four poster beds.
605/44/7 16 February 2004, Nicholas Parsons with Clement Freud, Tony Hawks, Graham Norton and Ross Noble, 10 things I hate.
606/44/8 23 February 2004, Nicholas Parsons with Clement Freud, Tony Hawks, Julian Clary and Stephen Fry, why I never rely on a single source.
607/44/9 1 March 2004, Nicholas Parsons with Clement Freud, Graham Norton, Linda Smith and Ross Noble, Warwick Castle.
608/44/10 8 March 2004, Nicholas Parsons with Clement Freud, Graham Norton, Linda Smith and Ross Noble, swashbuckling.
609/44/11 15 March 2004, Nicholas Parsons with Clement Freud, Tony Hawks, Julian Clary and Stephen Fry, how to matchmake.
610/45/1 12 July 2004, Nicholas Parsons with Paul Merton, Clement Freud, Tony Hawks and Stephen Fry, my favourite proverb.
611/45/2 19 July 2004, Nicholas Parsons with Paul Merton, Clement Freud, Tony Hawks and Charles Collingwood, how to spot a lady.
612/45/3 26 July 2004, Nicholas Parsons with Paul Merton, Clement Freud, Tony Hawks and Stephen Fry, what not to say to the Queen.
613/45/4 2 August 2004, Nicholas Parsons with Paul Merton, Clement Freud, Steve Frost and Victor Spinetti, mumbles.
614/45/5 9 August 2004, Nicholas Parsons with Paul Merton, Clement Freud, Tony Hawks and Charles Collingwood, how to recognise a spy.
615/45/6 16 August 2004, Nicholas Parsons with Paul Merton, Clement Freud, Julian Clary and Liza Tarbuck, what my body language is telling you.
616/45/7 23 August 2004, Nicholas Parsons with Paul Merton, Clement Freud, Dara O'Briain and Lee Mack, if women ruled the world.
617/45/8 6 September 2004, Nicholas Parsons with Paul Merton, Clement Freud, Marcus Brigstocke and Rob Brydon, being a Celt.
618/45/9 13 September 2004, Nicholas Parsons with Paul Merton, Clement Freud, Steve Frost and Victor Spinetti, the best thing about Wales.
619/45/10 20 September 2004, Nicholas Parsons with Paul Merton, Clement Freud, Julian Clary and Liza Tarbuck, loose talk.
620/46/1 24 January 2005, Nicholas Parsons with Paul Merton, Clement Freud, Jenny Eclair and Dara O'Briain, body building.
621/46/2 31 January 2005, Nicholas Parsons with Paul Merton, Graham Norton, Sue Perkins and Ross Noble, what I would say to a mermaid.
622/46/3 7 February 2005, Nicholas Parsons with Paul Merton, Clement Freud, Graham Norton and Linda Smith, pulling someone's leg.
623/46/4 14 February 2005, Nicholas Parsons with Paul Merton, Clement Freud, Jenny Eclair and Dara O'Briain, what I was like as a baby.
624/46/5 21 February 2005, Nicholas Parsons with Paul Merton, Graham Norton, Sue Perkins and Ross Noble, the work of William Shakespeare.
625/46/6 28 February 2005, Nicholas Parsons with Clement Freud, Tony Hawks, Julian Clary and Pam Ayres, the person I look up to most.
626/46/7 7 March 2005, Nicholas Parsons with Tony Hawks, Tim Rice, Linda Smith and Chris Neill, what I have in common with the chairman.
627/46/8 14 March 2005, Nicholas Parsons with Paul Merton, Clement Freud, Graham Norton and Linda Smith, answering back.
628/46/9 21 March 2005, Nicholas Parsons with Tony Hawks, Tim Rice, Linda Smith and Chris Neill, how to attract someone's attention.
629/46/10 28 March 2005, Nicholas Parsons with Clement Freud, Tony Hawks, Julian Clary and Pam Ayres, double Dutch.
630/46/11 4 April 2005, Nicholas Parsons with Paul Merton, Clement Freud, Kit Hesketh-Harvey and Linda Smith, how to attract someone's attention.
631/47/1 11 July 2005, Nicholas Parsons with Paul Merton, Clement Freud, Chris Neill and Rob Brydon, the girl next door.
632/47/2 18 July 2005, Nicholas Parsons with Paul Merton, Clement Freud, Kit Hesketh-Harvey and Linda Smith, my favourite book.
633/47/3 25 July 2005, Nicholas Parsons with Clement Freud, Tony Hawks, Sheila Hancock and Victor Spinetti, my pride and joy.
634/47/4 1 August 2005, Nicholas Parsons with Paul Merton, Clement Freud, Gyles Brandreth and Jenny Eclair, making waves.
635/47/5 8 August 2005, Nicholas Parsons with Paul Merton, Clement Freud, Chris Neill and Rob Brydon, skinny dipping.
636/47/6 15 August 2005, Nicholas Parsons with Clement Freud, Tony Hawks, Sheila Hancock and Victor Spinetti, my favourite Welsh celebrity.
637/47/7 22 August 2005, Nicholas Parsons with Paul Merton, Clement Freud, Gyles Brandreth and Jenny Eclair, bluffing.
638/47/8 29 August 2005, Nicholas Parsons with Paul Merton, Clement Freud, Bill Bailey and Owen O'Neill, a dream come true.
639/47/9 5 September 2005, Nicholas Parsons with Paul Merton, Clement Freud, John Sergeant and Rhod Gilbert, how to present a weather forecast.
640/48/1 2 January 2006, Nicholas Parsons with Paul Merton, Graham Norton, Gyles Brandreth and Sue Perkins, losing your rag.
641/48/2 9 January 2006, Nicholas Parsons with Paul Merton, Clement Freud, Tim Rice and Stephen Fry, my most embarrassing moment.
642/48/3 16 January 2006, Nicholas Parsons with Clement Freud, Tony Hawks, Julian Clary and Kate Robbins, keeping mum.
643/48/4 23 January 2006, Nicholas Parsons with Paul Merton, Clement Freud, Tim Rice and Stephen Fry, stage presence.
644/48/5 30 January 2006, Nicholas Parsons with Paul Merton, Clement Freud, Graham Norton and Jenny Eclair, bling.
645/48/6 6 February 2006, Nicholas Parsons with Paul Merton, Graham Norton, Gyles Brandreth and Sue Perkins, how I prepare for bed.
646/48/7 13 February 2006, Nicholas Parsons with Clement Freud, Tony Hawks, Julian Clary and Kate Robbins, my headmaster.
647/48/8 20 February 2006, Nicholas Parsons with Paul Merton, Clement Freud, Graham Norton and Jenny Eclair, the wow factor.
648/48/9 27 February 2006, Nicholas Parsons with Paul Merton, Clement Freud, Tony Hawks and Gyles Brandreth, grockles.
649/48/10 6 March 2006, Nicholas Parsons with Paul Merton, Kit Hesketh-Harvey, Liza Tarbuck and Chris Neill, a rolling stone.
650/48/11 13 March 2006, Nicholas Parsons with Paul Merton, Clement Freud, Tony Hawks and Gyles Brandreth, New York.
651/49/1 3 July 2006, Nicholas Parsons with Paul Merton, Clement Freud, Julian Clary and Pauline McLynn, Greenwich mean time.
652/49/2 10 July 2006, Nicholas Parsons with Paul Merton, Kit Hesketh-Harvey, Liza Tarbuck and Chris Neill, the most eccentric person I know of.
653/49/3 17 July 2006, Nicholas Parsons with Clement Freud, Graham Norton, Marcus Brigstocke and Pam Ayres, how to spot an exhibitionist.
654/49/4 24 July 2006, Nicholas Parsons with Paul Merton, Tony Hawks, Sue Perkins and Charles Collingwood, how to get a good night's sleep.
655/49/5 31 July 2006, Nicholas Parsons with Paul Merton, Clement Freud, Julian Clary and Pauline McLynn, the dome.
656/49/6 7 August 2006, Nicholas Parsons with Paul Merton, Clement Freud, Tim Rice and Ross Noble, plain sailing.
657/49/7 14 August 2006, Nicholas Parsons with Paul Merton, Tony Hawks, Sue Perkins and Charles Collingwood, the chairman's best kept secret.
658/49/8 21 August 2006, Nicholas Parsons with Paul Merton, Clement Freud, Ross Noble and Janey Godley, kangaroos.
659/49/9 28 August 2006, Nicholas Parsons with Paul Merton, Clement Freud, Pauline McLynn and Owen O'Neill, the best time to be in Edinburgh.
660/49/10 4 September 2006, Nicholas Parsons with Clement Freud, Graham Norton, Marcus Brigstocke and Pam Ayres, what I've got on my Ipod.
661/49/11 11 September 2006, Nicholas Parsons with Paul Merton, Clement Freud, Tim Rice and Ross Noble, Thomas Hardy.
662/50/1 1 January 2007, Nicholas Parsons with Paul Merton, Clement Freud, Chris Neill and Greg Proops, Alfred the Great.
663/50/2 8 January 2007, Nicholas Parsons with Paul Merton, Clement Freud, Kit Hesketh-Harvey and Maria McErlane, taking the waters.
664/50/3 15 January 2007, Nicholas Parsons with Clement Freud, Gyles Brandreth, Marcus Brigstocke and Pauline McLynn, mermaids.
665/50/4 22 January 2007, Nicholas Parsons with Paul Merton, Tim Rice, Chris Neill and Alun Cochrane, round robins.
666/50/5 29 January 2007, Nicholas Parsons with Paul Merton, Tony Hawks, Sue Perkins and Neil Mullarkey, all things bright and beautiful.
667/50/6 5 February 2007, Nicholas Parsons with Paul Merton, Clement Freud, Graham Norton and Chris Addison, the streets of London.
668/50/7 12 February 2007, Nicholas Parsons with Paul Merton, Clement Freud, Chris Neill and Greg Proops, the end of the world.
669/50/8 19 February 2007, Nicholas Parsons with Paul Merton, Clement Freud, Kit Hesketh-Harvey and Maria McErlane, pirates.
670/50/9 26 February 2007, Nicholas Parsons with Clement Freud, Gyles Brandreth, Marcus Brigstocke and Pauline McLynn, white elephants.
671/50/10 5 March 2007, Nicholas Parsons with Paul Merton, Tony Hawks, Sue Perkins and Neil Mullarkey, seaside postcards.
672/51/1 16 July 2007, Nicholas Parsons with Paul Merton, Pam Ayres, Maureen Lipman and Dara O'Briain, every trick in the book.
673/51/2 23 July 2007, Nicholas Parsons with Paul Merton, Clement Freud, Graham Norton and Chris Addison, how to be a thespian.
674/51/3 30 July 2007, Nicholas Parsons with Paul Merton, Gyles Brandreth, Julian Clary and Jenny Eclair, 1066.
675/51/4 6 August 2007, Nicholas Parsons with Paul Merton, Clement Freud, Tony Hawks and Dave Gorman, radio times.
676/51/5 13 August 2007, Nicholas Parsons with Paul Merton, Tim Rice, Chris Neill and Alun Cochrane, the Cheltenham Gold Cup.
677/51/6 20 August 2007, Nicholas Parsons with Paul Merton, Clement Freud, Fred MacAulay and Jo Caulfield, the Scotsman.
678/51/7 27 August 2007, Nicholas Parsons with Paul Merton, Clement Freud, Marcus Brigstocke and Janey Godley, five star review.
679/51/8 3 September 2007, Nicholas Parsons with Paul Merton, Marcus Brigstocke, Pam Ayres and Maureen Lipman, Timbuktu.
680/51/9 10 September 2007, Nicholas Parsons with Paul Merton, Clement Freud, Tony Hawks and Dave Gorman, happy hour.
681/51/10 17 September 2007, Nicholas Parsons with Paul Merton, Gyles Brandreth, Julian Clary and Jenny Eclair, why television will never catch on.
682/51/11 24 September 2007, Nicholas Parsons with Clement Freud, Graham Norton, Gyles Brandreth and Phill Jupitus, the bard.
683/52/1 31 December 2007, Nicholas Parsons with Paul Merton, Kenneth Williams, Clement Freud and Graham Norton, plus Derek Nimmo, Peter Jones, Tony Hawks, Sheila Hancock, Gyles Brandreth, Julian Clary, Linda Smith, Jenny Eclair, Ross Noble, Stephen Fry, Chris Neill, Alfred Marks, Barry Took, Tommy Trinder, Kenny Everett and Bob Monkhouse, 40th anniversary special.
684/52/2 7 January 2008, Nicholas Parsons with Paul Merton, Clement Freud, Chris Neill and Josie Lawrence, life begins at 40.
685/52/3 14 January 2008, Nicholas Parsons with Tony Hawks, Gyles Brandreth, Kit Hesketh-Harvey and Janey Godley, ruby anniversary.
686/52/4 21 January 2008, Nicholas Parsons with Clement Freud, Graham Norton, Gyles Brandreth and Phill Jupitus, the Scottish play.
687/52/5 28 January 2008, Nicholas Parsons with Paul Merton, Clement Freud, Jenny Eclair and Marcus Brigstocke, the Druids.
688/52/6 4 February 2008, Nicholas Parsons with Paul Merton, Clement Freud, Liza Tarbuck and Jack Dee, killing time.
689/52/7 11 February 2008, Nicholas Parsons with Paul Merton, Tony Hawks, Graham Norton and Sue Perkins, brass monkeys.
690/52/8 18 February 2008, Nicholas Parsons with Paul Merton, Clement Freud, Jenny Eclair and Marcus Brigstocke, family values.
691/52/9 25 February 2008, Nicholas Parsons with Paul Merton, Clement Freud, Chris Neill and Josie Lawrence, red Leicester.
692/52/10 3 March 2008, Nicholas Parsons with Tony Hawks, Gyles Brandreth, Kit Hesketh-Harvey and Janey Godley, Norfolk broads.
693/52/11 10 March 2008, Nicholas Parsons with Paul Merton, Clement Freud, Liza Tarbuck and Jack Dee, the 2012 Olympics.
694/52/12 17 March 2008, Nicholas Parsons with Paul Merton, Tony Hawks, Graham Norton and Sue Perkins, discovering America.
695/53/1 28 July 2008, Nicholas Parsons with Paul Merton, Clement Freud, Ross Noble and Phill Jupitus, longitude.
696/53/2 4 August 2008, Nicholas Parsons with Clement Freud, Gyles Brandreth, Marcus Brigstocke and Dave Gorman, hay fever.
697/53/3 11 August 2008, Nicholas Parsons with Paul Merton, Tony Hawks, Shappi Khorsandi and Ian McMillan, Old Trafford.
698/53/4 18 August 2008, Nicholas Parsons with Paul Merton, Clement Freud, Rhod Gilbert and Mike McShane, how to get an audience.
699/53/5 25 August 2008, Nicholas Parsons with Paul Merton, Clement Freud, Fred MacAulay and Lynn Ferguson, at the Edinburgh Festival.
700/53/6 1 September 2008, Nicholas Parsons with Paul Merton, Sue Perkins, Julian Clary and Chris Addison, brass monkeys.
701/53/7 8 September 2008, Nicholas Parsons with Paul Merton, Clement Freud, Ross Noble and Robin Ince, second-hand shops.
702/53/8 15 September 2008, Nicholas Parsons with Clement Freud, Gyles Brandreth, Marcus Brigstocke and Owen O'Neill, a month of Sundays.
703/53/9 22 September 2008, Nicholas Parsons with Paul Merton, Tony Hawks, Shappi Khorsandi and Ian McMillan, the War of the Roses.
704/53/10 29 September 2008, Nicholas Parsons with Paul Merton, Sue Perkins, Julian Clary and Chris Addison, glitz and glamour.
705/54/1 29 December 2008, Nicholas Parsons with Paul Merton, Graham Norton, Charles Collingwood and Shappi Khorsandi, my New Year's resolution.
706/54/2 5 January 2009, Nicholas Parsons with Paul Merton, Clement Freud, Julian Clary and Helen Lederer, dressed to kill.
707/54/3 12 January 2009, Nicholas Parsons with Paul Merton, Graham Norton, Charles Collingwood and Shappi Khorsandi, losing your marbles.
708/54/4 19 January 2009, Nicholas Parsons with Paul Merton, Clement Freud, Julian Clary and Josie Long, how to make a cup of tea.
709/54/5 26 January 2009, Nicholas Parsons with Paul Merton, Gyles Brandreth, Sue Perkins and Liza Tarbuck, if I could see into the future.
710/54/6 2 February 2009, Nicholas Parsons with Paul Merton, Clement Freud, Josie Lawrence and Jack Dee, my secret vice.
711/54/7 9 February 2009, Nicholas Parsons with Paul Merton, Gyles Brandreth, Sue Perkins and Liza Tarbuck, my favourite Shakespeare play.
712/54/8 16 February 2009, Nicholas Parsons with Paul Merton, Tony Hawks, Chris Neill and Justin Moorhouse, five things to do with a potato.
713/54/9 23 February 2009, Nicholas Parsons with Paul Merton, Clement Freud, Sheila Hancock and David Mitchell, Cinderella.
714/54/10 2 March 2009, Nicholas Parsons with Paul Merton, Clement Freud, Josie Lawrence and Jack Dee, what gets my back up.
715/54/11 9 March 2009, Nicholas Parsons with Paul Merton, Clement Freud, Sheila Hancock and David Mitchell, agony aunts.
716/54/12 16 March 2009, Nicholas Parsons with Paul Merton, Tony Hawks, Chris Neill and Justin Moorhouse, sneezing.
717/55/1 27 July 2009, Nicholas Parsons with Tony Hawks, Sue Perkins, Tim Rice and Pam Ayres, twittering.
718/55/2 3 August 2009, Nicholas Parsons with Paul Merton, Gyles Brandreth, Kit Hesketh-Harvey and Shappi Khorsandi, my hidden talent.
719/55/3 10 August 2009, Nicholas Parsons with Paul Merton, Jenny Eclair, Stephen Fry and Charles Collingwood, my idea of bliss.
720/55/4 17 August 2009, Nicholas Parsons with Paul Merton, Gyles Brandreth, Kit Hesketh-Harvey and Shappi Khorsandi, what others find irritating about me.
721/55/5 24 August 2009, Nicholas Parsons with Paul Merton, Sue Perkins, Mike McShane and Paul Sinha, what I wear in bed.
722/55/6 31 August 2009, Nicholas Parsons with Paul Merton, Sue Perkins, Janey Godley and Richard Herring, what I love about Edinburgh.
723/55/7 7 September 2009, Nicholas Parsons with Paul Merton, Jenny Eclair, Stephen Fry and Charles Collingwood, a perk of the job.
724/55/8 14 September 2009, Nicholas Parsons with Paul Merton, Graham Norton, Gyles Brandreth and Suki Webster, the long arm of the law.
725/55/9 21 September 2009, Nicholas Parsons with Tony Hawks, Sue Perkins, Tim Rice and Pam Ayres, chick lit.
726/55/10 28 September 2009, Nicholas Parsons with Paul Merton, Graham Norton, Gyles Brandreth and Pauline McLynn, how to outdo the other panellists.
727/56/1 4 January 2010, Nicholas Parsons with Paul Merton, Gyles Brandreth, Julian Clary and David Mitchell, New Year's Eve parties.
728/56/2 11 January 2010, Nicholas Parsons with Paul Merton, Chris Neill, Charles Collingwood and Josie Lawrence, how I know when I'm in love.
729/56/3 18 January 2010, Nicholas Parsons with Tony Hawks, Josie Lawrence, Dave Gorman and Justin Moorhouse, how to spot a mature student.
730/56/4 25 January 2010, Nicholas Parsons with Paul Merton, Gyles Brandreth, Julian Clary and David Mitchell, how to write a love letter.
731/56/5 1 February 2010, Nicholas Parsons with Paul Merton, Chris Neill, Charles Collingwood and Josie Lawrence, how to remember people's names.
732/56/6 8 February 2010, Nicholas Parsons with Paul Merton, Graham Norton, Sue Perkins and Liza Tarbuck, how to pass the time if you are stuck in traffic.
733/56/7 15 February 2010, Nicholas Parsons with Paul Merton, Gyles Brandreth, Jenny Eclair and Pam Ayres, if I were a time traveller.
734/56/8 22 February 2010, Nicholas Parsons with Paul Merton, Tony Hawks, Graham Norton and Sue Perkins, some strange facts about the people in this show.
735/56/9 1 March 2010, Nicholas Parsons with Tony Hawks, Josie Lawrence, Dave Gorman and Justin Moorhouse, the people you find in a student bar.
736/56/10 8 March 2010, Nicholas Parsons with Paul Merton, Graham Norton, Sue Perkins and Liza Tarbuck, what I see in the mirror.
737/56/11 15 March 2010, Nicholas Parsons with Paul Merton, Gyles Brandreth, Jenny Eclair and Pam Ayres, sitting on the throne.
738/56/12 22 March 2010, Nicholas Parsons with Paul Merton, Tony Hawks, Graham Norton and Sue Perkins, how to tell if someone is older than they look.
739/57/1 2 August 2010, Nicholas Parsons with Paul Merton, Graham Norton, Gyles Brandreth and Jenny Eclair, my idea of hell.
740/57/2 9 August 2010, Nicholas Parsons with Paul Merton, Sue Perkins, Liza Tarbuck and John Sergeant, my philosophy.
741/57/3 16 August 2010, Nicholas Parsons with Paul Merton, Tony Hawks, Sheila Hancock and Ross Noble, women in comedy.
742/57/4 23 August 2010, Nicholas Parsons with Paul Merton, Gyles Brandreth, Shappi Khorsandi and John Bishop, funny people.
743/57/5 30 August 2010, Nicholas Parsons with Paul Merton, Jenny Eclair, Fred MacAulay and Stephen K. Amos, the secret of my success.
744/57/6 6 September 2010, Nicholas Parsons with Paul Merton, Sue Perkins, Liza Tarbuck and John Sergeant, how to audition.
745/57/7 13 September 2010, Nicholas Parsons with Paul Merton, Graham Norton, Gyles Brandreth and Jenny Eclair, our American cousins.
746/57/8 20 September 2010, Nicholas Parsons with Paul Merton, Tony Hawks, Sheila Hancock and Ross Noble, a great adventure.
747/58/1 8 November 2010, Nicholas Parsons with Paul Merton, Tony Hawks, Kit Hesketh-Harvey and Alun Cochrane, my first kiss.
748/58/2 15 November 2010, Nicholas Parsons with Paul Merton, Sue Perkins, Julian Clary and Kevin Eldon, taking my driving test.
749/58/3 22 November 2010, Nicholas Parsons with Paul Merton, Tony Hawks, Kit Hesketh-Harvey and Alun Cochrane, my favourite character in Coronation Street.
750/58/4 29 November 2010, Nicholas Parsons with Paul Merton, Sheila Hancock, Gyles Brandreth and Ian McMillan, the British Library.
751/58/5 6 December 2010, Nicholas Parsons with Paul Merton, Sue Perkins, Julian Clary and Kevin Eldon, my relationship with the chairman.
752/58/6 13 December 2010, Nicholas Parsons with Paul Merton, Sheila Hancock, Gyles Brandreth and Ian McMillan, the English language.
753/59/1 7 February 2011, Nicholas Parsons with Paul Merton, Gyles Brandreth, Shappi Khorsandi and Rick Wakeman, dear listener.
754/59/2 14 February 2011, Nicholas Parsons with Paul Merton, Sheila Hancock, Sue Perkins and Marcus Brigstocke, hope over expectations.
755/59/3 21 February 2011, Nicholas Parsons with Paul Merton, Tony Hawks, Ross Noble and Liza Tarbuck, on Valentine's Day I received.
756/59/4 28 February 2011, Nicholas Parsons with Paul Merton, Graham Norton, Julian Clary and Terry Wogan, the history of the world.
757/59/5 7 March 2011, Nicholas Parsons with Paul Merton, Gyles Brandreth, Shappi Khorsandi and Rick Wakeman, musicals.
758/59/6 14 March 2011, Nicholas Parsons with Paul Merton, Sheila Hancock, Sue Perkins and Marcus Brigstocke, how I'd describe myself to an alien.
759/59/7 21 March 2011, Nicholas Parsons with Paul Merton, Tony Hawks, Ross Noble and Liza Tarbuck, Regent's Park.
760/59/8 28 March 2011, Nicholas Parsons with Paul Merton, Graham Norton, Julian Clary and Terry Wogan, national treasures.
761/60/1 16 May 2011, Nicholas Parsons with Paul Merton, Tony Hawks, Gyles Brandreth and Julian Clary, my motto.
762/60/2 23 May 2011, Nicholas Parsons with Paul Merton, Graham Norton, Jenny Eclair and Josie Lawrence, if I were a superhero.
763/60/3 30 May 2011, Nicholas Parsons with Paul Merton, Sue Perkins, Stephen Fry and Fi Glover, marbles.
764/60/4 6 June 2011, Nicholas Parsons with Paul Merton, Tony Hawks, Gyles Brandreth and Julian Clary, the first signs of summer.
765/60/5 13 June 2011, Nicholas Parsons with Paul Merton, Graham Norton, Jenny Eclair and Josie Lawrence, how to make small talk at parties.
766/60/6 20 June 2011, Nicholas Parsons with Paul Merton, Sue Perkins, Stephen Fry and Fi Glover, the best way to greet someone.
767/61/1 8 August 2011, Nicholas Parsons with Paul Merton, Tony Hawks, Sheila Hancock and Graham Norton, my personal assistant.
768/61/2 15 August 2011, Nicholas Parsons with Julian Clary, Josie Lawrence, Phill Jupitus and Rick Wakeman, the first time wearing spectacles.
769/61/3 22 August 2011, Nicholas Parsons with Paul Merton, Gyles Brandreth, Alun Cochrane and Jason Byrne, Scottish air.
770/61/4 29 August 2011, Nicholas Parsons with Paul Merton, Gyles Brandreth, Shappi Khorsandi and Russell Kane, my tartan underwear.
771/61/5 5 September 2011, Nicholas Parsons with Tony Hawks, Gyles Brandreth, Pam Ayres and Miles Jupp, Doctor Johnson.
772/61/6 12 September 2011, Nicholas Parsons with Paul Merton, Tony Hawks, Sheila Hancock and Graham Norton, Shakespeare's globe.
773/61/7 19 September 2011, Nicholas Parsons with Julian Clary, Josie Lawrence, Phill Jupitus and Rick Wakeman, my first day at school.
774/61/8 26 September 2011, Nicholas Parsons with Tony Hawks, Gyles Brandreth, Pam Ayres and Miles Jupp, middle England.
775/62/1 6 February 2012, Nicholas Parsons with Paul Merton, Gyles Brandreth, Jenny Eclair and Ross Noble, when I wear a top hat.
776/62/2 13 February 2012, Nicholas Parsons with Paul Merton, Gyles Brandreth, Jenny Eclair and Ross Noble, self-help books.
777/62/3 20 February 2012, Nicholas Parsons with Paul Merton, Sue Perkins, Julian Clary and Charles Collingwood, what I've got in my attic.
778/62/4 27 February 2012, Nicholas Parsons with Paul Merton, Kit Hesketh-Harvey, Liza Tarbuck and Josie Lawrence, the perfect lie-in.
779/62/5 5 March 2012, Nicholas Parsons with Paul Merton, Sue Perkins, Julian Clary and Charles Collingwood, the contents of Nicholas's wallet.
780/62/6 12 March 2012, Nicholas Parsons with Paul Merton, Kit Hesketh-Harvey, Liza Tarbuck and Josie Lawrence, electronic books.
781/62/7 19 March 2012, Nicholas Parsons with Paul Merton, Marcus Brigstocke, Cyrus Broacha and Anuvab Pal, a cultural exchange.
TV49/4/1 26 March 2012, Nicholas Parsons with Paul Merton, Graham Norton, Sue Perkins and Phill Jupitus, the Bermuda Triangle.
782/62/8 26 March 2012, Nicholas Parsons with Paul Merton, Marcus Brigstocke, Cyrus Broacha and Anuvab Pal, Mumbai traffic.
TV50/4/2 27 March 2012, Nicholas Parsons with Paul Merton, Julian Clary, Stephen Fry and Russell Tovey, tongue twisters.
TV51/4/3 28 March 2012, Nicholas Parsons with Paul Merton, Sue Perkins, Marcus Brigstocke and Ruth Jones, common misconceptions.
TV52/4/4 29 March 2012, Nicholas Parsons with Paul Merton, Gyles Brandreth, Liza Tarbuck and Miles Jupp, double acts.
TV53/4/5 30 March 2012, Nicholas Parsons with Paul Merton, Josie Lawrence, John Sergeant and Jason Manford, once upon a time.
TV54/4/6 2 April 2012, Nicholas Parsons with Paul Merton, Tony Hawks, Graham Norton and Sue Perkins, my 45th birthday.
TV55/4/7 3 April 2012, Nicholas Parsons with Paul Merton, Shappi Khorsandi, Jason Manford and Hugh Bonneville, when I met my hero.
TV56/4/8 4 April 2012, Nicholas Parsons with Paul Merton, Sue Perkins, Marcus Brigstocke and Stephen Mangan, teacher's pet.
TV57/4/9 5 April 2012, Nicholas Parsons with Paul Merton, Tony Hawks, Gyles Brandreth and Liza Tarbuck, pardon my French.
TV58/4/10 6 April 2012, Nicholas Parsons with Paul Merton, Julian Clary, Stephen Fry and Shappi Khorsandi, excuses for being late.
783/63/1 14 May 2012, Nicholas Parsons with Paul Merton, Sue Perkins, Julian Clary and Greg Proops, how I like my coffee.
784/63/2 21 May 2012, Nicholas Parsons with Paul Merton, Graham Norton, Gyles Brandreth and Alun Cochrane, the importance of eyebrows.
785/63/3 28 May 2012, Nicholas Parsons with Paul Merton, Sue Perkins, Julian Clary and Greg Proops, the worst night of my life.
786/63/4 4 June 2012, Nicholas Parsons with Tony Hawks, Jenny Eclair, Richard Herring and Paul Sinha, Yorkshire puddings.
787/63/5 11 June 2012, Nicholas Parsons with Paul Merton, Graham Norton, Gyles Brandreth and Alun Cochrane, things you should never do in public.
788/63/6 18 June 2012, Nicholas Parsons with Tony Hawks, Jenny Eclair, Richard Herring and Paul Sinha, grim up north.
789/64/1 6 August 2012, Nicholas Parsons with Paul Merton, Graham Norton, Sue Perkins and Liza Tarbuck, the biggest fib I've ever told.
790/64/2 13 August 2012, Nicholas Parsons with Paul Merton, Charles Collingwood, Pam Ayres and Miles Jupp, the best thing to do in the back row of the cinema.
791/64/3 20 August 2012, Nicholas Parsons with Paul Merton, Gyles Brandreth, Janey Godley and Hannibal Buress, my favourite pastime in Edinburgh.
792/64/4 27 August 2012, Nicholas Parsons with Paul Merton, Gyles Brandreth, Jason Byrne and Tim Vine, the joys of wearing a kilt.
793/64/5 3 September 2012, Nicholas Parsons with Paul Merton, Graham Norton, Sue Perkins and Liza Tarbuck, things I do when nobody's looking.
794/64/6 10 September 2012, Nicholas Parsons with Tony Hawks, Jenny Eclair, Alun Cochrane and Kevin Eldon, my preparations for Rio 2016.
795/64/7 17 September 2012, Nicholas Parsons with Paul Merton, Charles Collingwood, Pam Ayres and Miles Jupp, three things I have given up lately.
796/64/8 24 September 2012, Nicholas Parsons with Tony Hawks, Jenny Eclair, Alun Cochrane and Kevin Eldon, spotting a fake.
797/65/1 11 February 2013, Nicholas Parsons with Paul Merton, Graham Norton, Sue Perkins and Jason Manford, funny valentine.
798/65/2 18 February 2013, Nicholas Parsons with Paul Merton, Gyles Brandreth, Alun Cochrane and Stephen Mangan, Treasure Island.
799/65/3 25 February 2013, Nicholas Parsons with Paul Merton, Julian Clary, Jenny Eclair and Richard Herring, Marble Arch.
800/65/4 4 March 2013, Nicholas Parsons with Paul Merton, Sheila Hancock, Marcus Brigstocke and Josie Lawrence, spring cleaning.
801/65/5 11 March 2013, Nicholas Parsons with Paul Merton, Gyles Brandreth, Alun Cochrane and Stephen Mangan, the mother-in-law.
802/65/6 18 March 2013, Nicholas Parsons with Paul Merton, Julian Clary, Jenny Eclair and Richard Herring, my family tree.
803/65/7 25 March 2013, Nicholas Parsons with Paul Merton, Sheila Hancock, Marcus Brigstocke and Josie Lawrence, escaping from an awful party.
804/65/8 1 April 2013, Nicholas Parsons with Paul Merton, Graham Norton, Sue Perkins and Jason Manford, Paris in spring.
805/66/1 20 May 2013, Nicholas Parsons with Paul Merton, Graham Norton, Pam Ayres and Kevin Eldon, the 11 plus.
806/66/2 27 May 2013, Nicholas Parsons with Tony Hawks, Gyles Brandreth, Fred MacAulay and Roy Walker, the city of culture.
807/66/3 3 June 2013, Nicholas Parsons with Paul Merton, Gyles Brandreth, Richard Herring and Russell Kane, fast food.
808/66/4 10 June 2013, Nicholas Parsons with Paul Merton, Graham Norton, Pam Ayres and Kevin Eldon, the leader of the pack.
809/66/5 17 June 2013, Nicholas Parsons with Tony Hawks, Gyles Brandreth, Fred MacAulay and Roy Walker, the one that got away.
810/66/6 24 June 2013, Nicholas Parsons with Paul Merton, Gyles Brandreth, Richard Herring and Russell Kane, back seat drivers.
811/67/1 12 August 2013, Nicholas Parsons with Tony Hawks, Gyles Brandreth, Alun Cochrane and Patrick Kielty, moving house.
812/67/2 19 August 2013, Nicholas Parsons with Paul Merton, Sue Perkins, Greg Proops and Joe Lycett, porridge.
813/67/3 26 August 2013, Nicholas Parsons with Paul Merton, Sue Perkins, Russell Kane and Henry Blofeld, Burke and Hare.
814/67/4 2 September 2013, Nicholas Parsons with Paul Merton, Julian Clary, Jenny Eclair and Liza Tarbuck, nicknames.
815/67/5 9 September 2013, Nicholas Parsons with Tony Hawks, Gyles Brandreth, Alun Cochrane and Patrick Kielty, the food of the gods.
816/67/6 16 September 2013, Nicholas Parsons with Paul Merton, Gyles Brandreth, Pam Ayres and Stephen Mangan, a case of mistaken identity.
817/67/7 23 September 2013, Nicholas Parsons with Paul Merton, Julian Clary, Jenny Eclair and Liza Tarbuck, a night in.
JJAM1/1/1 11 November 2013, Nicholas Parsons with Jenny Eclair, Josie Lawrence, Kitty Fry and Zrey Sholapurkar, school uniforms.
JJAM2/1/2 12 November 2013, Nicholas Parsons with Jenny Eclair, Josie Lawrence, Rosa Calcraft and William Tyrell, the language I would most like to speak.
JJAM3/1/3 13 November 2013, Nicholas Parsons with Jenny Eclair, Josie Lawrence, Jonah Calkin and Francesca Daly, if I were Harry Potter.
JJAM4/1/4 14 November 2013, Nicholas Parsons with Jenny Eclair, Josie Lawrence, Sophie Shanahan and Leonardo Shaw, party games.
JJAM5/1/5 15 November 2013, Nicholas Parsons with Jenny Eclair, Josie Lawrence, Roberta Bannister and Will Pearce, the contents of my pencil case.
818/67/8 23 December 2013, Nicholas Parsons with Paul Merton, Gyles Brandreth, Pam Ayres and Stephen Mangan, building a snowman.
819/68/1 10 February 2014, Nicholas Parsons with Paul Merton, Tony Hawks, Gyles Brandreth and Fi Glover, growing bananas.
820/68/2 17 February 2014, Nicholas Parsons with Paul Merton, Alun Cochrane, Russell Kane and Rebecca Front, Dickensian London.
821/68/3 24 February 2014, Nicholas Parsons with Paul Merton, Sheila Hancock, Josie Lawrence and Richard Herring, hot cross buns.
822/68/4 3 March 2014, Nicholas Parsons with Paul Merton, Graham Norton, Miles Jupp and Holly Walsh, the tempest.
823/68/5 10 March 2014, Nicholas Parsons with Paul Merton, Tony Hawks, Gyles Brandreth and Fi Glover, painting the ceiling.
824/68/6 17 March 2014, Nicholas Parsons with Paul Merton, Sheila Hancock, Josie Lawrence and Richard Herring, April showers.
825/68/7 24 March 2014, Nicholas Parsons with Paul Merton, Alun Cochrane, Russell Kane and Rebecca Front, a habitual lie.
826/68/8 31 March 2014, Nicholas Parsons with Paul Merton, Graham Norton, Miles Jupp and Holly Walsh, a shotgun wedding.
827/69/1 19 May 2014, Nicholas Parsons with Paul Merton, Jenny Eclair, Julian Clary and Vanessa Feltz, exam revision.
828/69/2 26 May 2014, Nicholas Parsons with Gyles Brandreth, Shappi Khorsandi, Paul Sinha and Patrick Kielty, how to make the most of a bank holiday.
829/69/3 2 June 2014, Nicholas Parsons with Paul Merton, Sheila Hancock, Kevin Eldon and Joe Lycett, how to prepare sushi.
830/69/4 9 June 2014, Nicholas Parsons with Paul Merton, Jenny Eclair, Julian Clary and Vanessa Feltz, random acts of kindness.
831/69/5 16 June 2014, Nicholas Parsons with Gyles Brandreth, Shappi Khorsandi, Paul Sinha and Patrick Kielty, the summer solstice.
832/69/6 23 June 2014, Nicholas Parsons with Paul Merton, Sheila Hancock, Kevin Eldon and Joe Lycett, the confessions of a Radio Four panellist.
833/70/1 11 August 2014, Nicholas Parsons with Paul Merton, Liza Tarbuck, Alun Cochrane and Jonathan Ross, why I hate roller coasters.
834/70/2 18 August 2014, Nicholas Parsons with Paul Merton, Gyles Brandreth, Sue Perkins and Frank Skinner, fireworks.
835/70/3 25 August 2014, Nicholas Parsons with Paul Merton, Gyles Brandreth, Sue Perkins and Josie Long, the Commonwealth.
836/70/4 1 September 2014, Nicholas Parsons with Tony Hawks, Gyles Brandreth, Stephen Mangan and Kerry Godliman, ode to joy.
837/70/5 8 September 2014, Nicholas Parsons with Paul Merton, Sheila Hancock, Russell Kane and Holly Walsh, 900 jams.
838/70/6 15 September 2014, Nicholas Parsons with Paul Merton, Liza Tarbuck, Alun Cochrane and Jonathan Ross, the night I dreamt I painted the Sistine Chapel.
839/70/7 22 September 2014, Nicholas Parsons with Tony Hawks, Gyles Brandreth, Stephen Mangan and Kerry Godliman, things to do on a rainy day.
840/70/8 29 September 2014, Nicholas Parsons with Paul Merton, Sheila Hancock, Russell Kane and Holly Walsh, the Mona Lisa.
841/71/1 9 February 2015, Nicholas Parsons with Paul Merton, Julian Clary, Stephen Fry and David Tennant, a banana skin.
JJAM6/2/1 16 February 2015, Nicholas Parsons with Jenny Eclair, Josie Lawrence, Kalaivanan ? and Hamish McRae, my earliest memory.
842/71/2 16 February 2015, Nicholas Parsons with Paul Merton, Tony Hawks, Josie Lawrence and Alun Cochrane, a cathedral city.
JJAM7/2/2 17 February 2015, Nicholas Parsons with Jenny Eclair, Josie Lawrence, Amy ? and David ?, my least favourite smell.
JJAM8/2/3 18 February 2015, Nicholas Parsons with Jenny Eclair, Josie Lawrence, Oliver ? and Sarah Smart, my ideal picnic.
JJAM9/2/4 19 February 2015, Nicholas Parsons with Jenny Eclair, Josie Lawrence, Lottie Davies and Arun Uttamchandani, things of which I am scared.
JJAM10/2/5 20 February 2015, Nicholas Parsons with Jenny Eclair, Josie Lawrence, Rufus ? and Emily Slade, the last time I laughed so hard.
843/71/3 23 February 2015, Nicholas Parsons with Gyles Brandreth, Jenny Eclair, Marcus Brigstocke and Shappi Khorsandi, elephant and castle.
844/71/4 2 March 2015, Nicholas Parsons with Paul Merton, Sheila Hancock, Graham Norton and Robin Ince, paranormal activity.
845/71/5 9 March 2015, Nicholas Parsons with Paul Merton, Tony Hawks, Josie Lawrence and Alun Cochrane, the Canterbury tales.
846/71/6 16 March 2015, Nicholas Parsons with Gyles Brandreth, Jenny Eclair, Marcus Brigstocke and Shappi Khorsandi, heavy metal.
847/71/7 23 March 2015, Nicholas Parsons with Paul Merton, Sheila Hancock, Graham Norton and Robin Ince, a writing desk.
848/71/8 30 March 2015, Nicholas Parsons with Paul Merton, Julian Clary, Stephen Fry and David Tennant, the world cup.
849/72/1 18 May 2015, Nicholas Parsons with Paul Merton, Graham Norton, Tim Rice and Liza Tarbuck, English sparkling wine.
850/72/2 25 May 2015, Nicholas Parsons with Paul Merton, Gyles Brandreth, Alun Cochrane and Susan Calman, Nelson’s column.
851/72/3 1 June 2015, Nicholas Parsons with Paul Merton, Sheila Hancock, Pam Ayres and Mike McShane, the first cuckoo.
852/72/4 8 June 2015, Nicholas Parsons with Paul Merton, Gyles Brandreth, Marcus Brigstocke and Lucy Beaumont, Saint Patrick.
853/72/5 15 June 2015, Nicholas Parsons with Paul Merton, Graham Norton, Tim Rice and Liza Tarbuck, the Cornish pasty.
854/72/6 22 June 2015, Nicholas Parsons with Paul Merton, Sheila Hancock, Pam Ayres and Mike McShane, a hat-trick.
855/72/7 29 June 2015, Nicholas Parsons with Paul Merton, Gyles Brandreth, Marcus Brigstocke and Lucy Beaumont, received pronunciation.
856/72/8 6 July 2015, Nicholas Parsons with Paul Merton, Gyles Brandreth, Alun Cochrane and Susan Calman, frozen peas.
864/73/8 24 August 2015 and 23 November 2015, Nicholas Parsons with Paul Merton, Gyles Brandreth, Susan Calman and Tom Allen, whisky galore.
857/73/1 5 October 2015, Nicholas Parsons with Paul Merton, Gyles Brandreth, Janey Godley and Joe Lycett, street performers.
858/73/2 12 October 2015, Nicholas Parsons with Paul Merton, Julian Clary, Josie Lawrence and Susan Calman, a room with a view.
859/73/3 19 October 2015, Nicholas Parsons with Tony Hawks, Gyles Brandreth, Sue Perkins and Andy Hamilton, South Pacific.
860/73/4 26 October 2015, Nicholas Parsons with Paul Merton, Sheila Hancock, Jenny Eclair and Josh Widdicombe, caravanning.
861/73/5 2 November 2015, Nicholas Parsons with Paul Merton, Julian Clary, Josie Lawrence and Susan Calman, the sky at night.
JJAM11/2/6 8 November 2015, Nicholas Parsons with Paul Merton, Josie Lawrence, Douglas ? and Mathilda ?, the school disco.
862/73/6 9 November 2015, Nicholas Parsons with Tony Hawks, Gyles Brandreth, Sue Perkins and Andy Hamilton, dropping a clanger.
863/73/7 16 November 2015, Nicholas Parsons with Paul Merton, Sheila Hancock, Jenny Eclair and Josh Widdicombe, festive spirits.
JJAM12/2/7 25 December 2015, Nicholas Parsons with Paul Merton, Josie Lawrence, Joe ? and Sophie ?, if I owned a reindeer.
865/74/1 22 February 2016, Nicholas Parsons with Paul Merton, Graham Norton, Pam Ayres and Rufus Hound, optimism.
866/74/2 29 February 2016, Nicholas Parsons with Paul Merton, Gyles Brandreth, Tim Rice and Esther Rantzen, bubble and squeak.
867/74/3 7 March 2016, Nicholas Parsons with Jenny Eclair, Josie Lawrence, Stephen Fry and Nish Kumar, a catnap.
868/74/4 14 March 2016, Nicholas Parsons with Paul Merton, Graham Norton, Pam Ayres and Rufus Hound, breakfast at Tiffany's.
869/74/5 21 March 2016, Nicholas Parsons with Paul Merton, Gyles Brandreth, Tim Rice and Esther Rantzen, Kermit the frog.
870/74/6 28 March 2016, Nicholas Parsons with Jenny Eclair, Josie Lawrence, Stephen Fry and Nish Kumar, a vintage year.
871/75/1 16 May 2016, Nicholas Parsons with Paul Merton, Sheila Hancock, Gyles Brandreth and John Finnemore, Halley's comet.
872/75/2 23 May 2016, Nicholas Parsons with Paul Merton, Graham Norton, Josie Lawrence and Alexei Sayle, clock watching.
873/75/3 30 May 2016, Nicholas Parsons with Paul Merton, Sheila Hancock, Gyles Brandreth and John Finnemore, saving graces.
874/75/4 6 June 2016, Nicholas Parsons with Paul Merton, Marcus Brigstocke, Holly Walsh and Josh Widdicombe, Pinocchio.
875/75/5 13 June 2016, Nicholas Parsons with Paul Merton, Graham Norton, Josie Lawrence and Alexei Sayle, Virginia Wade.
876/75/6 20 June 2016, Nicholas Parsons with Paul Merton, Marcus Brigstocke, Holly Walsh and Josh Widdicombe, rock and roll.
877/76/1 8 August 2016, Nicholas Parsons with Paul Merton, Gyles Brandreth, Josie Lawrence and Katherine Ryan, A and E.
878/76/2 15 August 2016, Nicholas Parsons with Paul Merton, Tony Hawks, Julian Clary and Zoe Lyons, Andy Warhol.
879/76/3 22 August 2016, Nicholas Parsons with Paul Merton, Marcus Brigstocke, Janey Godley and Nish Kumar, the royal mile. '''))