from django.shortcuts import render
from django.core.urlresolvers import reverse

def main_page(request):
	return render(request,"hello/base.html",{})
