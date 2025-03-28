from api import ma
from api.models.author import AuthorModel

class AuthorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AuthorModel
        dump_only = ("id",)

author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)
