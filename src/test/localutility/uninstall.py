from .component import ITestUtility


def uninistall_utility(site):
    sm = site.getSiteManager()

    util = sm.queryUtility(ITestUtility)
    if util:
        sm.unregisterUtility(provided=ITestUtility)
        del util
        assert sm.queryUtility(ITestUtility) is None

        provided = sm.utilities._provided
        if provided.get(ITestUtility):
            del provided[ITestUtility]
        sm.utilities._provided = provided


def uninstall(context):

    if context.readDataFile('uninstall_step.txt') is None:
        return

    site = context.getSite()
    uninistall_utility(site)
