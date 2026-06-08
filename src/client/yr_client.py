#!/usr/bin/env python3

class YrClient:
    def __init__(self, http):
        self.m_http = http;

    def update(self, url):
        response = self.m_http.get(url)
        return response
