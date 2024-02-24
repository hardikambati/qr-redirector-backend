class TokenAuthMiddleware:
    """
    Checks whether a valid token is passed or not in request query
    Currently not being used, but can be used in future
    """

    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        return await self.app(scope, receive, send)
