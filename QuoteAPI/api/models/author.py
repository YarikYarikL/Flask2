from api import db
from sqlalchemy.orm import Mapped, mapped_column, relationship, WriteOnlyMapped
from sqlalchemy import String
# from .quote import QuoteModel


class AuthorModel(db.Model):
    __tablename__ = 'authors'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[int] = mapped_column(String(32), index=True, unique=True)
    #default -> for new instance
    #server_default -> for instances that already exist in table
    lastname: Mapped[str] = mapped_column(String(32), index=True, default='unknown', server_default="Smirnov", nullable=True)
    quotes: WriteOnlyMapped['QuoteModel']= relationship(back_populates='author')

    def __init__(self, name, lastname='Unknown'):
        self.name = name
        self.lastname = lastname

    def to_dict(self):
        return {
            'id': self.id
            ,'name': self.name
            ,'lastname': self.lastname
            }