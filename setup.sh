#!/usr/bin/env bash


key=$(curl -s -X POST -H "Content-Type: application/json" -d '{"name":"apikeycurl14", "role": "Admin"}' "http://admin:Tom03042003@192.168.58.3:3000/api/auth/keys" | jq -r ".key") 
curl -X POST --insecure -H "Authorization: Bearer ${key}" -H "Content-Type: application/json" -d @InfluxDB.json  http://192.168.58.3:3000/api/datasources
curl -X POST --insecure -H "Authorization: Bearer ${key}" -H "Content-Type: application/json" -d @DashboardBitcoin.json  http://192.168.58.3:3000/api/dashboards/db
