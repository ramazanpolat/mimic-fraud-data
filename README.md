# mimic-fraud-data

Mimic bank fraud data

## requirements

* Python 3.8
* `pip3.8 install -r requirements.txt`
* `chmod a+x loader.sh`

*Note*: We only need 2 packages:

* `pip install prodict`
* `pip install click`

## generate data

```bash
$ python3.8 generate.py --help
Usage: generate.py [OPTIONS] [USER_COUNT] [BATCH_SIZE] [PROCESS_COUNT]

Options:
  --help  Show this message and exit.
```

### recommended params

`python3.8 generate.py 15000000 1000000 8`

Generates 
* 1B user_detail rows
* 50K fraud_result rows
  
* 15M unique users in `user_detail`
* All dates are between `2017-01-01` and `2021-01-01`


## load data

`./loader.sh`

# docker

```bash
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

docker run -it -v $OUTPUT:/app/output ramazanpolat/mimic-fraud-data:v1 python generate_old.py 100 4
```

## In another window, start loading

```py
chmod
a + X
loader.sh
./ loader.sh
```

