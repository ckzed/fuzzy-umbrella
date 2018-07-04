# Internet Monitor

## Purpose

Monitor the internet bandwidth using [speedtest](http://www.speedtest.net/).

## Plan

We install grafana on influxdb docker instance and a script in the cronjob which
would run the speedtest and inject the current speeds into influxdb.
