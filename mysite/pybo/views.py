from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

# Create your views here.

from django.shortcuts import render
from .models import Qs, Aw

def index(request):
    qs_list = Qs.objects.order_by('-create_date')
    cot={'qs_list':qs_list}
    return render(request,'pybo/qs_list.html',cot)

def detail(request, qs_id):
    qs = get_object_or_404(Qs, pk=qs_id)
    con = {"qs":qs}
    return render(request, 'pybo/qs_detail.html',con)

def aw_create(request, qs_id):
    qs = get_object_or_404(Qs, pk=qs_id)
    aw = Aw(qs=qs, con=request.POST.get('con'),create_date=timezone.now())
    aw.save()
    return redirect('pybo:detail', qs_id=qs.id)