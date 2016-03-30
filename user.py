class User():
	def __init__(self, name, lvl):
		self.name = name
		self.lvl = lvl


	def __repr__(self):
		return "%s(%d)"%(self.name, self.lvl)



def load_users(filename="brukerdata.txt"):
	fil = open(filename, "r+")

	users = {}
	for userline in fil:
		name,lvl = userline.rstrip().split(",")
		users[name] = User(name, int(lvl)) 

	return users


def save_users(users, filename="brukerdata.txt"):
	fil = open(filename, "w+")
	
	for user in users.values():
		fil.write("%s,%s\n" % (user.name, user.lvl))




if __name__ == '__main__':
	users = load_users()

	user = users["Jonas"]
	user.lvl +=1
	users["Jonas"] = user

	users["Robin"].lvl += 1
	
	save_users(users)

	users = load_users()

	print(users)

