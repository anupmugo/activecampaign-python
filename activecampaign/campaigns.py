class Campaigns(object):
    def __init__(self, client):
        self.client = client


    def list_all_campaigns(self, **params):
        """
        View many (or all) campaigns by including their ID's or various filters.
        This is useful for searching for campaigns that match certain criteria -
        such as being part of a certain list, or having a specific custom field value.


        Returns:

        """
        return self.client._get("/campaigns", params=params)
