from fastapi import APIRouter

router=APIRouter()

@router.get('/health')
def check_health():
    return "Progress tracking service is running"
