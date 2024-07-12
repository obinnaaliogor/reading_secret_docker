import os

def read_secret(secret_name):
    secret_path = f'/run/secrets/{secret_name}'
    try:
        with open(secret_path, 'r') as secret_file:
            return secret_file.read().strip()
    except IOError:
        return None

# Read environment variables
myenv = os.getenv("password") or read_secret("password")
my_db_name = os.getenv("DB_NAME") or read_secret("DB_NAME")

print("My Password is:", myenv)
print("Database Name:", my_db_name)
