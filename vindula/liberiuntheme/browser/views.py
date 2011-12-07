# -*- coding: utf-8 -*-
from five import grok
from zope.interface import Interface
from plone.app.layout.navigation.interfaces import INavigationRoot


class ThemeSettingsView(grok.View):
    grok.context(Interface)
    grok.require('cmf.ManagePortal')
    grok.name('theme-settings-css')
    
    def render(self):
        portal = self.context.portal_url.getPortalObject()
        css = ''
        
        # Portal Width
        try:
            obj = portal.get('control-panel-objects').get('vindula_themeconfig')
        except:
            obj = None
        if obj:
            if obj.width_page != '':
                css += '#visual-portal-wrapper { width:%spx; }' % str(obj.width_page)
            
        return css