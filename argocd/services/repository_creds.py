from requests import sessions

from argocd import config


class RepositoryCredsService:
    def __init__(self, token=None):
        self.config = config.Config()
        self.session = sessions.Session()
        self.base_url = self.config.server_url
        token = token or self.config.authentication_token

        self.session.headers.update({"Authorization": f"Bearer {token}"})

    def list(self, repo=""):
        """
        ListRepositoryCredentials gets a list of all configured
        repository credential sets
        """
        params = {}
        if repo != "":
            params["repo"] = repo

        response = self.session.get(f"{self.base_url}/api/v1/repocreds", params=params)
        return response.json()
