from celery import shared_task

from vehicle.models import Car, Moto

@shared_task
def check_milage(pk, model):
    if model == 'Car':
        instance = Car.objects.filter(pk=pk).first()
    else:
        instance = Moto.objects.filter(pk=pk).first()
    if instance:
        prev_milage = -1
        for m in instance.milage.all():
            if prev_milage == -1:
                prev_milage = m.milage

            else:
                if prev_milage < m.milage:
                    print(f'Неверный пробег. Предыдущий пробег = {prev_milage}. Текущий пробег {m.milage}')
                    break

@shared_task
def check_filter():
    filter_price = {'price__lt': 500}

    if Car.objects.filter(**filter_price).exists():
        print(Moto.objects.filter(price__lt=500))
        print('Отчет по фильтру')
        # send_mail(
        #     subject='Отчет по фильтру',
        #     message='У нас есть машины под Ваш фильтр, заходите на сайт',
        #     from_email='admin@admin.com',
        #     recipient_list=[user.email],
        # )