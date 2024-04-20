from werkzeug.security import generate_password_hash
import sqlite3

# Assuming you're using the schema provided
DATABASE = 'verification_results.db'

def create_admin_user(username, password):
    # Connect to the database
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()

    # Hash the password for secure storage
    hashed_password = generate_password_hash(password)

    # Insert the new admin user
    cur.execute("INSERT INTO user (username, password, is_admin) VALUES (?, ?, ?)",
                (username, hashed_password, True))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    print(f"Admin user '{username}' created successfully.")

if __name__ == "__main__":
    # admin_username = input("Enter admin username: ")
    # admin_password = input("Enter admin password: ")/Users/kk/Documents/code/checkAppleID/Dockerfile
    admin_username = "admin"
    admin_password = "passwd"
    create_admin_user(admin_username, admin_password)
