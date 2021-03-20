import click
import json
import os
import time
import uuid
import random
from mimic import Mimic, DateTime
from datetime import datetime
from mybank.Mobile import Mobile
from mybank import packagen


class Switch:
    def __init__(self, switches):
        self.switches = switches
        self.between = len(switches[0]) == 3

    def __call__(self, x):
        for line in self.switches:
            if self.between:
                if line[0] <= x < line[1]:
                    return line[2]
            else:
                if line[0] == x:
                    return line[1]
        return None


between_table = [
    (1, 50, 'crbQuery1'),
    (50, 85, 'alienQuery'),
    (85, 90, 'admTestQuery1'),
    (90, 92, 'admTestQuery2'),
    (92, 96, 'accsTestQuery1'),
    (96, 101, 'smsTestQuery1'),
]


def probably(chance):
    return random.random() < chance


@click.command()
@click.argument('data_count', type=int)
@click.argument('result_per_user', type=int)
def generate_data(data_count, result_per_user=15):
    user_count = data_count // result_per_user
    print('data_count:', data_count)
    print('user_count:', user_count)
    print('result_per_user:', result_per_user)

    switch_query = Switch(between_table)

    from_ts = int(datetime(2015, 1, 1).timestamp())
    to_ts = int(datetime(2020, 12, 31).timestamp())

    from_mbb = 5301000000
    to_mbb = from_mbb + 200000

    from_imei = 990000862471854
    to_imei = from_imei + 200000
    start_time = time.time()

    random.seed()

    len_packages = len(packagen.packages)

    file_id = f"{int(time.time())}-{random.randint(1000, 9999)}"

    print(f"File id: {file_id}")

    user_file_gen_ext = f'./output/{file_id}-user.gen'
    user_file_load_ext = f'./output/{file_id}-user.load'

    result_file_gen_ext = f'./output/{file_id}-result.gen'
    result_file_load_ext = f'./output/{file_id}-result.load'

    user_file = open(user_file_gen_ext, 'w')
    result_file = open(result_file_gen_ext, 'w')

    for user in Mimic.generate(count=user_count):
        insert_dt = DateTime.between_ts(from_ts, to_ts)

        user.insert_date = str(insert_dt.date())
        user.insert_time = insert_dt.isoformat()
        user.user_detail_id = 1
        user.user_id = 1
        user.mbb = Mobile.phone(from_number=from_mbb, to_number=to_mbb)
        user.device_client_id = str(uuid.UUID(int=(0xFFFFFFFFFFFFFFFFFFFFFF0 * user.mbb) % 0xFFFFFFFFFFFFFFFFFFFFFFF))
        user.device_client_ip = Mobile.ip()
        user.device_os = Mobile.device_os()
        user.is_cracked = Mobile.is_cracked()
        user.connection_type = Mobile.connection_type()
        user.imei = Mobile.imei(from_imei, to_imei)
        user.carrier = Mobile.carrier()
        user.operation = Mobile.operation()
        # user.insert_date
        user.is_success = 1
        user.msisdn = '9' + user.device_client_id
        # user.user_code
        # user.smartphone_device_client_id

        user_file.write(json.dumps(user) + os.linesep)

        for result in Mimic.generate(count=result_per_user):
            record_date = DateTime.between_ts(insert_dt.timestamp(), to_ts)

            result.record_date = record_date.isoformat()
            result.mbb = user.mbb
            result.device_uid = user.imei
            result.query_name = switch_query(random.randint(1, 100))
            result.source = random.choice(["AB", "AF"])

            package_list = [packagen.packages[random.randint(0, len_packages - 1)]]
            if probably(15 / 100):
                package_list.append(packagen.packages[random.randint(0, len_packages - 1)])
            result.package_list = ','.join(package_list)

            result.device_client_id = user.device_client_id
            result.device_info = user.device_os

            result_file.write(json.dumps(result) + os.linesep)

    user_file.close()
    result_file.close()

    os.rename(result_file_gen_ext, result_file_load_ext)
    os.rename(user_file_gen_ext, user_file_load_ext)

    took = time.time() - start_time
    speed = user_count / took

    print(
        f"Generated user data: {user_count}, result data: {user_count}x{result_per_user}={result_per_user * user_count}\n"
        f"Time: {took}. Speed: {round(speed)} users/sec.")


if __name__ == '__main__':
    generate_data()
