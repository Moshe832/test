
while true
do
  echo -n "$(date '+%F %T')," >> latency.csv

  curl -o /dev/null -s \
       -w "%{http_code},%{time_connect},%{time_starttransfer},%{time_total}\n" \
       https://your-api >> latency.csv

  sleep 5
done