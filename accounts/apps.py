from django.apps import AppConfig


from sentence_transformers import SentenceTransformer


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

model_st = SentenceTransformer('distiluse-base-multilingual-cased')


"""
def signal_vector(sender, instance, *args, **kwargs):
    print(sender.user_id)
    # my code

post_save.connect(signal_vector)
"""