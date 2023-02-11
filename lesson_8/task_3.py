import json

dict_info = {
    111222: ('Siarhei', 28),
    222333: ('Natalli', 24),
    333444: ('Valeri', 45),
    444555: ('Ramzes', 4000),
    555666: ('Andjey', 27),
    666777: ('Igor', 38),
}

with open('taks3.json', 'w') as f_file:
    json.dump(dict_info, f_file)
