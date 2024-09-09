from django.shortcuts import render
from django.db.models import Q
from .models import Jigyousha,SJigyousha
from django.http import JsonResponse
from django.core.paginator import Paginator


def search_jigyousha(request):
    todofuken = request.GET.get('todofuken')
    shichoson = request.GET.get('shichoson')
    service_types = request.GET.getlist('service_type')
    keyword = request.GET.get('keyword')

    queryset = Jigyousha.objects.none()  # デフォルトで空のクエリセットを設定

    if todofuken or shichoson or service_types or keyword:
        queryset = Jigyousha.objects.all()

        if todofuken:
            queryset = queryset.filter(todofuken_name=todofuken)

        if shichoson:
            queryset = queryset.filter(shichoson_name=shichoson)

        if service_types:
            service_filters = Q()
            service_mapping = {
                '相談': ['居宅介護支援'],
                '訪問介護': [
                    '訪問介護', '訪問看護', '訪問リハビリテーション', '訪問入浴介護', '定期巡回・随時対応型訪問介護看護'
                ],
                '福祉用品利用': ['福祉用具貸与'],
                'デイサービス': [
                    '通所介護', '地域密着型通所介護', '認知症対応型通所介護'
                ],
                'ショートステイ': [
                    '短期入所生活介護', '看護小規模多機能型居宅介護', '小規模多機能型居宅介護',
                    '短期入所療養介護（介護老人保健施設）', '短期入所療養介護（介護医療院）', 
                    '短期入所療養介護', '療養通所介護'
                ],
                '施設入所': [
                    '認知症対応型共同生活介護',
                    '特定施設入居者生活介護（有料老人ホーム（サービス付き高齢者向け住宅））',
                    '特定施設入居者生活介護（有料老人ホーム（サービス付き高齢者向け住宅（外部サービス利用型））',
                    '地域密着型特定施設入居者生活介護（有料老人ホーム（サービス付き高齢者向け住宅））',
                    '特定施設入居者生活介護（軽費老人ホーム）',
                    '特定施設入居者生活介護（軽費老人ホーム（外部サービス利用型）',
                    '地域密着型特定施設入居者生活介護（軽費老人ホーム）',
                    '特定施設入居者生活介護（有料老人ホーム）',
                    '特定施設入居者生活介護（有料老人ホーム（外部サービス利用型））',
                    '地域密着型特定施設入居者生活介護（有料老人ホーム）',
                    '介護医療院', '介護療養型医療施設'
                ],
                '施設入所（費用減免制度あり）': [
                    '介護老人福祉施設', '介護老人保健施設'
                ]
            }
            for service_type in service_types:
                mapped_services = service_mapping.get(service_type, [])
                service_filters |= Q(service_type__in=mapped_services)
            queryset = queryset.filter(service_filters)

        if keyword:
            queryset = queryset.filter(Q(service_type__icontains=keyword))

    # 都道府県のリストを取得
    todofuken_list = Jigyousha.objects.values_list('todofuken_name', flat=True).distinct()
    shichoson_list = []
    if todofuken:
        shichoson_list = Jigyousha.objects.filter(todofuken_name=todofuken).values_list('shichoson_name', flat=True).distinct()
    
    paginator = Paginator(queryset, 6)  # 1ページに表示する件数を指定
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'jigyousha/search_jigyousha.html', {
        'results': queryset,
        'todofuken_list': todofuken_list,
        'shichoson_list': shichoson_list,
        'selected_todofuken': todofuken,
        'selected_shichoson': shichoson,
        'selected_service_types': service_types,
        'keyword': keyword,
        'page_obj': page_obj,
    })


def search_sjigyousha(request):
    todofuken = request.GET.get('todofuken')
    shichoson = request.GET.get('shichoson')
    service_types = request.GET.getlist('service_type')
    keyword = request.GET.get('keyword')

    queryset = SJigyousha.objects.none()  # デフォルトで空のクエリセットを設定

    if todofuken or shichoson or service_types or keyword:
        queryset = SJigyousha.objects.all()
        if todofuken:
            queryset = queryset.filter(Q(jigyousho_address_city__icontains=todofuken))

        if shichoson:
            queryset = queryset.filter(Q(jigyousho_address_city__icontains=shichoson))

        if service_types:
            service_filters = Q()
            service_mapping = {
        '訪問系サービス': [
            '居宅介護', '重度訪問介護', '同行援護', '行動援護', '重度障害者等包括支援'
        ],
        '日中活動系サービス': [
            '療養介護', '生活介護', '短期入所'
        ],
        '施設系サービス': [
            '施設入所支援'
        ],
        '居住系サービス': [
            '共同生活援助', '自立生活援助'
        ],
        '訓練系・就労系サービス': [
            '自立訓練(機能訓練)', '自立訓練(生活訓練)', '宿泊型自立訓練',
            '就労移行支援', '就労継続支援Ａ型', '就労継続支援Ｂ型', '就労定着支援'
        ],
        '障害児通所系サービス': [
            '児童発達支援', '医療型児童発達支援', '放課後等デイサービス',
            '居宅訪問型児童発達支援', '保育所等訪問支援'
        ],
        '障害児入所系サービス': [
            '福祉型障害児入所施設', '医療型障害児入所施設'
        ],
        '相談系サービス': [
            '地域相談支援(地域移行)', '地域相談支援(地域定着)', '計画相談支援', '障害児相談支援'
        ]
    }

            for service_type in service_types:
                mapped_services = service_mapping.get(service_type, [])
                service_filters |= Q(service_type__in=mapped_services)
            queryset = queryset.filter(service_filters)

        if keyword:
            queryset = queryset.filter(Q(service_type__icontains=keyword))

    # 都道府県のリストを取得
    todofuken_list = Jigyousha.objects.values_list('todofuken_name', flat=True).distinct()
    shichoson_list = []
    if todofuken:
        shichoson_list = Jigyousha.objects.filter(todofuken_name=todofuken).values_list('shichoson_name', flat=True).distinct()
    
    paginator = Paginator(queryset, 6)  # 1ページに表示する件数を指定
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'jigyousha/search_sjigyousha.html', {
        'results': queryset,
        'todofuken_list': todofuken_list,
        'shichoson_list': shichoson_list,
        'selected_todofuken': todofuken,
        'selected_shichoson': shichoson,
        'selected_service_types': service_types,
        'keyword': keyword,
        'page_obj': page_obj,
    })


def get_shichoson(request):
    todofuken = request.GET.get('todofuken')
    if todofuken:
        shichoson_list = (
            Jigyousha.objects
            .filter(todofuken_name=todofuken)
            .values_list('shichoson_name', flat=True)
            .distinct()
            .order_by('shichoson_name')
        )
        return JsonResponse(list(shichoson_list), safe=False)
    else:
        return JsonResponse({'error': 'No todofuken provided'}, status=400)


# def get_sshichoson(request):
#     todofuken = request.GET.get('prefecture_name')
#     if todofuken:
#         shichoson_list = (
#             Jigyousha.objects
#             .filter(todofuken_name=todofuken)
#             .values_list('city_name', flat=True)
#             .distinct()
#             .order_by('city_name')
#         )
#         return JsonResponse(list(shichoson_list), safe=False)
#     else:
#         return JsonResponse({'error': 'No todofuken provided'}, status=400)
    