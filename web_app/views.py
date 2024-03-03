from django.shortcuts import render
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index page accessed')
    return render(request, 'web_app/home.html')

def about(request):
    try:
        result = 1 / 0
    except Exception as e:
        logger.exception(f'Error in about page {e}')
        return HttpResponse('Smth went wroooong....')
    else:
        logger.debug('about page accessed')
        return HttpResponse("It's all about us")

# Create your views here.
