from blog.models import Post
from experiments.models import Experiment
from TRDWLL.models import Alert


def global_settings(request):
    return {
        'ALERTS': Alert.print_alerts(request)
    }