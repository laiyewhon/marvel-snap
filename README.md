# Marvel Snap

## Requirements

* Mac OS
* jq
* httpie
* date
* pyenv
* docker
* docker compose

```bash
# active virtual environment
source marvel-snap-py3/bin/activate
```

## Setup pyenv

```bash
pyenv install 3.10.6
pyenv activate 3.10.6 marvel-snap
```

## Pulling card database from marvelsnapzone.com

```bash
http https://marvelsnapzone.com/getinfo/\?searchtype\=cards\&searchcardstype\=true | jq '.success.cards' > marvel_snap.$(date +%Y%m%d_%H%M%S).json
```

## Starting the whole stack

```&bash
docker compose build
docker compose up -d
```

Getting jupyter url from docker logs

```&bash
docker logs marvel-snap-jupyterlab-1
```

## tldr

1. Build images `docker compose build`
2. Start containers `docker compose up -d`
3. Access jupyterlab notebook from the url retrieved from `docker logs marvel-snap-jupyterlab-1`
4. Download database from marvelsnap.io `database-download.ipynb`
5. Analyze data `marvel-snap.ipynb`

## References

1. [Kafdrop](http://localhost:9000/)
