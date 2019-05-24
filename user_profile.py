# this represents the user profile with the user preferences stored in the user_profile dict
user_profile = {'mirrors': [{"L" : 0}, {"R": 0}], 'accelerator': 'normal', 'steering': 'sport', 'temperature_inside': 22,
                'infotainment_music': 'Karel Gott - Biene Maya',
                'adresses': [{'street': "Campus_Boulevard", 'number': 30, 'postcode': 52074}, {'street': "Templergraben", 'number': 55, 'postcode': 52062}],
                'shops': ["Kaufhof", "Lidl", "Aldi", "Edeka"], 'POI':["Dreilaendereck", "Dom", "HbF", "FitnessBude"],
                'score': 1000, 'drive_mode': "eco", 'contacts':  {'name': "Alice", 'tel': "01282382929", 'name':"Bob", 'tel': "09129102810"}}

#used to update a specific user preference score if needed
def update_score(val):
    user_profile['score'] = val
