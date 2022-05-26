from strawberry.django.views import AsyncGraphQLView
from apps.country.dataloaders import (
    load_country_additonal_info,
    load_country_overviews_load,
)
from apps.good_practice.dataloaders import (
    load_gallery, load_good_practice_country
)
from starlette.requests import Request
from starlette.responses import Response
from typing import Any, Optional
from strawberry.dataloader import DataLoader


class CustomAsyncGraphQLView(AsyncGraphQLView):

    async def get_context(self, request: Request, response: Optional[Response]) -> Any:
        return {
            'request': request,
            'country_additonal_loader': DataLoader(load_fn=load_country_additonal_info),
            'country_overviews_loader': DataLoader(load_fn=load_country_overviews_load),
            'gallery_loader': DataLoader(load_fn=load_gallery),
            'good_practice_country_loader': DataLoader(load_fn=load_good_practice_country)
        }
