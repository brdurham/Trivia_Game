#!usr/bin/python3
#Brady Durham
#1/28/20

import pickle


questions = 
{ 1: ['In 1927, who became the first man to fly solo and non-stop across the Atlantic?','Charles Lindbergh', 'charles lindbergh', 'CHARLES LINDBURGH', ' Charles lindburgh'],
2: ['What was the family name of the Russian rulers from the 17th century until the 1917 revolution?','Romanov', 'romanov', 'ROMANOV', 'Good ol Romanov'],
3: ['Which was the first bridge to be built across the River Thames in London?','London Bridge', 'london bridge', 'LONDON BRIDGE', 'London bridge'],
4:  ['Which U.S. president had a home called The Hermitage?','Andrew Jackson', 'andrew jackson', 'ANDREW JACKSON', 'Andrew jackson'],
5: ['Which famous battle took place on Sunday, 18th June, 1815?','Waterloo', 'The battle of Waterloo', 'the battle of waterloo', 'waterloo'],
6: ['How many U.S. presidents have been assassinated?','Four', 'four', 'FOUR' '4'],
7: ['Which world leader, who came to power in 1949, is famous for his “Little Red Book”?','Mao Zedong', 'mao zedong', 'Mao zedong', 'MAO ZEDONG'],
8: ['In which country did the Easter Rising take place in 1916?','Ireland', 'ireland', 'IRELAND', 'Ire Land'],
9: ['What was the name of the first Space Shuttle to go into space?','Columbia', 'columbia', 'COLUMBIA', 'The Columbia'],
10: ['Who was president during the U.S. Civil War?','Abraham Lincoln', 'Abe Lincoln', 'Lincoln', 'abraham lincoln', 'lincoln'] }

Geography:

Question: What is Earths largest continent? Answer: 'Asia', 'asia', 'ASIA', 'As Ia']
Question: What river runs through Baghdad? Answer: 'Tigris River', 'The Tigris River', 'tigris river', 'Tigris']
Question: What country has the most natural lakes? Answer: 'Canada', 'canada', 'CANADA', 'Maple Syrup']
Question: What is the only sea without any coasts? Answer: 'Sargasso Sea', 'The Sargasso sea', 'The Sargasso Sea', 'Sargasso']
Question: What percentage of the River Nile is located in Egypt? Answer: '22%', 'twenty two', 'Twenty Two', 'Twenty-Two', '22']
Question: Which African nation has the most pyramids? Answer: 'Sudan', 'sudan', 'SUDAN', 'Su-dan']
Question: What African country served as the setting for Tatooine in Star Wars? Answer: 'Tunisia', 'tunisia', 'TUNISIA', 'Tun-isia']
Question: What is the oldest city in the world? Answer: 'Damascus', 'damascus', 'DAMASCUS', 'Dama-scus']
Question: Which U.S. state has the most active volcanoes? Answer: 'Alaska', 'alaska', 'ALASKA', 'Laska']
Question: What is the flattest continent? Answer: Australia

Music:

Which musical instrument has black and white keys? 'Piano', 'piano', 'keyboard' 'clicky thingies']
Who is considered as the Greek God of Music? 'Apollo', 'apollo', 'The god Apollo', 'the god apollo']
Which musician wrote Marriage of Figaro? 'Mozart', 'mozart', 'Amadeus Mozart', "wolfgang']
What is the level and intensity of sound measured in? 'Decibels', 'decibels', 'Decibel', 'ear noise'
Who was the first country music artist, who has a record of selling more than 10 million units of an album? 'Garth Brooks', 'garth', 'garth brooks', 'some country singer']
According to a survey by Billboard, who was rated the largest selling album musician in the 1970s? 'Elton John', 'elton john', 'elton', 'rocketman']
What is the name of the studio where ‘The Beatles’ recorded most of their songs? 'Abbey Road', 'abbey road', 'Abbey road' 'some sidewalk']
Who is well-known for playing drums with only one hand? 'Rick Allen', 'rick allen', 'Rick allen', 'drumsticks']
Which rock musician tried to bite the head off a bat in a live concert? 'Ozzy Osbourne', 'ozzy ozbourne', 'ozzy', 'go crazy']
Which music band sang ‘Staying Alive’? 'Bee Gees', 'bee gees', 'Bee gees', 'michael scott']
 
Video Games:

Question: The Vault Dweller is the protagonist of which video game? Answer: 'Fallout', 'fallout', 'FallOut', 'Vault 111']
Question: What is the name of the main protagonist of the Tomb Raider series of games? Answer: 'Lara Croft', 'Lara croft', 'lara croft', 'bear grylls']
Question: Mario first appeared in which classic video game? Answer: 'Donkey Kong', 'Donkey kong', 'donkey kong', 'donkey kong the game']
Question: Which company publishes World of Warcraft? Answer: 'Blizzard Entertainment', 'Blizzard entertainment', 'blizzard entertainment', 'Blizzard Entertainment Inc.']
Question: Master Hand is a character and a boss in which game series? Answer: 'Super Smash Bros', 'Super smash bros', 'super smash bros', 'Super Smash Bros.']
Question: Which game came bundled with the Nintendo Wii in all countries except Japan and North Korea? Answer: 'Wii Sports', 'Wii sports', 'wii sports', 'Wii Sports.']
Question: Which is the only video game in which Mario appears as the villain? Answer 'Donkey Kong Jr', 'Donkey Kong jr', 'donkey kong jr', 'Donkey Kong jr.']
Question:  Desmond Miles is a major character from which video game series? Answer: Assassins Creed
Question: Underground, Hot Pursuit and Most Wanted are instalments of which racing video game franchise? Answer: 'Need For Speed', 'Need for speed', ' Need for Speed', 'need for speed']
Question: Which game features The Nameless King as a boss character? Answer: 'Dark Souls 3', 'Dark souls 3', 'dark souls 3' 'you have died']

Random:

Question: How many players are there in a standard curling team? Answer: 'Four', 'four', '4', 'FOUR']
Question: How many squares are there on the traditional "Snakes & Ladders" board? Answer: '100', 'hundred', 'a hundred', 'one hundred']
Question: A person who starts fires maliciously is known as a what? Answer: 'Arsonist', 'arsonist', 'ARSONIST', 'Arson-ist']
Question: Where were police dogs first used? Answer: 'Belgium', 'belgium', 'BELGIUM', 'Bel gium']
Question: Ham is taken from what part of a pig? Answer: 'Hind Leg', 'Hind leg', 'hind leg', 'the hind leg']
Question: Alphabetically, which is the last of Santas reindeers? Answer: 'Vixen', 'vixen', 'Vix-en', 'Vixen the reindeer']
Question: Is it true that the Special Sauce on a Big Mac is Thousand Island Dressing? Answer: 'No', 'no', 'false', 'False']
Question: What sport would you be playing if the score was deuce? Answer: 'Tennis', 'tennis', 'TENNIS', 'austins sport']
Question: What is the name for Germanys high-speed highways? Answer: 'Autobahn', 'autobahn', 'The autobahn', 'AUTOBAHN']
Question: Mageirocophobia is a fear of what? Answer: 'Cooking', 'cooking', 'fear of cooking', 'COOKING'] }



datafile = open("Trivia_Game.pickle", "wb")
pickle.dump(questions, datafile)
datafile.close()