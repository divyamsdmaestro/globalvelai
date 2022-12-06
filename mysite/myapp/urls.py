from myapp.views import TagModelViewset, UserModelViewset, FileUploadViewsets, CountryViewsets, StateViewsets, DegreeViewsets, SkillsViewsets, YearOfExpViewsets, YearViewsets, IndustriesViewsets, SalaryExpViewsets, TestModelViewsets, RegisterUserDetailsViewsets, RestaurantsViewsets, TagRestaurantToCustomersViewsets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tag', TagModelViewset, basename='tag')
router.register(r'users', UserModelViewset, basename='user')
router.register(r'uploadfile', FileUploadViewsets, basename='uploadfile')
router.register(r'country', CountryViewsets, basename='country')
router.register(r'state', StateViewsets, basename='state')
router.register(r'degree', DegreeViewsets, basename='degree')
router.register(r'skills', SkillsViewsets, basename='skills')
router.register(r'yearofexp', YearOfExpViewsets, basename='yearofexp')
router.register(r'years', YearViewsets, basename='years')
router.register(r'industry', IndustriesViewsets, basename='industry')
router.register(r'salaryexp', SalaryExpViewsets, basename='salaryexp')
router.register(r'registerdetails', RegisterUserDetailsViewsets, basename='registerdetails')
router.register(r'restaurants', RestaurantsViewsets, basename='restaurants')
router.register(r'customers', TagRestaurantToCustomersViewsets, basename='customers')
router.register(r'testmodel', TestModelViewsets, basename='testmodel')

urlpatterns = router.urls