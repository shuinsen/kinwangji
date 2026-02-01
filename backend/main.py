from datetime import datetime, timedelta

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from wanji import display_pan, gangzhi

app = FastAPI(title="Wangji API")

# Allow cross-origin requests for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

element_map = {
    "甲": "wood", "乙": "wood",
    "丙": "fire", "丁": "fire",
    "戊": "earth", "己": "earth",
    "庚": "metal", "辛": "metal",
    "壬": "water", "癸": "water",
}

element_info = {
    "wood": ("東方", "綠色"),
    "fire": ("南方", "紅色"),
    "earth": ("中央", "黃色"),
    "metal": ("西方", "白色"),
    "water": ("北方", "黑色"),
}


@app.get("/fortune")
async def fortune(year: int, month: int, day: int, hour: int, minute: int = 0):
    """Return divination result for the next day of the given datetime."""
    try:
        dt = datetime(year, month, day, hour, minute)
        next_day = dt + timedelta(days=1)
        pan = display_pan(next_day.year, next_day.month, next_day.day, next_day.hour, next_day.minute)
        gz = gangzhi(next_day.year, next_day.month, next_day.day, next_day.hour, next_day.minute)
        stem = gz[2][0]  # Day heavenly stem
        elem = element_map.get(stem)
        direction, color = element_info.get(elem, ("未知", "未知"))
    except Exception as exc:  # pragma: no cover - defensive
        raise HTTPException(status_code=400, detail=str(exc))
    return {"pan": pan, "direction": direction, "color": color}
