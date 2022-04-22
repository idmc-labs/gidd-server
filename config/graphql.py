from strawberry.django.views import AsyncGraphQLView
from apps.country.dataloaders import load_country_additonal_info
from starlette.requests import Request
from starlette.responses import Response
from typing import Any, Optional
from strawberry.dataloader import DataLoader


class CustomAsyncGraphQLView(AsyncGraphQLView):

    async def get_context(self, request: Request, response: Optional[Response]) -> Any:
        return {
            "country_additonal_loader": DataLoader(load_fn=load_country_additonal_info)
        }