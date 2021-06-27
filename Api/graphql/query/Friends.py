from graphene_django import DjangoObjectType
from graphene_crud_maker.utils import CustomNode, CustomConnection

from Api.models import Friends


class FriendsType(DjangoObjectType):
    class Meta:
        model = Friends
        filter_fields = {
            'id': ['exact',],
        }
        interfaces = (CustomNode,)
        connection_class = CustomConnection

