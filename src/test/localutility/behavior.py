# -*- encoding: utf-8 -*-
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.content import Container
from plone.supermodel import model

from zope.interface import implementer
from zope.interface import alsoProvides
from z3c.relationfield.schema import RelationChoice
from plone.app.contenttypes.interfaces import IImage
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.app.dexterity.behaviors.metadata import MetadataBase
from plone.app.dexterity.behaviors.metadata import DCFieldProperty


class ITestBehavior(model.Schema):

    image_relation_x = RelationChoice(
        title=u"Lead Image - field nel behavior",
        source=ObjPathSourceBinder(
            object_provides=IImage.__identifier__
        ),
        required=False
    )


alsoProvides(ITestBehavior, IFormFieldProvider)
