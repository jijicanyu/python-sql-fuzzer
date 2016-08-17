import MySQLdb


HOST = 'localhost'
USER = 'root'
PASSWD = 'root'
DB = 'test'


raw = [chr(i) for i in range(32, 49)]
raw.extend([chr(i) for i in range(58, 66)])
raw.extend([chr(i) for i in range(91, 98)])
raw.extend([chr(i) for i in range(123, 127)])
raw.extend(['N', 'e'])
print raw
conn = MySQLdb.connect(host=HOST, user=USER, passwd=PASSWD, db=DB)


def three():
    count = 0
    for i in range(len(raw)):
        for j in range(len(raw)):
            for k in range(len(raw)):
                cursor = conn.cursor()
                SQL_QUERY = 'select 1[1]union select 1 from good where 1 limit 1;'
                payload = raw[i] + raw[j] + raw[k]
                SQL_QUERY = SQL_QUERY.replace('[1]', payload)
                try:
                    cursor.execute(SQL_QUERY)
                    print SQL_QUERY
                    count += 1
                    cursor.close()  # must close
                except:
                    pass
    print count


if __name__ == '__main__':
    three()