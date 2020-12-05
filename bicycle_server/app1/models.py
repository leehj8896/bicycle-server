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
    rank_5_cnt = models.CharField(db_column='RANK_5_CNT', max_length=50, blank=True, null=True)
    rank_6_cnt = models.CharField(db_column='RANK_6_CNT', max_length=50, blank=True, null=True)
    rank_7_cnt = models.CharField(db_column='RANK_7_CNT', max_length=50, blank=True, null=True)
    rank_8_cnt = models.CharField(db_column='RANK_8_CNT', max_length=50, blank=True, null=True)
    rank_9_cnt = models.CharField(db_column='RANK_9_CNT', max_length=50, blank=True, null=True)
    elim_cnt = models.CharField(db_column='ELIM_CNT', max_length=50, blank=True, null=True)
    down_po_cnt = models.CharField(db_column='DOWN_PO_CNT', max_length=50, blank=True, null=True)
    go_po_cnt = models.CharField(db_column='GO_PO_CNT', max_length=50, blank=True, null=True)
    period_no = models.CharField(db_column='PERIOD_NO', max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player'