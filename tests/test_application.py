"""There are 4 documentation routes"""
DEFAULT_ROUTE_COUNT = 4


def test_whenCreatingApp_thenRoutesAreRegistered(app):
    assert len(app.router.routes) > DEFAULT_ROUTE_COUNT
