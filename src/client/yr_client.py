#!/usr/bin/env python3

class YrClient:
    def __init__(self, baseUrl, http):
        self.m_http = http;
        self.m_baseUrl = baseUrl

    def update(self):
        url = self.m_baseUrl + "/wrong"
        response = self.m_http.get(url)
        # TODO persist if we got a usable response
        return response
