import logging
from typing import Any, Optional, Union

import osmnx

from .draw import plot, multiplot, create_preset, delete_preset, preset, presets

"""
What would I like from an interface:

1. Query by location name string or pair of coordinates (exists)
2. Separate entrypoints for radius fetching and whole region fetching.
3. Separate fetch and plot into two very easy to run commands.

"""

_LOGGER = logging.getLogger(__name__)

# --- Public -------------------------------------


def fetch_by_radius(
    query: Union[str, tuple[float, float]],
    radius: int,  # Of what unit?
    layers: Optional[dict[str, Any]] = None,  # TODO: Get the right typing here
    style: Optional[dict[str, Any]] = None,  # TODO: Get the right typing here
    preset: str = "default",
    circle: bool = False,
    **kwargs,
):
    """
    Fetch data from OSM through a query and a radius.
    """

    if layers is None:
        layers = {}
    if style is None:
        style = {}

    try:
        return plot(
            query,
            layers=layers,
            style=style,
            preset=preset,
            save_preset=False,
            update_preset=False,
            postprocessing=None,
            circle=circle,
            radius=radius,
            dilate=None,
            save_as=None,
            title=None,
            figsize=(12, 12),
            constrained_layout=True,
            multiplot=False,
            show=False,
            **kwargs,
        )
    except (osmnx._errors.EmptyOverpassResponse, ValueError):
        _LOGGER.error(f'Likely could not find "{query}". Ending.')
        raise


def fetch_by_region():
    pass
