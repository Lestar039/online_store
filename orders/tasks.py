from celery import task
from django.core.mail import send_mail
from .models import Order
from online_store.celery import app


@app.task
def order_created(order_id):
    """
    Отправка email-уведомлений при успешном оформлении заказа
    """
    order = Order.objects.get(id=order_id)
    subject = 'Заказ №. {}'.format(order.id)
    message = 'Здравствуйте, {}!\n\nВы совершили покупку в нашем интернет магазине.' \
              'Ваш номер заказа - {}.'.format(order.first_name, order.id)
    mail_sent = send_mail(subject, message, 'your_email', [order.email])

    return mail_sent
