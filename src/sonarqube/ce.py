class SonarQubeCe:
    def __init__(self, client):
        self.client = client

    def get_ce_activity(self, **kwargs):
        """
        Search for tasks.
        :param kwargs: The search parameters.
        """
        return self.client._get("api/ce/activity", params=kwargs)

    def get_ce_activity_status(self, componentId=None):
        """
        Returns CE activity related metrics.
        :param componentId: Component ID
        """
        params = {}
        if componentId:
            params["componentId"] = componentId
        return self.client._get("api/ce/activity_status", params=params)

    def get_ce_analysis_status(self, analysisId):
        """
        Get the analysis status of a given component.
        :param analysisId: Analysis ID
        """
        params = {"analysisId": analysisId}
        return self.client._get("api/ce/analysis_status", params=params)

    def cancel_ce_task(self, id):
        """
        Cancels a pending task.
        :param id: Task ID
        """
        params = {"id": id}
        return self.client._post("api/ce/cancel", params=params)

    def cancel_all_ce_tasks(self):
        """
        Cancels all pending tasks.
        """
        return self.client._post("api/ce/cancel_all")

    def get_ce_component(self, component):
        """
        Get the pending tasks, in-progress tasks and the last executed task of a given component.
        :param component: Component key
        """
        params = {"component": component}
        return self.client._get("api/ce/component", params=params)

    def dismiss_ce_analysis_warning(self, project, warning):
        """
        Permanently dismiss a specific analysis warning.
        :param project: Project key
        :param warning: Warning key
        """
        params = {"project": project, "warning": warning}
        return self.client._post("api/ce/dismiss_analysis_warning", params=params)

    def get_ce_indexation_status(self):
        """
        Returns the count of projects with completed issue indexing.
        """
        return self.client._get("api/ce/indexation_status")

    def get_ce_info(self):
        """
        Gets information about Compute Engine.
        """
        return self.client._get("api/ce/info")

    def pause_ce(self):
        """
        Requests pause of Compute Engine workers.
        """
        return self.client._post("api/ce/pause")

    def resume_ce(self):
        """
        Resumes pause of Compute Engine workers.
        """
        return self.client._post("api/ce/resume")

    def set_ce_worker_count(self, count):
        """
        Set the number of workers in the Compute Engine.
        :param count: Number of workers
        """
        params = {"count": count}
        return self.client._post("api/ce/set_worker_count", params=params)

    def submit_scanner_report(self, **kwargs):
        """
        Submits a scanner report to the queue.
        :param kwargs: The submission parameters.
        """
        return self.client._post("api/ce/submit", params=kwargs)

    def get_ce_task(self, id):
        """
        Give Compute Engine task details.
        :param id: Task ID
        """
        params = {"id": id}
        return self.client._get("api/ce/task", params=params)

    def get_ce_task_types(self):
        """
        List available task types.
        """
        return self.client._get("api/ce/task_types")

    def get_ce_worker_count(self):
        """
        Return number of Compute Engine workers.
        """
        return self.client._get("api/ce/worker_count")
