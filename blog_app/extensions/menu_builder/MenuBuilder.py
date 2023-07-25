from typing import List


class MenuItem:
    def __init__(self, label: str, url: str) -> None:
        self.label: str = label
        self.url: str = url
        self.children: List[MenuItem] = []

    def add_child(self, label: str, url: str) -> None:
        self.children.append(MenuItem(label, url))

    @property
    def has_children(self) -> bool:
        return len(self.children)  > 0
    
    def __repr__(self) -> str:
        return f"<MenuItem {self.label} {self.url}>"

class MenuBuilder:
    def __init__(self) -> None:
        self.menu: List[MenuItem] = []

    def add_menu_item(self, label: str, url: str) -> None:
        self.menu.append(MenuItem(label, url))

    def add_child(self, parent_label: str, label: str, url: str) -> None:
        for item in self.menu:
            if item.label == parent_label:
                item.add_child(label, url)
                return
        raise Exception(f"Parent menu item {parent_label} not found")

    def get_menu(self) -> List[MenuItem]:
        print(self.menu)
        return self.menu
