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
class IFeatureProfile(form.Schema):
    """ Feature Section """
    
    title = schema.TextLine(
        title=_(u"Título"),
        description=_(u"Insira o título do perfil."),
        required=True,
        )

    description_profile = schema.Text(
        title=_(u"Descrição"),
        description=_(u"Insira uma descrição do perfil, no máximo 280 caracteres."),
        required=True,
        max_length=280,
        )

    image_profile = RelationChoice(
        title=_(u"Imagem do Perfil"),
        description=_(u"Selecione a imagem que aparecerá do lado direito do título do perfil, recomendasse uma imagem 79x79."),
        source=ObjPathSourceBinder( portal_type = 'Image',),
        required=False,
        )
    
#View
class FeatureProfileView(grok.View):
    grok.context(IFeatureProfile)
    grok.require('zope2.View')
    
    def render(self):
        pass
        
        
            
            
            
            
            
            
            
            
            
            
            
            
            