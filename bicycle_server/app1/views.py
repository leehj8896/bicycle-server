from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from bicycle_server.app1.serializers import PlayerSerializer, EntrySerializer, ResultSerializer, MatchSerializer, ScehduleSerializer, RaceSerializer
from bicycle_server.app1.models import Player, Schedule, Entry, Result, Match
from django.http import JsonResponse
from django.db.models import Q
from django_pandas.io import read_frame
import pandas as pd
import json
from django.db.models import Count
import datetime

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]

def players(request, page):

    # permission_classes = [permissions.IsAuthenticated]

    queryset = Player.objects.all()[(page-1)*20:page*20]
    serializer = PlayerSerializer(queryset, many=True)
    return JsonResponse(serializer.data, 
        safe=False, 
        json_dumps_params={'ensure_ascii': False}
    )

def player_no(request, player_nm, player_no):

    # permission_classes = [permissions.IsAuthenticated]
    
    q_sum = Q(racer_no=player_no) & Q(racer_nm=player_nm)

    queryset = Player.objects.filter(q_sum)
    serializer = PlayerSerializer(queryset, many=True)
    return JsonResponse(serializer.data, 
        safe=False, 
        json_dumps_params={'ensure_ascii': False}
    )

def player_name(request, player_nm):

    # permission_classes = [permissions.IsAuthenticated]

    queryset = Player.objects.filter(racer_nm=player_nm)
    serializer = PlayerSerializer(queryset, many=True)
    return JsonResponse(serializer.data, 
        safe=False, 
        json_dumps_params={'ensure_ascii': False}
    )

def schedules(request, page):
    
    queryset = Schedule.objects.all()[(page-1)*20:page*20]
    serializer = ScehduleSerializer(queryset, many=True)
    return JsonResponse(serializer.data, 
        safe=False, 
        json_dumps_params={'ensure_ascii': False}
    )

def results(request, year, month, day, race_no):
    
    queryset = Result.objects.filter(
        Q(stnd_year=year) & 
        Q(race_day=f'{month.zfill(2)}{day.zfill(2)}') & 
        Q(race_no=race_no)).all()

    serializer = ResultSerializer(queryset, many=True)
    return JsonResponse(serializer.data, 
        safe=False, 
        json_dumps_params={'ensure_ascii': False}
    )


def races(request, year, month, day):
    
    date = f'{year}.{month.zfill(2)}.{day.zfill(2)}'
    
    queryset = Entry.objects.filter(race_dt=date).values(
        # 'id',
        # 'meet',
        # 'stnd_year',
        # 'tms',
        # 'day_ord',
        # 'race_dt',
        'race_no',
    ).distinct()
    serializer = RaceSerializer(queryset, many=True)
    return JsonResponse(serializer.data, 
        safe=False, 
        json_dumps_params={'ensure_ascii': False}
    )


def entries(request, year, month, day, race_no):
    
    date = f'{year}.{month.zfill(2)}.{day.zfill(2)}'
    
    queryset = Entry.objects.filter(Q(race_dt=date) & Q(race_no=race_no)).all()
    serializer = EntrySerializer(queryset, many=True)
    return JsonResponse(serializer.data, 
        safe=False, 
        json_dumps_params={'ensure_ascii': False}
    )


def matches(request, player_no_1, player_no_2):
    
    q1 = Q(player_no=player_no_1) & Q(partn_player_no=player_no_2)
    q2 = Q(player_no=player_no_2) & Q(partn_player_no=player_no_1)
    
    queryset = Match.objects.filter(q1 | q2).all()
    serializer = MatchSerializer(queryset, many=True)
    return JsonResponse(serializer.data, 
        safe=False, 
        json_dumps_params={'ensure_ascii': False}
    )


