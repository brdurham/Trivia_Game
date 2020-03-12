#!usr/bin/python3
#Brady Durham
#1/28/20

import pickle

#History

questions = { 1: ['In 1927, who became the first man to fly solo and non-stop across the Atlantic?','Charles Lindbergh', 'charles lindbergh', 'CHARLES LINDBURGH', ' Charles lindburgh'],
2: ['What was the family name of the Russian rulers from the 17th century until the 1917 revolution?','Romanov', 'romanov', 'ROMANOV', 'Good ol Romanov'],
3: ['Which was the first bridge to be built across the River Thames in London?','London Bridge', 'london bridge', 'LONDON BRIDGE', 'London bridge'],
4:  ['Which U.S. president had a home called The Hermitage?','Andrew Jackson', 'andrew jackson', 'ANDREW JACKSON', 'Andrew jackson'],
5: ['Which famous battle took place on Sunday, 18th June, 1815?','Waterloo', 'The battle of Waterloo', 'the battle of waterloo', 'waterloo'],
6: ['How many U.S. presidents have been assassinated?','Four', 'four', 'FOUR' '4'],
7: ['Which world leader, who came to power in 1949, is famous for his “Little Red Book”?','Mao Zedong', 'mao zedong', 'Mao zedong', 'MAO ZEDONG'],
8: ['In which country did the Easter Rising take place in 1916?','Ireland', 'ireland', 'IRELAND', 'Ire Land'],
9: ['What was the name of the first Space Shuttle to go into space?','Columbia', 'columbia', 'COLUMBIA', 'The Columbia'],
10: ['Who was president during the U.S. Civil War?','Abraham Lincoln', 'Abe Lincoln', 'Lincoln', 'abraham lincoln', 'lincoln'] }

#Geography

{ 1: ['What is Earths largest continent?','Asia', 'asia', 'ASIA', 'As Ia'],
2: ['What river runs through Baghdad?','Tigris River', 'The Tigris River', 'tigris river', 'Tigris'],
3: ['What country has the most natural lakes?','Canada', 'canada', 'CANADA', 'Maple Syrup'],
4: ['What is the only sea without any coasts?','Sargasso Sea', 'The Sargasso sea', 'The Sargasso Sea', 'Sargasso'],
5: ['What percentage of the River Nile is located in Egypt?','22%', 'twenty two', 'Twenty Two', 'Twenty-Two', '22'],
6: ['Which African nation has the most pyramids?','Sudan', 'sudan', 'SUDAN', 'Su-dan'],
7: ['What African country served as the setting for Tatooine in Star Wars?','Tunisia', 'tunisia', 'TUNISIA', 'Tun-isia'],
8: ['What is the oldest city in the world?','Damascus', 'damascus', 'DAMASCUS', 'Dama-scus'],
9: ['Which U.S. state has the most active volcanoes?','Alaska', 'alaska', 'ALASKA', 'Laska'],
10:['What is the flattest continent?','Australia', 'australia' 'the land down under', 'kangaroo land'] }

#Music

{ 1:['Which musical instrument has black and white keys?','Piano', 'piano', 'keyboard' 'clicky thingies']
2:['Who is considered as the Greek God of Music?','Apollo', 'apollo', 'The god Apollo', 'the god apollo']
3:['Which musician wrote Marriage of Figaro?','Mozart', 'mozart', 'Amadeus Mozart', 'wolfgang']
4:['What is the level and intensity of sound measured in?','Decibels', 'decibels', 'Decibel', 'ear noise'
5:['Who was the first country music artist, who has a record of selling more than 10 million units of an album?','Garth Brooks', 'garth', 'garth brooks', 'some country singer']
6:['According to a survey by Billboard, who was rated the largest selling album musician in the 1970s?','Elton John', 'elton john', 'elton', 'rocketman']
7:['What is the name of the studio where ‘The Beatles’ recorded most of their songs?','Abbey Road', 'abbey road', 'Abbey road' 'some sidewalk']
8:['Who is well-known for playing drums with only one hand?','Rick Allen', 'rick allen', 'Rick allen', 'drumsticks']
9:['Which rock musician tried to bite the head off a bat in a live concert?','Ozzy Osbourne', 'ozzy ozbourne', 'ozzy', 'go crazy']
10:['Which music band sang ‘Staying Alive’?','Bee Gees', 'bee gees', 'Bee gees', 'michael scott'] }
 
Video Games:

1: ['The Vault Dweller is the protagonist of which video game?','Fallout', 'fallout', 'FallOut', 'Vault 111']
2: ['What is the name of the main protagonist of the Tomb Raider series of games?','Lara Croft', 'Lara croft', 'lara croft', 'bear grylls']
3: ['Mario first appeared in which classic video game?','Donkey Kong', 'Donkey kong', 'donkey kong', 'donkey kong the game']
4: ['Which company publishes World of Warcraft?','Blizzard Entertainment', 'Blizzard entertainment', 'blizzard entertainment', 'Blizzard Entertainment Inc.']
5: ['Master Hand is a character and a boss in which game series?','Super Smash Bros', 'Super smash bros', 'super smash bros', 'Super Smash Bros.']
6: ['Which is the only video game in which Mario appears as the villain?','Donkey Kong Jr', 'Donkey Kong jr', 'donkey kong jr', 'Donkey Kong jr.']
7: ['Desmond Miles is a major character from which video game series?','Assassins Creed', 'assassins creed', 'ASSASSINS CREED', 'Assassins creed']
8: ['Underground, Hot Pursuit and Most Wanted are instalments of which racing video game franchise?','Need For Speed', 'Need for speed', ' Need for Speed', 'need for speed']
9: ['Which game features The Nameless King as a boss character?','Dark Souls 3', 'Dark souls 3', 'dark souls 3' 'you have died']

Random:

1: ['How many players are there in a standard curling team?' Answer: 'Four', 'four', '4', 'FOUR']
2: ['How many squares are there on the traditional "Snakes & Ladders" board?' Answer: '100', 'hundred', 'a hundred', 'one hundred']
3: ['A person who starts fires maliciously is known as a what?' Answer: 'Arsonist', 'arsonist', 'ARSONIST', 'Arson-ist']
4: ['Where were police dogs first used?' Answer: 'Belgium', 'belgium', 'BELGIUM', 'Bel gium']
5: ['Ham is taken from what part of a pig?' Answer: 'Hind Leg', 'Hind leg', 'hind leg', 'the hind leg']
6: ['Alphabetically, which is the last of Santas reindeers?' Answer: 'Vixen', 'vixen', 'Vix-en', 'Vixen the reindeer']
7: ['Is it true that the Special Sauce on a Big Mac is Thousand Island Dressing?' Answer: 'No', 'no', 'false', 'False']
8: ['What sport would you be playing if the score was deuce?' Answer: 'Tennis', 'tennis', 'TENNIS', 'austins sport']
9: ['What is the name for Germanys high-speed highways?' Answer: 'Autobahn', 'autobahn', 'The autobahn', 'AUTOBAHN']
10:['Mageirocophobia is a fear of what?' Answer: 'Cooking', 'cooking', 'fear of cooking', 'COOKING'] }



datafile = open("Trivia_Game.pickle", "wb")
pickle.dump(questions, datafile)
datafile.close()