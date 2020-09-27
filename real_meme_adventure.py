from random import *
from turtle import *
def no_answ():
	while user_input != "n" and user_input != "y": 
			print("What was that? I didn't hear what you said. Can you input a correct answer (y/n)?")
			user_input = input()
def draw_stars(x):
	bgcolor("black")
	pencolor("CadetBlue1")
	speed(x)
	for t in range(10):
		penup()
		goto(randrange(-300,300), randrange(-120,300))
		pendown()
		for i in range(5):	
			forward(10)
			right(144)

	exitonclick()
def smile():
	screensize(300, 300)
	speed(10)
	bgcolor("brown")
	pencolor("white")

	penup()
	goto(-75,150)
	pendown()
	circle(10)     #eye one

	penup()
	goto(75,150)
	pendown()
	circle(10)     #eye two

	penup()
	goto(0,0)
	pendown()
	circle(100,90)   #right smile

	penup()           
	setheading(180) # <-- look West
	goto(0,0)
	pendown()
	circle(-100,90)

	penup()
	goto(-200, 100)
	pendown()
	circle(-200)

	
	exitonclick()



print( '''
	You're walking next to a stream in the woods and you notice a perfectly round pebble; do you pick it up? (y/n)
	''')



pebble = False #for later 

user_input = input()

if  user_input == "y": 
	print('''
		You pick up the pebble and move on your way...
		''')
	pebble = True
elif user_input == "n":
	print('''
		You don't pick up the pebble and you keep walking...
		''')

print('''
	As you're walking, you see a pathway that strays away from the stream; do you take that path? (y/n)
	''')
user_input = input()
die = False
if user_input == "y":
	print('''
		You walk down the straying path...
		''')
	print('''
		It gets darker and darker as you walk down the path; however, you still have some visibility. 
		The path seems to have a lot of twists and turns, and it causes you to feel lost.
		''')
	print('''
		At some point it feels colder and colder as you keep walking, then you step into step into something that you think is water, 
		but it's actually some black slush that is difficult get out of. 
		As you wiggle more to try to escape, you slowly sink into the slush. 
		You see a low hanging branch next you, do you grab it to try to escape? (y/n)
		''')
	user_input = input()
	if user_input == "y":
		print('''
			You grab it and pull yourself out. You decide to turn back and go back to the path by the stream.
			''')
	elif user_input == "n":
		die = True
		
elif user_input == "n":
	print('''
		You keep walking next to the stream.
		''')

if die:
	print('''
		lol u die cuz no; GAME OVER
		''')
else:
	print('''
		As the night slowly creeps up, the darkness emitts a somber feeling that leaves you uneasy; however there are stars up in the sky; 
		do you want to see the stars? (y/n)
		''')
	
	user_input = input()

	if user_input == "y":
		draw_stars(3)
	elif user_input == "no":
		print("lol loser u keep walking...")
	print('''
		After a few minutes of walking, you see a small light in the distance; you walk a little faster in the hope of approaching the light.
		The light is from a small tavern that appears homely and safe. Do you want to enter the tavern? (y/n) ''')

	user_input = input()
	while user_input != "n" and user_input != "y": 
			print('''
				What was that? I didn't hear what you said. Can you input a correct answer (y/n)?
				''')
			user_input = input()
	if user_input == "y":	
		print('''
			You enter the tavern....
			''')

		print('''
			As you step inside, intimidating travelers glare at you and size you up. 
			A seat if empty at the bar and there's a free spot at a table with a few other nomads.
			 Do you want to at the bar or table? (bar/table)
			''')
		user_input = input()
		while user_input != "bar" and user_input != "table": 
			print('''
				There are no other seats left where you feel safe, which one the bar seat or table seat? (bar/table)
				''')
			user_input = input()

		if user_input == "bar":
			print('''
				You approach the bar and take a seat. 
				''')
			print(''' 
				The bartender approaches you and says, "Hello traveler ;) would you like something to drink?" (y/n)
				''')
			user_input = input()
			if user_input == "y":
				print(''' 
					"There you go, buddy ;), says the suspicious bartender as he hands you a bottle and glass.
					''')
		elif user_input == "table":
			print('''
			You take the seat at the table with other people, they stab you with their judge-filled eye-spears. 	
	
			"What's you're story, little fella," says a mencacing-looking man who has an eyepatch.
							Do you tell him your story? (y/n)''')

			user_input = input()
			if user_input == "y":
				print('''
				You tell him your story, containing hardships and heartbreaks, deaths and births. 
				The man's threatening look slowly turns into soft and pudgy one.
				
				"Wow," he said, "you've had it really hard. I really respect you now wow..."
				''')

				print('''

			"I CAN'T BELEIVE THIS- THEY SHOULD FIGHT TO PROVE THEIR ACTUAL STRENGTH!!" yelled an angry bar attendant.

			 "How about they traverse through Goldorf's mysterious castle to prove their courage!" said another. 
			 Everyone yelled in agreement. 

			 Will you fight to show your strength or venture through a castle to display courage?
				
				''')

	elif user_input == "n":
		print("Keep Walking")