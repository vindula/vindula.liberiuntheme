# -*- coding: utf-8 -*-
from zope import schema
from plone.directives import form
from plone.formwidget.contenttree import ObjPathSourceBinder
from vindula.liberiuntheme import MessageFactory as _
from z3c.relationfield.schema import RelationChoice

# Interface and schema

class ISocialNetwork(form.Schema):
    """ Social Network """
        
    image = RelationChoice(
        title=_(u"Imagem"),
         description=_(u"Insira uma imagem, ícone ou logo que faça referência à rede social."),
         source=ObjPathSourceBinder(
             portal_type = 'Image',
             ),
         required=False,
         )
    
    image_width = schema.Int(
        title=_(u"Largura da imagem"),
        description=_(u"Largura da imagem em pixels, insira apenas números iteiros."),
        default=32,
        required=False,
        )
    
    image_height = schema.Int(
        title=_(u"Altura da imagem"),
        description=_(u"Altura da imagem em pixels, insira apenas números iteiros."),
        default=32,
        required=False,
        )

    link = schema.TextLine(
        title=_(u"Link"),
        description=_(u"Insira a URL de destino do link."),
        required=False,
        )