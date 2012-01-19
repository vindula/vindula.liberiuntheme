# -*- coding: utf-8 -*-
from five import grok
from zope.interface import Interface
from plone.app.layout.viewlets.interfaces import IPortalHeader, IAboveContent, IPortalFooter
from Products.CMFCore.utils import getToolByName
from zope.app.component.hooks import getSite

grok.context(Interface) 

# Viewlet for portal logo top

class LogoTopViewlet(grok.Viewlet): 
    grok.name('vindula.liberiuntheme.logotop') 
    grok.require('zope2.View')
    grok.viewletmanager(IPortalHeader) 
    
    
# Viewlet for social network icons

class SocialNetworksViewlet(grok.Viewlet): 
    grok.name('vindula.liberiuntheme.social-networks') 
    grok.require('zope2.View')
    grok.viewletmanager(IPortalHeader)
    
    def getIcons(self):
        portal = self.context.portal_url.getPortalObject()
        if 'redes-sociais' in portal.objectIds():
            pasta = portal['redes-sociais']
            self.pc = getToolByName(self.context, 'portal_catalog')
            links = self.pc(path={'query':'/'.join(pasta.getPhysicalPath())},
                            portal_type='vindula.liberiuntheme.content.socialnetwork',
                            review_state='published',
                            sort_on="getObjPositionInParent")
            
            if links:
                L = []
                for link in links:
                    L.append(link.getObject())
                return L
            
            
# Viewlet for portal footer

class FooterViewlet(grok.Viewlet): 
    grok.name('vindula.liberiuntheme.footer') 
    grok.require('zope2.View')
    grok.viewletmanager(IPortalFooter)
    

# Viewlet for navigation

class NavigationViewlet(grok.Viewlet): 
    grok.name('vindula.liberiuntheme.navigation') 
    grok.require('zope2.View')
    grok.viewletmanager(IPortalFooter)
    
    def getContentTypes(self):
        portal = self.context.portal_url.getPortalObject()
        if 'control-panel-objects' in portal.keys():
            control = portal['control-panel-objects']
            if 'vindula_themeconfig' in control.keys():
                thema = control['vindula_themeconfig']    
                itens = thema.itens_menu
                
                if itens:
                    return itens
                else:
                    return ['Folder', 'Link']

            return ['Folder', 'Link']
        else:
            return ['Folder', 'Link']
    
    def getMenu(self):
        portal = self.context.portal_url.getPortalObject()
        types = self.getContentTypes()
                
        urltool = getSite().portal_url
        caminho = {'query': '/'.join(portal.getPhysicalPath()), 'depth': 1}
        ctool = getSite().portal_catalog
        menus = ctool(portal_type=types, path=caminho, sort_on='getObjPositionInParent')   
        #menus = portal.objectValues(['ATFolder','ATLink','vindula.content.content.vindulacontentmacro'])
        if menus:
            L = []
            for obj in menus:
                if self.checkObj(obj.getObject()):
                    L.append(obj.getObject())
            return L
         
    def getSubMenu(self, menu):
        submenus = menu.objectValues('ATFolder')
        if submenus:
            L = []
            for obj in submenus:
                if self.checkObj(obj):
                    L.append(obj)
            return L

    def checkObj(self, obj):
        roles = self.context.portal_membership.getAuthenticatedMember().getRoles()
        state = getToolByName(obj, 'portal_workflow').getInfoFor(obj, 'review_state', None)
        try:
            if obj.getExcludeFromNav() == True:
                return False
        except:
            try:
                if obj.exclude_from_nav == True:
                    return False
            except:
                return False
        
        if 'Anonymous' in roles and state == 'private':
            return False
        return True