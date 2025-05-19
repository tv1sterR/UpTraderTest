def build_menu_tree(menu_items, current_path):
    menu_dict = {}
    for item in menu_items:
        menu_dict[item.id] = {
            'id': item.id,
            'name': item.name,
            'url': item.get_url(),
            'parent_id': item.parent_id,
            'is_active': item.is_active(current_path),
            'children': [],
        }

    root_items = []
    for item_id, item_data in menu_dict.items():
        parent_id = item_data['parent_id']
        if parent_id is None:
            root_items.append(item_data)
        else:
            parent = menu_dict.get(parent_id)
            if parent:
                parent['children'].append(item_data)

    for item_id, item_data in menu_dict.items():
        if item_data['is_active']:
            parent_id = item_data['parent_id']
            while parent_id:
                parent = menu_dict.get(parent_id)
                if parent:
                    parent['is_expanded'] = True
                    parent_id = parent['parent_id']
                else:
                    break

    for item_id, item_data in menu_dict.items():
        if item_data['is_active']:
            for child in item_data['children']:
                child['is_expanded'] = True

    return root_items