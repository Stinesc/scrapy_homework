from celery import task
from celery.utils.log import get_task_logger
from .models import Garment, Size

logger = get_task_logger(__name__)


@task(name='add_items')
def add_items(items_list):
    items_count = len(items_list)
    for item in items_list:
        if not(list() in item.values()) and not(None in item.values()):
            garment = Garment.objects.create(title=item['title'][0], image_url=item['image'][0],
                              price=item['price'][0], color=item['color'][0], description=item['description'])
            sizes_list = list()
            for size in item['sizes']:
                sizes_list.append(Size(size_content=size.split(" ", 1)[0], garment_id=garment.pk))
            if sizes_list:
                Size.objects.bulk_create(sizes_list)
        else:
            items_count = items_count - 1
    logger.info(f'{items_count} garment objects are added.')
