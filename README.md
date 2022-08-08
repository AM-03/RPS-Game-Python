First published python project

This is a simple terminal based game, called Papper, Scissor, Stone

Objects-Classes :

There is just one simple class named "user". 
Used for defining players 
Also has many fields for their game info like winsCount,name and ... 


methodes : 

The performance of each function is clearly defined by a single line comment
There is many simple functions such as start new game, show panel of a player, load current database and .... whose performance is clearly explained by comments inside the file


data base - serialization :

I used JSON for user objects serialization ( of course you can use rapidJSON or orJSON instead of current serialization library ). 
Database file directory (dataBase.json) and main file directory should be the same. 
dataBase.json must exists before running the game because program reads primary database from dataBase. 
Since JSON is a human readable serialization format you can easily read dataBase.json file and edit it according to your wish. 











Run :

just run the rps-game.py throught terminal and read the displayed texts and follow steps !