# 특정 선수의 연도별 입상률
def player_prize_rate(request, player_nm):
    
    splayer = player_nm
    
    queryset = Entry.objects.all().values(
        'gear_rate', 
        'win_rate',
        'high_rate',
        'high_3_rate',
        'tot_tms_avg_scr',
        'stnd_year',
        'win_tot_cnt',
        'run_day_cnt',
        'rec_200m',
        'racer_nm',
    )
    chulgu = read_frame(queryset)
    
    # print()
    # print(chulgu.info())
    # print()

    # chulgu['AGE'] = chulgu['AGE'].astype('int') #제외
    chulgu['gear_rate'] = chulgu['gear_rate'].astype('float')
    chulgu['win_rate'] = chulgu['win_rate'].astype('int')
    chulgu['high_rate'] = chulgu['high_rate'].astype('int')
    chulgu['high_3_rate'] = chulgu['high_3_rate'].astype('float')
    chulgu['tot_tms_avg_scr'] = chulgu['tot_tms_avg_scr'].astype('float')
    chulgu['stnd_year'] = chulgu['stnd_year'].astype('int')
    chulgu['win_tot_cnt'] = chulgu['win_tot_cnt'].astype('float')
    chulgu['run_day_cnt'] = chulgu['run_day_cnt'].astype('float')
    chulgu['rec_200m_second'] = chulgu['rec_200m']
    chulgu['rec_200m_second'] = chulgu['rec_200m_second'].str.replace('""', '.')
    chulgu['rec_200m_second'] = chulgu['rec_200m_second'].str.replace('"', '')
    chulgu['rec_200m_second'] = chulgu['rec_200m_second'].astype('float')


#     print()
#     print(chulgu.info())
#     print()

    
    echulgu = chulgu[(chulgu['stnd_year']>= 2017)]
    echulgu.reset_index(drop=True, inplace=True)
    echulgu['PRIZE_RATE'] = (echulgu['win_tot_cnt'] / echulgu['run_day_cnt']) * 100
    echulgu["PRIZE_RATE"] = echulgu["PRIZE_RATE"].fillna(0)
    echulgu['PRIZE_RATE'] = echulgu['PRIZE_RATE'].round(2) 
    echulgu['TOT_SCR_RATE'] = (echulgu['tot_tms_avg_scr'] / 150) * 100
    echulgu['TOT_SCR_RATE'] = echulgu['TOT_SCR_RATE'].round(2)

    
    splayer_df =  echulgu[echulgu['racer_nm'] == splayer]
    pgroup= splayer_df.groupby(['stnd_year']).mean()
    pgroup = pd.DataFrame(pgroup)
    
    pgroup['EYRATE'] = 0
    # # 72 % 정확도
    for i in range(1, len(pgroup)):  
            pgroup['EYRATE'].iloc[i] = -42.0444 + 0.0739 * pgroup['high_rate'].iloc[i-1] + 0.6189 * pgroup['high_3_rate'].iloc[i-1] + 0.9403 * pgroup['TOT_SCR_RATE'].iloc[i-1]
    
    
    # print(type(pgroup['PRIZE_RATE'].to_json()))    
    # print(type(pgroup['PRIZE_RATE'].to_json()))
    # print(type(pgroup['PRIZE_RATE'].to_json()))
    
    temp1 = json.loads(pgroup['PRIZE_RATE'].to_json())
    real_rate = dict()
    for key in temp1:
        real_rate[f'year_{key}'] = temp1[key]
    
    temp2 = json.loads(pgroup['EYRATE'].to_json())
    expected_rate = dict()
    for key in temp2:
        expected_rate[f'year_{key}'] = temp2[key]

    result = {
        'real_rate': real_rate,
        'expected_rate': expected_rate,
    }

    
    return JsonResponse(result, 
        safe=False, 
        json_dumps_params={'ensure_ascii': False}
    )

