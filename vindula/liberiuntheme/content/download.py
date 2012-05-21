# -*- coding: utf-8 -*-
from five import grok

from vindula.liberiuntheme import MessageFactory as _

from AccessControl import ClassSecurityInfo

from vindula.liberiuntheme.content.interfaces import IDownload
from Products.ATContentTypes.content.document import ATDocumentSchema,ATDocumentBase

from zope.interface import implements
from Products.Archetypes.atapi import *
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from vindula.liberiuntheme.config import *
from DateTime.DateTime import DateTime
from time import strftime, gmtime


Download_schema = ATDocumentSchema.copy() + Schema((
                                                    
    TextField(
            name='desc_button',
            default_output_type='text/html',
            widget=RichWidget(
                label=_(u"Descrição do botão de download."),
                description=_(u"Insira uma descrição para o botão de download."),
                rows="5",
                label_msgid='vindula_liberiuntheme_label_desc_button',
                description_msgid='vindula_liberiuntheme_help_desc_button',
                i18n_domain='vindula_liberiuntheme',
            ),
            required=False,
    ),
    
    TextField(
            name='url_button',
            widget=StringWidget(
                label=_(u"URL para a fazer o download do primeiro botao."),
                description=_(u"Insira uma url para o primeiro botão."),
                label_msgid='vindula_liberiuntheme_label_url_button',
                description_msgid='vindula_liberiuntheme_help_url_button',
                i18n_domain='vindula_liberiuntheme',
            ),
        required=False,
    ),
    
    TextField(
            name='title_info_comp',
            widget=StringWidget(
                label=_(u"Título para coluna de informações complementares."),
                description=_(u"Insira um título para coluna de informações complementares."),
                label_msgid='vindula_liberiuntheme_label_title_info_comp',
                description_msgid='vindula_liberiuntheme_title_info_comp',
                i18n_domain='vindula_liberiuntheme',
            ),
        required=False,
    ),                                
    
    TextField(
            name='desc_info_comp',
            default_output_type='text/html',
            widget=RichWidget(
                label=_(u"Descrição para coluna de informações complementares."),
                description=_(u"Insira uma descrição para o botão de download."),
                rows="5",
                label_msgid='vindula_liberiuntheme_label_desc_info_comp',
                description_msgid='vindula_liberiuntheme_help_desc_info_comp',
                i18n_domain='vindula_liberiuntheme',
            ),
            required=False,
    ),
    
    StringField(
        name='version_download',
        widget=SelectionWidget(
            label=_(u"Versão do produto."),
            description=_(u"Selecione a versão deste produto"),
            format = 'select',
        ),
        vocabulary='voc_vesions',
        required=True,
    ),
    
    DateTimeField('release_date',
        searchable = 1,
        required = 0,
        default_method = 'getDefaultTime',
        widget = CalendarWidget(
            label=_(u"Data de Lancamento."),
            description=_(u"Selecione a data de lançamento da versão."),
            format = strftime("%d %m %Y", gmtime()),
            show_hm=False,
        ),
    ),
    
))

finalizeATCTSchema(Download_schema, folderish=False)

invisible = {'view':'invisible','edit':'invisible',}
#Download_schema['description'].widget.visible = invisible
Download_schema['text'].widget.visible = invisible

#Interface
class Download(ATDocumentBase):
    """ Download Page """
    
    security = ClassSecurityInfo()
    implements(IDownload)    
    portal_type = 'Download'
    _at_rename_after_creation = True
    schema = Download_schema
    
    def voc_vesions(self):
        return self.aq_parent.voc_vesions()
    
    def getDefaultTime(self):
        return DateTime()

registerType(Download, PROJECTNAME) 