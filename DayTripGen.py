# (5 points): As a developer, I want to make at least three commits with descriptive messages. (ignore till Friday)
# (5 points): As a developer, I want to store my destinations, restaurants, modes of transportation, 
#       and entertainments in their own separate lists. (4 each list)
# (5 points): As a user, I want a destination to be randomly selected for my day trip. 
# (5 points): As a user, I want a restaurant to be randomly selected for my day trip. 
# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip. 
# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip. 
# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, 
#       and/or form of entertainment if I don’t like one or more of those things. (re-select individually after 
#       selecting the one they want re-selected) 
# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections. 
# (10 points): As a user, I want to display my completed trip in the console. 
# (5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!


import random


destinations = ["MI", "Chicago", "NY", "AZ"]
restaurants = ["Pancheros", "Giordanos", "Pizza Suprema", "The Tavern"]
modes_of_transport = ["car", "train", "plane", "bus"]
entertainments = ["Ren Fest", "aquarium", "zoo", "National Park"]


def destination_gen(destination_lists):
    print("Welcome to the day trip generator! When you know you would like to do something, but aren't sure what, we can help!")
    destination_rand = random.choice(destination_lists)
    question_one = input(f'We have selected {destination_rand} for your destination! Does this sound good to you? Please enter y/n: ')
    while question_one == 'n':
        destination_rand = random.choice(destination_lists)
        question_one = input(f"Sorry you don't like this destination. No worries! Let's try something else! How does {destination_rand} sound? Please enter y/n: ")
    if question_one == 'y':
        print("Great! Let's move on.")
    return destination_rand


def restaurant_gen(restaurant_lists):
    restaurant_rand = random.choice(restaurant_lists)
    question_two = input(f'We have selected {restaurant_rand} for your restaurant! Does this sound good to you? Please enter y/n: ')
    while question_two == 'n':
        restaurant_rand = random.choice(restaurant_lists)
        question_two = input(f"Sorry you don't like this restaurant. No worries! Let's try something else! How does {restaurant_rand} sound? Please enter y/n: ")
    if question_two == 'y':
        print("Great! Let's move on.")
    return restaurant_rand


def transport_gen(transport_lists):
    transport_rand = random.choice(transport_lists)
    question_three = input(f'We have selected a {transport_rand} for your mode of transportation! Does this sound good? Enter y/n: ')
    while question_three == 'n':
        transport_rand = random.choice(transport_lists)
        question_three = input(f"Sorry you don't like this mode of transportation. No worries! We can try something else! How does {transport_rand} sound? Please enter y/n: ")
    if question_three == 'y':
            print("Great! Let's move on.")
    return transport_rand


def entertainment_gen(entertainment_lists):
    entertainment_rand = random.choice(entertainment_lists)
    question_four = input(f'We have selected the {entertainment_rand} for your entertainment! Does this sound good? Enter y/n: ')
    while question_four == 'n':
        entertainment_rand = random.choice(entertainment_lists)
        question_four = input(f"Sorry you don't like this entertainment selection. No worries! We can try something else! How does {entertainment_rand} sound? Please enter y/n: ")
    if question_four == 'y':
        print("Great! Let's move on. Next, we'll go over your selections made and a final confirmation!")
    return entertainment_rand

destination_rand = destination_gen(destinations) 
restaurant_rand = restaurant_gen(restaurants)
transport_rand = transport_gen(modes_of_transport)
entertainment_rand = entertainment_gen(entertainments)

def confirmation_flow(final_confirmation):
    confirmation = final_confirmation
    print(f'Destination: {destination_rand}')
    print(f'Restaurant: {restaurant_rand}')
    print(f'Transportation: {transport_rand}')
    print(f'Entertainment: {entertainment_rand}')

    question_five = input('Would you like to finalize your trip? Enter y/n: ')
    while question_five == 'n':
        question_five = input('please run day trip planner again or answer y: ')
    if question_five == 'y':
            print(f'Get ready for your next big day trip! You will be traveling to {destination_rand} by {transport_rand}, where you will be going to the {entertainment_rand}. You will be enjoying a meal at {restaurant_rand}.')
            return

confirmation = confirmation_flow(" ")

