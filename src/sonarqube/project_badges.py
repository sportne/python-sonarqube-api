class SonarQubeProjectBadges:
    def __init__(self, client):
        self.client = client

    def get_project_badge_ai_code_assurance(self, project, branch=None):
        """
        Generate a badge for project's AI assurance as an SVG.
        :param project: Project key
        :param branch: Branch key
        """
        params = {"project": project}
        if branch:
            params["branch"] = branch
        return self.client._get("api/project_badges/ai_code_assurance", params=params)

    def get_project_badge_measure(self, project, metric, branch=None):
        """
        Generate badge for project's measure as an SVG.
        :param project: Project key
        :param metric: Metric key
        :param branch: Branch key
        """
        params = {"project": project, "metric": metric}
        if branch:
            params["branch"] = branch
        return self.client._get("api/project_badges/measure", params=params)

    def get_project_badge_quality_gate(self, project, branch=None):
        """
        Generate badge for project's quality gate as an SVG.
        :param project: Project key
        :param branch: Branch key
        """
        params = {"project": project}
        if branch:
            params["branch"] = branch
        return self.client._get("api/project_badges/quality_gate", params=params)

    def renew_project_badge_token(self, project):
        """
        Creates new token replacing any existing token for project badge access.
        :param project: Project key
        """
        params = {"project": project}
        return self.client._post("api/project_badges/renew_token", params=params)

    def get_project_badge_token(self, project):
        """
        Retrieve a token to use for project badge access.
        :param project: Project key
        """
        params = {"project": project}
        return self.client._get("api/project_badges/token", params=params)
