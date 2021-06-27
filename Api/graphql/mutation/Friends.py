from graphene import Field
from graphene import ID, Mutation, List
from graphene_django.forms.mutation import DjangoModelFormMutation
from graphene_crud_maker.utils import CustomModelForm

from Api.models import Friends
from Api.graphql.query import FriendsType


class FriendsForm(CustomModelForm):
    class Meta:
        model = Friends
        fields = ['age', 'email', 'name', 'owner']


class FriendsMutation(DjangoModelFormMutation):
    class Meta:
        form_class = FriendsForm

    data = Field(FriendsType)

    def perform_mutate(form, info):
        try:
            data = form.save()
            return FriendsMutation(data=data)
        except Exception as ex:
            raise ex



class RemoveFriends(Mutation):
    class Arguments:
        ids = List(ID)

    class Meta:
        output = List(FriendsType)

    def mutate(self, info, **kwargs):
        deleted_items = []
        for item in Friends.objects.filter(pk__in=kwargs['ids']):
            item.delete()
            deleted_items.append(item)
        return deleted_items

