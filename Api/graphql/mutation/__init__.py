from graphene import ObjectType

from .Users import UsersMutation, RemoveUsers 
from .Friends import FriendsMutation, RemoveFriends 


class Mutation(ObjectType):
	users = UsersMutation.Field() 
	remove_users = RemoveUsers.Field() 

	friends = FriendsMutation.Field() 
	remove_friends = RemoveFriends.Field() 

