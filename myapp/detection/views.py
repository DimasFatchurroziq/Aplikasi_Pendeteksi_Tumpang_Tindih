from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse

from django.core.files.uploadedfile import SimpleUploadedFile
from detection.factories.factory import get_file_service
from detection.factories.factory import get_rule_service
from detection.factories.factory import get_embedding_service
from detection.factories.factory import get_comparison_service

# Create your views here.
class OneFileComparisonView(APIView):
    def post(self, request):
        file_obj = request.FILES['file']
        file_instance = FileService.handle_save_file(file_obj)
        list_tuple_rules = RuleService.extract_and_split(file_instance)
        embedded = EmbeddingService.sbert_embedded(list_tuple_rules)
        comparisons = ComparisonService.compare_within_rules(embedded)
        return Response({'success': True, 'comparisons': comparisons})


class TwoFileComparisonView(APIView):
    def post(self, request):
        file1 = request.FILES['file1']
        file2 = request.FILES['file2']
        file1_instance = FileService.save_file(file1)
        file2_instance = FileService.save_file(file2)
        rules1 = RuleService.extract_and_embed(file1_instance)
        rules2 = RuleService.extract_and_embed(file2_instance)
        comparisons = ComparisonService.compare_between_rules(rules1, rules2)
        return Response({'success': True, 'comparisons': comparisons})



from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from detection.factories import get_file_service

def upload_file_view(request):
    if request.method == "POST" and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        
        file_service = get_file_service()
        file_instance = file_service.handle_save_file(uploaded_file)

        return render(request, 'upload_success.html', {
            'file_name': file_instance.name,
            'file_url': file_instance.file.url,
        })

    return render(request, 'upload_form.html')
