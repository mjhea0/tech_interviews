"""
Question 2

Given a list of user dictionaries with the following structure:

[
    { id: 40, name: "Joe Bloggs", "posts": 4 },
    { id: 567, name: "Jenny Smith", posts: 3 },
    { id: 3, name: "Frank Jones", posts: 54 },
    { id: 46, name: "Samantha Wills", posts: 0 },
    { id: 6789, name: "Ahmed Joseph Naran", posts: 15}
]

Write a function that returns a list of objects with the following structure: 
first_name, last_name, posts, ordered by number of posts, removing any users that have not made any posts. E.g.:

[
    { "first_name": "Frank", "last_name": "Jones", "posts": 54 },
    { "first_name": "Ahmed Joseph", "last_name": "Naran", "posts": 15},
    { "first_name": "Joe", "last_name": "Bloggs", "posts": 4},
    { "first_name": "Jenny", "last_name": "Smith", "posts": 3 }
]
"""
import json
import codecs
from operator import itemgetter


def generate_list_of_objs(list_of_dicts):
    new_list = []
    for customer in list_of_dicts:
        if customer["posts"] > 0:
            converted_names = split_names(customer)
            new_dict = {"first_name":converted_names[0], \
                "last_name":converted_names[1],"posts":customer["posts"]}
            new_list.append(new_dict)
    return new_list

def split_names(dictionary):
    converted_names = []
    split_name = dictionary["name"].split(" ")
    last_name = split_name.pop()
    first_name  = " ".join(split_name)
    converted_names.extend([first_name,last_name])
    return converted_names


def sort_list(list_of_objs):
    sorted_list = sorted(list_of_objs, key=itemgetter("posts"), reverse=True)
    return sorted_list


#### ---- first test ---- ####


customers = [
    { "id": 40, "name": "Joe Bloggs", "posts": 4 },
    { "id": 567, "name": "Jenny Smith", "posts": 3 },
    { "id": 3, "name": "Frank Jones", "posts": 54 },
    { "id": 46, "name": "Samantha Wills", "posts": 0 },
    { "id": 6789, "name": "Ahmed Joseph Naran", "posts": 15}
]

test = generate_list_of_objs(customers)
print sort_list(test) == [
    { "first_name": "Frank", "last_name": "Jones", "posts": 54 },
    { "first_name": "Ahmed Joseph", "last_name": "Naran", "posts": 15},
    { "first_name": "Joe", "last_name": "Bloggs", "posts": 4},
    { "first_name": "Jenny", "last_name": "Smith", "posts": 3 }
]

#### ---- second test ---- ####


customers2 = [
    { "id": 44, "name": "Robert John Bloggs", "posts": 20 },
    { "id": 57, "name": "Jay Folds", "posts": 1 },
    { "id": 30, "name": "Rich Jones", "posts": 0 },
    { "id": 49, "name": "Michael Jeffrey Herman", "posts": 22 },
    { "id": 76, "name": "Joseph Naran", "posts": 11}
]

test2 = generate_list_of_objs(customers2)
print sort_list(test2) == [
    { "first_name": "Michael Jeffrey", "last_name": "Herman", "posts": 22 },
    { "first_name": "Robert John", "last_name": "Bloggs", "posts": 20},
    { "first_name": "Joseph", "last_name": "Naran", "posts": 11},
    { "first_name": "Jay", "last_name": "Folds", "posts": 1 }
]
