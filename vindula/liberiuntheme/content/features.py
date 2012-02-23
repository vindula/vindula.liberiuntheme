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
class IFeatures(form.Schema):
    """ Pricing """

#View
class FeaturesView(grok.View):
    grok.context(IFeatures)
    grok.require('zope2.View')
    grok.name('view')
    
    def getProfiles(self):
        results = self.context.values('ATFolder')
        L = []
        if results:
            for result in results:
                D = {}
                D['title'] = result.Title()
                D['description'] = result.Description()
                D['contents'] = []
                if result.values():
                    contents = result.values()
                    for content in contents:
                        if content.portal_type == 'vindula.liberiuntheme.content.featuresection':
                            DC = {}
                            DC['title_content'] = content.Title()
                            DC['description_content'] = content.Description()
                            D['contents'].append(DC)
                L.append(D)
                
        return L
        
    
    def getContent(self):
        pc = getToolByName(self.context, 'portal_catalog')
        query = '/'.join(self.context.getPhysicalPath())
        results = pc( path={'query': query},
                     portal_type='vindula.liberiuntheme.content.featuresection',
                     review_state='published',
                     sort_on= 'getObjPositionInParent',
                     sort_order='descending', )
        
        L = []
        if results:
            for result in results:
                obj = result.getObject()
                D = {}
                D['title'] = obj.Title()
                D['description'] = obj.Description()
                D['subtitle'] = obj.subtitle
                D['image'] = ''
                if obj.image_title:
                    D['image'] = obj.image_title.to_object.absolute_url()
                D['topics'] = []
                if obj.values():
                    topics = obj.values()
                    for topic in topics:
                        if topic.portal_type == 'Image':
                            DT = {}
                            DT['title_topic'] = topic.Title()
                            DT['description_topic'] = topic.Description()
                            DT['image_topic'] = topic.absolute_url()
                            D['topics'].append(DT)
                            
                L.append(D)
                
        return L
        
        
            
            
            
            
            
            
            
            
            
            
            
            
            