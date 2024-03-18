import django_filters
from .models import TuModelo
from .models import User

class UserFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(lookup_expr='exact')
    class Meta:
        model = User
        fields = ['email','password']