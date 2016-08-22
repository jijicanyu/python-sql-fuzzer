import MySQLdb


HOST = 'localhost'
USER = 'root'
PASSWD = 'root'
DB = 'test'

<<<<<<< HEAD
# del ; and # incase of dis
raw = [chr(i) for i in range(32, 49)]  #49
raw.extend([chr(i) for i in range(58, 66)])
raw.extend([chr(i) for i in range(91, 98)])
raw.extend([chr(i) for i in range(123, 128)])
raw.extend([':','N', 'e'])
raw_del = ['#',';']
for i in raw_del:
    raw.remove(i)
=======

raw = [chr(i) for i in range(32, 49)]
raw.extend([chr(i) for i in range(58, 66)])
raw.extend([chr(i) for i in range(91, 98)])
raw.extend([chr(i) for i in range(123, 127)])
raw.extend(['N', 'e'])
>>>>>>> bd0803d69bd43a4f0aa55d45b00c22c4fdea8518
print raw
conn = MySQLdb.connect(host=HOST, user=USER, passwd=PASSWD, db=DB)


def three():
    count = 0
    for i in range(len(raw)):
        for j in range(len(raw)):
            for k in range(len(raw)):
                cursor = conn.cursor()
<<<<<<< HEAD
                SQL_QUERY = 'select schema_name from information_schema.schemata where[1]schema_name=\'information_schema\''
                # SQL_QUERY = SQL_QUERY.replace(r"'","\'")
=======
                SQL_QUERY = 'select 1[1]union select 1 from good where 1 limit 1;'
>>>>>>> bd0803d69bd43a4f0aa55d45b00c22c4fdea8518
                payload = raw[i] + raw[j] + raw[k]
                SQL_QUERY = SQL_QUERY.replace('[1]', payload)
                try:
                    cursor.execute(SQL_QUERY)
<<<<<<< HEAD
                    #if '#' in (raw[i],raw[j],raw[k]):
                    if 'information_schema' in cursor.fetchone()[0]:
                        with open('output','a') as f:
                            f.write(SQL_QUERY+'\n')
                        count += 1

=======
                    print SQL_QUERY
                    count += 1
>>>>>>> bd0803d69bd43a4f0aa55d45b00c22c4fdea8518
                    cursor.close()  # must close
                except:
                    pass
    print count


if __name__ == '__main__':
    three()