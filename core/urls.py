from core.views import UserView
# from ebanking.application import ApplicationBase
from ebanking.urls_tornado import ApplicationBase

CORE_URL = ApplicationBase([
    (r"", UserView),
])
