from requests import Request, Session

api_token = '6fec5bff-a4be-4912-b67d-2f60c08d1893'
#region = 'sandbox'
api_url_base = 'http://ego-vehicle-api.azurewebsites.net/api/v1/vehicle/signals'

headers = {'Content-Type': 'application/json',
            'X-Api-Key': api_token}
data = {'battery_charging': 'no', 'battery_charging_current': 35, 'battery_health': 100, 'battery_loading_capacity': 11, 'battery_state_of_charge': 100, 'battery_total_kwh_capacity': 17.5, 'brake_fluid_level': 100, 'calculated_remaining_distance': 150, 'central_locking_system': 'closed', 'distance_to_object_back': 'NaN', 'distance_to_object_bottom': 20, 'distance_to_object_front': 24.88, 'distance_to_object_left': 'NaN', 'distance_to_object_right': 'NaN', 'distance_trip': 0, 'door_disc_front_left': 'open', 'door_disc_front_right': 'open', 'door_front_left': 'closed', 'door_front_right': 'closed', 'drive_mode': 'eco', 'flash': 'off', 'heated_seats': 'off', 'high_beam': 'off', 'infotainment': 'on', 'infotainment_volume': 6, 'location': '51,7', 'mileage': 0, 'motor_control_lamp': 'off', 'person_count': 0, 'pulse_sensor_steering_wheel': 143, 'power_consumption': 28, 'rain_sensor': 'rain', 'rear_running_lights': 'on', 'side_lights': 'on', 'speed': 200, 'stop_lights': 'on', 'temperature_inside': 24, 'temperature_outside': 10, 'tire_pressure_back_left': 3, 'tire_pressure_back_right': 3, 'tire_pressure_front_left': 3, 'tire_pressure_front_right': 3, 'trunk': 'open', 'turn_signal_left': 'on', 'turn_signal_right': 'on', 'warning_blinker': 'on', 'weight': 1980, 'windshield_wipers': 'off', 'wiping_water_level': 100}
from requests import Request, Session

s = Session()
req = Request('GET',  api_url_base, data=data, headers=headers)

prepped = s.prepare_request(req)

# do something with prepped.body
prepped.body = {'ListOfVehicleSignalsToUpdate': {
  "location": "50",
  "turn_signal_left": "on",
  "turn_signal_right": "off"
}}

# do something with prepped.headers
#prepped.headers['Keep-Dead'] = 'parrot'

resp = s.send(prepped,
    stream=stream,
    verify=verify,
    proxies=proxies,
    cert=cert,
    timeout=timeout
)

print(resp.status_code)