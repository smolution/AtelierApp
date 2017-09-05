# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField, TextAreaField, SelectField, HiddenField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, Email

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember_me', default = False)

class ContactForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(u'Uveďte prosím Vaši emailovou adresu, abychom Vás mohli kontaktovat.'), Email()])
    name = StringField(u'Jméno', validators=[DataRequired(u'Vaše jméno, prosím'), Length(min=3)])
    surname = StringField(u'Příjmení', validators=[DataRequired(u'Vaše příjmení'), Length(min=3)])
    telephone = StringField(u'Telefon', validators=[DataRequired(u'Vyplňte prosím Vaše telefonní číslo.'), Length(min=9)])
    message = TextAreaField(u'Vaše zpráva', validators=[DataRequired(u'Nechtěli jste nám něco sdělit?'), Length(min=1)])

class PhotoForm(FlaskForm):
    filename = HiddenField()
    category = QuerySelectField(u'Kategorie', allow_blank=True, blank_text=u'---', get_label="fullname")
    subcategory = QuerySelectField(u'Podkategorie', allow_blank=True, blank_text=u'---', get_label="fullname")
    collection = QuerySelectField(u'Kolekce', allow_blank=True, blank_text=u'---', get_label="fullname")
    featured = BooleanField(u'Zdůraznit', default= False)
    slideshow = BooleanField(u'Slideshow', default = False)
    active = BooleanField(u'Aktivní', default = True)
    save = BooleanField(u'Uložit', default = False)

