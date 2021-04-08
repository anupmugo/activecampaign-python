class Activities(object):
    def __init__(self, client):
        self.client = client


    def list_all_activities(self, **params):
        """
        View many (or all) activities by including their ID's or various filters.
        This is useful for searching for campaigns that match certain criteria -
        such as being part of a certain list, or having a specific custom field value.
        Returns:
        """
        return self.client._get("/activities", params=params)
