# mysql+pymysql://<username>:<password>@<hostname>/<database>
DATABASE_URL = "mysql+pymysql://hasan:1111@localhost/fastapi"
# python -c "import secrets; print(secrets.token_hex(32))"
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
