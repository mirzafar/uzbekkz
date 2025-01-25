from django.conf.urls.static import static
from django.contrib import admin
from uzbek import settings
from django.urls import path, include
from main.views import *

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/languages/', language_list, name='language_list'),
    path('api/donates/', donate, name='donate'),
    path('api/jointogroups/', join_to_group, name='join_to_group'),
    path('api/trans/', translations_list, name='translations_list'),
    path('api/traditions/', traditions, name='traditions'),
    path('api/ckeditor/', include('ckeditor_uploader.urls')),
    path('api/about-us/', about_us, name='about_us'),
    path('api/famous-persons/', famous_persons, name='famous_persons'),
    path('api/our-partners/', our_partners, name='our_partners'),
    path('api/who-are-we/', who_are_we, name='who_are_we'),
    path('api/our-history/', our_history, name='our_history'),
    path('api/youth-organizations/', youth_organizations, name='youth_organizations'),
    path('api/education/', education, name='education'),
    path('api/sport/', sport, name='sport'),
    path('api/help-those-in-need/', help_those_in_need, name='help_those_in_need'),
    path('api/important-doc/', important_doc, name='important_doc'),
    path('api/statutes/', statutes, name='statutes'),
    path('api/plans-for2025/', plans_for2025, name='plans_for2025'),
    path('api/projects-for2025/', projects_for2025, name='projects_for2025'),
    path('api/last-news/', last_news, name='last_news'),
    path('api/video-materials/', video_materials, name='video_materials'),
    path('api/photo-gallery/', photo_gallery, name='photo_gallery'),
    path('api/interview/', interview, name='interview'),
    path('api/etno-center/', etno_center, name='etno_center'),
    path('api/etno-center-manager/', etno_center_manager, name='etno_center_manager'),
    path('api/etno-center-region/', etno_center_region, name='etno_center_region'),
    path('api/association/', association, name='association'),
    path('api/contacts/', contact_list, name='contact_list'),
    path('api/pay-link/', pay_link, name='pay_link'),
    path('api/etno-center-contact/', etno_center_contact, name='etno_center_contact'),
    path('api/etno-center-info/', etno_center_info, name='etno_center_info'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
