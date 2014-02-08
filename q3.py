"""

question 3

Given the same list as specified in question 2 write a function to generate 
the average, median, max, min, and standard deviation of of number of posts.

[
    { id: 40, name: "Joe Bloggs", "posts": 4 },
    { id: 567, name: "Jenny Smith", posts: 3 },
    { id: 3, name: "Frank Jones", posts: 54 },
    { id: 46, name: "Samantha Wills", posts: 0 },
    { id: 6789, name: "Ahmed Joseph Naran", posts: 15}
]
"""

customers = [
    { "id": 40, "name": "Joe Bloggs", "posts": 4 },
    { "id": 567, "name": "Jenny Smith", "posts": 3 },
    { "id": 3, "name": "Frank Jones", "posts": 54 },
    { "id": 46, "name": "Samantha Wills", "posts": 0 },
    { "id": 6789, "name": "Ahmed Joseph Naran", "posts": 15}
]

import math

def grab_posts(customer_list):
    post_list = []
    for customer in customers:
        post_list.append(customer["posts"])
    return post_list

def avg(post_list):
    average = sum(post_list) / (1.0 * (len(post_list)))
    return average

def median(post_list):
    sorted_list = sorted(post_list)
    length = len(sorted_list)
    if not length % 2:
        return (sorted_list[length / 2] + sorted_list[length / 2 - 1]) / 2.0
    return sorted_list[length / 2]

def maximum(post_list): 
    max_value = post_list[0]   
    for elm in post_list[1:]:        
        if elm > max_value:
            max_value = elm
    return max_value

def minimum(post_list):
    min_value = post_list[0]
    for elm in post_list[1:]:
        if elm < min_value:           
            min_value = elm
    return min_value                

def std_dev(post_list):
    average = avg(post_list)
    variance = map(lambda x: (x - average)**2, post_list)
    standard_deviation = math.sqrt(avg(variance))
    return round(standard_deviation, 5) # => population Standard deviation

def main():
    posts = grab_posts(customers)
    print avg(posts) == 15.2
    print median(posts) == 4
    print maximum(posts) == 54
    print minimum(posts) == 0
    print std_dev(posts) == 20.05393

if __name__ == '__main__':
    main()

