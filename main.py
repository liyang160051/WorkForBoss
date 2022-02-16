import time
from service.boss import BossService

BossService.create_boss_obj("boss")
BossService.open_boss_browser("boss")
time.sleep(5)
BossService.log_in("boss")
time.sleep(5)
BossService.recommend("boss")

