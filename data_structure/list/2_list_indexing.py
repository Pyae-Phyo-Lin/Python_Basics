#List Indexing , Accessing

my_list = ["p","y","t","h","o","n"]

#List items index start from 0
print(f"First item : {my_list[0]} ")
print(f"Second item : {my_list[1]} ")

#negative indexing - from the end to start
print(f"Last item : {my_list[-1]} ")


#list slicing
print(f"List items from index 1 to 3 : {my_list[1:4]}")
print(f"List items from begining to index 2 : {my_list[:3]}")
print(f"List items from index 3 to end : {my_list[3:]}")
print(f"All items : {my_list[::]}")
print(f"Reverse list items : {my_list[::-1]}")


