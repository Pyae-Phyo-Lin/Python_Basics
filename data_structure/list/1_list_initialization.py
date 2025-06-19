# List Starting

#Empty List
empty_list =[]
print(f"A empty list : {empty_list}, {type(empty_list)}")

string_list = ["python","coffee","technology"]   #string list
number_list = [0,7,9,5]    #numbers list
mix_list = ["apple", 10, 3.14, None, True] #in a python list can include string, int, float, boolean

print(f"String List : {string_list}.")
print(f"Numbers List : {number_list}.")
print(f"Mixed List : {mix_list}.")

#List Add item
string_list.append("github")
print(string_list)              #['python', 'coffee', 'technology', 'github']

string_list.insert(0,"code")    #index 0 (first position) insert an item
print(string_list)              #['code', 'python', 'coffee', 'technology', 'github']


#Change item value
string_list[0] = "code_space"
print(string_list)