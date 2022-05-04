from strawberry.django.views import AsyncGraphQLView
from apps.country.dataloaders import (
    load_country_additonal_info,
    load_country_overviews_load,
    load_country_contact_persons,
    load_country_essential_links,
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
            'country_contact_persons_loader': DataLoader(load_fn=load_country_contact_persons),
            'country_essential_links_loader': DataLoader(load_fn=load_country_essential_links),
        }
