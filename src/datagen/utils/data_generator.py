from faker import Faker
import random

def generate_user_interaction(faker: Faker, config) -> dict:
    """
    Generate a single user interaction record.
    
    :param faker: An instance of Faker for generating fake data.
    :param config: Configuration object with details like product list, actions, etc.
    :return: A dictionary representing a user interaction.
    """

    # Example product categories and user actions - these can be customized or loaded from config
    product_categories = ['Electronics', 'Books', 'Clothing', 'Home & Garden']
    actions = ['view', 'add_to_cart', 'purchase']

    interaction = {
        'user_id': faker.uuid4(),
        'product_category': random.choice(product_categories),
        'product_id': faker.uuid4(),
        'action': random.choice(actions),
        'interaction_time': faker.iso8601(),
        'price': round(random.uniform(10.0, 500.0), 2) if random.choice(actions) == 'purchase' else None,
        'quantity': random.randint(1, 5) if random.choice(actions) == 'purchase' else None
    }

    return interaction
