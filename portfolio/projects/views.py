# projects/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Project, Inquiry
from .forms import ContactForm
from django.contrib.auth.decorators import login_required

class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'
    ordering = ['-date_posted']

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'

class ProjectCreateView(CreateView):
    model = Project
    fields = ['title', 'description', 'short_description', 'image', 'project_url']

class ProjectUpdateView(UpdateView):
    model = Project
    fields = ['title', 'description', 'short_description', 'image', 'project_url']

class ProjectDeleteView(DeleteView):
    model = Project
    success_url = '/'

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'projects/contact.html', {'form': form})

def contact_success_view(request):
    return render(request, 'projects/contact_success.html')

def dashboard(request):
    inquiries = Inquiry.objects.all()
    return render(request, 'projects/dashboard.html', {'inquiries': inquiries})