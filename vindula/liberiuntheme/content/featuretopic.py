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
class IFeatureTopic(form.Schema):
    """ Feature Section """
      
    image_topic = RelationChoice(
        title=_(u"Imagem do tópico"),
        description=_(u"Selecione a imagem que irá aparecer para o novo tópico."),
        source=ObjPathSourceBinder( portal_type = 'Image',),
        required=False,
        )
    
#View
class FeatureTopicView(grok.View):
    grok.context(IFeatureTopic)
    grok.require('zope2.View')
    
    def render(self):
        pass
        
        
            
            
            
            
            
            
            
            
            
            
            
            
            