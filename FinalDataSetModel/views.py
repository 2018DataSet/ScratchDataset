# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from DataSetModel.models import ScratchApiProduction, ScratchApiAntlrscore, ScratchApiProductionhint, \
    CourseUserbehaviorlesson, ScratchApiUser, ScratchApiTeacher, ScratchApiClassTeacher, CourseLesson, \
    ScratchApiCompetition, ScratchApiQuestionproductionscore, CourseChapter, ScratchApiProduction, \
    ScratchApiProductionProfile, ProductionProcessProductionListforaddblock, ProductionProcessProductionListfordelblock, \
    ProductionProcessProductionListfordelspr, ProductionProcessProductionListforspr, \
    ProductionProcessProductionListforbackdrop, ProductionProcessProductionListforsound, \
    ProductionProcessProductionListforcostume, ProductionProcessProductionListfordelcos, \
    ProductionProcessProductionListfordelsnd, ProductionProcessProductionListfordelbac, ScratchApiLikeproduction, \
    ScratchApiFavoriteproduction, ScratchApiUuidtaggeditem, TaggitTag
from .models import StudentModel, TeacherModel, CTModel, LearnModel, KnowModel, KnowModel1, ProductionModel, \
    ProductionModelSb2Profile, ProcessModel1, ProcessModel2, ProcessModel3

"""
test10
"""


def ProcessModel3Trans(request):
    # bb = ProductionProcessProductionListforbackdrop.objects.all()
    # for b in bb:
    #     object = ProcessModel3()
    #     object.production = ProductionModel.objects.get(id=b.productions_id)
    #     object.op_type = b.addbac_add
    #     object.obj_type = b.addbac_odd
    #     object.obj_name = b.addbac_name
    #     object.obj_from = b.addbac_from
    #     object.time = b.addbac_time
    #     object.save()
    # bb1 = ProductionProcessProductionListfordelbac.objects.all()
    # for b1 in bb1:
    #     object1 = ProcessModel3()
    #     object1.production = ProductionModel.objects.get(id=b1.productions_id)
    #     object1.op_type = b1.delbac_del
    #     object1.obj_type = b1.delbac_odd
    #     object1.obj_name = b1.delbac_name
    #     object1.obj_from = b1.delbac_from
    #     object1.time = b1.delbac_time
    #     object1.save()
    # bb2 = ProductionProcessProductionListforsound.objects.all()
    # for b2 in bb2:
    #     object2 = ProcessModel3()
    #     object2.production = ProductionModel.objects.get(id=b2.productions_id)
    #     object2.op_type = b2.addsnd_add
    #     object2.obj_type = b2.addsnd_odd
    #     object2.obj_name = b2.addsnd_name
    #     object2.obj_from = b2.addsnd_from
    #     object2.time = b2.addsnd_time
    #     object2.save()
    # bb3 = ProductionProcessProductionListfordelsnd.objects.all()
    # for b3 in bb3:
    #     object3 = ProcessModel3()
    #     object3.production = ProductionModel.objects.get(id=b3.productions_id)
    #     object3.op_type = b3.delsnd_del
    #     object3.obj_type = b3.delsnd_odd
    #     object3.obj_name = b3.delsnd_name
    #     object3.obj_from = b3.delsnd_from
    #     object3.time = b3.delsnd_time
    #     object3.save()
    # bb4 = ProductionProcessProductionListforcostume.objects.all()
    # for b4 in bb4:
    #     object4 = ProcessModel3()
    #     object4.production = ProductionModel.objects.get(id=b4.productions_id)
    #     object4.op_type = b4.addcos_add
    #     object4.obj_type = b4.addcos_odd
    #     object4.obj_name = b4.addcos_name
    #     object4.obj_from = b4.addcos_from
    #     object4.time = b4.addcos_time
    #     object4.save()
    # bb5 = ProductionProcessProductionListfordelcos.objects.all()
    # for b5 in bb5:
    #     object5 = ProcessModel3()
    #     object5.production = ProductionModel.objects.get(id=b5.productions_id)
    #     object5.op_type = b5.delcos_del
    #     object5.obj_type = b5.delcos_odd
    #     object5.obj_name = b5.delcos_name
    #     object5.obj_from = b5.delcos_from
    #     object5.time = b5.delcos_time
    #     object5.save()
    return HttpResponse(str(ProductionProcessProductionListforbackdrop.objects.count()) + str('s/c') + str(
        ProcessModel3.objects.count()))


