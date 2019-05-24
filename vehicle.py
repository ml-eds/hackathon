#This module represents the calculations done for the vehicle sensors
import api
import user_profile
import scoring
import infotainment
#storing the api
v_api = api.get()

def update_api(dict1, dict2):
    return dict(list(dict1.items()) + list(dict2.items()))


def set_key(key, value):
    if key in v_api.keys():
        v_api[key] = value


tmp = user_profile.user_profile


v_api = update_api(v_api, tmp)

# this function calculates the gamification score which is stored in the scoring.score variable based on sensor values
def calculate_score():
    if v_api['steering_wheel_turn_left'] == 1 and v_api['turn_signal_left'] == 'off' and v_api['speed'] > 0:
        scoring.decrease_score('turn without blinker')
    if v_api['steering_wheel_turn_right'] == 1 and v_api['turn_signal_right'] == 'off' and v_api['speed'] > 0:
        scoring.decrease_score('turn without blinker')
    if v_api['heated_seats'] == 'on':
        scoring.decrease_score('heated seats')
    if v_api['seat_belts'] == 'off' and v_api['speed'] > 0:
        scoring.decrease_score('no belt')
    if v_api['pulse_sensor_steering_wheel'] == 0:
        scoring.decrease_score('no hands on wheel')
    if (v_api['speed']/3.6)/10 >= 4:
        scoring.decrease_score('fast accel')
    if v_api['speed'] > 50:
        scoring.decrease_score('speeding'),
    if v_api['tire_pressure_back_left'] > 2 and v_api['tire_pressure_back_right'] > 2 and v_api['tire_pressure_front_left'] > 2 and v_api['tire_pressure_front_right'] > 2:
        scoring.increase_score('low friction')
    if v_api['drive_mode'] == 'eco':
        scoring.increase_score('eco mode on')
    if v_api['location'] == '51,7':
        scoring.increase_score('return to station')
    if v_api['battery_charging'] == 'yes':
        scoring.increase_score('recharge')
    if v_api['person_count'] >= 1:
        scoring.increase_score('passenger > 1')
    if v_api['battery_charging_recuperation'] > 0:
        scoring.increase_score('recuperation breaking')

    user_profile.update_score(scoring.score)


#calculate_score()
print("Your score is", scoring.score)
infotainment.set_api(str(scoring.score))