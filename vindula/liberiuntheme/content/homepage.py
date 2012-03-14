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
                portal_type = ['Image','Banner',]
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
    
    # Fieldset highlights_left
    form.fieldset('highlights_left',
            label=_(u"Destaques da Esquerda"),
            fields=['highlight_left_title',
                    'highlight_left_title_content',
                    'highlight_left_link_content',
                    'highlight_left_description_content',
                    'highlight_left_image_content',
#                    'sub_highlight_left', 
#                    'sub_highlight_right', 
                    ])
    
    highlight_left_title = schema.TextLine(
        title=_(u"Título principal do destaque."),
        description=_(u"Insira um título para o destaque da esquerda."),
        required=False,
        )
    
    highlight_left_title_content = schema.TextLine(
        title=_(u"Título do conteúdo."),
        description=_(u"Insira um título do conteúdo da esquerda."),
        required=False,
        )
    
    highlight_left_link_content = schema.TextLine(
        title=_(u"Link para o título do conteúdo."),
        description=_(u"Insira um link para o título do conteúdo da esquerda."),
        required=False,
        )
    
    highlight_left_description_content = RichText(
        title=_(u"Descrição do conteúdo."),
        description=_(u"Insira uma descrição para o conteúdo da esquerda."),
        required=False,
        )
    
    highlight_left_image_content = RelationChoice(
        title=_(u"Imagem do conteúdo."),
        description=_(u"Selecine a imagem para o conteúdo da esquerda."),
        required=False,
        source=ObjPathSourceBinder(
            portal_type = 'Image',
            ),
        )
    
