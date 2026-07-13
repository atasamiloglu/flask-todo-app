class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:123456@localhost:5432/todo_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "your-secret-key"