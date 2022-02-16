from infrastructure.singleton import singleton

@singleton
class DomainRepostiory(object):

    def __init__(self):
        self._repo = {}
        pass

    def find_domain_obj(self, alias):
        return self._repo.get(alias, None)

    def add_obj(self, alias, obj):
        if alias not in self._repo:
            self._repo[alias] = obj
        else:
            print("obj {alias} is in repo".format(alias=alias))

    @property
    def repo(self):
        return self._repo
