import django_filters
from myapp.models import PersonalDetails, State, YearsOfExp

class RegisterUserFilter(django_filters.FilterSet):
    statename = django_filters.ModelChoiceFilter(field_name='state__id', method='filter_state', queryset=State.objects.all())
    # work = django_filters.ModelChoiceFilter(field_name='work', method='filter_exp', queryset=YearsOfExp.objects.all())
    
    def filter_state(self, queryset, name, value):
        return queryset.filter(state__id=value.id)

    # def filter_exp(self, queryset, name, value):
    #     # print(name)
    #     # breakpoint()
    #     queryset = queryset.prefetch_related('work').filter(year_exp_id__id=value.id)
    #     return queryset

    class Meta:
        model = PersonalDetails
        fields = ('first_name', 'last_name', 'statename')