def match_graph(request, player_nm_1, player_nm_2):
    
    player_1 = player_nm_1
    # player_1 = '이홍주'

    player_2 = player_nm_2
    # player_2 = '정진호'

    
    queryset = Entry.objects.all().values(
        # 'gear_rate', 
        # 'win_rate',
        # 'high_rate',
        # 'high_3_rate',
        'tot_tms_avg_scr',
        'stnd_year',
        'win_tot_cnt',
        'run_day_cnt',
        'rec_200m',
        'racer_nm',
    )
    chulgu = read_frame(queryset)
    
    # print()
    # print(chulgu.info())
    # print()

    # chulgu['AGE'] = chulgu['AGE'].astype('int') #제외
    # chulgu['gear_rate'] = chulgu['gear_rate'].astype('float')
    # chulgu['win_rate'] = chulgu['win_rate'].astype('int')
    # chulgu['high_rate'] = chulgu['high_rate'].astype('int')
    # chulgu['high_3_rate'] = chulgu['high_3_rate'].astype('float')
    chulgu['tot_tms_avg_scr'] = chulgu['tot_tms_avg_scr'].astype('float')
    chulgu['stnd_year'] = chulgu['stnd_year'].astype('int')
    chulgu['win_tot_cnt'] = chulgu['win_tot_cnt'].astype('float')
    chulgu['run_day_cnt'] = chulgu['run_day_cnt'].astype('float')
    chulgu['rec_200m_second'] = chulgu['rec_200m']
    chulgu['rec_200m_second'] = chulgu['rec_200m_second'].str.replace('""', '.')
    chulgu['rec_200m_second'] = chulgu['rec_200m_second'].str.replace('"', '')
    chulgu['rec_200m_second'] = chulgu['rec_200m_second'].astype('float')

    echulgu = chulgu[(chulgu['stnd_year']>= 2017)]
    echulgu.reset_index(drop=True, inplace=True)
    echulgu['prize_rate'] = (echulgu['win_tot_cnt'] / echulgu['run_day_cnt']) * 100
    echulgu["prize_rate"] = echulgu["prize_rate"].fillna(0)
    echulgu['prize_rate'] = echulgu['prize_rate'].round(2) 
    echulgu['tot_scr_rate'] = (echulgu['tot_tms_avg_scr'] / 150) * 100
    echulgu['tot_scr_rate'] = echulgu['tot_scr_rate'].round(2)

    ebar_1 =  echulgu[(echulgu['racer_nm'] == player_1)]
    ebar_2 = echulgu[(echulgu['racer_nm'] == player_2)]
    ebar = pd.concat([ebar_1, ebar_2], ignore_index=True)

    e = ebar[['racer_nm','rec_200m_second','prize_rate', 'tot_scr_rate']].groupby(['racer_nm']).mean()
    e = pd.DataFrame(e)
    e = e.transpose()
    
    # print(e)
    
    # result = {}
    
    # result = {
    #     'real_rate': json.loads(pgroup['PRIZE_RATE'].to_json()),
    #     'expected_rate': json.loads(pgroup['EYRATE'].to_json()),
    # }
    result = dict()
    temp = json.loads(e.to_json())
    i = 1
    for key in temp:
        result[f'player{i}'] = temp[key]
        i += 1
    
    return JsonResponse(
        result, 
        safe=False, 
        json_dumps_params={'ensure_ascii': False}
    )

def player_grade(request, player_nm):
    
    # player_nm = '정해권'
    start_year = datetime.datetime.today().year - 10 + 1
    end_year = datetime.datetime.today().year
    
    queryset = Entry.objects.all().values('stnd_year', 'racer_nm', 'racer_grd').filter(Q(stnd_year__gte=start_year) & Q(racer_nm=player_nm))
    
    q1 = queryset.filter(Q(racer_grd='특선')).annotate(Count('stnd_year')).order_by('stnd_year')
    q2 = queryset.filter(Q(racer_grd='우수')).annotate(Count('stnd_year')).order_by('stnd_year')
    q3 = queryset.filter(Q(racer_grd='선발')).annotate(Count('stnd_year')).order_by('stnd_year')
    
    dict_grade = {
        '특선':'grade1',
        '우수':'grade2',
        '선발':'grade3',
    }
    list_year = list(range(start_year, end_year+1))
    result = {f"year_{y}":{dict_grade[key]:0 for key in dict_grade} for y in list_year}
    
    for line in list(q1):
        result[f"year_{line['stnd_year']}"][dict_grade[line['racer_grd']]] = line['stnd_year__count']
    for line in list(q2):
        result[f"year_{line['stnd_year']}"][dict_grade[line['racer_grd']]] = line['stnd_year__count']
    for line in list(q3):
        result[f"year_{line['stnd_year']}"][dict_grade[line['racer_grd']]] = line['stnd_year__count']
        
    return JsonResponse(
        result, 
        safe=False, 
        json_dumps_params={'ensure_ascii': False}
    )
