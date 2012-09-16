from requests.auth import AuthBase


class BearerAuth(AuthBase):
    """Adds a HTTP Bearer token to the given Request object."""
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers['Authorization'] = 'Bearer %s' % self.token
        return r
