#!/usr/bin/env bash

current_dir=$(dirname "$(readlink -f "$0")")
server_tcp_port=8082
workers_num=5
threads_per_worker=2

cd "$current_dir"/src && gunicorn --workers=$workers_num --threads=$threads_per_worker -b 0.0.0.0:$server_tcp_port main:app