"""
test9
"""


def ProcessModel2Trans(request):
    # bb = ProductionProcessProductionListforspr.objects.all()
    # for b in bb:
    #     object = ProcessModel2()
    #     object.production = ProductionModel.objects.get(id=b.productions_id)
    #     object.spr_type = b.addspr_add
    #     object.spr_name = b.addspr_name
    #     object.spr_from = b.addspr_from
    #     object.time = b.addspr_time
    #     object.save()
    # bb1 = ProductionProcessProductionListfordelspr.objects.all()
    # for b1 in bb1:
    #     object1 = ProcessModel2()
    #     object1.production = ProductionModel.objects.get(id=b1.productions_id)
    #     object1.spr_type = b1.delspr_del
    #     object1.spr_name = b1.delspr_name
    #     object1.spr_from = b1.delspr_from
    #     object1.time = b1.delspr_time
    #     object1.save()
    return HttpResponse(str(
        ProductionProcessProductionListforspr.objects.count() + ProductionProcessProductionListfordelspr.objects.count()) + str(
        's/c') + str(
        ProcessModel2.objects.count()))


"""
test8
"""


def ProcessModel1Trans(request):
    # bb1 = ProductionProcessProductionListfordelblock.objects.all()
    # for b1 in bb1:
    #     object1 = ProcessModel1()
    #     object1.production = ProductionModel.objects.get(id=b1.productions_id)
    #     object1.type = b1.del_del
    #     object1.op = b1.del_op
    #     object1.time = b1.del_time
    #     object1.save()
    # bb = ProductionProcessProductionListforaddblock.objects.all()
    # for b in bb:
    #     object = ProcessModel1()
    #     object.production = ProductionModel.objects.get(id=b.productions_id)
    #     object.type = b.type
    #     object.op = b.op
    #     object.loc = b.loc
    #     object.time = b.time
    #     object.save()

    return HttpResponse(str(ProductionProcessProductionListforaddblock.objects.count()+ProductionProcessProductionListfordelblock.objects.count()) + str('s/c') + str(
        ProcessModel1.objects.count()))


"""
test7
"""


def ProductionModelSb2ProfileTrans(request):
    # ProductionModelSb2Profile.objects.all().delete()
    # pp = ScratchApiProductionProfile.objects.all()
    # for p in pp:
    #     object = ProductionModelSb2Profile()
    #     object.production_id = ProductionModel.objects.get(id=p.production_id_id)
    #     object.motion_num = p.motion_num
    #     object.looklike_num = p.looklike_num
    #     object.sounds_num = p.sounds_num
    #     object.draw_num = p.draw_num
    #     object.event_num = p.event_num
    #     object.control_num = p.control_num
    #     object.sensor_num = p.sensor_num
    #     object.operate_num = p.operate_num
    #     object.more_num = p.more_num
    #     object.data_num = p.data_num
    #     object.sprite_num = p.sprite_num
    #     object.backdrop_num = p.backdrop_num
    #     object.snd_num = p.snd_num
    #     object.save()
    return HttpResponse(
        str(ScratchApiProductionProfile.objects.count()) + str('s/c') + str(ProductionModelSb2Profile.objects.count()))


"""
test6
"""


