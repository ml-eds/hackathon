#as it was not possible to alternate the given API values we added some extra sensor values in the above dictionary
import api_connect1
api = {'battery_charging': 'no', 'battery_charging_recuperation': 2,'battery_charging_current': 0, 'battery_health': 100, 'battery_loading_capacity': 11,
        'battery_state_of_charge': 100, 'battery_total_kwh_capacity': 17.5, 'brake_fluid_level': 100, 'calculated_remaining_distance': 150,
        'central_locking_system': 'closed', 'distance_to_object_back': 'NaN', 'distance_to_object_bottom': 20, 'distance_to_object_front': 'NaN',
        'distance_to_object_left': 'NaN', 'distance_to_object_right': 'NaN', 'distance_trip': 0, 'door_disc_front_left': 'open',
        'door_disc_front_right': 'open', 'door_front_left': 'closed', 'door_front_right': 'closed', 'drive_mode': 'eco', 'flash': 'off',
        'heated_seats': 'off', 'high_beam': 'off', 'infotainment': 'on', 'infotainment_volume': 6, 'infotainment_music':"Darude - Sandstorm",
        'location': '51,7', 'mileage': 0, 'motor_control_lamp': 'off', 'person_count': 1, 'pulse_sensor_steering_wheel': 143,
        'power_consumption': 28, 'rain_sensor': 'rain', 'rear_running_lights': 'on', 'side_lights': 'on', 'speed': 100,
        'stop_lights': 'off', 'temperature_inside': 24, 'temperature_outside': 10, 'tire_pressure_back_left': 3, 'tire_pressure_back_right': 3,
        'tire_pressure_front_left': 3, 'tire_pressure_front_right': 3, 'trunk': 'open', 'turn_signal_left': 'on', 'turn_signal_right': 'on',
        'warning_blinker': 'on', 'weight': 1200, 'windshield_wipers': 'off', 'wiping_water_level': 100, 'steering_wheel_turn_left': '1', 'steering_wheel_turn_right': '0', 'seat_belts': 'on'}
apii = api_connect1.get_api()


def update_api(dict1, dict2):
    return dict(list(dict1.items()) + list(dict2.items()))
api = update_api(api, apii)

#print(api)


def get():
    return api

def patch(key, value):
    if key in api:
        api[key] = value

def getvalue(key):
    if key in api:
        return api[key]
    else:
        return None


#weather real time information out of the rain sensor. The windshield wiper speed adopts with the intensity of the rain.
#Therefore we are able to transmit these data to external institutions to provide real time information for weather maps.
