import time, random
class Player():
	def __init__(self, name):
		self.name  = name
		self.health =  100
		self.damage = 15
		self.heal = 10
		self.no_of_heals = 5
	def take_damage(self, damage):
		self.health -= damage
	def heal_(self):
		self.health += self.heal


player = Player("Player")
enemy = Player("Enemy")
start = time.time()
while player.health > 0 and enemy.health > 0:
	enemy_move = random.choice(["you dodged ", "Dodge", "Heal"])
	while enemy_move == "Heal" and enemy.no_of_heals == 0:
		enemy_move = random.choice(["Attack", "Dodge", "Heal"])
	print(f"\n  SpongeBob Health {player.health}\n  Squidward Health {enemy.health}")
	print(f"\n type **attack** to Attack\n type **dodge** to Dodge\n type **eat** to heal ({player.no_of_heals} uses left)")
	
	try:
		player_move = int(input(":"))
		player_move = ["Attack", "dodge", "Heal"][player_move - 1]
	except:
		player_move = random.choice(["Attack", "Dodge", "Heal"])

	if player_move == "Heal":
		if player.no_of_heals > 0:
			player.heal_()
			player.no_of_heals -= 1
			print("\nSpongeBob ate a craby patty himself .Heal.")
	if enemy_move == "Heal":
		enemy.heal_()
		enemy.no_of_heals -= 1
		print("\nSquidward just healed .Heal.")
	if player_move == "Attack" and enemy_move == "Dodge":
		print("\nYou used bubble shot but squidward dodged it .slow attack.")
	elif player_move == "Dodge" and enemy_move == "Attack":
		print("\nSpongeBob dodged Squidwards tentacle attack .fast dodge.")
	elif player_move == "Dodge" and enemy_move == "Dodge":
		print("\nBoth of you dodged .both of you are scared.")
	elif player_move == "Attack" and enemy_move == "Attack":
		print("Both of you got hit by bubble and tentacles .both attack.")
		player.take_damage(enemy.damage)
		enemy.take_damage(player.damage)
	else:
		if player_move == "Attack":
			print("You shot bubbles at squidward .fast attack.")
			enemy.take_damage(player.damage)
		if enemy_move == "Attack":
			print("Squidawrd sliced you with his tentacle .superfast attack.")
			player.take_damage(enemy.damage)
		if player_move == "Dodge":
			print("You dodged .coward move.")
		if enemy_move == "Dodge":
			print("Squidward is scared .enemy dodge.")
else:
	if player.health > 0:
		end = time.time()
		print("*The Ambulence Arrived* You Put Squidward in the hospital/you won/")
		print(f"\nTIME TAKEN : {round(end - start, 1)} seconds")
	elif enemy.health > 0:
		print("\n*The Ambulence Arrived* Squidward put you in the hospital/you lost/")
	else:
		print("Mr.Krabs found you guys both dead in the back of the krusty crab /its a tie/")