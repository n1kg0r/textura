from django.core.validators import FileExtensionValidator

from django.db import models
 

# declare a new model with a name 
class CorporaEntityData(models.Model):
 
    title = models.CharField(max_length = 200)
    time_period = models.CharField(max_length = 50)
    category = models.TextField()
    avg_sentence_length = models.FloatField(default=None, blank=True, null=True) 
    avg_word_length = models.FloatField(default=None, blank=True, null=True) 

    class Meta:
        app_label = 'textura_app'
    def __str__(self):
        return self.title


class CorpusEntityData(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, blank=False)
    path = models.CharField(max_length = 200)
    title = models.CharField(max_length = 200)

    time_period = models.CharField(max_length = 50)
    category = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)

    header = models.TextField() 
    created = models.CharField(max_length=200)
    genre_fi = models.CharField(max_length=200)
    texttype = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    chronotop = models.CharField(max_length=200)
    style = models.CharField(max_length=200)
    subcorpus = models.CharField(max_length=200)

    #block basic
    avg_sentence_length = models.FloatField(default=None, blank=True, null=True) 
    avg_sentence_length_stdev = models.FloatField(default=None, blank=True, null=True) 
    avg_sentence_length_median = models.FloatField(default=None, blank=True, null=True) 
    avg_sentence_length_iqr = models.FloatField(default=None, blank=True, null=True) 
    max_sentence_length = models.FloatField(default=None, blank=True, null=True) 
    
    avg_word_length = models.FloatField(default=None, blank=True, null=True) 
    avg_word_length_stdev = models.FloatField(default=None, blank=True, null=True) 
    avg_word_length_median = models.FloatField(default=None, blank=True, null=True) 
    avg_word_length_iqr = models.FloatField(default=None, blank=True, null=True) 
    max_word_length = models.FloatField(default=None, blank=True, null=True) 

    avg_syl_per_word = models.FloatField(default=None, blank=True, null=True) 


    # block vocab
    type_token_ratio = models.FloatField(default=None, blank=True, null=True) 
    lexical_density = models.FloatField(default=None, blank=True, null=True) 


    # block complexity
    hard_words_quantity = models.FloatField(default=None, blank=True, null=True) 
    fres = models.FloatField(default=None, blank=True, null=True) 
    gunning_fog = models.FloatField(default=None, blank=True, null=True) 
    ari = models.FloatField(default=None, blank=True, null=True) 
    smog = models.FloatField(default=None, blank=True, null=True) 
    cli = models.FloatField(default=None, blank=True, null=True) 


    # block sentiment
    blanchefort_positive = models.FloatField(default=None, blank=True, null=True) 
    blanchefort_neutral = models.FloatField(default=None, blank=True, null=True) 
    blanchefort_negative = models.FloatField(default=None, blank=True, null=True) 

    class Meta:
        app_label = 'textura_app'
    def __str__(self):
        return self.title



class UploadedText(models.Model):

    # block metadata
    file = models.FileField(upload_to='texts/', validators=[FileExtensionValidator(allowed_extensions=['txt'])])
    title = models.CharField(max_length=100, default=None, blank=True, null=True)
    author = models.CharField(max_length=100, default=None, blank=True, null=True)
    time_period = models.CharField(max_length = 50, default=None, blank=True, null=True)
    category = models.CharField(max_length=50, default=None, blank=True, null=True)
    

    #block basic
    avg_sentence_length = models.FloatField(default=None, blank=True, null=True) 
    avg_sentence_length_stdev = models.FloatField(default=None, blank=True, null=True) 
    avg_sentence_length_median = models.FloatField(default=None, blank=True, null=True) 
    avg_sentence_length_iqr = models.FloatField(default=None, blank=True, null=True) 
    max_sentence_length = models.FloatField(default=None, blank=True, null=True) 
    
    avg_word_length = models.FloatField(default=None, blank=True, null=True) 
    avg_word_length_stdev = models.FloatField(default=None, blank=True, null=True) 
    avg_word_length_median = models.FloatField(default=None, blank=True, null=True) 
    avg_word_length_iqr = models.FloatField(default=None, blank=True, null=True) 
    max_word_length = models.FloatField(default=None, blank=True, null=True) 

    avg_syl_per_word = models.FloatField(default=None, blank=True, null=True) 


    # block vocab
    type_token_ratio = models.FloatField(default=None, blank=True, null=True) 
    lexical_density = models.FloatField(default=None, blank=True, null=True) 


    # block complexity
    hard_words_quantity = models.FloatField(default=None, blank=True, null=True) 
    fres = models.FloatField(default=None, blank=True, null=True) 
    gunning_fog = models.FloatField(default=None, blank=True, null=True) 
    ari = models.FloatField(default=None, blank=True, null=True) 
    smog = models.FloatField(default=None, blank=True, null=True) 
    cli = models.FloatField(default=None, blank=True, null=True) 


    # block sentiment
    blanchefort_positive = models.FloatField(default=None, blank=True, null=True) 
    blanchefort_neutral = models.FloatField(default=None, blank=True, null=True) 
    blanchefort_negative = models.FloatField(default=None, blank=True, null=True) 




    def delete(self, *args, **kwargs):
        self.file.delete()
        super(UploadedText, self).delete(*args, **kwargs)

    def __str__(self):
        return self.title



class FiltersModel(models.Model):
 
    time_period = models.CharField(max_length = 50, default=None, blank=True, null=True)
    category = models.CharField(max_length = 50, default=None, blank=True, null=True)
    author = models.CharField(max_length = 100, default=None, blank=True, null=True)

    
    created = models.CharField(max_length=200, default=None, blank=True, null=True)
    genre_fi = models.CharField(max_length=200, default=None, blank=True, null=True)
    texttype = models.CharField(max_length=200, default=None, blank=True, null=True)
    topic = models.CharField(max_length=200, default=None, blank=True, null=True)
    chronotop = models.CharField(max_length=200, default=None, blank=True, null=True)
    style = models.CharField(max_length=200, default=None, blank=True, null=True)
    subcorpus = models.CharField(max_length=200, default=None, blank=True, null=True)

    class Meta:
        app_label = 'textura_app'
    def __str__(self):
        return self.title