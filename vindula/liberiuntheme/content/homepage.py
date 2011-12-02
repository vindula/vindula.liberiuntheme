# -*- coding: utf-8 -*-
from five import grok
from zope import schema
from plone.directives import form
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.app.textfield import RichText
from vindula.liberiuntheme import MessageFactory as _
from z3c.relationfield.schema import RelationList, RelationChoice
from Products.CMFCore.utils import getToolByName

# Interface and schema

class IHomePage(form.Schema):
    """ Home Page """
    
    # Fieldset Banner
    form.fieldset('banner',
            label=_(u"Banner"),
            fields=['title', 
                    'banner', 
                    'time_transition',
                    'banner_height',                    
                    ])
        
    title = schema.TextLine(
        title=_(u"Título"),
        description=_(u"Insira um nome para Home Page."),
        required=False,
        )
    
    banner = RelationList(
        title=_(u"Banner"),
        description=_(u"Selecione as imagens que deverão rotacionar na área de destaque abaixo do menu."),
        default=[],
        value_type=RelationChoice(
            title=_(u"Banner"),
            source=ObjPathSourceBinder(
                portal_type = 'Image',
                )
            ),
        required=False,
        )
    
    time_transition = schema.Int(
        title=_(u"Velocidade da rotação"),
        description=_(u"Tempo em milisegundos que a imagem leva para rotacionar, insira apenas números iteiros."),
        default=8000,
        required=True,
        )
    
    banner_height = schema.Int(
        title=_(u"Altura"),
        description=_(u"Altura em pixels da área onde as imagens irão rotacionar, insira apenas números iteiros."),
        default=340,
        required=True,
        )
    
    # Fieldset highlights
    form.fieldset('highlights',
            label=_(u"Destaques"),
            fields=['highlight_left_title', 
                    'highlight_left',
                    'highlight_right_title',
                    'highlight_right', 
                    'sub_highlight_left', 
                    'sub_highlight_right', 
                    ])
    
    highlight_left_title = schema.TextLine(
        title=_(u"Título"),
        description=_(u"Insira um título para o destaque da esquerda."),
        required=False,
        )

    highlight_left = RichText(
        title=_(u"Destaque da esquerda"),
        description=_(u"Conteúdo do destaque da esquerda."),
        required=False,
        )
    
    highlight_right_title = schema.TextLine(
        title=_(u"Título"),
        description=_(u"Insira um título para o destaque da direita."),
        required=False,
        )
    
    highlight_right = RichText(
        title=_(u"Destaque da direita"),
        description=_(u"Conteúdo do destaque da direita."),
        required=False,
        )
    
    sub_highlight_left = RichText(
        title=_(u"Sub destaque da esquerda"),
        description=_(u"Conteúdo do sub destaque da esquerda."),
        required=False,
        )
    
    sub_highlight_right = RichText(
        title=_(u"Sub destaque da direita"),
        description=_(u"Conteúdo do sub destaque da direita."),
        required=False,
        )
    
    
    # Fieldset content boxes
    form.fieldset('content_boxes',
            label=_(u"Caixas de Conteúdo"),
            fields=['content_box_left_title', 
                    'content_box_left', 
                    'content_box_middle_title', 
                    'content_box_middle', 
                    'content_box_right_title', 
                    'content_box_right', 
                    ])
    
    content_box_left_title = schema.TextLine(
        title=_(u"Título"),
        description=_(u"Título da caixa de conteúdo da esquerda."),
        default=_(u""),
        required=False,
        )
    
    content_box_left = RelationList(
        title=_(u"Caixa de conteúdo da esquerda"),
        description=_(u"Selecione páginas ou notícias para serem listadas na caixa de conteúdo da esquerda. \
                        Será apresentado somente o título, descrição e a imagem se for uma notícia."),
        default=[],
        value_type=RelationChoice(
            title=_(u"Caixa de conteúdo da esquerda"),
            source=ObjPathSourceBinder(
                portal_type = ('vindula.content.content.vindulanews', 'Document'), 
                review_state='published'
                )
            ),
        required=False,
        )
    
    content_box_middle_title = schema.TextLine(
        title=_(u"Título"),
        description=_(u"Título da caixa de conteúdo do meio."),
        default=_(u""),
        required=False,
        )
    
    content_box_middle = RelationList(
        title=_(u"Caixa de conteúdo do meio"),
        description=_(u"Selecione páginas ou notícias para serem listadas na caixa de conteúdo do meio. \
                        Será apresentado somente o título, descrição e a imagem se for uma notícia."),
        default=[],
        value_type=RelationChoice(
            title=_(u"Caixa de conteúdo do meio"),
            source=ObjPathSourceBinder(
                portal_type = ('vindula.content.content.vindulanews', 'Document'), 
                review_state='published'
                )
            ),
        required=False,
        )
    
    content_box_right_title = schema.TextLine(
        title=_(u"Título"),
        description=_(u"Título da caixa de conteúdo da direita."),
        default=_(u""),
        required=False,
        )
    
    content_box_right = RelationList(
        title=_(u"Caixa de conteúdo da direita"),
        description=_(u"Selecione páginas e notícias para serem listadas na caixa de conteúdo da direita. \
                        Será apresentado somente o título, descrição e a imagem se for uma notícia."),
        default=[],
        value_type=RelationChoice(
            title=_(u"Caixa de conteúdo da direita"),
            source=ObjPathSourceBinder(
                portal_type = ('vindula.content.content.vindulanews', 'Document'), 
                review_state='published'
                )
            ),
        required=False,
        )
    
    # Fieldset content list
    form.fieldset('content_lists',
            label=_(u"Listas de Conteúdo"),
            fields=['content_list_left_title', 
                    'content_list_left', 
                    'content_list_right_title', 
                    'content_list_right', 
                    ])
    
    content_list_left_title = schema.TextLine(
        title=_(u"Título"),
        description=_(u"Título da lista de conteúdo da esquerda."),
        required=False,
        )
    
    content_list_left = RelationList(
        title=_(u"Lista de conteúdo da esquerda"),
        description=_(u"Selecione a pasta onde estão os conteúdos que serão listados. \
                        Serão listados conteúdos do tipo página, notícia e evento."),
        default=[],                        
        value_type=RelationChoice(
            title=_(u"Caixa de conteúdo da esquerda"),
            source=ObjPathSourceBinder(
                portal_type = 'Event',  
                review_state='published'       
                )
            ),
        required=False,
        )
    
    content_list_right_title = schema.TextLine(
        title=_(u"Título"),
        description=_(u"Título da lista de conteúdo da direita."),
        required=False,
        )
    
    content_list_right = RelationList(
        title=_(u"Lista de conteúdo da direita"),
        description=_(u"Selecione a pasta onde estão os conteúdos que serão listados. \
                        Serão listados conteúdos do tipo página, notícia e evento."),
        default=[],                        
        value_type=RelationChoice(
            title=_(u"Caixa de conteúdo da direita"),
            source=ObjPathSourceBinder(
                portal_type = 'vindula.content.content.vindulanews',  
                review_state='published'       
                )
            ),
        required=False,
        )
    
