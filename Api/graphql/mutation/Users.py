from graphene import Field
from graphene import ID, Mutation, List
from graphene_django.forms.mutation import DjangoModelFormMutation
from graphene_crud_maker.utils import CustomModelForm

from Api.models import Users
from Api.graphql.query import UsersType


class UsersForm(CustomModelForm):
    class Meta:
        model = Users
        fields = ['account_state', 'company_name', 'email', 'first_name', 'image', 'is_active', 'is_staff', 'is_superuser', 'last_name', 'password', 'tin', 'user_code', 'username']


class UsersMutation(DjangoModelFormMutation):
    class Meta:
        form_class = UsersForm

    data = Field(UsersType)

    def perform_mutate(form, info):
        try:
            data = form.save()
            return UsersMutation(data=data)
        except Exception as ex:
            raise ex



class RemoveUsers(Mutation):
    class Arguments:
        ids = List(ID)

    class Meta:
        output = List(UsersType)

    def mutate(self, info, **kwargs):
        deleted_items = []
        for item in Users.objects.filter(pk__in=kwargs['ids']):
            item.delete()
            deleted_items.append(item)
        return deleted_items

