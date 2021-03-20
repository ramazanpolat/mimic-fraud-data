

while true
do
	sleep 0.1
	file_count=$(ls *.load 2> /dev/null | wc -l)
	if [[ $file_count -gt 0 ]]
	then
		for file in $(ls *.load 2>/dev/null)
		do
			if [[ "$file" == *user* ]]
			then
				printf 'loading %s ...' "$file"
				cat $file | docker run -i --rm --link ch1:ch1 yandex/clickhouse-client --host ch1 -q "insert into user(insert_time, user_detail_id, user_id, mbb, device_client_id, device_client_ip, device_os, is_cracked, connection_type, imei, carrier, operation, is_success,msisdn) FORMAT JSONEachRow"
				printf 'done.\n'
			fi

			if [[ "$file" == *result* ]]
      then
        printf 'loading %s ...' "$file"
        cat $file | docker run -i --rm --link ch1:ch1 yandex/clickhouse-client --host ch1 -q "insert into result(record_date, device_uid, query_name, source, package_list, device_client_id, device_info) FORMAT JSONEachRow"
        printf 'done.\n'
      fi
			echo "deleting $file"
			#mv $file $file.ok
			rm -rf $file
			sleep 0.1
		done
	fi
done
