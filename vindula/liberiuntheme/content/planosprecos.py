# -*- coding: utf-8 -*-
from five import grok

from vindula.liberiuntheme import MessageFactory as _

from AccessControl import ClassSecurityInfo

from vindula.liberiuntheme.content.interfaces import IPlanosPrecos
from Products.ATContentTypes.content.document import ATDocumentSchema,ATDocumentBase

from zope.interface import implements
from Products.Archetypes.atapi import *
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from vindula.liberiuntheme.config import *
from DateTime.DateTime import DateTime
from time import strftime, gmtime


PlanosPrecos_schema = ATDocumentSchema.copy() + Schema((

    TextField(
            name='URLButton',
            widget=StringWidget(
                label=_(u"URL do destino."),
                description=_(u"Insira a URL que o usuário será direcionado ao clicar no botão de 'assinar'."),
                label_msgid='vindula_liberiuntheme_label_title_URLButton',
                description_msgid='vindula_liberiuntheme_title_URLButton',
                i18n_domain='vindula_liberiuntheme',
            ),
        required=True,
    ),        
    
    
    IntegerField(
        name='preco',
        widget=IntegerWidget(
            label=_(u"Valor do plano"),
            description=_(u"Valor do plano."),
            
            label_msgid='vindula_liberiuntheme_label_preco',
            description_msgid='vindula_liberiuntheme_help_preco',
            i18n_domain='vindula_liberiuntheme',
        ),
        required=True,
    ),                        
    
    LinesField(
        name='featuresPlan',
        widget=InAndOutWidget(
            label=_(u"Funcionalidades do plano."),
            description=_(u"Selecione as funcionalidades presentes nessa versao."),
        ),
        vocabulary='getFeatures',
        required=True,
    ),
    
))

finalizeATCTSchema(PlanosPrecos_schema, folderish=False)

invisible = {'view':'invisible','edit':'invisible',}
#PlanosPrecos_schema['description'].widget.visible = invisible
PlanosPrecos_schema['text'].widget.visible = invisible

#Interface
class PlanosPrecos(ATDocumentBase):
    """ PlanosPrecos Page """
    
    security = ClassSecurityInfo()
    implements(IPlanosPrecos)    
    portal_type = 'PlanosPrecos'
    _at_rename_after_creation = True
    schema = PlanosPrecos_schema
    
    def getFeatures(self):
        L=[]
        dics = self.aq_parent.getFeatures()
        for dic in dics:
            L.append(dic['feature'])
        return L

registerType(PlanosPrecos, PROJECTNAME) 