# -*- coding: utf-8 -*-
from five import grok
from zope import schema
from plone.directives import form
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.app.textfield import RichText
from vindula.liberiuntheme import MessageFactory as _
from z3c.relationfield.schema import RelationList, RelationChoice
from Products.CMFCore.utils import getToolByName

#Interface
class IFeatureSection(form.Schema):
    """ Feature Section """
    
    subtitle = schema.TextLine(
        title=_(u"Subtítulo"),
        description=_(u"Insira um texto para aparacer em baixo do título."),
        required=False,
        )
    
    image_header = RelationChoice(
        title=_(u"Imagem superior"),
        description=_(u"Selecione a imagem que aparecerá abaixo do titulo da funcionalidade, no header, recomendasse uma imagem 257x79."),
        source=ObjPathSourceBinder( portal_type = 'Image',),
        required=False,
        )
    
    image_title = RelationChoice(
        title=_(u"Imagem do título"),
        description=_(u"Selecione a imagem que aparecerá do lado esquerdo do título, recomendasse uma imagem 66x66."),
        source=ObjPathSourceBinder( portal_type = 'Image',),
        required=False,
        )
    
#View
class FeatureSectionView(grok.View):
    grok.context(IFeatureSection)
    grok.require('zope2.View')
    
    def render(self):
        pass
        
        
            
            
            
            
            
            
            
            
            
            
            
            
            