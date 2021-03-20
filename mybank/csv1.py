import csv

csv_columns = ['device_uid', 'package_list', 'device_client_id','device_info']
dict_data = [
    {'device_uid': 18810016389859667, 'package_list': "",
     'device_client_id': '00000000-0fff-ffff-ffff-ffed7c6ed308',
     'device_info': 'ANDROID 10|V4.1.10|Samsung Galaxy S4|TR|400136'},
    {'device_uid': 18810016389859667, 'package_list': "",
     'device_client_id': '00000000-0fff-ffff-ffff-ffed7c6ed308',
     'device_info': 'ANDROID 10|V4.1.10|Samsung Galaxy S4|TR|400136'},
    {'device_uid': 18810016389859667, 'package_list': "",
     'device_client_id': '00000000-0fff-ffff-ffff-ffed7c6ed308',
     'device_info': 'ANDROID 10|V4.1.10|Samsung Galaxy S4|TR|400136'},
    {'device_uid': 18810016389859667, 'package_list': "",
     'device_client_id': '00000000-0fff-ffff-ffff-ffed7c6ed308',
     'device_info': 'ANDROID 10|V4.1.10|Samsung Galaxy S4|TR|400136'},
    {'device_uid': 18810016389859667, 'package_list': "",
     'device_client_id': '00000000-0fff-ffff-ffff-ffed7c6ed308',
     'device_info': 'ANDROID 10|V4.1.10|Samsung Galaxy S4|TR|400136'},
    {'device_uid': 18810016389859667, 'package_list': "",
     'device_client_id': '00000000-0fff-ffff-ffff-ffed7c6ed308',
     'device_info': 'ANDROID 10|V4.1.10|Samsung Galaxy S4|TR|400136'},
    {'device_uid': 18810016389859667, 'package_list': "",
     'device_client_id': '00000000-0fff-ffff-ffff-ffed7c6ed308',
     'device_info': 'ANDROID 10|V4.1.10|Samsung Galaxy S4|TR|400136'},
    {'device_uid': 18810016389859667, 'package_list': "",
     'device_client_id': '00000000-0fff-ffff-ffff-ffed7c6ed308',
     'device_info': 'ANDROID 10|V4.1.10|Samsung Galaxy S4|TR|400136'},
    {'device_uid': 18810016389859667, 'package_list': "",
     'device_client_id': '00000000-0fff-ffff-ffff-ffed7c6ed308',
     'device_info': 'ANDROID 10|V4.1.10|Samsung Galaxy S4|TR|400136'},
    {'device_uid': 18810016389859667, 'package_list': "",
     'device_client_id': '00000000-0fff-ffff-ffff-ffed7c6ed308',
     'device_info': 'ANDROID 10|V4.1.10|Samsung Galaxy S4|TR|400136'}
]
csv_filename = "names.csv"
try:
    with open(csv_filename, 'w') as csv_file:
        # writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
        writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
        # writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
except IOError:
    print("I/O error")
