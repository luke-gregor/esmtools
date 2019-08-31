from .exceptions import CoordinateError
from .utils import check_xarray

# NOTE: Add testing
# NOTE: Compile docs for new API. Delete old functions.


@check_xarray(0)
def _convert_lon_to_180to180(ds, coord='lon'):
    """Convert from 0 to 360 (degrees E) grid to -180 to 180 (W-E) grid.

    .. note::
        Longitudes are not sorted after conversion (i.e., spanning -180 to 180 or
        0 to 360 from index 0, ..., N), as it is expected that the user will plot
        via ``cartopy``, ``basemap``, or ``xarray`` plot functions.

    Args:
        ds (xarray object): Dataset to be converted.
        coord (optional str): Name of longitude coordinate.

    Returns:
        xarray object: Dataset with converted longitude grid.
    """
    ds = ds.copy()
    lon = ds[coord].values
    # Convert everything over 180 back to the negative (degrees W) values.
    lon[lon > 180] = lon[lon > 180] - 360
    # Need to account for clarifying dimensions if the grid is 2D.
    ds.coords[coord] = (ds[coord].dims, lon)
    return ds


@check_xarray(0)
def _convert_lon_to_0to360(ds, coord='lon'):
    """Convert from -180 to 180 (W-E) to 0 to 360 (degrees E) grid.

    .. note::
        Longitudes are not sorted after conversion (i.e., spanning -180 to 180 or
        0 to 360 from index 0, ..., N), as it is expected that the user will plot
        via ``cartopy``, ``basemap``, or ``xarray`` plot functions.

    Args:
        ds (xarray object): Dataset to be converted.
        coord (optional str): Name of longitude coordinate.

    Returns:
        xarray object: Dataset with converted longitude grid.
    """
    ds = ds.copy()
    lon = ds[coord].values
    # Convert -180 to 0 into scale reaching 360.
    lon[lon < 0] = lon[lon < 0] + 360
    # Need to account for clarifying dimensions if the grid is 2D.
    ds.coords[coord] = (ds[coord].dims, lon)
    return ds


@check_xarray(0)
def convert_lon(ds, coord='lon'):
    """Converts longitude grid from -180to180 to 0to360 and vice versa.

    .. note::
        Longitudes are not sorted after conversion (i.e., spanning -180 to 180 or
        0 to 360 from index 0, ..., N), as it is expected that the user will plot
        via ``cartopy``, ``basemap``, or ``xarray`` plot functions.

    Args:
        ds (xarray object): Dataset to be converted.
        coord (optional str): Name of longitude coordinate.

    Returns:
        xarray object: Dataset with converted longitude grid.

    Raises:
        CoordinateError: If ``coord`` does not exist in the dataset.
    """
    if coord not in ds.coords:
        raise CoordinateError(f'{coord} not found in coordinates.')
    # NOTE: Check weird POP grid that Eleanor sent. Could have a min less than 0
    # and max greater than 180. Could just throw error then.
    if ds[coord].min() < 0:
        ds = _convert_lon_to_0to360(ds, coord=coord)
    else:
        ds = _convert_lon_to_180to180(ds, coord=coord)
    return ds