# View
    
class HomePageView(grok.View):
    grok.context(IHomePage)
    grok.require('zope2.View')
    grok.name('view')
    
    # Methods for News
    
    def getContentBoxes(self):
        fields = [self.context.content_box_left, 
                  self.context.content_box_middle, 
                  self.context.content_box_right]
        
        titles = [self.context.content_box_left_title, 
                  self.context.content_box_middle_title, 
                  self.context.content_box_right_title]
        
        contents = []
        n = 0
        
        for field in fields:
            L = []
            if field:
                for obj in field:
                    obj = obj.to_object
                    if obj is None:
                        objs.remove(obj)
                        continue
                    D = {}
                    D['title'] = obj.Title()
                    D['link'] = obj.absolute_url()
                    D['image'] = ''
                    if obj.portal_type == 'vindula.content.content.vindulanews':
                        D['description'] = obj.summary
                        
                        if obj.image:
                            D['image'] = obj.image.to_object.absolute_url()  + '/image_tile'      
                    else:
                        D['description'] = obj.Description()
                    L.append(D)
            
            item = [titles[n], L]
            contents.append(item)
            n += 1
        
        return contents
    
    def getContentLists(self):
        fields = [self.context.content_list_left, 
                  self.context.content_list_right]
        
        titles = [self.context.content_list_left_title, 
                  self.context.content_list_right_title]
        
        contents = []
        n = 0
        
        for field in fields:
            L = []
            if field:
                for obj in field:
                    obj = obj.to_object
                    if obj is None:
                        objs.remove(obj)
                        continue
                    D = {}
                    D['title'] = obj.Title()
                    D['link'] = obj.absolute_url()
                    D['image'] = ''
                    if obj.portal_type == 'vindula.content.content.vindulanews':
                        D['description'] = obj.summary
                        
                        if obj.image:
                            D['image'] = obj.image.to_object.absolute_url()  + '/image_tile'      
                    else:
                        D['description'] = obj.Description()
                    L.append(D)
            
            item = [titles[n], L]
            contents.append(item)
            n += 1
        
        return contents