from contextlib import redirect_stderr
from questions.models import Question
from django.shortcuts import redirect, render
from django.http import Http404
from django.views import defaults
from . import utils
import copy

# Create your views here.
def questionD(request):
    return redirect("/question/1")

def question(request,q):
    if q in (1,2,3,4):
        if request.method == 'POST':
            body = request.POST
            request.session[f"QPage{q}"] = utils.getData(body)
            if q<4:
                return redirect(f"/question/{q+1}")
            else:
                data = []
                for i in range(1,5):
                    data.append(request.session[f"QPage{i}"])
                request.session["PersonalityID"] =  utils.submiteData(data)
                return redirect('/signup')
        else:
            questions = Question.objects.all().filter(questionPage=q).order_by('questionNumber')
            return render(request,'Question.html',{'questions':questions})
    else:
        return render(request,'404.html')
        # TODO add correcy Http 404