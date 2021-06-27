from graphene import ObjectType 
from Core.utils import CustomNode 
from graphene_django.filter import DjangoFilterConnectionField 

from .Users import UsersType 
from .Friends import FriendsType 


class Query(ObjectType):
	users = CustomNode.Field(UsersType) 
	all_users = DjangoFilterConnectionField(UsersType) 

	friends = CustomNode.Field(FriendsType) 
	all_friends = DjangoFilterConnectionField(FriendsType) 


