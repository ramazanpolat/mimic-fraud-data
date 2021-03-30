while true; do
  sleep 0.1
  file_count=$(ls output/*.load 2>/dev/null | wc -l)
  if [[ $file_count -gt 0 ]]; then
    for file in $(ls output/*.load 2>/dev/null); do
      if [[ "$file" == *user* ]]; then
        printf 'loading %s ...' "$file"
        #cat $file | docker run -i --rm --link ch1:ch1 yandex/clickhouse-client --host ch1 -q "insert into user(insert_time, user_detail_id, user_id, mbb, device_client_id, device_client_ip, device_os, is_cracked, connection_type, imei, carrier, operation, is_success,msisdn) FORMAT JSONEachRow"
        docker run -i --rm --link clickhouse:clickhouse yandex/clickhouse-client:20.8.12.2 --host clickhouse -q "insert into user_detail(user_detail_id,user_id,mbb,device_client_id,device_client_ip,device_os,is_cracked,connection_type,imei,carrier,operation,insert_date,insert_time,is_success,msisdn,type) FORMAT JSONEachRow" <$file
        echo "Loading $file..."
        sleep 1
        printf 'done.\n'
      fi

      if [[ "$file" == *fraud* ]]; then
        printf 'loading %s ...' "$file"
        docker run -i --rm --link clickhouse:clickhouse yandex/clickhouse-client:20.8.12.2 --host clickhouse -q "insert into fraud_result(record_date,mbb,device_uid,query_name,source,package_list,device_client_id,device_info,type) FORMAT JSONEachRow" <$file
        #cat $file | docker run -i --rm --link ch1:ch1 yandex/clickhouse-client --host ch1 -q "insert into result(record_date, device_uid, query_name, source, package_list, device_client_id, device_info) FORMAT JSONEachRow"
        echo "Loading $file..."
        sleep 1
        printf 'done.\n'
      fi
      echo "deleting $file"
      #mv $file $file.ok
      rm -rf $file
      sleep 0.1
    done
  fi
done
