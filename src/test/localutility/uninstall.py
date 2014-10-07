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

        subscribers = sm.utilities._subscribers
        if subscribers[0].get(ITestUtility):
            del subscribers[0][ITestUtility]
        sm.utilities._subscribers = subscribers

        # regsistrations = sm._utility_registrations
        # _utility_registrations
        # _reconstructor
        # utilities

    # import pdb; pdb.set_trace()


def uninstall(context):

    if context.readDataFile('uninstall_step.txt') is None:
        return

    site = context.getSite()
    uninistall_utility(site)
