#!/usr/bin/env python3

#SCRATCH
class YrClient:
    def __init__(self, http):
        self.m_http = http;

    def update(self, url):
        response = self.m_http.get(url)
        return response

class NotFoundHttp:
    def get(self, url):
        return {"status": 404}
#END SCRATCH

class TestClient:

    def test_wrong_url_not_found(self):
        """if we have a wrong url, we'd expect 404"""
        http = NotFoundHttp()
        client = YrClient(http)

        url = "wrong"
        response = client.update(url);
        assert response["status"] == 404
        # TODO verify that the client took note of the error, so we can potentially persist issues for future investigation
