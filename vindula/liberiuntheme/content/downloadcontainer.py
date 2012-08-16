# -*- coding: utf-8 -*-
from five import grok

from vindula.content import MessageFactory as _
from AccessControl import ClassSecurityInfo
from Products.CMFCore.utils import getToolByName

from vindula.liberiuntheme.content.interfaces import IDownloadContainer
from plone.app.folder.folder import ATFolder

from zope.interface import implements
from Products.Archetypes.atapi import *
from archetypes.referencebrowserwidget.widget import ReferenceBrowserWidget
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from vindula.liberiuntheme.config import *


DownloadContainer_schema =  ATFolder.schema.copy() + Schema((
                                                            
    ReferenceField('image_banner',
        multiValued=0,
        allowed_types=('Image', 'Banner'),
        relationship='image_banner',
        widget=ReferenceBrowserWidget(
            default_search_index='SearchableText',
            label=_(u"Banner"),
            description=_(u"Selecione as imagens que deverão rotacionar na área de destaque abaixo do menu."),
            
            label_msgid='vindula_liberiuntheme_label_image_banner',
            description_msgid='vindula_liberiuntheme_help_image_banner',
            i18n_domain='vindula_liberiuntheme',
            ),
        required=False
    ),
    
#    IntegerField(
#        name='time_transition',
#        widget=IntegerWidget(
#            label=_(u"Velocidade da rotação do banner"),
#            description=_(u"Tempo em milisegundos que a imagem do banner leva para rotacionar, \
#                          insira apenas números iteiros."),
#            
#            label_msgid='vindula_liberiuntheme_label_time_transition',
#            description_msgid='vindula_liberiuntheme_help_time_transition',
#            i18n_domain='vindula_liberiuntheme',
#        ),
#        default=8000,
#        required=True,
#    ),
    
#    IntegerField(
#        name='banner_height',
#        widget=IntegerWidget(
#            label=_(u"Altura"),
#            description=_(u"Altura em pixels da área onde as imagens irão rotacionar, insira apenas números iteiros."),
#            
#            label_msgid='vindula_liberiuntheme_label_banner_height',
#            description_msgid='vindula_liberiuntheme_help_banner_height',
#            i18n_domain='vindula_liberiuntheme',
#        ),
#        default=340,
#        required=True,
#    ),
    
    StringField(
        name='current_vesion',
        widget=SelectionWidget(
            label=_(u"Versão Atual"),
            description=_(u"Selecione a versão atual"),
            format = 'select',
        ),
        vocabulary='voc_vesions',
        required=True,
    ),
    
    ReferenceField('primeira_coluna',
        multiValued=0,
        allowed_types=('Download'),
        relationship='primeira_coluna',
        widget=ReferenceBrowserWidget(
            default_search_index='SearchableText',
            label=_(u"Selecione o primeiro Download"),
            description=_(u"Selecione um conteúdo Download para apercer na visulização dos downloads."),
            
            label_msgid='vindula_liberiuntheme_label_primeira_coluna',
            description_msgid='vindula_liberiuntheme_help_primeira_coluna',
            i18n_domain='vindula_liberiuntheme',
            ),
        required=False
    ),
    
    ReferenceField('segunda_coluna',
        multiValued=0,
        allowed_types=('Download'),
        relationship='segunda_coluna',
        widget=ReferenceBrowserWidget(
            default_search_index='SearchableText',
            label=_(u"Selecione o segundo Download"),
            description=_(u"Selecione um conteúdo Download para apercer na visulização dos downloads."),
            
            label_msgid='vindula_liberiuntheme_label_segunda_coluna',
            description_msgid='vindula_liberiuntheme_help_segunda_coluna',
            i18n_domain='vindula_liberiuntheme',
            ),
        required=False
    ),
    
    ReferenceField('terceira_coluna',
        multiValued=0,
        allowed_types=('Download'),
        relationship='terceira_coluna',
        widget=ReferenceBrowserWidget(
            default_search_index='SearchableText',
            label=_(u"Selecione o terceiro Download"),
            description=_(u"Selecione um conteúdo Download para apercer na visulização dos downloads."),
            
            label_msgid='vindula_liberiuntheme_label_terceira_coluna',
            description_msgid='vindula_liberiuntheme_help_terceira_coluna',
            i18n_domain='vindula_liberiuntheme',
            ),
        required=False
    ),
    
    TextField(
            name='title_others',
            widget=StringWidget(
                label=_(u"Titulo para otros Downloads."),
                description=_(u"Insira um título para aparecer na parte de outros Downloads."),
                label_msgid='vindula_liberiuntheme_label_description_others',
                description_msgid='vindula_liberiuntheme_description_others',
                i18n_domain='vindula_liberiuntheme',
            ),
        required=False,
    ), 
    
    TextField(
            name='description_others',
            widget=TextAreaWidget(
                label=_(u"Descrição para outros Downloads."),
                description=_(u"Insira uma descrição para aparecer na parte de outros Downloads."),
                label_msgid='vindula_liberiuntheme_label_description_others',
                description_msgid='vindula_liberiuntheme_description_others',
                i18n_domain='vindula_liberiuntheme',
                rows="3",
            ),
        required=False,
    ), 
    
    TextField(
            name='versions',
            widget=TextAreaWidget(
                label=_(u"Versões existes para Download."),
                description=_(u"Cadastre as versões disponiveis para download. Uma versão por linha."),
                
                label_msgid='vindula_liberiuntheme_label_versions',
                description_msgid='vindula_liberiuntheme_help_versions',
                i18n_domain='vindula_liberiuntheme',
            ),
        default='1.0',
        required=True,
    ),
    
))

