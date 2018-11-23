# _*_ coding:utf-8 _*_
__author__ = 'pengcong'
__date__ = '2018/11/21 16:20'
from django.conf.urls import url, include
from .views import CTModelTrans, LearnModelTrans, StudentModelTrans, TeacherModelTrans, KnowModel1Trans, KnowModelTrans, \
    ProductionModelTrans, ProductionModelSb2ProfileTrans, ProcessModel1Trans, ProcessModel2Trans, ProcessModel3Trans

urlpatterns = [
    url(r'^test/', CTModelTrans, name='CTModelTrans'),
    url(r'^test1/', LearnModelTrans, name='LearnModelTrans'),
    url(r'^test2/', StudentModelTrans, name='StudentModelTrans'),
    url(r'^test3/', TeacherModelTrans, name='TeacherModelTrans'),
    url(r'^test4/', KnowModelTrans, name='KnowModelTrans'),
    url(r'^test5/', KnowModel1Trans, name='KnowModel1Trans'),
    url(r'^test6/', ProductionModelTrans, name='ProductionModelTrans'),
    url(r'^test7/', ProductionModelSb2ProfileTrans, name='ProductionModelSb2ProfileTrans'),
    url(r'^test8/', ProcessModel1Trans, name='ProcessModel1Trans'),
    url(r'^test9/', ProcessModel2Trans, name='ProcessModel2Trans'),
    url(r'^test10/', ProcessModel3Trans, name='ProcessModel3Trans'),
]
