import user_profile
import api
import vehicle
score_values = {'turn_without_blinker': 5, 'seatheating': 2, 'no_belt': 10, 'no_hands_on_wheel': 10, 'max_accel': 5,
                'speeding': 5, 'low friction': 2, 'eco_mode_on': 5, 'return_to_station': 10, 'recharge': 10, 'passenger>1': 5, 'recup_break': 2}
startscore = 1000
score = 1000

def get_score():
    return score

def increase_score(key):
    for k in score_values:
        if key == k:
            score + score_values[k]

def decrease_score(value):
    for k in score_values:
        if key == k:
            score - score_values[k]

#def update_api(key, value):
#    if key in vehicle.v_api:
#        vehicle.set_key(key, value)


increase_score('eco_mode_on')
print(score)