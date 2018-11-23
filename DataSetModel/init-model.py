# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Ctmodel(models.Model):
    ap_score = models.IntegerField()
    parallelism_score = models.IntegerField()
    synchronization_score = models.IntegerField()
    flow_control_score = models.IntegerField()
    user_interactivity_score = models.IntegerField()
    logical_thinking_score = models.IntegerField()
    data_representation_score = models.IntegerField()
    total = models.IntegerField()
    code_organization_score = models.IntegerField()
    content_score = models.IntegerField()
    hint = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'CTModel'


class OjProblem(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    input_description = models.TextField()
    output_description = models.TextField()
    hint = models.CharField(max_length=100, blank=True, null=True)
    permission = models.CharField(max_length=2)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    time_limit = models.IntegerField()
    memory_limit = models.IntegerField()
    submission_number = models.IntegerField()
    accepted_number = models.IntegerField()
    acrate = models.FloatField(db_column='ACrate')  # Field name made lowercase.
    level = models.CharField(max_length=10)
    author = models.ForeignKey('ScratchApiTeacher', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'OJ_problem'


class OjProblemClasses(models.Model):
    problem = models.ForeignKey(OjProblem, models.DO_NOTHING)
    formatclass = models.ForeignKey('ScratchApiFormatclass', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'OJ_problem_classes'
        unique_together = (('problem', 'formatclass'),)


class OjProblemTags(models.Model):
    problem = models.ForeignKey(OjProblem, models.DO_NOTHING)
    tag = models.ForeignKey('OjTag', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'OJ_problem_tags'
        unique_together = (('problem', 'tag'),)


class OjSubmission(models.Model):
    submission_time = models.DateTimeField()
    code = models.TextField()
    result = models.IntegerField()
    info = models.TextField()
    language = models.CharField(max_length=20)
    problem = models.ForeignKey(OjProblem, models.DO_NOTHING)
    user = models.ForeignKey('ScratchApiUser', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'OJ_submission'


class OjSubmissiondailystatistical(models.Model):
    submission_day = models.DateField()
    submission_count = models.IntegerField()
    user = models.ForeignKey('ScratchApiUser', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'OJ_submissiondailystatistical'


class OjTag(models.Model):
    name = models.CharField(max_length=10)
    count = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'OJ_tag'


class OjTestcase(models.Model):
    order = models.IntegerField()
    input_test = models.CharField(max_length=100)
    output_test = models.CharField(max_length=100)
    problem = models.ForeignKey(OjProblem, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'OJ_testcase'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = True
        db_table = 'auth_group'


class AuthGroup1(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = True
        db_table = 'auth_group1'


class AuthPermission(models.Model):
    name = models.CharField(max_length=50)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'auth_permission'


class AuthPermission1(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType1', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'auth_permission1'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'auth_user_groups'


class AuthtokenToken1(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.ForeignKey('ScratchApiBaseuser', models.DO_NOTHING, unique=True)

    class Meta:
        managed = True
        db_table = 'authtoken_token1'


class AvatarAvatar1(models.Model):
    primary = models.IntegerField()
    avatar = models.CharField(max_length=1024)
    date_uploaded = models.DateTimeField()
    user = models.ForeignKey('ScratchApiBaseuser', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'avatar_avatar1'


class CourseChapter(models.Model):
    chapter_id = models.IntegerField()
    name = models.CharField(max_length=50)
    content = models.TextField()
    audio = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    lesson = models.ForeignKey('CourseLesson', models.DO_NOTHING)
    order = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'course_chapter'
        unique_together = (('lesson', 'name'),)


class CourseLesson(models.Model):
    lesson_id = models.IntegerField(unique=True)
    name = models.CharField(unique=True, max_length=50)
    introduction = models.TextField()
    short_introduction = models.TextField(blank=True, null=True)
    audio = models.CharField(max_length=100, blank=True, null=True)
    image = models.CharField(max_length=100)
    author = models.ForeignKey('ScratchApiTeacher', models.DO_NOTHING, blank=True, null=True)
    permission = models.CharField(max_length=2)
    task = models.TextField()

    class Meta:
        managed = True
        db_table = 'course_lesson'


class CourseLessonClasses(models.Model):
    lesson = models.ForeignKey(CourseLesson, models.DO_NOTHING)
    formatclass = models.ForeignKey('ScratchApiFormatclass', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'course_lesson_classes'
        unique_together = (('lesson', 'formatclass'),)


class CourseUserbehaviorlesson(models.Model):
    user = models.CharField(max_length=50)
    lesson_id = models.IntegerField()
    chapter_id = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    click_audio = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'course_userbehaviorlesson'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'django_admin_log'


class DjangoAdminLog1(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType1', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('ScratchApiBaseuser', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'django_admin_log1'


class DjangoCommentFlags1(models.Model):
    flag = models.CharField(max_length=30)
    flag_date = models.DateTimeField()
    comment = models.ForeignKey('DjangoComments1', models.DO_NOTHING)
    user = models.ForeignKey('ScratchApiBaseuser', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'django_comment_flags1'
        unique_together = (('user', 'comment', 'flag'),)


class DjangoComments1(models.Model):
    object_pk = models.TextField()
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=254)
    user_url = models.CharField(max_length=200)
    comment = models.TextField()
    submit_date = models.DateTimeField()
    ip_address = models.CharField(max_length=39, blank=True, null=True)
    is_public = models.IntegerField()
    is_removed = models.IntegerField()
    content_type = models.ForeignKey('DjangoContentType1', models.DO_NOTHING)
    site = models.ForeignKey('DjangoSite1', models.DO_NOTHING)
    user = models.ForeignKey('ScratchApiBaseuser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'django_comments1'


class DjangoContentType(models.Model):
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoContentType1(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'django_content_type1'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations'


class DjangoMigrations1(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations1'


class DjangoSession1(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_session1'


class DjangoSite1(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'django_site1'


class GuardianGroupobjectpermission1(models.Model):
    object_pk = models.CharField(max_length=255)
    content_type = models.ForeignKey(DjangoContentType1, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup1, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission1, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'guardian_groupobjectpermission1'
        unique_together = (('group', 'permission', 'object_pk'),)


class GuardianUserobjectpermission1(models.Model):
    object_pk = models.CharField(max_length=255)
    content_type = models.ForeignKey(DjangoContentType1, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission1, models.DO_NOTHING)
    user = models.ForeignKey('ScratchApiBaseuser', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'guardian_userobjectpermission1'
        unique_together = (('user', 'permission', 'object_pk'),)


class PinaxBadgesBadgeaward1(models.Model):
    awarded_at = models.DateTimeField()
    slug = models.CharField(max_length=255)
    level = models.IntegerField()
    user = models.ForeignKey('ScratchApiBaseuser', models.DO_NOTHING)
    image = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'pinax_badges_badgeaward1'


class ProductionProcessListtest(models.Model):
    labels = models.TextField()

    class Meta:
        managed = True
        db_table = 'production_process_listtest'


class ProductionProcessProductionListforaddblock(models.Model):
    time = models.DateTimeField()
    type = models.CharField(max_length=100)
    op = models.CharField(max_length=100)
    loc = models.CharField(max_length=100)
    productions = models.ForeignKey('ScratchApiProduction', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'production_process_production_listforaddblock'


class ProductionProcessProductionListforbackdrop(models.Model):
    addbac_time = models.DateTimeField()
    addbac_add = models.CharField(max_length=100)
    addbac_odd = models.CharField(max_length=100)
    addbac_name = models.CharField(max_length=100)
    addbac_from = models.CharField(max_length=100)
    productions = models.ForeignKey('ScratchApiProduction', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'production_process_production_listforbackdrop'


class ProductionProcessProductionListforchange(models.Model):
    change_time = models.DateTimeField()
    change_change = models.CharField(max_length=100)
    change_odd = models.CharField(max_length=100)
    change_pername = models.CharField(max_length=100)
    change_nowname = models.CharField(max_length=100)
    productions = models.ForeignKey('ScratchApiProduction', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'production_process_production_listforchange'


class ProductionProcessProductionListforchangeop(models.Model):
    change_time = models.DateTimeField()
    change_change = models.CharField(max_length=100)
    change_odd = models.CharField(max_length=100)
    change_perop = models.CharField(max_length=100)
    change_nowop = models.CharField(max_length=100)
    productions = models.ForeignKey('ScratchApiProduction', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'production_process_production_listforchangeop'


class ProductionProcessProductionListforcostume(models.Model):
    addcos_time = models.DateTimeField()
    addcos_add = models.CharField(max_length=100)
    addcos_odd = models.CharField(max_length=100)
    addcos_name = models.CharField(max_length=100)
    addcos_from = models.CharField(max_length=100)
    productions = models.ForeignKey('ScratchApiProduction', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'production_process_production_listforcostume'


class ProductionProcessProductionListfordelbac(models.Model):
    delbac_time = models.DateTimeField()
    delbac_del = models.CharField(max_length=100)
    delbac_odd = models.CharField(max_length=100)
    delbac_name = models.CharField(max_length=100)
    delbac_from = models.CharField(max_length=100)
    productions = models.ForeignKey('ScratchApiProduction', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'production_process_production_listfordelbac'


class ProductionProcessProductionListfordelblock(models.Model):
    del_time = models.DateTimeField()
    del_del = models.CharField(max_length=100)
    del_op = models.CharField(max_length=100)
    productions = models.ForeignKey('ScratchApiProduction', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'production_process_production_listfordelblock'


class ProductionProcessProductionListfordelcos(models.Model):
    delcos_time = models.DateTimeField()
    delcos_del = models.CharField(max_length=100)
    delcos_odd = models.CharField(max_length=100)
    delcos_name = models.CharField(max_length=100)
    delcos_from = models.CharField(max_length=100)
    productions = models.ForeignKey('ScratchApiProduction', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'production_process_production_listfordelcos'


class ProductionProcessProductionListfordelsnd(models.Model):
    delsnd_time = models.DateTimeField()
    delsnd_del = models.CharField(max_length=100)
    delsnd_odd = models.CharField(max_length=100)
    delsnd_name = models.CharField(max_length=100)
    delsnd_from = models.CharField(max_length=100)
    productions = models.ForeignKey('ScratchApiProduction', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'production_process_production_listfordelsnd'


class ProductionProcessProductionListfordelspr(models.Model):
    delspr_time = models.DateTimeField()
    delspr_del = models.CharField(max_length=100)
    delspr_odd = models.CharField(max_length=100)
    delspr_name = models.CharField(max_length=100)
    delspr_from = models.CharField(max_length=100)
    productions = models.ForeignKey('ScratchApiProduction', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'production_process_production_listfordelspr'


class ProductionProcessProductionListfordoubleclickblock(models.Model):
    dou_time = models.DateTimeField()
    dou_name = models.CharField(max_length=100)
    dou_odd = models.CharField(max_length=100)
    dou_op = models.CharField(max_length=100)
    productions = models.ForeignKey('ScratchApiProduction', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'production_process_production_listfordoubleclickblock'


class ProductionProcessProductionListforsound(models.Model):
    addsnd_time = models.DateTimeField()
    addsnd_add = models.CharField(max_length=100)
    addsnd_odd = models.CharField(max_length=100)
    addsnd_name = models.CharField(max_length=100)
    addsnd_from = models.CharField(max_length=100)
    productions = models.ForeignKey('ScratchApiProduction', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'production_process_production_listforsound'


class ProductionProcessProductionListforspr(models.Model):
    addspr_time = models.DateTimeField()
    addspr_add = models.CharField(max_length=100)
    addspr_odd = models.CharField(max_length=100)
    addspr_name = models.CharField(max_length=100)
    addspr_from = models.CharField(max_length=100)
    productions = models.ForeignKey('ScratchApiProduction', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'production_process_production_listforspr'


class ProductionProcessProductionProsess(models.Model):
    listforaddblock = models.TextField(blank=True, null=True)
    production_id = models.ForeignKey('ScratchApiProduction', models.DO_NOTHING, unique=True)
    listforbackdrop = models.TextField(db_column='listforBackdrop', blank=True, null=True)  # Field name made lowercase.
    listforchange = models.TextField(db_column='listforChange', blank=True, null=True)  # Field name made lowercase.
    listforchangeop = models.TextField(db_column='listforChangeOp', blank=True, null=True)  # Field name made lowercase.
    listforcostume = models.TextField(db_column='listforCostume', blank=True, null=True)  # Field name made lowercase.
    listfordoubleclickblock = models.TextField(db_column='listforDoubleclickBlock', blank=True, null=True)  # Field name made lowercase.
    listforsound = models.TextField(db_column='listforSound', blank=True, null=True)  # Field name made lowercase.
    listforspr = models.TextField(db_column='listforSpr', blank=True, null=True)  # Field name made lowercase.
    listfordelbac = models.TextField(blank=True, null=True)
    listfordelblock = models.TextField(blank=True, null=True)
    listfordelcos = models.TextField(blank=True, null=True)
    listfordelsnd = models.TextField(blank=True, null=True)
    listfordelspr = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'production_process_production_prosess'


class QaAnswer(models.Model):
    answer_text = models.TextField()
    pub_date = models.DateTimeField()
    updated = models.DateTimeField()
    answer = models.IntegerField()
    positive_votes = models.IntegerField()
    negative_votes = models.IntegerField()
    total_points = models.IntegerField()
    question = models.ForeignKey('QaQuestion', models.DO_NOTHING)
    user = models.ForeignKey('ScratchApiBaseuser', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'qa_answer'
        unique_together = (('user', 'question'),)


class QaAnswervote(models.Model):
    value = models.IntegerField()
    answer = models.ForeignKey(QaAnswer, models.DO_NOTHING)
    user = models.ForeignKey('ScratchApiBaseuser', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'qa_answervote'
        unique_together = (('user', 'answer'),)


class QaQuestion(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField()
    update_date = models.DateTimeField()
    closed = models.IntegerField()
    positive_votes = models.IntegerField()
    negative_votes = models.IntegerField()
    total_points = models.IntegerField()
    user = models.ForeignKey('ScratchApiBaseuser', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'qa_question'


class QaQuestionvote(models.Model):
    value = models.IntegerField()
    question = models.ForeignKey(QaQuestion, models.DO_NOTHING)
    user = models.ForeignKey('ScratchApiBaseuser', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'qa_questionvote'
        unique_together = (('user', 'question'),)


class ScratchApiAdviser(models.Model):
    teacher_ptr = models.ForeignKey('ScratchApiTeacher', models.DO_NOTHING, primary_key=True)
    local_province = models.CharField(max_length=30, blank=True, null=True)
    local_city = models.CharField(max_length=30, blank=True, null=True)
    local_district = models.CharField(max_length=30, blank=True, null=True)
    is_boss = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'scratch_api_adviser'


class ScratchApiAnticheating(models.Model):
    time = models.DateTimeField()
    competition = models.ForeignKey('ScratchApiCompetition', models.DO_NOTHING)
    user = models.ForeignKey('ScratchApiUser', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'scratch_api_anticheating'


class ScratchApiAntlrscore(models.Model):
    ap_score = models.IntegerField()
    parallelism_score = models.IntegerField()
    synchronization_score = models.IntegerField()
    flow_control_score = models.IntegerField()
    user_interactivity_score = models.IntegerField()
    logical_thinking_score = models.IntegerField()
    data_representation_score = models.IntegerField()
    production_id = models.ForeignKey('ScratchApiProduction', models.DO_NOTHING, unique=True)
    total = models.IntegerField()
    code_organization_score = models.IntegerField()
    content_score = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'scratch_api_antlrscore'


class ScratchApiBaseuser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    username = models.CharField(primary_key=True, max_length=30)
    is_admin = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'scratch_api_baseuser'


class ScratchApiBaseuser2Session(models.Model):
    session_key = models.CharField(max_length=40)
    user = models.ForeignKey(ScratchApiBaseuser, models.DO_NOTHING, unique=True)

    class Meta:
        managed = True
        db_table = 'scratch_api_baseuser2session'


class ScratchApiBaseuserGroups(models.Model):
    baseuser = models.ForeignKey(ScratchApiBaseuser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup1, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'scratch_api_baseuser_groups'
        unique_together = (('baseuser', 'group'),)


class ScratchApiBaseuserUserPermissions(models.Model):
    baseuser = models.ForeignKey(ScratchApiBaseuser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission1, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'scratch_api_baseuser_user_permissions'
        unique_together = (('baseuser', 'permission'),)


class ScratchApiClass(models.Model):
    class_name = models.CharField(max_length=40)
    school_name = models.ForeignKey('ScratchApiSchool', models.DO_NOTHING)
    code = models.CharField(max_length=6)

    class Meta:
        managed = True
        db_table = 'scratch_api_class'
        unique_together = (('school_name', 'class_name'),)


class ScratchApiClassTeacher(models.Model):
    class_field = models.ForeignKey(ScratchApiClass, models.DO_NOTHING, db_column='class_id')  # Field renamed because it was a Python reserved word.
    teacher = models.ForeignKey('ScratchApiTeacher', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'scratch_api_class_teacher'
        unique_together = (('class_field', 'teacher'),)


class ScratchApiCommenteachother(models.Model):
    comment_score = models.IntegerField()
    production = models.ForeignKey('ScratchApiProduction', models.DO_NOTHING)
    user = models.ForeignKey('ScratchApiUser', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'scratch_api_commenteachother'


class ScratchApiCompetition(models.Model):
    title = models.CharField(unique=True, max_length=100)
    create_time = models.DateTimeField()
    start_time = models.DateTimeField(blank=True, null=True)
    stop_time = models.DateTimeField(blank=True, null=True)
    content = models.CharField(max_length=100, blank=True, null=True)
    creator = models.ForeignKey('ScratchApiTeacher', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'scratch_api_competition'


class ScratchApiCompetitionAdvisers(models.Model):
    competition = models.ForeignKey(ScratchApiCompetition, models.DO_NOTHING)
    adviser = models.ForeignKey(ScratchApiAdviser, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'scratch_api_competition_advisers'
        unique_together = (('competition', 'adviser'),)


class ScratchApiCompetitionRater(models.Model):
    competition = models.ForeignKey(ScratchApiCompetition, models.DO_NOTHING)
    teacher = models.ForeignKey('ScratchApiTeacher', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'scratch_api_competition_rater'
        unique_together = (('competition', 'teacher'),)


class ScratchApiCompetitionquestion(models.Model):
    question = models.CharField(max_length=100)
    detail = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField()
    competition = models.ForeignKey(ScratchApiCompetition, models.DO_NOTHING)
    limit_score = models.IntegerField()
    limit_small_score = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'scratch_api_competitionquestion'


class ScratchApiCompetitionquestionProduction(models.Model):
    competitionquestion = models.ForeignKey(ScratchApiCompetitionquestion, models.DO_NOTHING)
    production = models.ForeignKey('ScratchApiProduction', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'scratch_api_competitionquestion_production'
        unique_together = (('competitionquestion', 'production'),)


class ScratchApiCompetitionuser(models.Model):
    competition = models.ForeignKey(ScratchApiCompetition, models.DO_NOTHING)
    tutor = models.ForeignKey('ScratchApiTeacher', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('ScratchApiUser', models.DO_NOTHING)
    delay_time = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'scratch_api_competitionuser'
        unique_together = (('competition', 'user'),)


class ScratchApiDatavisualization(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=500)
    create_time = models.DateTimeField()
    description = models.TextField()
    fileurl = models.CharField(db_column='fileUrl', max_length=500)  # Field name made lowercase.
    is_active = models.IntegerField()
    charttitle1 = models.CharField(db_column='chartTitle1', max_length=50)  # Field name made lowercase.
    chartanalysistitle1 = models.CharField(db_column='chartAnalysisTitle1', max_length=50)  # Field name made lowercase.
    chartanalysisdescription1 = models.TextField(db_column='chartAnalysisDescription1', blank=True, null=True)  # Field name made lowercase.
    chartfileurl1 = models.CharField(db_column='chartFileUrl1', max_length=500)  # Field name made lowercase.
    charttitle2 = models.CharField(db_column='chartTitle2', max_length=50)  # Field name made lowercase.
    chartanalysistitle2 = models.CharField(db_column='chartAnalysisTitle2', max_length=50)  # Field name made lowercase.
    chartanalysisdescription2 = models.TextField(db_column='chartAnalysisDescription2', blank=True, null=True)  # Field name made lowercase.
    chartfileurl2 = models.CharField(db_column='chartFileUrl2', max_length=500)  # Field name made lowercase.
    charttitle3 = models.CharField(db_column='chartTitle3', max_length=50)  # Field name made lowercase.
    chartanalysistitle3 = models.CharField(db_column='chartAnalysisTitle3', max_length=50)  # Field name made lowercase.
    chartanalysisdescription3 = models.TextField(db_column='chartAnalysisDescription3', blank=True, null=True)  # Field name made lowercase.
    chartfileurl3 = models.CharField(db_column='chartFileUrl3', max_length=500)  # Field name made lowercase.
    charttitle4 = models.CharField(db_column='chartTitle4', max_length=50)  # Field name made lowercase.
    chartanalysistitle4 = models.CharField(db_column='chartAnalysisTitle4', max_length=50)  # Field name made lowercase.
    chartanalysisdescription4 = models.TextField(db_column='chartAnalysisDescription4', blank=True, null=True)  # Field name made lowercase.
    chartfileurl4 = models.CharField(db_column='chartFileUrl4', max_length=500)  # Field name made lowercase.
    uploader = models.ForeignKey(ScratchApiBaseuser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'scratch_api_datavisualization'


class ScratchApiDownloadsource(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    fileurl = models.CharField(db_column='fileUrl', max_length=500)  # Field name made lowercase.
    is_active = models.IntegerField()
    uploader = models.ForeignKey(ScratchApiBaseuser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'scratch_api_downloadsource'


class ScratchApiFavoritegallery(models.Model):
    favorite_time = models.TimeField()
    gallery = models.ForeignKey('ScratchApiGallery', models.DO_NOTHING)
    user = models.ForeignKey('ScratchApiUser', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'scratch_api_favoritegallery'


class ScratchApiFavoriteproduction(models.Model):
    favorite_time = models.TimeField()
    production = models.ForeignKey('ScratchApiProduction', models.DO_NOTHING)
    user = models.ForeignKey('ScratchApiUser', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'scratch_api_favoriteproduction'


class ScratchApiFormatclass(models.Model):
    grade = models.IntegerField()
    class_num = models.IntegerField()
    is_interest = models.IntegerField()
    add_time = models.DateTimeField()
    is_active = models.IntegerField()
    chief = models.ForeignKey('ScratchApiTeacher', models.DO_NOTHING)
    format_school = models.ForeignKey('ScratchApiFormatschool', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'scratch_api_formatclass'
        unique_together = (('format_school', 'grade', 'class_num', 'is_interest'),)


class ScratchApiFormatschool(models.Model):
    name = models.CharField(max_length=20)
    province = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    district = models.CharField(max_length=20)
    add_time = models.DateTimeField()
    is_active = models.IntegerField()
    chief = models.ForeignKey('ScratchApiTeacher', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'scratch_api_formatschool'
        unique_together = (('province', 'city', 'district', 'name'),)


class ScratchApiGallery(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=50)
    is_active = models.IntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    image = models.CharField(max_length=100, blank=True, null=True)
    hit = models.BigIntegerField()
    like = models.BigIntegerField()
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(ScratchApiBaseuser, models.DO_NOTHING, blank=True, null=True)
    start_time = models.DateTimeField()
    stop_time = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'scratch_api_gallery'


class ScratchApiGalleryproduction(models.Model):
    admin_checked = models.IntegerField()
    gallery = models.ForeignKey(ScratchApiGallery, models.DO_NOTHING)
    production = models.ForeignKey('ScratchApiProduction', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'scratch_api_galleryproduction'


class ScratchApiLikegallery(models.Model):
    token = models.CharField(max_length=50, blank=True, null=True)
    favorite_time = models.TimeField()
    gallery = models.ForeignKey(ScratchApiGallery, models.DO_NOTHING)
    user = models.ForeignKey(ScratchApiBaseuser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'scratch_api_likegallery'
        unique_together = (('user', 'gallery', 'token'),)


class ScratchApiLikeproduction(models.Model):
    token = models.CharField(max_length=50, blank=True, null=True)
    favorite_time = models.TimeField()
    production = models.ForeignKey('ScratchApiProduction', models.DO_NOTHING)
    user = models.ForeignKey(ScratchApiBaseuser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'scratch_api_likeproduction'
        unique_together = (('user', 'production', 'token'),)


class ScratchApiPosition(models.Model):
    name = models.CharField(max_length=100)
    permissions = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'scratch_api_position'


class ScratchApiProduction(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=50)
    file = models.CharField(max_length=100)
    is_active = models.IntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    image = models.CharField(max_length=100, blank=True, null=True)
    author = models.ForeignKey('ScratchApiUser', models.DO_NOTHING, blank=True, null=True)
    belong_to = models.ForeignKey(ScratchApiClass, models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    comment_eachother_all_score = models.IntegerField()
    hit = models.BigIntegerField()
    lesson = models.ForeignKey(CourseLesson, models.DO_NOTHING, blank=True, null=True)
    level = models.IntegerField()
    lft = models.IntegerField()
    like = models.BigIntegerField()
    operation_instructions = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    rght = models.IntegerField()
    tree_id = models.IntegerField()
    production_duration = models.IntegerField()
    script_count = models.IntegerField()
    sprite_count = models.IntegerField()
    is_competition = models.IntegerField()
    format_class = models.ForeignKey(ScratchApiFormatclass, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'scratch_api_production'


class ScratchApiProductionProfile(models.Model):
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
    production_id = models.ForeignKey(ScratchApiProduction, models.DO_NOTHING, unique=True)

    class Meta:
        managed = True
        db_table = 'scratch_api_production_profile'


class ScratchApiProductionhint(models.Model):
    hint = models.CharField(max_length=100)
    production_id = models.ForeignKey(ScratchApiProduction, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'scratch_api_productionhint'


class ScratchApiQuestionproductionscore(models.Model):
    score = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    score_time = models.DateTimeField()
    production = models.ForeignKey(ScratchApiProduction, models.DO_NOTHING)
    question = models.ForeignKey(ScratchApiCompetitionquestion, models.DO_NOTHING)
    rater = models.ForeignKey('ScratchApiTeacher', models.DO_NOTHING)
    is_adviser = models.IntegerField()
    small_score = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'scratch_api_questionproductionscore'


class ScratchApiSchool(models.Model):
    school_name = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = True
        db_table = 'scratch_api_school'


class ScratchApiTeacher(models.Model):
    baseuser_ptr = models.ForeignKey(ScratchApiBaseuser, models.DO_NOTHING, primary_key=True)
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    school = models.CharField(max_length=50)
    position = models.ForeignKey(ScratchApiPosition, models.DO_NOTHING, blank=True, null=True)
    belong_adviser = models.ForeignKey(ScratchApiAdviser, models.DO_NOTHING, blank=True, null=True)
    format_school = models.ForeignKey(ScratchApiFormatschool, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'scratch_api_teacher'


class ScratchApiTeacherscore(models.Model):
    score = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    production_id = models.ForeignKey(ScratchApiProduction, models.DO_NOTHING, unique=True)

    class Meta:
        managed = True
        db_table = 'scratch_api_teacherscore'


class ScratchApiUser(models.Model):
    baseuser_ptr = models.ForeignKey(ScratchApiBaseuser, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=30)
    sex = models.CharField(max_length=30, blank=True, null=True)
    grade = models.CharField(max_length=30, blank=True, null=True)
    student_id = models.CharField(max_length=30, blank=True, null=True)
    created_at = models.DateTimeField()
    school = models.ForeignKey(ScratchApiSchool, models.DO_NOTHING, related_name='school', blank=True, null=True)
    school_second = models.ForeignKey(ScratchApiSchool, models.DO_NOTHING, related_name='school_second', blank=True, null=True)
    student_class = models.ForeignKey(ScratchApiClass, models.DO_NOTHING, related_name='student_class', blank=True, null=True)
    student_class_second = models.ForeignKey(ScratchApiClass, models.DO_NOTHING, related_name='student_class_second', blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    local_city = models.CharField(max_length=30, blank=True, null=True)
    local_district = models.CharField(max_length=30, blank=True, null=True)
    local_province = models.CharField(max_length=30, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    self_introduction = models.TextField(blank=True, null=True)
    coding_duration = models.IntegerField()
    enrollment_number = models.CharField(unique=True, max_length=20, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    format_school = models.ForeignKey(ScratchApiFormatschool, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'scratch_api_user'


class ScratchApiUserClasses(models.Model):
    user = models.ForeignKey(ScratchApiUser, models.DO_NOTHING)
    class_field = models.ForeignKey(ScratchApiClass, models.DO_NOTHING, db_column='class_id')  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = True
        db_table = 'scratch_api_user_classes'
        unique_together = (('user', 'class_field'),)


class ScratchApiUserFormatClass(models.Model):
    user = models.ForeignKey(ScratchApiUser, models.DO_NOTHING)
    formatclass = models.ForeignKey(ScratchApiFormatclass, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'scratch_api_user_format_class'
        unique_together = (('user', 'formatclass'),)


class ScratchApiUuidtaggeditem(models.Model):
    object_id = models.CharField(max_length=32)
    content_type = models.ForeignKey(DjangoContentType1, models.DO_NOTHING)
    tag = models.ForeignKey('TaggitTag', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'scratch_api_uuidtaggeditem'


class TaggitTag(models.Model):
    name = models.CharField(unique=True, max_length=100)
    slug = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = True
        db_table = 'taggit_tag'


class TaggitTaggeditem(models.Model):
    object_id = models.IntegerField()
    content_type = models.ForeignKey(DjangoContentType1, models.DO_NOTHING)
    tag = models.ForeignKey(TaggitTag, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'taggit_taggeditem'


class ThreadedcommentsComment1(models.Model):
    comment_ptr = models.ForeignKey(DjangoComments1, models.DO_NOTHING, primary_key=True)
    title = models.TextField()
    tree_path = models.CharField(max_length=500)
    last_child = models.ForeignKey('self', models.DO_NOTHING, related_name='last_child1', blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, related_name='parent1', blank=True, null=True)
    newest_activity = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'threadedcomments_comment1'


class WebshellScript1(models.Model):
    name = models.CharField(max_length=100)
    source = models.TextField()

    class Meta:
        managed = True
        db_table = 'webshell_script1'
