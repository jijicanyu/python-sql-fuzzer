import MySQLdb


HOST = 'localhost'
USER = 'root'
PASSWD = 'root'
DB = 'test'

# del ; and # incase of dis
raw = [chr(i) for i in range(32, 49)]  #49
raw.extend([chr(i) for i in range(58, 66)])
raw.extend([chr(i) for i in range(91, 98)])
raw.extend([chr(i) for i in range(123, 128)])
raw.extend([':','N', 'e'])
raw_del = ['#',';']
for i in raw_del:
    raw.remove(i)
print raw
conn = MySQLdb.connect(host=HOST, user=USER, passwd=PASSWD, db=DB)


def three():
    count = 0
    for i in range(len(raw)):
        for j in range(len(raw)):
            for k in range(len(raw)):
                cursor = conn.cursor()
                SQL_QUERY = 'select schema_name from information_schema.schemata where[1]schema_name=\'information_schema\''
                # SQL_QUERY = SQL_QUERY.replace(r"'","\'")
                payload = raw[i] + raw[j] + raw[k]
                SQL_QUERY = SQL_QUERY.replace('[1]', payload)
                try:
                    cursor.execute(SQL_QUERY)
                    #if '#' in (raw[i],raw[j],raw[k]):
                    if 'information_schema' in cursor.fetchone()[0]:
                        with open('output','a') as f:
                            f.write(SQL_QUERY+'\n')
                        count += 1

                    cursor.close()  # must close
                except:
                    pass
    print count


if __name__ == '__main__':
    three()