from api import ma
from api.models.user import UserModel


#       schema          flask
# object ------>  dict ----------> json


# Сериализация ответа(response)
class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = UserModel
        # Явно указали поля, которые будут использоваться схемой
        fields = ('id', 'username', "role")


# Десериализация запроса(request)
class UserRequestSchema(ma.SQLAlchemySchema):
    class Meta:
        model = UserModel

    username = ma.Str(required=True)
    password = ma.Str()
    role = ma.Str()


user_schema = UserSchema()
users_schema = UserSchema(many=True)
