#for statement (example 2)

#create a sample collection
users = {'lone': 'active','nagalot':'inactive','shmlux': 'active'}


#strat: Iterate over a copy 
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]


#strat: Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status 

print(users)