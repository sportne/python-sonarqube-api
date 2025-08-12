class SonarQubeProjectAnalyses:
    def __init__(self, client):
        self.client = client

    def create_project_analysis_event(self, analysis, name, category=None):
        """
        Create a project analysis event.
        :param analysis: Analysis key
        :param name: Event name
        :param category: Event category
        """
        params = {"analysis": analysis, "name": name}
        if category:
            params["category"] = category
        return self.client._post("api/project_analyses/create_event", params=params)

    def delete_project_analysis(self, analysis):
        """
        Delete a project analysis.
        :param analysis: Analysis key
        """
        params = {"analysis": analysis}
        return self.client._post("api/project_analyses/delete", params=params)

    def delete_project_analysis_event(self, event):
        """
        Delete a project analysis event.
        :param event: Event key
        """
        params = {"event": event}
        return self.client._post("api/project_analyses/delete_event", params=params)

    def search_project_analyses(self, project, **kwargs):
        """
        Search a project analyses and attached events.
        :param project: Project key
        :param kwargs: Additional parameters
        """
        params = {"project": project}
        params.update(kwargs)
        return self.client._get("api/project_analyses/search", params=params)

    def update_project_analysis_event(self, event, name):
        """
        Update a project analysis event.
        :param event: Event key
        :param name: New name
        """
        params = {"event": event, "name": name}
        return self.client._post("api/project_analyses/update_event", params=params)
