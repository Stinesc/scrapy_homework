from celery import task
from celery.utils.log import get_task_logger
from .models import Garment, Size

logger = get_task_logger(__name__)


@task(bind=True)
def add_items(items_list):
    objects_list = list()
    for item in items_list:
        sizes_list = list()
        for size in item['sizes']:
            sizes_list.append(Size(size_content=size))
        garment = Garment(title=item['title'], image_url=item['image'],
                          price=item['price'], color=item['color'], description=item['description'])
        garment.related_set.set(sizes_list)
        objects_list.append(garment)
    Garment.objects.bulk_create(objects_list)
    logger.info(f'{len(objects_list)} garment objects are added.')
