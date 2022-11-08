import strawberry
from .models import StaticPage


StaticPageTypeEnum = strawberry.enum(StaticPage.Type, name="StaticPageTypeEnum")
