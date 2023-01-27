from api import app, request, multi_auth
from api.models.user import UserModel
from api.schemas.user import user_schema, users_schema, UserSchema, UserRequestSchema
from utility.helpers import get_object_or_404
from flask_apispec import doc, marshal_with, use_kwargs


@app.route("/users/<int:user_id>", methods=["GET"])
@doc(description='Api for only user.', tags=['Users'], summary="Get user by id")
@marshal_with(UserSchema, code=200)
def get_user_by_id(user_id):
    user = get_object_or_404(UserModel, user_id)
    if user is None:
        return {"error": "User not found"}, 404
    return user, 200


@app.route("/users")
@doc(description='Api for all users.', tags=['Users'])
@marshal_with(UserSchema(many=True), code=200)
def get_users():
    users = UserModel.query.all()
    return users, 200


@app.route("/users", methods=["POST"])
@doc(description='Create user', tags=['Users'], summary="Create user")
@marshal_with(UserSchema, code=201)
@use_kwargs(UserRequestSchema, location='json')
def create_user(**kwargs):
    user = UserModel(**kwargs)
    # DONE: добавить обработчик на создание пользователя с неуникальным username
    if UserModel.query.filter_by(username=user.username).one_or_none():
        return {"error": "User already exists"}, 409
    user.save()
    return user, 201


@app.route("/users/<int:user_id>", methods=["PUT"])
@doc(description='Edit user.', tags=['Users'], summary="Edit user")
@marshal_with(UserSchema, code=200)
@use_kwargs(UserRequestSchema, location='json')
@doc(security=[{"basicAuth": []}])
@doc(responses={"401": {"description": "Unauthorized"}})
@doc(responses={"404": {"description": "Not found"}})
@multi_auth.login_required(role="admin")
def edit_user(user_id, **kwargs):
    user = get_object_or_404(UserModel, user_id)
    for key, value in kwargs.items():
        setattr(user, key, value)
    user.save()
    return user, 200


@app.route("/users/<int:user_id>", methods=["DELETE"])
@doc(description='Delete user by id.', tags=['Users'], summary="Delete user by id")
@doc(responses={"404": {"description": "Not found"}})
@multi_auth.login_required(role="admin")
def delete_user(user_id):
    """
    Пользователь должен удаляться только со своими заметками
    1. Найти пользователя по user_id
    2. Вызвать метод delete()
    """
    user = get_object_or_404(UserModel, user_id)
    user.delete()
    return {"message": f'User with id={user_id} has deleted.'}, 200
