import multiprocessing
import subprocess
import time
import click


@click.command()
@click.argument('total_data_count', type=int, default=30000)
@click.argument('batch_count', type=int, default=10000)
@click.argument('process_count', type=int, default=5)
def parallel_gen(total_data_count, batch_count, process_count=None):
    print('total_data_count:', total_data_count)
    print('batch_count:', batch_count)
    if process_count == 0:
        process_count = multiprocessing.cpu_count() // 2

    print(f'Using {process_count} processes.')
    count_for_each = round(batch_count / process_count)

    print('count_for_each:', count_for_each)

    total_counter = 0
    i = 0
    while total_counter < total_data_count:
        i += 1
        print(f'=== BATCH {i} === batch_count: {batch_count}')
        command = ["python", "generate_old.py", f"{batch_count}", f"{process_count}"]
        print('command:', command)
        sub = subprocess.Popen(command)
        sub.wait()
        total_counter += batch_count
        time.sleep(1)

    print('All jobs finished.')


if __name__ == '__main__':
    parallel_gen()
