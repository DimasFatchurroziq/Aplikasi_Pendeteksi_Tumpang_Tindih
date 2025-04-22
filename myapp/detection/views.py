from django.shortcuts import render

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
