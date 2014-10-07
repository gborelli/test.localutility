from zope.interface import Interface
from zope.interface import implementer


class ITestUtility(Interface):
    pass


@implementer(ITestUtility)
class TestUtility(object):
    pass
