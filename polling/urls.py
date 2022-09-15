from django.urls import path
from polling.views import PollDetailView, PollListView

urlpatterns = [
    # path('', list_view, name="poll_index"),  # this was commented out when we switched from functions to class-based views
    path('', PollListView.as_view(), name="poll_index"),
    path('polls/<int:pk>', PollDetailView.as_view(), name="poll_detail"),
    # path('polls/<int:poll_id>', detail_view, name="poll_detail")  # this was commented out when we switched from functions to class-based views
]