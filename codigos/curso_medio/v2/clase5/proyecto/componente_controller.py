from component import *


class ComponentController:

    def __init__(self):
        if not ModelComponent.table_exists():
            ModelComponent.create_table()

    def insert(self, component: Component):
        component.get_model().save()

    def get(self, id):
        return ModelComponent.get_by_id(id)

    def get_all(self):
        return [ Component.get_component(c) for c in ModelComponent.select() ]

    def delete(self, id: int):
        ModelComponent.get_by_id(id).delete_instance()

    def update(self, component: Component):
        component.get_model().save()

    def search_by_code(self, code: str):
        id = int(code) if code.isdigit() else 0

        components_model = ModelComponent.select().where(
            (ModelComponent.id == id) | (ModelComponent.code.contains(code))
        )

        return {
            "components": [Component.get_component(c) for c in components_model],
            "size": components_model.count(),
        }

    def get_size(self):
        return ModelComponent.select().count()

    def search(self, text: str):
        components_model = ModelComponent.select().where(
            (ModelComponent.name.contains(text))
            | (ModelComponent.code.contains(text))
            | (ModelComponent.description.contains(text))
        )

        return {
            "components": [Component.get_component(c) for c in components_model],
            "size": components_model.count(),
        }