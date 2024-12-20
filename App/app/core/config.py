import environ

env = environ.Env()

# Load .env file
environ.Env.read_env()

class Settings:
    CELERY_BROKER_URL: str = env("RABBITMQ_BROKER_URL")
    CELERY_RESULT_BACKEND: str = env("RABBITMQ_BACKEND_URL")

settings = Settings()