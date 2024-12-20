from app.core.celery_app import celery_app

@celery_app.task
def send_notification(user_id: int, message: str):
    # Aquí pondrías tu lógica de envío
    return f"Notification sent to user {user_id} with message: {message}"