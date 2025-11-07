from fastapi import FastAPI
import pymysql 

app= FastAPI()

@app.get("/")
def read_root():
    return f"hello Api"



def get_db_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="campus_db")

@app.get("/check_db")
def connect_to_db():
    try:
        connection = get_db_connection()
        if connection.open:
            connection.close()
            return{"status":"Database connected successfull"}
        else:
             return{"status":"Database  is not connected successfull"}
        
    except Exception as e:
        return {"error": str(e)}


@app.post("/create_table")
def create_table():
    try:
        connection = get_db_connection()
       
        cursor = connection.cursor()
        create_table = """
        CREATE TABLE IF NOT EXISTS api (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100),
            age INT
        )
        """
        cursor.execute(create_table)
        connection.commit()
        cursor.close()
        connection.close()
        return "Table 'hars' created successfully"
    except Exception as e:
        return f"Error: {e}"
    


@app.post("/show_databases")
def show_databases():
    try:
        connection = get_db_connection()
       
        cursor = connection.cursor()
       
        cursor = connection.cursor()
        cursor.execute("SHOW DATABASES;")
        databases = cursor.fetchall()
        cursor.close()
        connection.close()
        return {"databases": databases}
    except Exception as e:
        return f"Error: {e}"


@app.post("/insert_data")
def insert_data(name:str, email:str, age:int):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        insert_query = """
        INSERT INTO api (name, email, age)
        VALUES (%s, %s, %s)
        """
        cursor.execute(insert_query, (name, email, age))
        connection.commit()
        cursor.close()
        connection.close()
        return {"message": "Data inserted successfully"}
    except Exception as e:
        return {"error": str(e)}
    

@app.delete("/delete_database")
def delete_database(db_name: str):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(f"DROP DATABASE IF EXISTS {db_name}")
        connection.commit()
        cursor.close()
        connection.close()

        return {"message": f"Database '{db_name}' deleted successfully"}
    except Exception as e:
        return {"error": str(e)}


@app.get("/fetch_data")
def fetch_data():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM api")
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        return {"data": rows}

    except Exception as e:
        return {"error": str(e)}


@app.put("/update_data")
def update_data(id: int, name: str = None, email: str = None, age: int = None):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        update_query = "UPDATE api SET name=%s, email=%s, age=%s WHERE id=%s"
        cursor.execute(update_query, (name, email, age, id))
        connection.commit()
        cursor.close()
        connection.close()
        return {"message": f"Record with ID {id} updated successfully"}
    except Exception as e:
        return {"error": str(e)}
