# coding: utf-8
from django.db import models
from DataSetModel.models import ScratchApiProduction, ScratchApiProductionhint, ScratchApiTeacher


#
#
# Create your models here.


class StudentModel(models.Model):
    username = models.CharField(max_length=30, primary_key=True, verbose_name='用户名')
    gender = models.CharField(max_length=30, verbose_name='性别', blank=True, null=True)
    age = models.IntegerField(verbose_name='年龄', blank=True, null=True)
    school = models.CharField(max_length=50, verbose_name='学校', blank=True, null=True)
    grade = models.CharField(max_length=40, verbose_name='年级', blank=True, null=True)
    district = models.CharField(max_length=100, verbose_name='地区', blank=True, null=True)
    student_id = models.CharField(max_length=30, verbose_name='学号', blank=True, null=True)
    phone_number = models.CharField(max_length=15, verbose_name='手机号', blank=True, null=True)
    registration_time = models.DateTimeField(verbose_name='注册时间', blank=True, null=True)

    coursetimes = models.IntegerField(verbose_name='学习的课程数', blank=True, null=True,default=0)
    favtimes = models.IntegerField(verbose_name='收藏的作品数', blank=True, null=True,default=0)
    creativetimes = models.IntegerField(verbose_name='创作数', blank=True, null=True,default=0)
    remixtimes = models.IntegerField(verbose_name='改编数', blank=True, null=True,default=0)
    course_list = models.TextField(verbose_name='学习的课程列表', blank=True, null=True)
    production_list = models.TextField(verbose_name='创作作品列表', blank=True, null=True)
    fav_list = models.TextField(verbose_name='创作收藏列表', blank=True, null=True)
    remix_tree = models.TextField(verbose_name='改编树', blank=True, null=True)
    learning_duration = models.IntegerField(verbose_name='学习总时长', blank=True, null=True)
    active_level = models.CharField(max_length=30, verbose_name='用户活跃等级', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'DataSet_StudentModel'

    def __str__(self):
        return self.username


class TeacherModel(models.Model):
    teacher_id = models.CharField(max_length=30, primary_key=True, verbose_name='用户名')
    school = models.CharField(max_length=50, verbose_name='学校', blank=True, null=True)
    teach_class = models.CharField(max_length=100, verbose_name='所教班级', blank=True, null=True)
    email = models.CharField(max_length=50, verbose_name='邮箱', blank=True, null=True)
    phone_number = models.CharField(max_length=15, verbose_name='手机号', blank=True, null=True)
    course_times = models.IntegerField(verbose_name='创建课程数', default=0, blank=True, null=True)
    contest_times = models.IntegerField(verbose_name='发起的竞赛数', default=0, blank=True, null=True)
    production_evalu = models.TextField(verbose_name='评价记录')

    class Meta:
        managed = True
        db_table = 'DataSet_TeacherModel'


class LearnModel(models.Model):
    username = models.CharField(max_length=50, verbose_name='用户名')
    lesson_id = models.IntegerField()
    chapter_id = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    learn_time = models.BigIntegerField(blank=True, null=True)
    click_audio = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'DataSet_LearnModel'

    def __str__(self):
        return str(self.lesson_id) + '/' + str(self.chapter_id) + '/' + str(self.start_time) + '/' + str(
            self.learn_time)

    def __unicode__(self):
        return str(self.lesson_id) + '/' + str(self.chapter_id) + '/' + str(self.start_time) + '/' + str(
            self.learn_time)


class KnowModel(models.Model):
    lesson_id = models.IntegerField(primary_key=True, verbose_name='课程编号')
    name = models.CharField(verbose_name='课程名', max_length=50)
    short_introduction = models.TextField(verbose_name='简介', blank=True, null=True)
    author = models.ForeignKey(TeacherModel, verbose_name='出课老师', blank=True, null=True)
    learn_times = models.IntegerField(verbose_name='学习次数', default=0)

    class Meta:
        managed = True
        db_table = 'DataSet_KnowModel_lesson'


class KnowModel1(models.Model):
    lesson = models.ForeignKey(KnowModel, verbose_name='课程编号', blank=True, null=True)
    chapter_id = models.IntegerField()
    name = models.CharField(max_length=50, verbose_name='知识点名称')
    content = models.TextField(verbose_name='知识点内容')
    audio = models.CharField(max_length=100, verbose_name='音频描述', blank=True, null=True)
    create_time = models.DateTimeField(verbose_name='创建时间')

    class Meta:
        managed = True
        db_table = 'DataSet_KnowModel_chapter'
        unique_together = (('lesson', 'chapter_id', 'name'),)


class ProductionModel(models.Model):
    id = models.CharField(primary_key=True, max_length=32, verbose_name='作品ID')
    name = models.CharField(max_length=50, verbose_name='作品名称', blank=True, null=True)
    author = models.ForeignKey(StudentModel, verbose_name='作者', blank=True, null=True)
    type = models.CharField(max_length=20, verbose_name='类型', blank=True, null=True)
    create_time = models.DateTimeField()

    liketimes = models.IntegerField(verbose_name='点赞数', default=0, blank=True, null=True)
    favtimes = models.IntegerField(verbose_name='被收藏数', default=0, blank=True, null=True)
    remixedtimes = models.IntegerField(verbose_name='被改编数', default=0, blank=True, null=True)

    parent_id = models.CharField(max_length=32, verbose_name='改编来源', blank=True, null=True)
    lesson_id = models.IntegerField(blank=True, null=True)
    belong_class = models.CharField(max_length=40, verbose_name='年级', blank=True, null=True)

    sb2file = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'DataSet_ProductionModel'


class ProductionModelSb2Profile(models.Model):
    motion_num = models.IntegerField()
    looklike_num = models.IntegerField()
    sounds_num = models.IntegerField()
    draw_num = models.IntegerField()
    event_num = models.IntegerField()
    control_num = models.IntegerField()
    sensor_num = models.IntegerField()
    operate_num = models.IntegerField()
    more_num = models.IntegerField()
    data_num = models.IntegerField()
    sprite_num = models.IntegerField()
    backdrop_num = models.IntegerField()
    snd_num = models.IntegerField()
    production_id = models.ForeignKey(ProductionModel, unique=True, verbose_name='作品ID')

    class Meta:
        managed = True
        db_table = 'DataSet_ProductionModelSb2Profile'


class CTModel(models.Model):
    production_id = models.ForeignKey(ProductionModel, models.DO_NOTHING, unique=True, verbose_name='作品ID')
    ap_score = models.IntegerField(verbose_name='抽象化')
    parallelism_score = models.IntegerField(verbose_name='并行')
    synchronization_score = models.IntegerField(verbose_name='同步性')
    flow_control_score = models.IntegerField(verbose_name='流控制')
    user_interactivity_score = models.IntegerField(verbose_name='用户交互')
    logical_thinking_score = models.IntegerField(verbose_name='逻辑性')
    data_representation_score = models.IntegerField(verbose_name='数据表示')
    total = models.IntegerField(verbose_name='总分')
    hint = models.CharField(max_length=100, verbose_name='作品提示')

    class Meta:
        managed = True
        db_table = 'DataSet_CTModel'


class ProcessModel1(models.Model):
    type = models.CharField(max_length=100, verbose_name='操作类型', blank=True, null=True)
    op = models.CharField(max_length=100, verbose_name='块名称', blank=True, null=True)
    loc = models.CharField(max_length=100, verbose_name='块连接方式', blank=True, null=True)
    time = models.DateTimeField(verbose_name='操作时间', blank=True, null=True)
    production = models.ForeignKey(ProductionModel, verbose_name='作品ID', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'DataSet_ProcessModel_block'


class ProcessModel2(models.Model):
    spr_type = models.CharField(max_length=100, verbose_name='操作类型', blank=True, null=True)
    spr_name = models.CharField(max_length=100, verbose_name='角色名称', blank=True, null=True)
    spr_from = models.CharField(max_length=100, verbose_name='角色来源', blank=True, null=True)
    time = models.DateTimeField(verbose_name='操作时间', blank=True, null=True)
    production = models.ForeignKey(ProductionModel, verbose_name='作品ID', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'DataSet_ProcessModel_sprite'


class ProcessModel3(models.Model):
    op_type = models.CharField(max_length=100, verbose_name='操作方式', blank=True, null=True)
    obj_type = models.CharField(max_length=100, verbose_name='资源类型', blank=True, null=True)
    obj_name = models.CharField(max_length=100, verbose_name='资源名称', blank=True, null=True)
    obj_from = models.CharField(max_length=100, verbose_name='资源来源', blank=True, null=True)
    time = models.DateTimeField(verbose_name='操作时间', blank=True, null=True)
    production = models.ForeignKey(ProductionModel, verbose_name='作品ID', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'DataSet_ProcessModel_backdrop_sound_costume'
