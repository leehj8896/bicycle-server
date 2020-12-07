from django.contrib.auth.models import User, Group
from rest_framework import serializers
from bicycle_server.app1.models import Player, Schedule, Match, Entry, Result

def get_lower(x):
            return x.lower()
    
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ScehduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Schedule
        fields = [
            'id', 
            'schedule_code', 
            'schedule_year', 
            'schedule_month', 
            'schedule_day', 
            'title', 
            'schedule_content'
        ]
        
class MatchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Match
        fields = list(map(get_lower, [
            'id',
            'PLAYER_NO',
            'PLAYER_NM',
            'PLAYER_STRTGY_CD',
            'PLAYER_STRTGY_NM',
            'PARTN_PLAYER_NO',
            'PARTN_PLAYER_NM',
            'PARTN_PLAYER_STRTGY_CD',
            'PARTN_PLAYER_STRTGY_NM',
            'VICTRY_GG_CO',
            'DEFEAT_GG_CO',
            'TIE_GG_CO',
        ]))

class ResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Result
        fields = list(map(get_lower, [
            'id',
            'STND_YEAR',
            'RACE_DAY',
            'MEET',
            'TMS',
            'DAY_ORD',
            'RACE_NO',
            'RANK1',
            'RANK2',
            'RANK3',
            'POOL001',
            'POOL002',
            'POOL004',
            'POOL005',
            'POOL006',
        ]))



class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        def get_lower(x):
            return x.lower()
        fields = list(map(get_lower, [
            'id',
            'stnd_year',
            'racer_no',
            'racer_nm',
            'racer_grd',
            'run_cnt',
            'run_day_cnt',
            'rank_1_cnt',
            'win_rate',
            'rank_2_cnt',
            'high_rate',
            'rank_3_cnt',
            'high_3_rate',
            'RANK_4_CNT',
            'RANK_5_CNT',
            'RANK_6_CNT',
            'RANK_7_CNT',
            'RANK_8_CNT',
            'RANK_9_CNT',
            'ELIM_CNT',
            'DOWN_PO_CNT',
            'GO_PO_CNT',
            'PERIOD_NO',
            'PRE_RANK1_CNT',
            'BRK_RANK1_CNT',
            'PAS_RANK1_CNT',
            'MRK_RANK1_CNT',
            'WARN_CNT',
            'CARE_CNT',
            'ESTM_SCR',
            'GEAR_RATE',
            'TOT_RANK',
        ]))


class EntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entry
        fields = list(map(get_lower, [
            'id',
            'MEET',
            'STND_YEAR',
            'TMS',
            'DAY_ORD',
            'RACE_DT',
            'RACE_NO',
            'BACK_NO',
            'COLOR',
            'RACER_NM',
            'PERIOD_NO',
            'AGE',
            'GEAR_RATE',
            'REC_200M',
            'TRNG_PLC',
            'WIN_RATE',
            'HIGH_RATE',
            'HIGH_3_RATE',
            'RACER_GRD',
            'STR_TM',
            'ROUND_CNT',
            'RACE_LEN',
            'WIN_TOT_CNT',
            'RUN_DAY_CNT',
            'PRE_WIN_CNT',
            'PAS_WIN_CNT',
            'BRK_WIN_CNT',
            'MRK_WIN_CNT',
            'RACER_GRD_CUR',
            'RACER_GRD_BEF',
            'AREA_TMS3_AVG_SCR',
            'TOT_TMS_AVG_SCR',
            'BF1_MEET_NM',
            'BF1_DAY1_DT',
            'BF1_DAY1_RANK',
            'BF1_DAY2_RANK',
            'BF1_DAY3_RANK',
            'BF2_MEET_NM',
            'BF2_DAY1_DT',
            'BF2_DAY1_RANK',
            'BF2_DAY2_RANK',
            'BF2_DAY3_RANK',
            'BF3_MEET_NM',
            'BF3_DAY1_DT',
            'BF3_DAY1_RANK',
            'BF3_DAY2_RANK',
            'BF3_DAY3_RANK',
        ]))
