from graphene_django import DjangoObjectType
from graphene_crud_maker.utils import CustomNode, CustomConnection

from Api.models import Users


class UsersType(DjangoObjectType):
    class Meta:
        model = Users
        filter_fields = {
            'id': ['exact',],
        }
        interfaces = (CustomNode,)
        connection_class = CustomConnection

