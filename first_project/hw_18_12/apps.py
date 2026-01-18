from django.apps import AppConfig

class Hw1812Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hw_18_12'

    def ready(self):
        # Импортируем модели и группы внутри ready, чтобы избежать проблем с импортами
        from django.contrib.auth.models import Group, Permission
        from django.contrib.contenttypes.models import ContentType
        from .models import Book

        # Создаем группу "Читачі", если она не существует
        group_name = "Читачі"
        group, created = Group.objects.get_or_create(name=group_name)

        # Получаем разрешения только на просмотр книг
        content_type = ContentType.objects.get_for_model(Book)
        view_perm = Permission.objects.filter(content_type=content_type, codename='view_book')

        # Добавляем разрешение группе
        for perm in view_perm:
            group.permissions.add(perm)
