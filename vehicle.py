import api
import changes
import user_profile

v_api = api.get()

print(v_api)

def update_api(dict1, dict2):
    return dict(list(dict1.items()) + list(dict2.items()))


tmp = user_profile.user_profile
print(tmp)

v_api = update_api(v_api, tmp)

print(v_api)