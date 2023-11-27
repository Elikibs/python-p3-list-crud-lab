# Create an empty list
def create_an_empty_list():
    return []
print(create_an_empty_list())

# Create a list with 4 items
def create_a_list(list):
    return list

list = create_a_list(["Elisha", "Emmanuel", 34, 45])
print(list)

# Add element to end of list
def add_element_to_end_of_list(l, element):
    l.append(element)
    return l
print(add_element_to_end_of_list(list, "Tito"))


# Add element to start of list
def add_element_to_start_of_list(l, element):
    l.insert(0, element)
    return l
print(add_element_to_start_of_list(list, "Maureen"))


# Remove element at end of list using pop()
def remove_element_from_end_of_list(l):
    l.pop(-1)
    return l
print(remove_element_from_end_of_list(list))


# Remove element at start of list using del()
def remove_element_from_start_of_list(l):
    del(l[0])
    return l
print(remove_element_from_start_of_list(list))


# retrieve_first_element_from_list
def retrieve_first_element_from_list(l):
    return l[0]
print(retrieve_first_element_from_list(list))

# retrieve_element_from_some_index_to_another 
def retrieve_element_from_index(l, index):
    return l[index]

print(retrieve_element_from_index(list, 2))


#  retrieve_last_element_from_list
def retrieve_last_element_from_list(l):
    return l[-1]
print(retrieve_last_element_from_list(list))
