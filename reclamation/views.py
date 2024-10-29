# memberships/views.py
from django.shortcuts import render, get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Reclamation, Response  # Import both models

from .forms import ResponseForm  # Import your form for Response
from .forms import ReclamationForm
from .utils import analyze_sentiment
class ReclamationListView(ListView):
    model = Reclamation
    template_name = 'reclamation/reclamation_list.html'
    context_object_name = 'reclamations'

class ReclamationDetailView(DetailView):
    model = Reclamation
    template_name = 'reclamation/reclamation_detail.html'
    context_object_name = 'reclamation'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['responses'] = self.object.responses.all()  # Add responses to context
        return context

class ReclamationCreateView(CreateView):
    model = Reclamation
    fields = ['title', 'description', 'priority', 'category', 'attachment']
    template_name = 'reclamation/reclamation_form.html'
    success_url = reverse_lazy('reclamation-list')


    def form_valid(self, form):
        form.instance.user = self.request.user
        # Analyze sentiment and set it in the form before saving
        form.instance.sentiment = analyze_sentiment(form.instance.description)
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ReclamationUpdateView(UpdateView):
    model = Reclamation
    fields = ['title', 'description', 'priority', 'category', 'attachment']
    template_name = 'reclamation/reclamation_form.html'
    success_url = reverse_lazy('reclamation-list')

class ReclamationDeleteView(DeleteView):
    model = Reclamation
    template_name = 'reclamation/reclamation_confirm_delete.html'
    success_url = reverse_lazy('reclamation-list')

# def reclamation_detail(request, pk):
#     reclamation = get_object_or_404(Reclamation, pk=pk)
#     responses = reclamation.responses.all()  # Get all responses related to the reclamation
#     return render(request, 'reclamation/reclamation_detail.html', {
#         'reclamation': reclamation,
#         'responses': responses,  # Pass the responses to the template
#     })
def add_response(request, pk):
    reclamation = get_object_or_404(Reclamation, pk=pk)
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.reclamation = reclamation
            response.user = request.user  # Set the current user
            response.save()
            return redirect('reclamation-detail', pk=reclamation.pk)
    else:
        form = ResponseForm()
    return render(request, 'reclamation/add_response.html', {'form': form, 'reclamation': reclamation})

class ResponseDeleteView(DeleteView):
    model = Response
    template_name = 'reclamation/response_confirm_delete.html'
    context_object_name = 'response'

    def get_success_url(self):
        # Redirect back to the reclamation detail page after deletion
        return reverse_lazy('reclamation-detail', kwargs={'pk': self.object.reclamation.pk})
    
    def delete_response(request, pk):
       response = get_object_or_404(Response, pk=pk)
       reclamation_id = response.reclamation.pk  # Get the related reclamation ID
       response.delete()
       return redirect('reclamation-detail', pk=reclamation_id)