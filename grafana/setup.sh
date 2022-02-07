#!/usr/bin/env bash


key=$(curl -s -X POST -H "Content-Type: application/json" -d '{"name":"apikeycurl", "role": "Admin"}' "http://admin:Tom03042003@localhost:3000/api/auth/keys" | jq -r ".key") 
curl -X POST --insecure -H "Authorization: Bearer ${key}" -H "Content-Type: application/json" -d @InfluxDB.json http://localhost:3000/api/datasources
uid=$(curl -s -X GET --insecure -H "Authorization: Bearer ${key}" -H "Content-Type: application/json" http://localhost:3000/api/datasources/1 | jq -r '.uid')
sed -i "s/DBUID/${uid}/g" DashboardBitcoin.json
curl -X POST --insecure -H "Authorization: Bearer ${key}" -H "Content-Type: application/json" -d @DashboardBitcoin.json http://localhost:3000/api/dashboards/db
uid=$(curl -s -X POST --insecure -H "Authorization: Bearer ${key}" -H "Content-Type: application/json" -d @baseprom.json http://localhost:3000/api/datasources | jq -r '.datasource.uid')
sed -i "s/UID/${uid}/g" finalprom.json
curl -s -X PUT --insecure -H "Authorization: Bearer ${key}" -H "Content-Type: application/json" -d @finalprom.json  http://localhost:3000/api/datasources/2
curl -X POST --insecure -H "Authorization: Bearer ${key}" -H "Content-Type: application/json" -d @Prometheus.json http://localhost:3000/api/dashboards/db
