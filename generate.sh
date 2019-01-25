curl -H "content-Type: application/json" -X GET -d "$(jq . generate.json)" localhost:5000/generate | \
    jq '.submission_str = .display_str' > output.json

