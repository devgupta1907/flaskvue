import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
from .models import Category


def num_of_services_in_each_category():
    result = {}
    categories = Category.query.all()
    for category in categories:
        result[category.name] = len(category.services)
    return result


def chart_for_category_services():
    result = num_of_services_in_each_category()
    category_names = result.keys()
    service_counts = result.values()
    
    plt.figure(figsize=(8, 5))
    plt.bar(category_names, service_counts, color='skyblue')
    plt.xlabel('Category')
    plt.ylabel("Count of Services")
    plt.title('Number of Services in Each Category')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    backend_dir = os.path.dirname(os.path.abspath(__file__))  # utility.py location
    project_root = os.path.dirname(os.path.dirname(backend_dir))  # Move up to flaskvue/
    image_path = os.path.join(project_root, 'frontend', 'src', 'assets', 'graphs', 'services_in_category.png')

    plt.savefig(image_path)
    return 'services_in_category.png'

    