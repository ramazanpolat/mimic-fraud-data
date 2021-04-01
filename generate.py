import multiprocessing
import subprocess
import time
import click


@click.command()
@click.argument('user_count', type=int, default=15000000)
@click.argument('batch_size', type=int, default=1000000)
@click.argument('process_count', type=int, default=8)
def parallel_gen(user_count, batch_size, process_count):
    print('user_count:', user_count)
    if process_count == 0:
        process_count = multiprocessing.cpu_count() // 2

    print(f'Using {process_count} processes.')
    count_for_each = round(batch_size / process_count)

    print('count_for_each:', count_for_each)

    fraud_count = 50_000
    start_year = 2017
    end_year = 2021
    user_start = 0
    user_data_per_device = 67
    batch_id = 1
    while user_start + batch_size < user_count:
        print(f'=== BATCH {batch_id} ===')
        sub = None
        for i in range(process_count):
            print(
                f'{i + 1}-> python gen1b.py {count_for_each} {fraud_count} {start_year} {end_year} {user_start} {user_data_per_device}')
            command = ['python', 'gen1b.py', f'{count_for_each}', f'{fraud_count}', f'{start_year}', f'{end_year}',
                       f'{user_start}', f'{user_data_per_device}']
            print('command:', command)
            sub = subprocess.Popen(command)
            user_start += count_for_each
            time.sleep(0.1)

        if sub:
            print('WAIT for data generation to finish...')
            sub.wait()
            time.sleep(1)
            print(f'-> BATCH {batch_id} finished.')
            batch_id += 1

    print('All jobs finished.')


if __name__ == '__main__':
    parallel_gen()
