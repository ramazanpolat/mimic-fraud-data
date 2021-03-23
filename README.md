# mimic-fraud-data

Mimic fraud data bank

## requirements

* Python 3.8
* `pip3.8 install -r requirements.txt`
* `chmod a+x loader.sh`

## generate data

`python3.8 generate.py DATA_COUNT PROCESS_COUNT`

E.g:

```bash
$ python3.8 generate.py 3000000 10

data_count: 300000
Using 4 processes.
count_for_each: 75000
1-> python gen-cb.py 75000
command: ['python', 'gen-cb.py', '75000', '15']
data_count: 75000
user_count: 5000
result_per_user: 15
File id: 1616268098-4196
2-> python gen-cb.py 75000
command: ['python', 'gen-cb.py', '75000', '15']
data_count: 75000
user_count: 5000
result_per_user: 15
File id: 1616268099-7064
3-> python gen-cb.py 75000
command: ['python', 'gen-cb.py', '75000', '15']
data_count: 75000
user_count: 5000
result_per_user: 15
File id: 1616268100-1813
4-> python gen-cb.py 75000
command: ['python', 'gen-cb.py', '75000', '15']
data_count: 75000
user_count: 5000
result_per_user: 15
File id: 1616268101-6989
Generated user data: 5000, result data: 5000x15=75000
Time: 3.3086609840393066. Speed: 1511 users/sec.
All jobs finished.
Press ENTER to exit.
Generated user data: 5000, result data: 5000x15=75000
Time: 3.318495988845825. Speed: 1507 users/sec.
Generated user data: 5000, result data: 5000x15=75000
Time: 3.2984821796417236. Speed: 1516 users/sec.
Generated user data: 5000, result data: 5000x15=75000
Time: 3.314347505569458. Speed: 1509 users/sec.
```

## load data

`./loader.sh`

# Docker

docker pull ramazanpolat/mimic-fraud-data:v1

mkdir -p mimic/output
cd mimic
MIMIC=$(pwd)
cd output
OUTPUT=$(pwd)
cd ..

-> NEW WINDOW
docker run -it --rm --name=mimic ramazanpolat/mimic-fraud-data:v1 bash

-> OLD WINDOW
docker copy mimic:/app/loader.sh $MIMIC

docker run -it -v $OUTPUT:/app/output ramazanpolat/mimic-fraud-data:v1 python generate.py 100 4
