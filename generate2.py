import multiprocessing
import subprocess
import time
import click


@click.command()
@click.argument('data_count', type=int, default=3000)
@click.argument('process_count', type=int, default=2)
def parallel_gen(data_count, process_count=None):
    print('data_count:', data_count)
    if process_count == 0:
        process_count = multiprocessing.cpu_count() // 2

    print(f'Using {process_count} processes.')
    count_for_each = round(data_count / process_count)

    print('count_for_each:', count_for_each)

    total_count = 0
    i = 0
    while total_count < data_count:
        i += 1
        print(f'=== BATCH {i} === count_for_each: {count_for_each}')
        command = ["python", "generate.py", f"{count_for_each}", f"{process_count}"]
        print('command:', command)
        sub = subprocess.Popen(command)
        sub.wait()
        total_count += count_for_each
        time.sleep(1)

    print('All jobs finished.')


if __name__ == '__main__':
    parallel_gen()
