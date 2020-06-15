import traceback
import json
import re
from app.reader import Reader
from os import path


class Reader_fn(Reader):
    def __init__(self):
        super().__init__()

    def get(self, fns, trafo):
        try:
            dct = {}
            for fn in [fn for fn in fns if path.exists(fn)]:
                isTimestamp = re.search('\/(\d{10})_', fn)
                if isTimestamp:
                    dct.update({'timestamp': isTimestamp.group(1)})
                dct.update(json.loads(open(fn).read()))
            return tuple(trafo(dct))
        except Exception:
            print("******* File-Name ****** : ", fn)
            traceback.print_exc(limit=2)
        return False
