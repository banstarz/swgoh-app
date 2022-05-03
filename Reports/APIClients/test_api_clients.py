
import requests

from swgohGG import SwgohGGApiClient

class MockResponse:

    def __init__(self, url='', headers='', data=''):
        self.url = url
        self.headers = headers
        self.body = data

    def __enter__(self):
        return self

    def __exit__(*args, **kwargs):
        pass

class MockSuccessResponse(MockResponse):

    def json(self):
        return {'result': "Mocked"}

    @property
    def status_code(self):
        return 200

class MockBadResponse(MockResponse):

    @property
    def status_code(self):
        return 403

class TestSwgohGG:
    def test_swgoh_characters(self, monkeypatch):
        def mock_post_success(*args, **kwargs):
            return MockSuccessResponse(args, kwargs)

        def mock_post_failed(*args, **kwargs):
            return MockBadResponse(args, kwargs)

        monkeypatch.setattr(requests, "post", mock_post_success)

        result = SwgohGGApiClient.swgoh_characters()
        assert type(result) is dict

        monkeypatch.setattr(requests, "post", mock_post_failed)

        result = SwgohGGApiClient.swgoh_characters()
        assert result is None

    def test_swgoh_ships(self, monkeypatch):
        def mock_post_success(*args, **kwargs):
            print(args)
            print(kwargs)
            return MockSuccessResponse(args, kwargs)

        def mock_post_failed(*args, **kwargs):
            return MockBadResponse(args, kwargs)

        monkeypatch.setattr(requests, "post", mock_post_success)

        result = SwgohGGApiClient.swgoh_ships()
        assert type(result) is dict

        monkeypatch.setattr(requests, "post", mock_post_failed)

        result = SwgohGGApiClient.swgoh_ships()
        assert result is None