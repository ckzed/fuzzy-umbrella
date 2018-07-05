SPEEDTEST = ckzed-speedtest
GRAFANA = ckzed-grafana

all: build
	docker-compose up -d

run-host:
	docker run -d --net=host -p 3000:3000 --name grafana grafana/grafana:latest ||:
	docker run -d --net=host -p 8086:8086 --name influxdb -e INFLUXDB_DB=speedtest influxdb:latest ||:
	docker run -d --net=host  --name collector $(SPEEDTEST):latest

build: build-collector build-grafana

build-collector:
	docker build -f Dockerfile.collector -t $(SPEEDTEST):latest .

build-grafana:
	docker build -f Dockerfile.grafana -t $(GRAFANA):latest .