def ProductionModelTrans(request):
    # ProductionModel.objects.all().delete()
    # 计算点赞、收藏次数
    # hh = ScratchApiLikeproduction.objects.all()
    # for h in hh:
    #     id = h.production_id
    #     if ProductionModel.objects.filter(id=id).exists():
    #         p = ProductionModel.objects.get(id=id)
    #         p.liketimes += 1
    #         p.save()
    # ff = ScratchApiFavoriteproduction.objects.all()
    # for f in ff:
    #     id1 = f.production_id
    #     if ProductionModel.objects.filter(id=id1).exists():
    #         p1 = ProductionModel.objects.get(id=id1)
    #         p1.favtimes += 1
    #         p1.save()

    # 计算改编次数
    # rr = ProductionModel.objects.all()
    # for r in rr:
    #     if r.parent_id:
    #         if ProductionModel.objects.filter(id=r.parent_id).exists():
    #             production = ProductionModel.objects.get(id=r.parent_id)
    #             production.remixedtimes += 1
    #             production.save()

    # 计算作品类别
    # tt = ScratchApiUuidtaggeditem.objects.all()
    # for t in tt:
    #     t_id = t.object_id
    #     if ProductionModel.objects.filter(id=t_id).exists():
    #         production = ProductionModel.objects.get(id=t_id)
    #         production.type = t.tag.name
    #         production.save()

    # 得到作品的基本元数据
    # pp = ScratchApiProduction.objects.all()
    # for p in pp:
    #     object = ProductionModel()
    #     object.id = p.id
    #     if p.name:
    #         object.name = p.name
    #     object.create_time = p.create_time
    #     if p.parent:
    #         object.parent_id = p.parent_id
    #     if p.lesson:
    #         object.lesson_id = p.lesson_id
    #     if p.belong_to:
    #         object.belong_class = p.belong_to.class_name
    #     if p.file:
    #         object.sb2file = p.file
    #     if p.author:
    #         object.author = StudentModel.objects.get(username=p.author_id)
    #     object.save()
    return HttpResponse(str(ScratchApiProduction.objects.count()) + str('s/c') + str(ProductionModel.objects.count()))


"""
test5
"""


def KnowModel1Trans(request):
    # 计算学习次数
    # cc = LearnModel.objects.all()
    # for c in cc:
    #     if KnowModel1.objects.filter(lesson_id=c.lesson_id, chapter_id=c.chapter_id).exists():
    #         chapter = KnowModel1.objects.get(chapter_id=c.chapter_id, lesson_id=c.lesson_id)
    #         chapter.learn_times += 1
    #         chapter.save()
    #     else:
    #         print(c.lesson_id)

    # KnowModel1.objects.all().delete()
    # 获得章节信息
    # cc = CourseChapter.objects.all()
    # for c in cc:
    #     print(c.id)
    #     object = KnowModel1()
    #     if c.lesson:
    #         if KnowModel.objects.filter(lesson_id=c.lesson_id).exists():
    #             object.lesson = KnowModel.objects.get(lesson_id=c.lesson_id)
    #     object.chapter_id = c.chapter_id
    #     object.name = c.name
    #     object.content = c.content
    #     if c.audio:
    #         object.audio = c.audio
    #     object.create_time = c.create_time
    #     object.save()
    return HttpResponse(str(CourseChapter.objects.count()) + str('s/c') + str(KnowModel1.objects.count()))


"""
test4
"""


def KnowModelTrans(request):
    # 计算学习次数
    # cc = LearnModel.objects.all()
    # for c in cc:
    #     if KnowModel.objects.filter(lesson_id=c.lesson_id).exists():
    #         lesson = KnowModel.objects.get(lesson_id=c.lesson_id)
    #         lesson.learn_times += 1
    #         lesson.save()
    #     else:
    #         print(c.lesson_id)

    # 获得课程信息
    # cc = CourseLesson.objects.all()
    # for c in cc:
    #     object = KnowModel()
    #     object.lesson_id = c.lesson_id
    #     object.name = c.name
    #     object.short_introduction = c.short_introduction
    #     if c.author:
    #         object.author = TeacherModel.objects.get(teacher_id=c.author_id)
    #     object.save()
    return HttpResponse(str(CourseLesson.objects.count()) + str('s/c') + str(KnowModel.objects.count()))


"""
test3
"""


