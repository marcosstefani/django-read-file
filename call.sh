curl \
 -X PUT "http://127.0.0.1:8000/file/" \
 -H "Accept: application/json" \
 -H "Content-Type: multipart/form-data" \
 -F "text=./file.txt;type=text/plain" \
