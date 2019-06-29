from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import get_object_or_404

# Create your views here.
def blog(request):
    return render(request, 'counter.html')


def result(request):
    count = request.GET["count"]
    count_list = count.lower().split()
    count_dict = {}

    def word_count(word):
        for word in count_list:
            if word in count_dict:
                count_dict[word] = count_dict[word] + 1
                continue
            else:
                count_dict[word] = 1

        return count_dict

    result = word_count(count)
    return render(request, 'result.html', {'result': result})

   