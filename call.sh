#!/bin/bash
set -e

line=$(curl -X PUT "http://127.0.0.1:8000/file/" -H "Accept: application/json" -H "Content-Type: multipart/form-data" -F "text=@file.txt;type=text/plain" | jq -r '.line')
highest_occurrence=$(curl -X PUT "http://127.0.0.1:8000/file/" -H "Accept: application/json" -H "Content-Type: multipart/form-data" -F "text=@file.txt;type=text/plain" | jq -r '.highest_occurrence')

CREATE="
CREATE TABLE IF NOT EXISTS reading (
    id SERIAL PRIMARY KEY,
    line varchar(10000) NOT NULL,
    highest_occurrence varchar(1) NOT NULL
);

INSERT INTO reading(line, highest_occurrence)
VALUES ('${line}', '${highest_occurrence}');"

docker exec -it db-read-file sh -c "psql -U postgres -d postgres -c \"$CREATE\" ";

SELECT="SELECT * FROM reading;"
docker exec -it db-read-file sh -c "psql -U postgres -d postgres -c \"$SELECT\" ";