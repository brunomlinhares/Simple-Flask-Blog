class ViewTable:
    def __init__(
        self,
        headers: list[str],
        rows: list[str],
        action_links_info: list[dict],
        have_action: bool = False,
    ) -> None:
        self.headers = headers
        self.rows = rows
        self.action_links_info =  action_links_info
        self.have_action = have_action

