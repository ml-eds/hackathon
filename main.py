#main function to initiate everything
import vehicle
import infotainment
import api


def main():
    ap = api.get()
    for k in ap.keys():
        if k == 'pulse_sensor_steering_wheel':
            if ap['pulse_sensor_steering_wheel'] >= 140:
                print("Warning! We detected a high heart rate: ", ap['pulse_sensor_steering_wheel'])
    vehicle.calculate_score()
    infotainment.set_image()
main()