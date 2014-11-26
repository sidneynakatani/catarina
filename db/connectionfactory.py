import psycopg2


class ConnectionFactory:



    def create(self):

        host = "host = 'ec2-54-197-241-82.compute-1.amazonaws.com'" 
        dbname = "dbname = 'dakr17pq1c5236'" 
        user = "user = 'tdvtpvxbzvxrqc'" 
        password = "password = 'GpTck_d1IKA2tv3lu-7JZEMR0F'"

        conn_string = " ".join([host, dbname, user, password])
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute('SELECT version()')          
        ver = cursor.fetchone()
	conn.close()

        return ver

