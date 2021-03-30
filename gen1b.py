import hashlib
import click
import json
import os
import time
import random
from prodict import Prodict

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
@click.argument('user_count', type=int, default=150)
@click.argument('fraud_count', type=int, default=50)
@click.argument('start_year', type=int, default=2017)
@click.argument('end_year', type=int, default=2021)
@click.argument('user_start', type=int, default=0)
@click.argument('user_data_per_device', type=int, default=67)
def generate_data(user_count=150, fraud_count=50, start_year=2017, end_year=2021, user_start=0,
                  user_data_per_device=67):
    print(f'Generating {user_count} data. Offset: {user_start}')
    switch_query = Switch(between_table)

    from_ts = int(datetime(start_year, 1, 1).timestamp())
    to_ts = int(datetime(end_year, 1, 1).timestamp())

    len_packages = len(packagen.packages)

    seed = 5301000000
    user_seed = seed + user_start

    file_id = f"{int(time.time())}-{random.randint(1000, 9999)}"

    print(f"File id: {file_id}")

    user_file_gen_ext = f'./output/{file_id}-user.gen'
    user_file_load_ext = f'./output/{file_id}-user.load'

    fraud_file_gen_ext = f'./output/{file_id}-fraud.gen'
    fraud_file_load_ext = f'./output/{file_id}-fraud.load'

    user_file = open(user_file_gen_ext, 'w')
    fraud_file = open(fraud_file_gen_ext, 'w')

    random.seed(0)

    for ix, base in enumerate(Mimic.generate(count=user_count)):
        user_seed += 1
        user_seed_str = str(user_seed)

        base.type = 'user_detail'
        base.user_detail_id = user_seed
        base.user_id = 9999999999 - user_seed
        base.mbb = user_seed
        base.device_client_id = hashlib.sha512(user_seed_str.encode()).hexdigest()
        base.imei = hashlib.md5(user_seed_str.encode()).hexdigest().upper()[:15]
        base.msisdn = str(9055500000 + base.mbb * pow(10, 10))

        for user in Mimic.generate(count=user_data_per_device):
            insert_dt = DateTime.between_ts(from_ts, to_ts)

            user.insert_date = str(insert_dt.date())
            user.insert_time = insert_dt.isoformat()

            user.type = base.type

            user.user_detail_id = base.user_detail_id  # static
            user.user_id = base.user_id  # static
            user.mbb = base.mbb  # static
            user.device_client_id = base.device_client_id  # static
            user.device_client_ip = Mobile.ip()
            user.device_os = Mobile.device_os()
            user.is_cracked = Mobile.is_cracked()
            user.connection_type = Mobile.connection_type()
            user.imei = base.imei  # static
            user.carrier = Mobile.carrier()
            user.operation = Mobile.operation()
            user.is_success = Mobile.is_success()
            user.msisdn = base.msisdn
            user_file.write(json.dumps(user) + os.linesep)
            # print(user)

        if user_seed - seed < fraud_count:
            fraud = Prodict()
            record_date = DateTime.between_ts(from_ts, to_ts)

            fraud.type = 'fraud_result'
            fraud.record_date = str(record_date.date())
            fraud.mbb = base.mbb
            fraud.device_uid = base.imei.lower()
            fraud.query_name = switch_query(random.randint(1, 100))
            fraud.source = random.choice(["AB", "AF"])

            # package_list = [packagen.packages[random.randint(0, len_packages - 1)]]
            # if probably(5 / 100):
            #     package_list.append(packagen.packages[random.randint(0, len_packages - 1)])
            # fraud.package_list = ','.join(package_list)
            fraud.package_list = packagen.packages[random.randint(0, len_packages - 1)]

            fraud.device_client_id = base.device_client_id
            fraud.device_info = Mobile.device_os()
            fraud_file.write(json.dumps(fraud) + os.linesep)

    print('Done.')
    user_file.close()
    fraud_file.close()
    os.rename(fraud_file_gen_ext, fraud_file_load_ext)
    os.rename(user_file_gen_ext, user_file_load_ext)


if __name__ == '__main__':
    generate_data()
