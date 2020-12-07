from django.db import models

class Player(models.Model):
    stnd_year = models.CharField(db_column='STND_YEAR', max_length=50, blank=True, null=True)
    racer_no = models.CharField(db_column='RACER_NO', max_length=50, blank=True, null=True)
    racer_nm = models.CharField(db_column='RACER_NM', max_length=50, blank=True, null=True)
    racer_grd = models.CharField(db_column='RACER_GRD', max_length=50, blank=True, null=True)
    run_cnt = models.CharField(db_column='RUN_CNT', max_length=50, blank=True, null=True)
    run_day_cnt = models.CharField(db_column='RUN_DAY_CNT', max_length=50, blank=True, null=True)
    rank_1_cnt = models.CharField(db_column='RANK_1_CNT', max_length=50, blank=True, null=True)
    win_rate = models.CharField(db_column='WIN_RATE', max_length=50, blank=True, null=True)
    rank_2_cnt = models.CharField(db_column='RANK_2_CNT', max_length=50, blank=True, null=True)
    high_rate = models.CharField(db_column='HIGH_RATE', max_length=50, blank=True, null=True)
    rank_3_cnt = models.CharField(db_column='RANK_3_CNT', max_length=50, blank=True, null=True)
    high_3_rate = models.CharField(db_column='HIGH_3_RATE', max_length=50, blank=True, null=True)
    rank_4_cnt = models.CharField(db_column='RANK_4_CNT', max_length=50, blank=True, null=True)
    rank_5_cnt = models.TextField(db_column='RANK_5_CNT', blank=True, null=True)
    rank_6_cnt = models.TextField(db_column='RANK_6_CNT', blank=True, null=True)
    rank_7_cnt = models.TextField(db_column='RANK_7_CNT', blank=True, null=True)
    rank_8_cnt = models.TextField(db_column='RANK_8_CNT', blank=True, null=True)
    rank_9_cnt = models.TextField(db_column='RANK_9_CNT', blank=True, null=True)
    elim_cnt = models.TextField(db_column='ELIM_CNT', blank=True, null=True)
    down_po_cnt = models.TextField(db_column='DOWN_PO_CNT', blank=True, null=True)
    go_po_cnt = models.TextField(db_column='GO_PO_CNT', blank=True, null=True)
    period_no = models.TextField(db_column='PERIOD_NO', blank=True, null=True)
    pre_rank1_cnt = models.TextField(db_column='PRE_RANK1_CNT', blank=True, null=True)
    brk_rank1_cnt = models.TextField(db_column='BRK_RANK1_CNT', blank=True, null=True)
    pas_rank1_cnt = models.TextField(db_column='PAS_RANK1_CNT', blank=True, null=True)
    mrk_rank1_cnt = models.TextField(db_column='MRK_RANK1_CNT', blank=True, null=True)
    warn_cnt = models.TextField(db_column='WARN_CNT', blank=True, null=True)
    care_cnt = models.TextField(db_column='CARE_CNT', blank=True, null=True)
    estm_scr = models.TextField(db_column='ESTM_SCR', blank=True, null=True)
    gear_rate = models.TextField(db_column='GEAR_RATE', blank=True, null=True)
    tot_rank = models.TextField(db_column='TOT_RANK', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player'
    
    
    class Meta:
        managed = False
        db_table = 'player'
        
class Schedule(models.Model):
    schedule_code = models.TextField(db_column='SCHEDULE_CODE', blank=True, null=True)
    schedule_year = models.TextField(db_column='SCHEDULE_YEAR', blank=True, null=True)
    schedule_month = models.TextField(db_column='SCHEDULE_MONTH', blank=True, null=True)
    schedule_day = models.TextField(db_column='SCHEDULE_DAY', blank=True, null=True)
    title = models.TextField(db_column='TITLE', blank=True, null=True)
    schedule_content = models.TextField(db_column='SCHEDULE_CONTENT', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schedule'
        
class Result(models.Model):
    stnd_year = models.TextField(db_column='STND_YEAR', blank=True, null=True)
    race_day = models.TextField(db_column='RACE_DAY', blank=True, null=True)
    meet = models.TextField(db_column='MEET', blank=True, null=True)
    tms = models.TextField(db_column='TMS', blank=True, null=True)
    day_ord = models.TextField(db_column='DAY_ORD', blank=True, null=True)
    race_no = models.TextField(db_column='RACE_NO', blank=True, null=True)
    rank1 = models.TextField(db_column='RANK1', blank=True, null=True)
    rank2 = models.TextField(db_column='RANK2', blank=True, null=True)
    rank3 = models.TextField(db_column='RANK3', blank=True, null=True)
    pool001 = models.TextField(db_column='POOL001', blank=True, null=True)
    pool002 = models.TextField(db_column='POOL002', blank=True, null=True)
    pool004 = models.TextField(db_column='POOL004', blank=True, null=True)
    pool005 = models.TextField(db_column='POOL005', blank=True, null=True)
    pool006 = models.TextField(db_column='POOL006', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'result'

class Match(models.Model):
    player_no = models.TextField(db_column='PLAYER_NO', blank=True, null=True)
    player_nm = models.TextField(db_column='PLAYER_NM', blank=True, null=True)
    player_strtgy_cd = models.TextField(db_column='PLAYER_STRTGY_CD', blank=True, null=True)
    player_strtgy_nm = models.TextField(db_column='PLAYER_STRTGY_NM', blank=True, null=True)
    partn_player_no = models.TextField(db_column='PARTN_PLAYER_NO', blank=True, null=True)
    partn_player_nm = models.TextField(db_column='PARTN_PLAYER_NM', blank=True, null=True)
    partn_player_strtgy_cd = models.TextField(db_column='PARTN_PLAYER_STRTGY_CD', blank=True, null=True)
    partn_player_strtgy_nm = models.TextField(db_column='PARTN_PLAYER_STRTGY_NM', blank=True, null=True)
    victry_gg_co = models.TextField(db_column='VICTRY_GG_CO', blank=True, null=True)
    defeat_gg_co = models.TextField(db_column='DEFEAT_GG_CO', blank=True, null=True)
    tie_gg_co = models.TextField(db_column='TIE_GG_CO', blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'match'
        

class Entry(models.Model):
    meet = models.TextField(db_column='MEET', blank=True, null=True)
    stnd_year = models.TextField(db_column='STND_YEAR', blank=True, null=True)
    tms = models.TextField(db_column='TMS', blank=True, null=True)
    day_ord = models.TextField(db_column='DAY_ORD', blank=True, null=True)
    race_dt = models.TextField(db_column='RACE_DT', blank=True, null=True)
    race_no = models.TextField(db_column='RACE_NO', blank=True, null=True)
    back_no = models.TextField(db_column='BACK_NO', blank=True, null=True)
    color = models.TextField(db_column='COLOR', blank=True, null=True)
    racer_nm = models.TextField(db_column='RACER_NM', blank=True, null=True)
    period_no = models.TextField(db_column='PERIOD_NO', blank=True, null=True)
    age = models.TextField(db_column='AGE', blank=True, null=True)
    gear_rate = models.TextField(db_column='GEAR_RATE', blank=True, null=True)
    rec_200m = models.TextField(db_column='REC_200M', blank=True, null=True)
    trng_plc = models.TextField(db_column='TRNG_PLC', blank=True, null=True)
    win_rate = models.TextField(db_column='WIN_RATE', blank=True, null=True)
    high_rate = models.TextField(db_column='HIGH_RATE', blank=True, null=True)
    high_3_rate = models.TextField(db_column='HIGH_3_RATE', blank=True, null=True)
    racer_grd = models.TextField(db_column='RACER_GRD', blank=True, null=True)
    str_tm = models.TextField(db_column='STR_TM', blank=True, null=True)
    round_cnt = models.TextField(db_column='ROUND_CNT', blank=True, null=True)
    race_len = models.TextField(db_column='RACE_LEN', blank=True, null=True)
    win_tot_cnt = models.TextField(db_column='WIN_TOT_CNT', blank=True, null=True)
    run_day_cnt = models.TextField(db_column='RUN_DAY_CNT', blank=True, null=True)
    pre_win_cnt = models.TextField(db_column='PRE_WIN_CNT', blank=True, null=True)
    pas_win_cnt = models.TextField(db_column='PAS_WIN_CNT', blank=True, null=True)
    brk_win_cnt = models.TextField(db_column='BRK_WIN_CNT', blank=True, null=True)
    mrk_win_cnt = models.TextField(db_column='MRK_WIN_CNT', blank=True, null=True)
    racer_grd_cur = models.TextField(db_column='RACER_GRD_CUR', blank=True, null=True)
    racer_grd_bef = models.TextField(db_column='RACER_GRD_BEF', blank=True, null=True)
    area_tms3_avg_scr = models.TextField(db_column='AREA_TMS3_AVG_SCR', blank=True, null=True)
    tot_tms_avg_scr = models.TextField(db_column='TOT_TMS_AVG_SCR', blank=True, null=True)
    bf1_meet_nm = models.TextField(db_column='BF1_MEET_NM', blank=True, null=True)
    bf1_day1_dt = models.TextField(db_column='BF1_DAY1_DT', blank=True, null=True)
    bf1_day1_rank = models.TextField(db_column='BF1_DAY1_RANK', blank=True, null=True)
    bf1_day2_rank = models.TextField(db_column='BF1_DAY2_RANK', blank=True, null=True)
    bf1_day3_rank = models.TextField(db_column='BF1_DAY3_RANK', blank=True, null=True)
    bf2_meet_nm = models.TextField(db_column='BF2_MEET_NM', blank=True, null=True)
    bf2_day1_dt = models.TextField(db_column='BF2_DAY1_DT', blank=True, null=True)
    bf2_day1_rank = models.TextField(db_column='BF2_DAY1_RANK', blank=True, null=True)
    bf2_day2_rank = models.TextField(db_column='BF2_DAY2_RANK', blank=True, null=True)
    bf2_day3_rank = models.TextField(db_column='BF2_DAY3_RANK', blank=True, null=True)
    bf3_meet_nm = models.TextField(db_column='BF3_MEET_NM', blank=True, null=True)
    bf3_day1_dt = models.TextField(db_column='BF3_DAY1_DT', blank=True, null=True)
    bf3_day1_rank = models.TextField(db_column='BF3_DAY1_RANK', blank=True, null=True)
    bf3_day2_rank = models.TextField(db_column='BF3_DAY2_RANK', blank=True, null=True)
    bf3_day3_rank = models.TextField(db_column='BF3_DAY3_RANK', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entry'