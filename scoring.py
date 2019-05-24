import infotainment
# This module provides simple arithmetic operations for the calculate score function in vehicle.py

#score_values are values that we consider for our gamification score

score_values = {'turn without blinker': 5, 'heated seats': 2, 'no belt': 10, 'no hands on wheel': 10, 'fast accel': 5,
                'speeding': 5, 'low friction': 2, 'eco mode on': 5, 'returning to station': 10, 'recharging': 10, 'passenger > 1': 5, 'recuperation breaking': 2}
startscore = 1000
score = 1000

#getter for score value
def get_score():
    return score

#increase gamification score by value of transmitted key
def increase_score(key):
    global score
    for k in score_values.keys():
        if k == key:
            score += score_values[k]
            print("Congratulations you received points for", key, ". ")
            string = "Congratulations you received points for" + key + ". \n"
            infotainment.set_api(string)
            return

#descrease gamification score y value of transmitted key
def decrease_score(key):
    global score
    for k in score_values.keys():
        if k == key:
            score -= score_values[k]
            print("You lost points for", key, ". ")
            string = "You lost points for" + key + ". \n"
            infotainment.set_api(string)
            return

