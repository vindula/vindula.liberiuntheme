# -*- coding: utf-8 -*-
from five import grok
from zope import schema
from plone.directives import form
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.app.textfield import RichText
from vindula.liberiuntheme import MessageFactory as _
from z3c.relationfield.schema import RelationList, RelationChoice
from Products.CMFCore.utils import getToolByName

# Interface and schema

class IHomePage(form.Schema):
    """ Home Page """
        
    
    title = schema.TextLine(
        title=_(u"Título"),
        description=_(u"Insira um nome para Home Page."),
        )
    

    
# View
    
class HomePageView(grok.View):
    grok.context(IHomePage)
    grok.require('zope2.View')
    grok.name('view')
    
    # Methods for News