def TeacherModelTrans(request):
    # 获取所有的课程数
    # cs = CourseLesson.objects.all()
    # for c in cs:
    #     if TeacherModel.objects.filter(teacher_id=c.author_id).exists():
    #         teacher = TeacherModel.objects.get(teacher_id=c.author_id)
    #         teacher.course_times += 1
    #         teacher.save()

    # 获取所有的竞赛数
    # cs = ScratchApiCompetition.objects.all()
    # for c in cs:
    #     teacher = TeacherModel.objects.get(teacher_id=c.creator_id)
    #     teacher.contest_times += 1
    #     teacher.save()

    # 获取作品记录评价
    # ss = ScratchApiQuestionproductionscore.objects.all()
    # for s in ss:
    #     teacher = TeacherModel.objects.get(teacher_id=s.rater_id)
    #     if teacher.production_evalu:
    #         teacher.production_evalu = teacher.production_evalu + '|' + str(s.production_id) + ':' + str(s.score) + ':'
    #     else:
    #         teacher.production_evalu = '|' + str(s.production_id) + ':' + str(s.score) + ':'
    #     if s.comment:
    #         teacher.production_evalu = teacher.production_evalu + str(s.comment)
    #     teacher.save()

    # 获取所有教课的班级
    # rs = ScratchApiClassTeacher.objects.all()
    # for r in rs:
    #     teacher = TeacherModel.objects.get(teacher_id=r.teacher_id)
    #     teacher.teach_class = '/' + str(r.class_field.class_name)
    #     teacher.save()

    # 获得教师信息
    # teahcers = ScratchApiTeacher.objects.all()
    # for t in teahcers:
    #     object = TeacherModel()
    #     object.teacher_id = t.baseuser_ptr_id
    #     if t.school:
    #         object.school = t.school
    #     if t.email:
    #         object.email = t.email
    #     if t.phone_number:
    #         object.phone_number = t.phone_number
    #     object.save()
    return HttpResponse(str(ScratchApiTeacher.objects.count()) + str('s/c') + str(TeacherModel.objects.count()))


"""
test2
"""


def StudentModelTrans(request):
    # StudentModel.objects.all().delete()
    # 获得学习的课程数和总学习时长、
    # uu = StudentModel.objects.all()
    # for u in uu:
    #     if LearnModel.objects.filter(username=u.username).exists():
    #         u.coursetimes = LearnModel.objects.filter(username=u.username).values('lesson_id').distinct().count()
    #         u.learning_duration = 0
    #         ll = LearnModel.objects.filter(username=u.username)
    #         for l in ll:
    #             u.learning_duration += l.learn_time
    #         u.save()

    # 获得课程学习记录
    # uu = StudentModel.objects.all()
    # for u in uu:
    #     if LearnModel.objects.filter(username=u.username).exists():
    #         ss = LearnModel.objects.filter(username=u.username).values('lesson_id').distinct()
    #         for s in ss:
    #             if u.course_list:
    #                 u.course_list = u.course_list + '/' + str(s)
    #             else:
    #                 u.course_list = '/' + str(s)
    #         u.save()

    # 获得收藏数、收藏列表
    # ff = ScratchApiFavoriteproduction.objects.all()
    #     # for f in ff:
    #     #     username = f.user_id
    #     #     if StudentModel.objects.filter(username=username).exists():
    #     #         u = StudentModel.objects.get(username=username)
    #     #         if u.favtimes:
    #     #             u.favtimes += 1
    #     #         else:
    #     #             u.favtimes = 1
    #     #         if u.fav_list:
    #     #             u.fav_list = u.fav_list + '/' + str(f.production_id)
    #     #         else:
    #     #             u.fav_list = '/' + str(f.production_id)
    #     #         u.save()

    # 创作次数、创作列表、改编次数、改编树
    # uu = StudentModel.objects.all()
    # for u in uu:
    #     if ProductionModel.objects.filter(author=u).exists():
    #         pp = ProductionModel.objects.filter(author=u)
    #         for p in pp:
    #             if u.creativetimes:
    #                 u.creativetimes += 1
    #             else:
    #                 u.creativetimes = 1
    #             if u.production_list:
    #                 u.production_list = u.production_list + '/' + str(p.id)
    #             else:
    #                 u.production_list = '/' + str(p.id)
    #             if p.parent_id:
    #                 if u.remixtimes:
    #                     u.remixtimes += 1
    #                 else:
    #                     u.remixtimes = 1
    #                 if u.remix_tree:
    #                     u.remix_tree = u.remix_tree + '/' + str(p.parent_id) + '->' + str(p.id)
    #                 else:
    #                     u.remix_tree = '/' + str(p.parent_id) + '->' + str(p.id)
    #         u.save()

    # 获得学生信息
    # users = ScratchApiUser.objects.all()
    # for user in users:
    #     object = StudentModel()
    #     object.username = user.baseuser_ptr_id
    #     if user.sex:
    #         object.gender = user.sex
    #     if user.birthday:
    #         object.age = 2018 - int(user.birthday.year)
    #     if user.school:
    #         object.school = user.school.school_name
    #     if user.student_class:
    #         object.grade = user.student_class.class_name
    #     if user.local_province:
    #         object.district = str(user.local_province)
    #     if user.local_city:
    #         object.district = object.district + str(user.local_city)
    #     if user.local_district:
    #         object.district = object.district + str(user.local_district)
    #     if user.student_id:
    #         object.student_id = user.student_id
    #     if user.phone_number:
    #         object.phone_number = user.phone_number
    #     if user.created_at:
    #         object.registration_time = user.created_at
    #     object.save()
    return HttpResponse(str(ScratchApiUser.objects.count()) + str('s/c') + str(StudentModel.objects.count()))


