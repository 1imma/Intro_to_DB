import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost:3306",
            user="root",  
            password="mr1President"  
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create the database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            # Print success message
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        # Print error message if connection or creation fails
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

# Run the function to create the database
create_database()
