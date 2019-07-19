#!/usr/bin/env bash
port=$1
url=$2

[[ -z $port ]] && port="5000"
[[ -z $url ]] && url="localhost"

curl -H "content-Type: application/json" -X GET -d "$(jq . generate.json)" $url:$port/generate | \
    jq '.submission_str = .display_str' > output.json

