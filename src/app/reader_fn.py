import traceback
import json
from app.reader import Reader


class Reader_fn(Reader):
    def __init__(self):
        super().__init__()

    def get(self, fns, trafo):
        try:
            dct = {}
            for fn in fns:
                dct.update(json.loads(open(fn).read()))
            return tuple(trafo(dct))
        except Exception:
            traceback.print_exc()
        return False
