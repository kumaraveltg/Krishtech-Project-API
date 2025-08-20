from datetime import datetime, timedelta
from jose import jwt
import secrets

key = secrets.token_hex(32)
print(key)

SECRET_KEY = key
ALGORITHM = "HS256"

def create_token():
    expire = datetime.utcnow() + timedelta(minutes=3)
    payload = {"exp": expire}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

# Run the function directly
if __name__ == "__main__":
    token = create_token()
    print("Generated Token:", token)
