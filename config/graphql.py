from strawberry.django.views import AsyncGraphQLView
from apps.country.dataloaders import (
    load_country_additonal_info,
    load_country_overviews,
    load_good_practices_count,
    load_figure_analysis,
)
from apps.good_practice.dataloaders import (
    load_gallery, load_good_practice_country,
    load_good_practice_image,
    load_good_practice_tags,
    load_good_practice_driver_of_displacement,
    load_good_practice_focus_area,
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
            'country_good_practice_loader': DataLoader(load_fn=load_good_practices_count),
            'country_overviews_loader': DataLoader(load_fn=load_country_overviews),
            'gallery_loader': DataLoader(load_fn=load_gallery),
            'good_practice_country_loader': DataLoader(load_fn=load_good_practice_country),
            'good_practice_image_loader': DataLoader(load_fn=load_good_practice_image),
            'good_practice_tags_loader': DataLoader(load_fn=load_good_practice_tags),
            'good_practice_driver_of_displacement_loader': DataLoader(load_fn=load_good_practice_driver_of_displacement),
            'good_practice_focus_area_loader': DataLoader(load_fn=load_good_practice_focus_area),
            'figure_analysis_loader': DataLoader(load_fn=load_figure_analysis),
        }
