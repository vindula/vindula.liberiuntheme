# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName

def installTheme(context):    
    portal = context.getSite()
    portal_workflow = getToolByName(portal, 'portal_workflow')
    
    if not 'social-networks' in portal.objectIds():
        portal.invokeFactory('Folder', 
                              id='social-networks', 
                              title='Redes Sociais',
                              excludeFromNav = True)
        
        pasta = portal['social-networks']
        pasta.setConstrainTypesMode(1)
        pasta.setLocallyAllowedTypes(('vindula.liberiuntheme.content.socialnetwork',))
        portal_workflow.doActionFor(pasta, 'publish')