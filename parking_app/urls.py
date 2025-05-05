# parking_app/urls.py
from django.urls import path
from .views import auth_views, parking_views, review_views, system_views, test_views, survey_views
from .views.upload_parking_lot import upload_parking_lot
from .views.static_pages import pseudo_points_history

urlpatterns = [
    path('upload_parking_lot/', upload_parking_lot, name='upload_parking_lot'),
    path('', parking_views.index, name='index'),
    path('parking/<int:id>/', parking_views.parking_detail, name='parking_detail'),
    path('parking/<int:id>/add_review/', review_views.add_review, name='add_review'),
    path('register/', auth_views.register, name='register'),
    path('login/', auth_views.login_view, name='login'),
    path('logout/', auth_views.logout_view, name='logout'),
    path('forgot_password/', auth_views.forgot_password, name='forgot_password'),
    path('forgot_password/set_new_pw/', auth_views.set_new_pw, name='set_new_pw'),
    path('map/', parking_views.map_page, name='map_page'),
    path('deduct_points/', system_views.deduct_points_view, name='deduct_points'),
    path('award_points/', system_views.award_points_view, name='award_points'),
    path('view_points/', system_views.view_points_view, name='view_points'),
    path('autoban/', system_views.autoban_view, name='autoban'),
    path('send_warnings/', system_views.send_warnings_view, name='send_warnings'),
    path('process_image/', system_views.process_image_view, name='process_image'),
    path('issue_warning/', system_views.issue_warning_view, name='issue_warning'),
    path('audit_user/', system_views.audit_user_view, name='audit_user'),
    path('generate_user_report/', system_views.generate_user_report_view, name='generate_user_report'),
    path('generate_parking_report/', system_views.generate_parking_report_view, name='generate_parking_report'),
    path('test/leave_comment/<int:user_id>/<int:parking_id>/', test_views.test_leave_comment, name='test_leave_comment'),
    path('test/report_info/<int:user_id>/<int:parking_id>/', test_views.test_report_info, name='test_report_info'),
    path('test/upload_parking/<int:user_id>/', test_views.test_upload_parking, name='test_upload_parking'),
    path('test/edit_parking/<int:user_id>/<int:parking_id>/', test_views.test_edit_parking, name='test_edit_parking'),
    path('test/leave_review/<int:user_id>/<int:parking_id>/', test_views.test_leave_review, name='test_leave_review'),
    path('system/load_parking_data/', system_views.load_parking_data_view, name='load_parking_data'),
    path('test/', test_views.test_page, name='test_page'),
    path('account/', auth_views.account_manage, name = 'account_manage'),
    path('pseudo_points_history/', pseudo_points_history, name='pseudo_points_history'),
    path('survey/', survey_views.survey, name='survey'),
    path('success/', survey_views.survey_success, name='survey_success'),
]
