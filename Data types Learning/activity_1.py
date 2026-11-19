name = input("Hello Agent!\nCan you please tell me your name?: ")
gaget = input("Also tell me your favorite gaget!: ")
agent_number = 5.5
agent_age = 20
is_active = True

print(type(gaget))
print(type(name))
print(type(agent_number))
print(type(agent_age))
print(type(is_active))

print(f"Hello {name}!\nYour favorite gaget is {gaget}!")

agent_number_string = str(agent_number)
agent_age_string = str(agent_age)
is_active_string = str(is_active)

print(type(agent_number_string))
print(type(agent_age_string))
print(type(is_active_string))
 
slicing_name = name[0:1]
reverse_name = name[::-1]
upper_name = name.upper()
print (slicing_name)
print (reverse_name)
print (upper_name)