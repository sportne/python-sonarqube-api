class SonarQubeNotifications:
    def __init__(self, client):
        self.client = client

    def add_notification(self, login, type, channel=None, project=None):
        """
        Add a notification.
        :param login: User login
        :param type: Notification type
        :param channel: Channel
        :param project: Project key
        """
        params = {"login": login, "type": type}
        if channel:
            params["channel"] = channel
        if project:
            params["project"] = project
        return self.client._post("api/notifications/add", params=params)

    def list_notifications(self, login=None):
        """
        List notifications.
        :param login: User login
        """
        params = {}
        if login:
            params["login"] = login
        return self.client._get("api/notifications/list", params=params)

    def remove_notification(self, login, type, channel=None, project=None):
        """
        Remove a notification.
        :param login: User login
        :param type: Notification type
        :param channel: Channel
        :param project: Project key
        """
        params = {"login": login, "type": type}
        if channel:
            params["channel"] = channel
        if project:
            params["project"] = project
        return self.client._post("api/notifications/remove", params=params)
