import os
import django
from faker import Faker
import random
from django.utils import timezone

# Configure Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hangarin_project.settings')
django.setup()

from core.models import Task, SubTask, Category, Priority, Note

fake = Faker()

def create_data():
    # 1. Create Categories and Priorities automatically
    categories = ['Work', 'School', 'Personal', 'Finance', 'Projects']
    priorities = ['High', 'Medium', 'Low']
    
    cat_objs = [Category.objects.get_or_create(name=c)[0] for c in categories]
    prio_objs = [Priority.objects.get_or_create(name=p)[0] for p in priorities]
    
    print("Categories and Priorities created automatically.")

    # 2. Create Tasks linked to those categories and priorities
    for _ in range(10):
        task = Task.objects.create(
            title=fake.sentence(nb_words=4),
            description=fake.paragraph(),
            deadline=fake.future_datetime(end_date='+30d', tzinfo=timezone.get_current_timezone()),
            status=random.choice(['Pending', 'In Progress', 'Completed']),
            category=random.choice(cat_objs),
            priority=random.choice(prio_objs)
        )
        
        # 3. Create SubTasks
        for _ in range(random.randint(1, 3)):
            SubTask.objects.create(
                parent_task=task,
                title=fake.sentence(nb_words=3),
                status=random.choice(['Pending', 'In Progress', 'Completed'])
            )
            
        # 4. Create Notes
        for _ in range(random.randint(0, 2)):
            Note.objects.create(
                task=task,
                content=fake.text()
            )

    print("Tasks, SubTasks, and Notes created successfully.")

if __name__ == '__main__':
    create_data()