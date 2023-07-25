from flask.views import MethodView
from flask import jsonify, request

from blog_app import csrf
from .. import db


class ItemAPI(MethodView):
    decorators = [csrf.exempt]
    init_every_request = False

    def __init__(self, model):
        self.model = model

    def _get_item(self, id):
        return self.model.query.get_or_404(id)

    def get(self, id):
        item = self._get_item(id)
        return jsonify(item.to_json())

    def patch(self, id):
        item = self._get_item(id)
        data = request.get_json()
        for key, value in data.items():
            setattr(item, key, value)
        db.session.commit()
        return jsonify(item.to_json())

    def delete(self, id):
        item = self._get_item(id)
        db.session.delete(item)
        db.session.commit()
        return "", 204


class GroupAPI(MethodView):
    decorators = [csrf.exempt]
    init_every_request = False

    def __init__(self, model):
        self.model = model

    def get(self):
        items = self.model.query.all()
        return jsonify([item.to_json() for item in items])

    def post(self):
        errors = self.validator.validate(request.json)

        if errors:
            return jsonify(errors), 400

        db.session.add(self.model.from_json(request.json))
        db.session.commit()


def register_api(blueprint, model, name):
    item = ItemAPI.as_view(f"{name}-item", model)
    group = GroupAPI.as_view(f"{name}-group", model)
    blueprint.add_url_rule(f"/{name}/<int:id>", view_func=item)
    blueprint.add_url_rule(f"/{name}/", view_func=group)
