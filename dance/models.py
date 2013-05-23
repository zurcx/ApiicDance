# encoding: utf-8

from django.db import models

class Rhythm(models.Model):
    name = models.CharField(verbose_name=u'Nome', max_length=150,
        help_text=u'O nome do ritmo')
    slug = models.SlugField(verbose_name=u'Apelido', max_length=100)
    description = models.TextField(verbose_name=u'Descrição',
        blank=True)

    photo = models.ImageField(upload_to='rhythms', verbose_name=u'Foto',
        null=True, blank=True)

    created_on = models.DateTimeField(auto_now_add=True,
        verbose_name=u'Criado em')
    update_on = models.DateTimeField(auto_now=True,
        verbose_name=u'Atualizado em')

    features = models.BooleanField(verbose_name="Preferidos", default=True, blank=True)

    @models.permalink
    def get_absolute_url(self):
        return ('dancestep_by_rhythm', (), {'slug': self.slug})

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Ritmo'
        verbose_name_plural = u'Ritmos'
        ordering = ['name']

class Level(models.Model):
    name = models.CharField(verbose_name=u'Nome', max_length=150,
        help_text=u'O nome do nível')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Nível'
        verbose_name_plural = u'Níveis'
        ordering = ['name']



class DanceStep(models.Model):
    name = models.CharField(verbose_name=u'Nome', max_length=200,
        help_text=u'O nome do passo de dança')
    slug = models.SlugField(verbose_name=u'Apelido')
    rhythm = models.ForeignKey(Rhythm, verbose_name=u'Ritmo',
        related_name=u'dancesteps', null=True, blank=True)
    level = models.ForeignKey(Level, verbose_name=u'Nível',
        related_name=u'level', null=True, blank=True)
    description = models.TextField(verbose_name=u'Descrição',
        blank=True)
    dica = models.TextField(verbose_name=u'Dicas', blank=True)
    features = models.BooleanField(verbose_name="Preferidos", default=True, blank=True)


    @models.permalink
    def get_absolute_url(self):
        return ('dancestep_details',(), {'slug': self.slug})


    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Passo'
        verbose_name_plural = u'Passos'
        ordering = ['name']




    """docstring for Rhythm"models.Model d

    ef __init__(self, arg):
        super(Rhythm,models.Model._

            _init__()
        self.arg = arg"""