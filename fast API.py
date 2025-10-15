from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional



class UserRole(str, Enum):
    """نقش‌های ثابت برای کاربران."""
    admin = "مدیر"
    customer = "مشتری"
    editor = "ویرایشگر"

class User(BaseModel):
    id: int
    full_name: str
    phone_number: str
  
    roles: UserRole

class Product(BaseModel):
    id: int
    name: str
    price: float
    details: str
    sale_count: int
    
class film(BaseModel):
    id: int
    name: str
    categories: str  
    duration: float 

fake_users_db: List[User] = [
    User(id=1, full_name="آريا اکبري", phone_number="09906543391", roles=UserRole.admin),
    User(id=2, full_name="امیر کریمی", phone_number="09345678234", roles=UserRole.customer),
    User(id=3, full_name="سارا حديث", phone_number="09193341489", roles=UserRole.editor),
]

fake_products_db: List[Product] = [
    Product(id=1, name=" مکانیکی", price=99.99, details="کیبورد گیمینگ RGB با نورپردازی", sale_count=150),
    Product(id=2, name="کنسول", price=25.50, details="با حجم 1070G",sale_count=500),
    Product(id=3, name="مانیتور 27 اینچ", price=450.00, details="نمایشگر 4K با نرخ نوسازی 144Hz", sale_count=80),
]

fake_film_db: List[Podcast] = [
    Podcast(id=1, name="ميان ستاره اي", categories="اکشن,علمي-تخيلي,حماسي", duration=45.5),
    Podcast(id=2, name="روح", categories="کمدي,حماسي", duration=60.0),
    Podcast(id=3, name="اجل معلق", categories="کمدي,علمي", duration=30.2),
]


app = FastAPI(title="Multi-Table Fake DB Example", description="مثالی از سه مدل داده‌ای با Pydantic و Enum")

@app.get("/users", response_model=List[User], summary="دریافت لیست کاربران")
def get_users(role: Optional[UserRole] = None):
    """لیست کاربران را بر اساس نقش (اختیاری) فیلتر می‌کند."""
    if role:
        return [u for u in fake_users_db if u.roles == role]
    return fake_users_db

@app.get("/products", response_model=List[Product], summary="دریافت لیست محصولات")
def get_products():
    """همه محصولات را برمی‌گرداند."""
    return fake_products_db

@app.get("/podcasts", response_model=List[Podcast], summary="دریافت لیست پادکست‌ها")
def get_podcasts():
    """همه پادکست‌ها را برمی‌گرداند."""
    return fake_podcasts_db
