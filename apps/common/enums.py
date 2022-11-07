from strawberry.enum import _process_enum
from .models import StaticPage

StaticPageTypeEnum = _process_enum(StaticPage.Type, "StaticPageTypeEnum", "Static page types")