"""
test
"""


def CTModelTrans(request):
    # items = ScratchApiAntlrscore.objects.filter().all()
    # for item in items:
    #     production = ProductionModel.objects.get(id=item.production_id_id)
    #     if not CTModel.objects.filter(production_id=production).exists():
    #         object = CTModel()
    #         object.production_id = production
    #         object.ap_score = item.ap_score
    #         object.parallelism_score = item.parallelism_score
    #         object.synchronization_score = item.synchronization_score
    #         object.flow_control_score = item.flow_control_score
    #         object.user_interactivity_score = item.user_interactivity_score
    #         object.logical_thinking_score = item.logical_thinking_score
    #         object.data_representation_score = item.data_representation_score
    #         object.total = item.total
    #         if ScratchApiProductionhint.objects.filter(production_id=item.production_id).exists():
    #             object.hint = ScratchApiProductionhint.objects.filter(production_id=item.production_id).first().hint
    #         object.save()
    #     else:
    #         pass
    return HttpResponse(str(ScratchApiAntlrscore.objects.count()) + str('s/c') + str(CTModel.objects.count()))


"""
test1
"""


def LearnModelTrans(request):
    # items = CourseUserbehaviorlesson.objects.filter().all()
    # for item in items:
    #     object = LearnModel()
    #     object.username = item.user
    #     object.lesson_id = item.lesson_id
    #     object.chapter_id = item.chapter_id
    #     object.click_audio = item.click_audio
    #     object.start_time = item.start_time
    #     object.end_time = item.end_time
    #     object.learn_time = (item.end_time - item.start_time).seconds
    #     object.save()

    # total_time = 0
    # objects = LearnModel.objects.all()
    # for object in objects:
    #     total_time += object.learn_time
    # user_count = LearnModel.objects.all().values('username').count()
    # users = LearnModel.objects.all().values('username').distinct()
    # for user in users:
    #     rr = LearnModel.objects.filter(username=user['username'])
    #     time = 0
    #     for r in rr:
    #         time += r.learn_time
    #     s = LearningTimeStatistic.objects.create(username=user['username'], total_learn_time=time)

    # user_count = ProductionModel.objects.all().values('author_id').distinct().count()
    # total_pro = ProductionModel.objects.all().count()
    # user=StudentModel.objects.all().count()
    return HttpResponse(str(CourseUserbehaviorlesson.objects.count()) + str('s/c') + str(LearnModel.objects.count()))
