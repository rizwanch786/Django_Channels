import threading
from .models import *
from faker import Faker
fake = Faker()
import time
import random
from channels.layers import  get_channel_layer
from asgiref.sync import async_to_sync

class CreateStudentThread(threading.Thread):
    
    def __init__(self , total):
        self.total = total
        threading.Thread.__init__(self)
    
    def run(self):
        try:
            print('Thread Execution Start')
            channel_layer = get_channel_layer()
            for current_total, _ in enumerate(range(self.total), start=1):
                student_obj = Student.objects.create(
                    student_name = fake.name(),
                    student_email = fake.email(),
                    address = fake.address(),
                    age = random.randint(10, 50)
                )
                channel_layer = get_channel_layer()
                data = {'current_total':current_total, 'total':self.total, 'student_name': student_obj.student_name, 'student_email': student_obj.student_email, 'address': student_obj.address, 'age':str(student_obj.age)}
                print(data)
                async_to_sync(channel_layer.group_send)(
                    'new_consumer_group', {
                        'type' : 'send_notification',
                        'value' : json.dumps(data)
                    })
                time.sleep(1)
        except Exception as e:
            print(e)