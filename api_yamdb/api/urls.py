from django.urls import include, path
from rest_framework.routers import DefaultRouter
from reviews.views import (CategoryDetail, CategoryList, CommentViewSet,
                           GenreDetail, GenreList, ReviewViewSet, TitleViewSet)
from users.views import APIGetToken, APISignup, UsersViewSet

app_name = 'api'
api_ver = 'v1/'
router_v1 = DefaultRouter()
router_v1.register('titles', TitleViewSet, basename="titles")
router_v1.register('users', UsersViewSet)
router_v1.register(
    r'titles/(?P<title_id>\w+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router_v1.register(
    r'titles/(?P<title_id>\w+)/reviews/(?P<review_id>\w+)/comments',
    CommentViewSet,
    basename='comments'
)

auth_urls = [
    path('signup/', APISignup.as_view()),
    path('token/', APIGetToken.as_view())
]

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path(api_ver, include(router_v1.urls)),
    path(api_ver + 'auth/', include(auth_urls)),
    path(api_ver + 'categories/',
         CategoryList.as_view(),
         name='category_list'),
    path(api_ver + 'categories/<slug:slug>/',
         CategoryDetail.as_view(),
         name='category_detail'),
    path(api_ver + 'genres/',
         GenreList.as_view(),
         name='genres_list'),
    path(api_ver + 'genres/<slug:slug>/',
         GenreDetail.as_view(),
         name='genres_detail'),
]
