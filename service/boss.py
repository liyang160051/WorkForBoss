from domain.boss.boss import Boss
from infrastructure.repository.domain import DomainRepostiory


class BossService(object):

    @staticmethod
    def create_boss_obj(alias):
        boss = Boss(alias)
        DomainRepostiory().add_obj(alias, boss)

    @staticmethod
    def open_boss_browser(bossAlias):
        bossObj = DomainRepostiory().find_domain_obj(bossAlias)
        bossObj.open_browser()

    @staticmethod
    def log_in(bossAlias):
        bossObj = DomainRepostiory().find_domain_obj(bossAlias)
        bossObj.log_in()

    @staticmethod
    def recommend(ailas):
        obj = DomainRepostiory().find_domain_obj(ailas)
        obj.recommend_btn()
