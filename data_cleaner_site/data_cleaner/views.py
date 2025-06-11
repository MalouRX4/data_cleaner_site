from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
from utils.cleaning import load_and_clean

def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        files = request.FILES.getlist('file_field')
        if form.is_valid() and files:
            merge_io, clean_io, html_table = load_and_clean(files)
            request.session['table'] = html_table
            response = render(request, 'data_cleaner/index.html', {
                'form': form,
                'merge_file': merge_io.getvalue().decode(),
                'clean_file': clean_io.getvalue().decode()
            })
            return response
    else:
        form = UploadFileForm()
    return render(request, 'data_cleaner/index.html', {'form': form})

def dashboard(request):
    html_table = request.session.get('table', 'Pas de données.')
    return render(request, 'data_cleaner/dashboard.html', {'table_html': html_table})
