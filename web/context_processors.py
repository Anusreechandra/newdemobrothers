from .models import SocialMedia

def main_context(request):
    medias = SocialMedia.objects.all()
    return {
        'domain' : request.META['HTTP_HOST'],
        'medias'  : medias,
    }