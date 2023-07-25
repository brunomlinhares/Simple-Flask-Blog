class GridView:
    def __init__(
        self,
        list_items: list[(str, str)],
        cols_quantity: int,
        action_links_info: list[dict],
        have_action: bool = False,
    ) -> None:
        self.list_items = self.sanitize_items(list_items)
        self.cols_quantity = cols_quantity
        self.action_links_info = action_links_info
        self.have_action = have_action

    def sanitize_items(self, list_items):
        return [
            {"name": item[0], "image_url": item[1], "url": item[2]}
            for item in list_items
        ]
