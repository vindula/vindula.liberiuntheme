# -*- coding: utf-8 -*-
from five import grok

from vindula.content import MessageFactory as _
from AccessControl import ClassSecurityInfo
from Products.CMFCore.utils import getToolByName

from vindula.liberiuntheme.content.interfaces import IPlanosPrecosContainer
from plone.app.folder.folder import ATFolder

from zope.interface import implements
from Products.Archetypes.atapi import *
from archetypes.referencebrowserwidget.widget import ReferenceBrowserWidget
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from vindula.liberiuntheme.config import *

# Local imports
from Products.DataGridField import DGFMessageFactory as _
from Products.DataGridField import DataGridField, DataGridWidget
from Products.DataGridField.Column import Column
from Products.DataGridField.SelectColumn import SelectColumn
from Products.DataGridField.RadioColumn import RadioColumn
from Products.DataGridField.CheckboxColumn import CheckboxColumn
from Products.DataGridField.FixedColumn import FixedColumn
from Products.DataGridField.DataGridField import FixedRow
from Products.DataGridField.HelpColumn import HelpColumn


PlanosPrecosContainer_schema =  ATFolder.schema.copy() + Schema((
                                                                 
    TextField(
            name='compareTitle',
            widget=StringWidget(
                label=_(u"Titulo para tabela comparativa."),
                description=_(u"Insira um título para aparecer sobre a tabela comparativa."),
                label_msgid='vindula_liberiuntheme_label_compareTitle',
                description_msgid='vindula_liberiuntheme_compareTitle',
                i18n_domain='vindula_liberiuntheme',
            ),
        default='Comparativo',
        required=False,
    ),
    
    TextField(
            name='compareSubtitle',
            widget=StringWidget(
                label=_(u"Subtitulo para tabela comparativa."),
                description=_(u"Insira um subtítulo para aparecer sobre a tabela comparativa."),
                label_msgid='vindula_liberiuntheme_label_compareSubtitle',
                description_msgid='vindula_liberiuntheme_compareSubtitle',
                i18n_domain='vindula_liberiuntheme',
            ),
        default='Planos x Funcionalidade',
        required=False,
    ),                                                             
                                                                 
    TextField(
            name='Topics',
            widget=TextAreaWidget(
                label=_(u"Funcionalidades existentes nos planos."),
                description=_(u"Cadastre as funcionalidades dos planos. Uma funcionalidade por linha."),
                
                label_msgid='vindula_liberiuntheme_label_versions',
                description_msgid='vindula_liberiuntheme_help_versions',
                i18n_domain='vindula_liberiuntheme',
            ),
        required=False,
    ),
                                                                 
    DataGridField('Features',
        searchable=True,
        columns=('feature', 'topic'),
#        fixed_rows = "getPredefinedSkillsData",
        allow_delete = True,
        allow_insert = True,
        allow_reorder = True,
        widget = DataGridWidget(
            label="Funcionalidades",
            label_msgid='vindula_liberiuntheme_label_versions',
            description="Funcionalidades existentes nos planos.",
            description_msgid='vindula_liberiuntheme_help_versions',
            columns= {
                "feature" : Column(_(u"Funcionalidade")),
                "topic" : SelectColumn(_(u"Topico"), vocabulary="getTopics")
            }
        ),
    ),                                                            
))

finalizeATCTSchema(PlanosPrecosContainer_schema, folderish=True)
PlanosPrecosContainer_schema.changeSchemataForField('Topics', 'Cadastrar Funcionalidades')
PlanosPrecosContainer_schema.changeSchemataForField('Features', 'Cadastrar Funcionalidades')

invisivel = {'view':'invisible','edit':'invisible',}
# Dates
L = ['effectiveDate','expirationDate','creation_date','modification_date']   
# Categorization
L += ['subject','relatedItems','location','language']
# Ownership
L += ['creators','contributors','rights']
# Settings
L += ['allowDiscussion','excludeFromNav', 'nextPreviousEnabled']

for i in L:
    PlanosPrecosContainer_schema[i].widget.visible = invisivel  

class PlanosPrecosContainer(ATFolder):
    """ Planos e Precos Container """
    security = ClassSecurityInfo()
    implements(IPlanosPrecosContainer)
    portal_type = 'PlanosPrecosContainer'
    _at_rename_after_creation = True
    schema = PlanosPrecosContainer_schema
    
    def getTopics(self):
        L=[]
        topics = self.Topics().replace('\r','').split('\n')
        for topic in topics:
            L.append(((topic), _(topic)))
        return DisplayList(tuple(L))

registerType(PlanosPrecosContainer, PROJECTNAME)
    
#View
class PlanosPrecosContainerView(grok.View):
    grok.context(IPlanosPrecosContainer)
    grok.require('zope2.View')
    grok.name('view')
    
    def getPlanos(self):
        pc = getToolByName(self.context, 'portal_catalog')
        query = {}
        query['portal_type'] = 'PlanosPrecos'
        query['review_state'] = 'published'
        query['sort_on'] = 'getObjPositionInParent'
        query['path'] = {'query': '/'.join(self.context.getPhysicalPath()), 'depth': 1}
        results = pc(query)
        
        if results:
            return results
        return None
    
    def getTopics(self):
        L = []
        [L.append(dic['topic']) for dic in self.context.getFeatures() if dic['topic'] not in L]
        return L
    
    def getFeatures(self, topic=None):
        L = []
        [L.append(dic['feature']) for dic in self.context.getFeatures() if dic['topic'] == topic ]
        return L
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    