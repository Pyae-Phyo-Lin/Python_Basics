mylist = ['python', 'odoo', 'pandas', 'numpy']

########################################
#get itesm by loops
########################################

#get items by for loop
for i in range(len(mylist)):
    print(mylist[i])

#get items by while loop
i = 0
while i < len(mylist):
    print(mylist[i])
    i += 1

#get items by list comprehensive
[print(x) for x in mylist]


########################################
#get new list containing value with list comprehension
########################################

my_newlist = []
for x in mylist:
    if "o" in x:
        my_newlist.append(x)
print(my_newlist)           #['python', 'odoo']


my_newlist_2 = []
my_newlist_2 = [x.capitalize() for x in mylist if "p" in x]
print(my_newlist_2)         #['Python', 'Pandas', 'Numpy']
