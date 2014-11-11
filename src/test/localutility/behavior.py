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

    #form.widget(image_relation=ContentTreeFieldWidget)
    image_relation_x = RelationChoice(
        title=u"Lead Image - related",
        source=ObjPathSourceBinder(
            object_provides=IImage.__identifier__
        ),
        required=False
    )


alsoProvides(ITestBehavior, IFormFieldProvider)


@implementer(ITestBehavior)
class TestBehavior(MetadataBase):
    pass

    # image_relation_x = DCFieldProperty(ITestBehavior['image_relation_x'])


# @implementer(ITestBehavior)
# class TestBehavior(MetadataBase):
#     def __init__(self, context):
#         self.context = context

