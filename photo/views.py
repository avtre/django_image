from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView

from photo.models import Photo


class PhotoUploadView(CreateView):
    model = Photo
    fields = ['image']

    def get_context_data(self, **kwargs):
        context = super(PhotoUploadView, self).get_context_data(**kwargs)
        context['image'] = Photo.objects.all()
        return context

    def form_valid(self, form):
        form.save()
        return redirect('photo_upload')


class PhotoExifView(ListView):
    def get(self, request, *args, **kwargs):
        photo_id = request.GET.get('photo_id', None)
        if photo_id:
            photo = Photo.objects.get(id=photo_id)
            return render(request, 'photo/photo_detail.html', {'photo': photo.get_exif_data()})
