while true; do
  sleep 0.1
  file_count=$(ls output/*.load 2>/dev/null | wc -l)
  if [[ $file_count -gt 0 ]]; then
    for file in $(ls output/*.load 2>/dev/null); do
      if [[ "$file" == *user* ]]; then
        printf 'loading %s ...' "$file"
        # asagidaki satiri kendinize gore degistiriniz
        docker run -i --rm --link clickhouse:clickhouse yandex/clickhouse-client --host clickhouse -q "insert into user_detail(user_detail_id,user_id,mbb,device_client_id,device_client_ip,device_os,is_cracked,connection_type,imei,carrier,operation,insert_date,insert_time,is_success,msisdn,type) FORMAT JSONEachRow SETTINGS max_insert_threads=16" < $file
        printf 'done.\n'
        sleep 0.1
      fi

      if [[ "$file" == *fraud* ]]; then
        printf 'loading %s ...' "$file"
        # asagidaki satiri kendinize gore degistiriniz
        docker run -i --rm --link clickhouse:clickhouse yandex/clickhouse-client --host clickhouse -q "insert into fraud_result(record_date,mbb,device_uid,query_name,source,package_list,device_client_id,device_info,type) FORMAT JSONEachRow SETTINGS max_insert_threads=16" < $file
        printf 'done.\n'
        sleep 0.1
      fi
      echo "deleting $file"
      #mv $file $file.ok
      rm -rf $file
      sleep 0.1
    done
  fi
done