#    sub_highlight_left = RichText(
#        title=_(u"Sub destaque da esquerda"),
#        description=_(u"Conteúdo do sub destaque da esquerda."),
#        required=False,
#        )
#    
#    sub_highlight_right = RichText(
#        title=_(u"Sub destaque da direita"),
#        description=_(u"Conteúdo do sub destaque da direita."),
#        required=False,
#        )
    
    
    # Fieldset highlights_right
    form.fieldset('highlights_right',
            label=_(u"Destaques da Direita"),
            fields=['highlight_right_title',
                    'highlight_right_title_content_1',
                    'highlight_right_link_content_1',
                    'highlight_right_description_content_1',
                    'highlight_right_image_content_1',
                    'highlight_right_title_content_2',
                    'highlight_right_link_content_2',
                    'highlight_right_description_content_2',
                    'highlight_right_image_content_2',
                    ])
    
    highlight_right_title = schema.TextLine(
        title=_(u"Título principal do destaque"),
        description=_(u"Insira um título para o destaque da direita."),
        required=False,
        )
    
    highlight_right_title_content_1 = schema.TextLine(
        title=_(u"Título do primeiro conteúdo."),
        description=_(u"Insira um título do primeiro conteúdo da direita."),
        required=False,
        )
    
    highlight_right_link_content_1 = schema.TextLine(
        title=_(u"Link para o título do primeiro conteúdo."),
        description=_(u"Insira um link para o título do primeiro conteúdo da direita."),
        required=False,
        )
    
    highlight_right_description_content_1 = RichText(
        title=_(u"Descrição do primeiro conteúdo."),
        description=_(u"Insira uma descrição para o primeiro conteúdo da direita."),
        required=False,
        )
    
    highlight_right_image_content_1 = RelationChoice(
        title=_(u"Imagem do primeiro conteúdo."),
        description=_(u"Selecine a imagem para o primeiro conteúdo da direita."),
        required=False,
        source=ObjPathSourceBinder(
            portal_type = 'Image',
            ),
        )
    
    highlight_right_title_content_2 = schema.TextLine(
        title=_(u"Título do segundo conteúdo."),
        description=_(u"Insira um título do segundo conteúdo da direita."),
        required=False,
        )
    
    highlight_right_link_content_2 = schema.TextLine(
        title=_(u"Link para o segundo título do conteúdo."),
        description=_(u"Insira um link para o segundo título do conteúdo da direita."),
        required=False,
        )
    
    highlight_right_description_content_2 = RichText(
        title=_(u"Descrição do conteúdo."),
        description=_(u"Insira uma descrição para o conteúdo da direita."),
        required=False,
        )
    
    highlight_right_image_content_2 = RelationChoice(
        title=_(u"Imagem do segundo conteúdo."),
        description=_(u"Selecine a imagem para o segundo conteúdo da direita."),
        required=False,
        source=ObjPathSourceBinder(
            portal_type = 'Image',
            ),
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
                portal_type = ('VindulaNews', 'Document'), 
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
                portal_type = ('VindulaNews', 'Document'), 
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
                portal_type = ('VindulaNews', 'Document'), 
                review_state='published'
                )
            ),
        required=False,
        )
    
    # Fieldset content list
    form.fieldset('content_lists',
            label=_(u"Listas de Conteúdo"),
            fields=['content_list_left_title',
                    'choice_type_left',
                    'content_list_left',
                    'content_list_collection_left',
                    'content_list_right_title',
                    'choice_type_right',
                    'content_list_right',
                    'content_list_collection_right',
                    'items_page',
                    ])
    
    content_list_left_title = schema.TextLine(
        title=_(u"Título"),
        description=_(u"Título da lista de conteúdo da esquerda."),
        required=False,
        )
    
    choice_type_left = schema.Bool(
        title=_(u"Usar Coleção."),
        description=_(u"Selecione se vai usar um conteúdo Coleção."),
        required=False,
        )
    
    content_list_left = RelationList(
        title=_(u"Lista de conteúdo da esquerda."),
        description=_(u"Selecione a pasta onde estão os conteúdos que serão listados. \
                        Serão listados conteúdos do tipo Notícia e Evento. \n \
                        (Se a opção usar coleção estiver marcada os conteúdos marcados aqui serão ignorados.)"),
        default=[],                        
        value_type=RelationChoice(
            title=_(u"Caixa de conteúdo da esquerda"),
            source=ObjPathSourceBinder(
                portal_type = ('VindulaNews', 'Event'),  
                review_state='published'       
                )
            ),
        required=False,
        )
    
    content_list_collection_left = RelationChoice(
        title=_(u"Lista de conteúdo da esquerda (Coleção)."),
        description=_(u"Selecione um conteúdo Coleção com conteúdos de tipo notícia ou evento que serão listados do painel da esquerda."),
        source=ObjPathSourceBinder(
            portal_type = 'Topic',  
            review_state='published'       
            ),
        required=False,
        )
    
    content_list_right_title = schema.TextLine(
        title=_(u"Título"),
        description=_(u"Título da lista de conteúdo da direita."),
        required=False,
        )
    
    choice_type_right = schema.Bool(
        title=_(u"Usar Coleção."),
        description=_(u"Selecione se vai usar um conteúdo Coleção."),
        required=False,
        )
    
    content_list_right = RelationList(
        title=_(u"Lista de conteúdo da direita"),
        description=_(u"Selecione a pasta onde estão os conteúdos que serão listados. \
                        Serão listados conteúdos do tipo Notícia e Evento. \n \
                        (Se a opção usar coleção estiver marcada os conteúdos marcados aqui serão ignorados.)"),
        default=[],                        
        value_type=RelationChoice(
            title=_(u"Caixa de conteúdo da direita"),
            source=ObjPathSourceBinder(
                portal_type = ('VindulaNews', 'Event'),
                review_state='published'       
                )
            ),
        required=False,
        )
    
    content_list_collection_right = RelationChoice(
        title=_(u"Lista de conteúdo da direita (Coleção)."),
        description=_(u"Selecione um conteúdo Coleção com conteúdos de tipo notícia ou evento que serão listados do painel da direita."),
        source=ObjPathSourceBinder(
            portal_type = 'Topic',  
            review_state='published'       
            ),
        required=False,
        )
    
    items_page = schema.Int(
        title=_(u"Itens por página."),
        description=_(u"Quantos itens serão exibidos por página."),
        required=True,
        default=4,
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
                    if obj.portal_type == 'VindulaNews':
                        D['description'] = self.limitTextSize(350, obj.Description())
                        if obj.getImageRelac():
                            D['image'] = obj.getImageRelac().absolute_url()  + '/image_tile'
                    else:
                        D['description'] = self.limitTextSize(350, obj.Description())
                    L.append(D)
            
            item = [titles[n], L]
            contents.append(item)
            n += 1
        
        return contents
    
    def getContentLists(self):
        fields = []
        titles = []

        if self.context.choice_type_left:
            try:
                fields.append(self.context.content_list_collection_left.to_object.queryCatalog())
                titles.append(self.context.content_list_left_title)
            except:
                pass
        else:
            if len(self.context.content_list_left) >= 1:
                fields.append(self.context.content_list_left)
                titles.append(self.context.content_list_left_title) 
        
        
        if self.context.choice_type_right:
            try:
                fields.append(self.context.content_list_collection_right.to_object.queryCatalog())
                titles.append(self.context.content_list_right_title)
            except:
                pass
        else:
            if len(self.context.content_list_right) >= 1:
                fields.append(self.context.content_list_right)
                titles.append(self.context.content_list_right_title)
        
        contents = []
        n = 0
        for field in fields:
            L = []
            if field:
                for obj in field:
                    try:
                        obj = obj.to_object
                    except:
                        obj = obj.getObject()
                    if obj is None:
                        field.remove(obj)
                        continue
                    D = {}
                    D['title'] = obj.Title()
                    D['link'] = obj.absolute_url()
                    D['image'] = ''
                    D['event'] = ''
                    D['author'] = ''
                    if obj.portal_type == 'VindulaNews':
                        D['description'] = self.limitTextSize(350, obj.Description())
                        D['author'] = obj.Creator() 
                        if obj.getImageRelac():
                            D['image'] = obj.getImageRelac().absolute_url()  + '/image_tile'      
                    else:
                        D['event'] = obj.startDate.strftime('%d/%m/%Y %H:%M') + ' Local: ' + obj.location
                        D['description'] = self.limitTextSize(350, obj.Description())
                    L.append(D)
            
            item = [titles[n], L]
            contents.append(item)
            n += 1
        
        return contents
    
    def getBanner(self):
        L = []
        if self.context.banner:
            for banner in self.context.banner:
                obj = banner.to_object
                try:
                    type_obj = obj.Type()
                except:
                    return L
                D={}
                if type_obj == 'Image':
                    D['image'] = obj.absolute_url()
                    D['url_image'] = ''
                    D['title'] = obj.title
                elif type_obj == 'Banner':
                    if obj.getLink():
                        D['url_image'] = ''
                        D['image'] = ''
                        D['title'] = obj.title
                        if obj.getRawImagem_banner():
                            D['image'] = obj.getRawImagem_banner().absolute_url()
                            
                        link = obj.getLink()
                        if link: 
                            if link[:4] == 'http':
                                D['url_image'] = link
                            else:
                                D['url_image'] = 'http://%s' % link
                L.append(D)
        return L
   
    def limitTextSize(self, size, text):
        if len(text) > size:
            i = size
            while text[i] != " ":
                i += 1              
            return text[:i]+'...'
        else:
            return text        