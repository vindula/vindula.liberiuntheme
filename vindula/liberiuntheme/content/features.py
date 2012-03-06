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
        results = self.context.values()
        L = []
        if results:
            for result in results:
                if result.portal_type == 'vindula.liberiuntheme.content.featureprofile':
                    D = {}
                    D['title'] = result.Title()
                    D['description'] = result.description_profile
                    D['image'] = '/++theme++vindula.liberiuntheme/imagens/img_box_destaque.jpg'
                    if result.image_profile:
                        D['image'] = '%s/image_thumb' % result.image_profile.to_object.absolute_url()
                    D['contents'] = []
                    if result.values():
                        contents = result.values()
                        for content in contents:
                            if content.portal_type == 'vindula.liberiuntheme.content.featuresection':
                                DC = {}
                                DC['id_content'] = content.getId()
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
                     sort_on= 'getObjPositionInParent', )
        
        L = []
        if results:
            for result in results:
                obj = result.getObject()
                D = {}
                D['id'] = obj.getId()
                D['title'] = obj.Title()
                D['description'] = obj.Description()
                D['subtitle'] = obj.subtitle
                D['image'] = ''
                if obj.image_title:
                    try:
                        D['image'] = obj.image_title.to_object.absolute_url()
                    except:
                        D['image'] = ''
                D['topics'] = []
                if obj.values():
                    topics = obj.values()
                    for topic in topics:
                        if topic.portal_type == 'vindula.liberiuntheme.content.featuretopic':
                            DT = {}
                            DT['id_topic'] = topic.getId()
                            DT['title_topic'] = topic.Title()
                            DT['description_topic'] = topic.Description()
                            DT['image_topic'] = ''
                            if topic.image_topic:
                                try:
                                    DT['image_topic'] = topic.image_topic.to_object.absolute_url()
                                except:
                                    DT['image_topic'] = ''
                            D['topics'].append(DT)
                            
                L.append(D)
                
        return L
        
        
            
            
            
            
            
            
            
            
            
            
            
            
            