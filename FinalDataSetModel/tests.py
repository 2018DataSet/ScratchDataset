from django.test import TestCase
from DataSetModel.models import ScratchApiProduction, ScratchApiAntlrscore, ScratchApiProductionhint
from .models import CTModel


# Create your tests here.

class TestTranform(TestCase):
    def CTModelTrans(self):
        items = ScratchApiAntlrscore.objects.filter()
        for item in items:
            production = ScratchApiProduction.objects.get(id=item.production_id)
            object = CTModel()
            object.production_id = item.production_id
            object.ap_score = item.ap_score
            object.parallelism_score = item.parallelism_score
            object.synchronization_score = item.synchronization_score
            object.flow_control_score = item.flow_control_score
            object.user_interactivity_score = item.user_interactivity_score
            object.logical_thinking_score = item.logical_thinking_score
            object.data_representation_score = item.data_representation_score
            object.total = item.total
            object.hint = ScratchApiProductionhint.objects.get(production_id=production).hint
            object.save()
