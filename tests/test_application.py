from unittest.mock import MagicMock
from app.application import ApplicationFactory


TITLE = 'API'
DESCRIPTION = 'some description'

FACTORY = ApplicationFactory(TITLE, DESCRIPTION)


def create_router():
    router = MagicMock()
    router.register = MagicMock()

    return router


def test_whenCreatingApp_thenTitleIsSet():
    app = FACTORY.create(debug=True)

    assert app.title == TITLE


def test_whenCreatingApp_thenDescriptionIsSet():
    app = FACTORY.create(debug=True)

    assert app.description == DESCRIPTION


def test_whenCreatingApp_thenRoutesAreRegistered():
    router = create_router()

    FACTORY.create(debug=True, router=router)

    router.register.assert_called_once()
