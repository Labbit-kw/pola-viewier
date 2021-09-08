from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Filter
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.template import loader
import simplejson as json
from .forms import NameForm, IpLoad, JoinForm
# Create your views here.
#
# class DbFilter_list(ListView):
#     model = Filter


def home(request):
    models = Filter.objects.all()
    return render(request, 'home.html',{'models':models})



def base(request):
    models = Filter.objects.all()
    # return HttpResponse(temp.render(model, requeset))
    return render(request, 'home/base.html',{'models':models})


def test(request):
    jsonObject = json.loads(request.body)
    print(jsonObject.get('title'))
    print(jsonObject.get('content'))
    return JsonResponse(jsonObject)


def list_db_func(request):
    sdata = Filter.objects.filter(name='cctv1')
    datas = []
    for s in sdata:
        dict = {'name':s.name,'ip1':s.ip_1,'ip2':s.ip_2,'ip3':s.ip_3,'ip4':s.ip_4}
        datas.append(dict)
    return HttpResponse(json.dumps(datas), content_type = 'application/json')


def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            return HttpResponseRedirect('../base/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, '../base/', {'form': form})


def create(request):
    if request.method == 'POST':
        form = IpLoad(request.POST)
        if form.is_valid():
            form.save()
        return redirect('../base')
    else:
        form = IpLoad()

    return render(request, 'home/base.html',{'form':form})


def loadip(request):
    form = IpLoad()
    if request.is_ajax():
        form = IpLoad(request.POST)
        if form.is_valid():
            # form.save()
            return JsonResponse({
                'msg':'succuses'
            })
    return render(request, 'home/base.html', {'form':form})


def create_post(request):
    if request.method == 'POST':
        post_text = request.POST.get('the_post')
        response_data = {}

        post = Filter(text=post_text, author=request.user)
        post.save()

        response_data['result'] = 'Create post successful!'
        response_data['postpk'] = post.pk
        response_data['text'] = post.name
        response_data['ip_1'] = post.ip_1
        response_data['ip_2'] = post.ip_2
        response_data['ip_3'] = post.ip_3
        response_data['ip_4'] = post.ip_4

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

#
# class JoinFormView(FormView):
#     form_class = JoinForm
#     template_name = 'forms/ajax.html'
#     success_url = '/form-success/'
#
#     def form_invalid(self, form):
#         response = super(JoinFormView, self).form_invalid(form)
#         if self.request.is_ajax():
#             return JsonResponse(form.errors, status = 400)
#         else:
#             return response
#
#     def form_valid(self, form):
#         response = super(JoinFormView, self).form_valid(form)
#         if self.request.is_ajax():
#             print(form.cleaned_data)
#             data = {
#                 'message': "Successfully submitted form data."
#             }
#             return JsonResponse(data)
#         else:
#             return response