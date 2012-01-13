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
class IPricing(form.Schema):
    """ Pricing """
    
    contact = RichText(
        title=_(u"Forma de contato"),
        description=_(u"Insira formas de contatos"),
        required=False,
        )
    
    observation = RichText(
        title=_(u"Observações"),
        description=_(u"Observações que serão mostradas na parte de baixa na página"),
        required=False,
        )

#View
class PricingVindulaView(grok.View):
    grok.context(IPricing)
    grok.require('zope2.View')
    grok.name('view')
    
    def getColumns(self):
#        pc = getToolByName(self.context, 'portal_catalog')
#        result = pc(path={'query': self.context.absolute_url()},
#                         portal_type='Folder',
#                         review_state='published',
#                         sort_on='effective',
#                         sort_order='descending',)

        results = self.context.items('ATFolder')
        if results:
            L = []
            for result in results:
                D = {}
                D['id'] = result[0]
                D['name'] = result[1].Title()
                L.append(D)
        
        
        
            
            
            
            
            
            
            
            
            
            
            
            
            