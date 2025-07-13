import jwt
import datetime

payload = {
    "sub": "admin",             # username yang terdaftar di Airflow
    "role_name": "Admin",       # role-nya, harus valid di Airflow
    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # expired 1 jam
}

secret = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9"

token = jwt.encode(payload, secret, algorithm="HS256")
print(token)