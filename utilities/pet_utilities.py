#lib
import random
import json
from faker import Faker
from faker.providers import DynamicProvider

#global
fake = Faker() 

class PetUtilities:
    '''
    A class used to represent a pet and provide some functions to modify the pet

    Atributes
    ---------

    id : integer
        a unique value for the pet
    pet_as_json : str
        a string that contains all the pet information in format json
    pet_as_dic : dict
        a dict that containes all the pet information
    
    '''
    
    def __init__(self) -> None:
        self.id = random.randint(0,9223372036854053000) 
        self.__create_provides_faker()
        self.make_randon_pet()
     
    def make_pet_to_json(self) -> None: 
        self.pet_as_json = json.dumps(self.pet_as_dic,indent = 1)

    def make_randon_pet(self) -> None:
        '''
        Fill pet_as_json and pet_as_dic with randon valid information

        '''
        self.pet_as_dic = {
            "id": self.id,
            "category": {
                "id": random.randint(0,9223372036854053000),
                "name": fake.pet_category()
            },
            "name": "doggie",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": random.randint(0,9223372036854053000),
                    "name": "string"
                }
            ], 
            "status": fake.pet_status()
        }

        self.make_pet_to_json()
        
    def clean_pet(self) -> None:
        self.pet_as_dic = {}

    @staticmethod
    def __create_provides_faker() -> None:
        pet_category_provider = DynamicProvider(
            provider_name = "pet_category",
            elements = ["Fish", "Dog", "Cat", "Reptile", "Bird"]
        )
        pet_status_provider = DynamicProvider(
            provider_name = "pet_status",
            elements = ["availeble", "pending", "sold"]
        )

        fake.add_provider(pet_category_provider)
        fake.add_provider(pet_status_provider)    