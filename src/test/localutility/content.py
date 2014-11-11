# -*- encoding: utf-8 -*-
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.content import Container
from plone.supermodel import model

from zope.interface import implementer
from zope.interface import alsoProvides
from z3c.relationfield.schema import RelationChoice
from plone.app.contenttypes.interfaces import IImage
from plone.formwidget.contenttree import ObjPathSourceBinder


class IProva(model.Schema):

    image_relation = RelationChoice(
        title=u"Lead Image - field nel content type",
        source=ObjPathSourceBinder(
            object_provides=IImage.__identifier__
        ),
        required=False,
    )


alsoProvides(IProva, IFormFieldProvider)


@implementer(IProva)
class Prova(Container):
    pass
