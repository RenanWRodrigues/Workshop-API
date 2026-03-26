import psycopg2


class PostgreSQLConnectionL:
    def __init__(self, dbmname, user, password, host='localhost', port='5432'):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None


    def connect(self):
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            print("Connection to PostgreSQL database established successfully.")
        except psycopg2.Error as e:
            print(f"Error connecting to PostgreSQL database: {e}")

    def select_user(self, query):
        if not self.conn:
            print("Você não está conectado ao banco de dados.")
            return None
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            return rows
        except psycopg2.Error as e:
            print(f"Error executing query: {e}")
            return None

        

    def insert_user(self, id, name, area, job_description, role, salary, is_active, last_evaluation):
        if not self.conn:
            print("Você não está conectado ao banco de dados.")
            return None
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO users (id, name, area, job_description, role, salary, is_active, last_evaluation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (user.id, user.name, user.email))
            self.conn.commit()
            cursor.close()
            print("User inserted successfully.")
        except psycopg2.Error as e:
            print(f"Error inserting user: {e}")
            return None

    def delete_user(self, user_id: int):
        if not self.conn:
            print("Você não está conectado ao banco de dados.")
            return None
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
            self.conn.commit()
            cursor.close()
            print("User deleted successfully.")
        except psycopg2.Error as e:
            print(f"Error deleting user: {e}")
            return None

    def update_user(self, user_id: int, user: User):
        if not self.conn:
            print("Você não está conectado ao banco de dados.")
            return None
        try:
            cursor = self.conn.cursor()
            cursor.execute("UPDATE users SET name = %s, area = %s, job_description = %s, role = %s, salary = %s, is_active = %s, last_evaluation = %s WHERE id = %s",
                           (user.name, user.area, user.job_description, user.role, user.salary, user.is_active, user.last_evaluation, user_id))
            self.conn.commit()
            cursor.close()
            print("User updated successfully.")
        except psycopg2.Error as e:
            print(f"Error updating user: {e}")
            return None


    def update_user(self, id, name=None, job_description=None, role=None, salary=None, is_active=None, last_evaluation=None):
        if not self.conn:
            print("Você não está conectado ao banco de dados.")
            return None
        
        try:
            cursor = self.conn.cursor()
            update_query = "UPDATE user SET"
            update_values = []

            if name is not None:
                update_query += " name = %s,"
                update_values.append(name)


            if area is not None:
                update_query += " area = %s,"
                update_values.append(area)


            if job_description is not None:
                update_query += " job_description = %s,"
                update_values.append(job_description)


            if role is not None:
                update_query += " role = %s,"
                update_values.append(role)

            if salary is not None:
                update_query += " salary = %s,"
                update_values.append(salary)

            if is_active is not None:
                update_query += " is_active = %s,"
                update_values.append(is_active)

            if last_evaluation is not None:
                update_query += " last_evaluation = %s,"
                update_values.append(last_evaluation)
            update_query = update_query.rstrip(',') + " WHERE id = %s"
            update_values.append(id)

            cursor.execute(update_query, tuple(update_values))
            self.conn.commit()
            cursor.close()
            print("Usuário Atualizado")
        except psycopg2.Error as e:
            print(f"Error updating user: {e}")
            return None


    
    def close(self):
        if self.conn:
            self.conn.close()
            print("Conexão Encerrada!")
