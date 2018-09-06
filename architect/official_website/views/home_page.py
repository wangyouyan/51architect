from django.shortcuts import render_to_response, HttpResponse

# Create your views here.

def index(request):
    if request.method == 'GET':
        return render_to_response('BizPage/index.html')

def contact_us(request):
    if request.method == 'POST':
        print(request.body)
        """
        b'name=wangyy32&email=wangyouyan201314%40163.com&subject=%E5%95%8A%E5%95%8A%E5%95%8A%E5%95%8A%E5%95%8A%E5%95%8A%E5%95%8A%E5%95%8A%E5%95%8A%E5%95%8A%E5%95%8A%E5%95%8A%E5%95%8A%E5%95%8A%E5%95%8A&message=%E5%95%8A%E5%95%8A%E5%95%8A%E5%95%8A%E5%95%8A%E5%95%8A%E5%95%8A%E5%95%8A%E5%95%8A%E5%95%8A%E5%95%8A%E5%95%8A%E5%95%8A%E5%95%8A%E5%95%8A'sss
        """
        return HttpResponse('We have received your email')