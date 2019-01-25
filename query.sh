
curl -H "content-Type: application/json" -X GET -d "$(jq . output.json)" localhost:5000/query/word_hints 
curl -H "content-Type: application/json" -X GET -d "$(jq . output.json)" localhost:5000/query/sentence_hints 
curl -H "content-Type: application/json" -X GET -d "$(jq . output.json)" localhost:5000/query/count_word_errors 
curl -H "content-Type: application/json" -X GET -d "$(jq . output.json)" localhost:5000/query/count_sentence_errors 
curl -H "content-Type: application/json" -X GET -d "$(jq . output.json)" localhost:5000/query/is_correct 
