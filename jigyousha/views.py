from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import allowed,disallowed
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.conf import settings

def search_allowed(request):
    todofuken = request.GET.get('todofuken')
    shichoson = request.GET.get('shichoson')
    # service_types = request.GET.getlist('service_type')
    keyword = request.GET.get('keyword')

    queryset = allowed.objects.none() 

    if todofuken or shichoson  or keyword:
        queryset = allowed.objects.all()

        if todofuken:
            queryset = queryset.filter(facility_address_pref=todofuken)

        if shichoson:
            queryset = queryset.filter(facility_address_city=shichoson)

        # if service_types:
        #     service_filters = Q()
        #     service_mapping = {
        #         '相談': ['居宅介護支援'],
        #         '訪問介護': [
        #             '訪問介護', '訪問看護', '訪問リハビリテーション', '訪問入浴介護', '定期巡回・随時対応型訪問介護看護'
        #         ],
        #         '福祉用品利用': ['福祉用具貸与'],
        #         'デイサービス': [
        #             '通所介護', '地域密着型通所介護', '認知症対応型通所介護'
        #         ],
        #         'ショートステイ': [
        #             '短期入所生活介護', '看護小規模多機能型居宅介護', '小規模多機能型居宅介護',
        #             '短期入所療養介護（介護老人保健施設）', '短期入所療養介護（介護医療院）', 
        #             '短期入所療養介護', '療養通所介護'
        #         ],
        #         '施設入所': [
        #             '認知症対応型共同生活介護',
        #             '特定施設入居者生活介護（有料老人ホーム（サービス付き高齢者向け住宅））',
        #             '特定施設入居者生活介護（有料老人ホーム（サービス付き高齢者向け住宅（外部サービス利用型））',
        #             '地域密着型特定施設入居者生活介護（有料老人ホーム（サービス付き高齢者向け住宅））',
        #             '特定施設入居者生活介護（軽費老人ホーム）',
        #             '特定施設入居者生活介護（軽費老人ホーム（外部サービス利用型）',
        #             '地域密着型特定施設入居者生活介護（軽費老人ホーム）',
        #             '特定施設入居者生活介護（有料老人ホーム）',
        #             '特定施設入居者生活介護（有料老人ホーム（外部サービス利用型））',
        #             '地域密着型特定施設入居者生活介護（有料老人ホーム）',
        #             '介護医療院', '介護療養型医療施設'
        #         ],
        #         '施設入所（費用減免制度あり）': [
        #             '介護老人福祉施設', '介護老人保健施設'
        #         ]
        #     }
        #     for service_type in service_types:
        #         mapped_services = service_mapping.get(service_type, [])
        #         service_filters |= Q(service_type__in=mapped_services)
        #     queryset = queryset.filter(service_filters)

        if keyword:
            queryset = queryset.filter(Q(service_type__icontains=keyword))

    todofuken_list = list(
    allowed.objects.filter(facility_address_pref__isnull=False)
    .values_list('facility_address_pref', flat=True)
    .distinct()
     )
    prefecture_order = [
    '北海道','青森県','岩手県','宮城県','秋田県','山形県','福島県','茨城県','栃木県','群馬県','埼玉県','千葉県','東京都','神奈川県','新潟県','富山県',
    '石川県','福井県','山梨県','長野県','岐阜県','静岡県','愛知県','三重県','滋賀県','京都府','大阪府','兵庫県','奈良県',
    '和歌山県','鳥取県','島根県','岡山県','広島県','山口県','徳島県','香川県','愛媛県','高知県','福岡県','佐賀県','長崎県','熊本県',
    '大分県','宮崎県','鹿児島県','沖縄県'
     ]
    order_map = {pref: index for index, pref in enumerate(prefecture_order)}
    sorted_pref_list = sorted(todofuken_list, key=lambda x: order_map.get(x, 999))
   
    shichoson_list = []
    if todofuken:
        shichoson_list = allowed.objects.filter(facility_address_pref=todofuken).values_list('facility_address_city', flat=True).distinct()
    
    paginator = Paginator(queryset, 6)  # 1ページに表示する件数を指定
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'jigyousha/search_allowed.html', {
        'results': queryset,
        'todofuken_list': sorted_pref_list,
        'shichoson_list': shichoson_list,
        'selected_todofuken': todofuken,
        'selected_shichoson': shichoson,
        # 'selected_service_types': service_types,
        'keyword': keyword,
        'page_obj': page_obj,
    })


def search_disallowed(request):
    todofuken = request.GET.get('todofuken')
    shichoson = request.GET.get('shichoson')
    # service_types = request.GET.getlist('service_type')
    keyword = request.GET.get('keyword')

    queryset = disallowed.objects.none()  

    if todofuken or shichoson  or keyword:
        queryset = disallowed.objects.all()

        if todofuken:
            queryset = queryset.filter(address_pref=todofuken)

        if shichoson:
            queryset = queryset.filter(address_city=shichoson)

        if keyword:
            queryset = queryset.filter(Q(service_type__icontains=keyword))

    # 都道府県のリストを取得
    prefecture_order = [
    '北海道','青森県','岩手県','宮城県','秋田県','山形県','福島県','茨城県','栃木県','群馬県','埼玉県','千葉県','東京都','神奈川県','新潟県','富山県',
    '石川県','福井県','山梨県','長野県','岐阜県','静岡県','愛知県','三重県','滋賀県','京都府','大阪府','兵庫県','奈良県',
    '和歌山県','鳥取県','島根県','岡山県','広島県','山口県','徳島県','香川県','愛媛県','高知県','福岡県','佐賀県','長崎県','熊本県',
    '大分県','宮崎県','鹿児島県','沖縄県'
     ]
    todofuken_list = list(
    disallowed.objects.filter(address_pref__isnull=False)
    .values_list('address_pref', flat=True)
    .distinct()
     )

    order_map = {pref: index for index, pref in enumerate(prefecture_order)}
    sorted_pref_list = sorted(todofuken_list, key=lambda x: order_map.get(x, 999))
    shichoson_list = []
    if todofuken:
        shichoson_list = disallowed.objects.filter(address_pref=todofuken).values_list('address_city', flat=True).distinct()
    
    paginator = Paginator(queryset, 6)  # 1ページに表示する件数を指定
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'jigyousha/search_disallowed.html', {
        'results': queryset,
        'todofuken_list': sorted_pref_list,
        'shichoson_list': shichoson_list,
        'selected_todofuken': todofuken,
        'selected_shichoson': shichoson,
        # 'selected_service_types': service_types,
        'keyword': keyword,
        'page_obj': page_obj,
    })

def allowed_detail(request, pk):
    facility = get_object_or_404(allowed, pk=pk)
    return render(request, 'jigyousha/allowed_detail.html', {'facility': facility,'google_api_key': settings.GOOGLE_API_KEY})

def disallowed_detail(request, pk):
    facility = get_object_or_404(disallowed, pk=pk)
    return render(request, 'jigyousha/disallowed_detail.html', {'facility': facility,'google_api_key':settings.GOOGLE_API_KEY})

def get_shichoson(request):
    todofuken = request.GET.get('todofuken')
    if todofuken:
        shichoson_list = (
            allowed.objects
            .filter(facility_address_pref=todofuken)
            .values_list('facility_address_city', flat=True)
            .distinct()
            .order_by('facility_address_city')
        )
        return JsonResponse(list(shichoson_list), safe=False)
    else:
        return JsonResponse({'error': 'No todofuken provided'}, status=400)

    