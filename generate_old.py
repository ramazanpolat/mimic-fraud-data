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

    sub = None
    for i in range(process_count):
        print(f'{i + 1}-> python gen-cb.py {count_for_each}')
        command = ["python", "gen-cb.py", f"{count_for_each}", "15"]
        print('command:', command)
        sub = subprocess.Popen(command)
        time.sleep(1)

    if sub:
        print('WAIT for data generation to finish...')
        sub.wait()
        time.sleep(1)

    print('All jobs finished.')


if __name__ == '__main__':
    parallel_gen()
