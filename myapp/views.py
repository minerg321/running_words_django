from django.views import View
from django.http import HttpResponse
from .utils import make_video
from .models import VideoRequest

def home(request):
    # здесь код для обработки главной страницы
    return render(request, 'home.html')
class MyView(View):
    def get(self, request, text):
        make_video(text)
        # сохраняем запрос в базе данных
        VideoRequest.objects.create(text=text)
        with open('output.mp4', 'rb') as f:
            response = HttpResponse(f.read(), content_type='video/mp4')
            response['Content-Disposition'] = 'attachment; filename=output.mp4'
            return response
