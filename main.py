import random
import data
import logo


def compare(a, b, c):
    if a > b and c == "a":
        print("You are right! ")
        return True
    if b > a and c == "a":
        print("Sorry, that's wrong.")
        return False
    if a > b and c == "b":
        print("Sorry, that's wrong.")
        return False
    if b > a and c == "b":
        print("You are right! ")
        return True


game_score = 0
game = True
rand_data_one = random.choice(data.data)

while game:
    print(logo.logo)
    print(f"Compare A: {rand_data_one['name']}, a {rand_data_one['description']}, from {rand_data_one['country']}")
    A = rand_data_one['follower_count']
    print(logo.vs)
    rand_data_two = random.choice(data.data)
    # if random are the same:
    if rand_data_one == rand_data_two:
        rand_data_two = random.choice(data.data)
    print(f"Compare B: {rand_data_two['name']}, a {rand_data_two['description']}, from {rand_data_two['country']}")
    B = rand_data_two['follower_count']
    # input by user
    user_input = input("Who has more follower? Type 'A' or 'B': ").lower()
    return_value = compare(A, B, user_input)
    if return_value is False:
        print(f"Your final score: {game_score}!")
        game = False
    else:
        game_score += 1
        print(f"Your game score: {game_score}!")
        rand_data_one = rand_data_two
