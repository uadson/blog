from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    """Representação de uma postagem e seus atributos:
        - autor
        - titulo
        - texto
        - data de criacao da postagem 
        - data da publicação da postagem
    """
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
        )
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)
    data_publicacao = models.DateTimeField(blank=True, null=True)

    def publicar(self):
        """ Método que definirá uma data de publicação quando esta ação for
        requesitada.
        """
        self.data_publicacao = timezone.now()
        self.save()

    def __str__(self):
        """Retorna uma string com o título da postagem
        """
        return f'{self.titulo}{self.autor}'
    