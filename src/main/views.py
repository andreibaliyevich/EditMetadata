from django.http import FileResponse
from django.shortcuts import render, redirect
from .forms import UploadImageGPSForm
from .utilities import handle_uploaded_file, edit_image


def index(request):
    if request.method == 'POST':
        form = UploadImageGPSForm(request.POST, request.FILES)
        if form.is_valid():
            form_cd = form.cleaned_data
            img_path = handle_uploaded_file(request.FILES['image'])
            new_img_path = edit_image(img_path, form_cd)
            return FileResponse(open(new_img_path, 'rb'), as_attachment=True)
    else:
        form = UploadImageGPSForm()
    return render(request, 'index.html', {'form': form})


def error_400(request, exception):
    """ Error 400 """
    return render(request, 'errors/400.html', status=400)


def error_403(request, exception):
    """ Error 403 """
    return render(request, 'errors/403.html', status=403)


def error_404(request, exception):
    """ Error 404 """
    return render(request, 'errors/404.html', status=404)


def error_500(request):
    """ Error 500 """
    return render(request, 'errors/500.html', status=500)
