def create_an_empty_list():
    # Create and return an empty list
    return []

def create_a_list():
    # Create and return a list with four elements
    return [1, 'apple', 3.14, True]

def add_element_to_end_of_list(l, element):
    # Add an element to the end of the list
    l.append(element)
    return l

def add_element_to_start_of_list(l, element):
    # Add an element to the start of the list
    l.insert(0, element)
    return l

def remove_element_from_end_of_list(l):
    # Remove the last element from the list
    l.pop()
    return l

def remove_element_from_start_of_list(l):
    # Remove the first element from the list
    del l[0]
    return l

def retrieve_first_element_from_list(l):
    # Retrieve the first element of the list
    return l[0]

def retrieve_element_from_index(l, index):
    # Retrieve the element at the given index
    return l[index]

def retrieve_last_element_from_list(l):
    # Retrieve the last element of the list
    return l[-1]