finalizeATCTSchema(DownloadContainer_schema, folderish=True)
DownloadContainer_schema.changeSchemataForField('versions', 'Cadastrar Versões')

class DownloadContainer(ATFolder):
    """ Download Container """
    security = ClassSecurityInfo()
    implements(IDownloadContainer)
    portal_type = 'DownloadContainer'
    _at_rename_after_creation = True
    schema = DownloadContainer_schema
    
    def voc_vesions(self):
        L=[]
        versions = self.versions().replace('\r','').split('\n')
        if versions:
            L = versions
        return L

registerType(DownloadContainer, PROJECTNAME) 
    
#View
class DownloadContainerView(grok.View):
    grok.context(IDownloadContainer)
    grok.require('zope2.View')
    grok.name('view')
    
    def getBanner(self):
        D = {}
        if self.context.getImage_banner():
            banner = self.context.getImage_banner()
            try:
                type_obj = banner.Type()
            except:
                return L
            if type_obj == 'Image':
                D['image'] = banner.absolute_url()
                D['url_image'] = ''
                D['title'] = banner.title
            elif type_obj == 'Banner':
                if banner.getLink():
                    D['url_image'] = ''
                    D['image'] = ''
                    D['target'] = banner.getTarget()
                    D['title'] = banner.title
                    if banner.getRawImagem_banner():
                        D['image'] = banner.getRawImagem_banner().absolute_url()
                        
                    link = banner.getLink()
                    if link: 
                        if link[:4] == 'http':
                            D['url_image'] = link
                        else:
                            D['url_image'] = 'http://%s' % link
        return D
    
    
    def getSelectedDownloads(self):
        primeira = self.context.getPrimeira_coluna()
        segunda = self.context.getSegunda_coluna()
        terceira = self.context.getTerceira_coluna()
        selected_downloads = [primeira, segunda, terceira]
        L=[]
        if selected_downloads:
            for selected_download in selected_downloads:
                if selected_download:
                    D={}
                    D = self.getDicDownload(selected_download)  
                    L.append(D)
        return L
    
    
    def getOtherVersions(self):
        current_version = self.context.getCurrent_vesion()
        pc = getToolByName(self.context, 'portal_catalog')
        query = '/'.join(self.context.getPhysicalPath())
        results = pc( path={'query': query},
                     portal_type='Download',
                     review_state='published',
                     sort_on= 'getObjPositionInParent', )
        L=[]
        if results:
            for item in results:
                obj = item.getObject()
                if obj.getVersion_download() != current_version:
                    D={}
                    D = self.getDicDownload(obj)                
                    L.append(D)
        if L:
            L.sort(key=lambda item:item['release_date'], reverse=True)
        return L
    
    
    def getDicDownload(self, obj):
        if obj.Type() == 'Download':
            D={}
            D['title'] = obj.Title()
            D['description'] = obj.Description()
            D['absolute_url'] = obj.absolute_url()
            D['desc_button'] = obj.getDesc_button().replace('<p>','').replace('</p>','').replace('\n', '<br>')
            D['url_button'] = obj.getUrl_button()
            if D['url_button'][:4] != 'http':
                D['url_button'] = 'http://'+obj.getUrl_button()
            D['title_info_comp'] = obj.getTitle_info_comp()
            D['desc_info_comp'] = obj.getDesc_info_comp()
            D['release_date'] = obj.release_date.strftime('%d/%m/%Y')
            return D
        return None
            
            
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    