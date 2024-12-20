from fastapi import APIRouter
from app.services.notification_tasks import send_notification

router = APIRouter()

@router.post("/notify")
async def notify(user_id: int, message: str):
    task = send_notification.delay(user_id, message)
    return {"task_id": task.id, "status": "Notification scheduled"}