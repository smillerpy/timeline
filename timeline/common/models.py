
class Registrator():
    @classmethod
    def register(cls, key=None):
        def onCall(clss, *args):
            if key:
                key_1 = "%s" % key
                reg = getattr(cls, "registered", {})
                reg[key_1] = clss
            else:
                reg = getattr(cls, "registered", [])
                reg.append(clss)
            cls.registered = reg
            return clss
        return onCall

    @classmethod
    def get_cls_by_type(cls, type_key):
        type_key = "%s" % type_key
        return cls.registered.get(type_key, None)
