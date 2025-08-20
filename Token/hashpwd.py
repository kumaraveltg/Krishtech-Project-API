from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

def hass_password(password: str) :
    return pwd_context.hash(password)

def verify_hasspassword(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password,hashed_password)
