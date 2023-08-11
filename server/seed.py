#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
# from faker import Faker

# Local imports
from app import app
from models import Potion, Ingredient, PotionIngredients, db
# from models import db
# from config import db


if __name__ == '__main__':
    # fake = Faker()
    
    ingredients = [
        {
            'id': 1,
            'name': 'ruby dust',
            'description': 'Associated with passion and the element of fire',
            'thumbnail': 'https://imgur.com/l69eEFF.png'
        },
        {
            'id': 2,
            'name': 'sunstone dust',
            'description': 'Associated with the sun and the element of fire',
            'thumbnail': 'https://imgur.com/86KJp1m.png'
        },
        {
            'id': 3,
            'name': 'emerald dust',
            'description': 'Associated with fortune, good or bad, and the element of earth ',
            'thumbnail': 'https://imgur.com/yVkwDBb.png'
        },
        {
            'id': 4,
            'name': 'moonstone dust',
            'description': 'Associated with the moon and the element of water',
            'thumbnail': 'https://imgur.com/961BVmX.png'
        },
        {
            'id': 5,
            'name': 'amethyst dust',
            'description': 'Associated with peace, healing, and the element of air',
            'thumbnail': 'https://imgur.com/gXDixgE.png'
        },
        {
            'id': 6,
            'name': 'lavender sprig',
            'description': 'posesses a calming effect',
            'thumbnail': 'https://imgur.com/kPF0lCR.png'
        },
        {
            'id': 7,
            'name': 'skullcap',
            'description': 'extremely poisonous if ingested',
            'thumbnail': 'https://imgur.com/225vWsc.png'
        },
        {
            'id': 8,
            'name': 'sunflower petal',
            'description': 'associated with joy',
            'thumbnail': 'https://imgur.com/baoCZQt.png'
        },
        {
            'id': 9,
            'name': 'four leaf clover',
            'description': 'associated with good luck',
            'thumbnail': 'https://imgur.com/PC9vlf7.png'
        },
        {
            'id': 10,
            'name': 'valerian root',
            'description': 'well known for its potent healing properties',
            'thumbnail': 'https://imgur.com/xPPAG0b.png'
        },
        {
            'id': 11,
            'name': 'toadstool cap',
            'description': 'associated with transformation',
            'thumbnail': 'https://imgur.com/X0hqWg0.png'
        },
        {
            'id': 12,
            'name': 'dandelion root',
            'description': 'a hardy plant with healing and transformative properties',
            'thumbnail': 'https://imgur.com/PtcyXFw.png'
        },
        {
            'id': 13,
            'name': 'wolfsbane',
            'description': 'strongly associated with the lunar cycles',
            'thumbnail': 'https://imgur.com/RtjJtvv.png'
        },
        {
            'id': 14,
            'name': 'daffodil petal',
            'description': 'the sunshine flower',
            'thumbnail': 'https://imgur.com/reyS00F.png'
        },
        {
            'id': 15,
            'name': 'rose petal',
            'description': 'associated with beauty',
            'thumbnail': 'https://imgur.com/BXPvppa.png'
        },
        {
            'id': 16,
            'name': 'dove feather',
            'description': 'symbolic of pure love',
            'thumbnail': 'https://imgur.com/5ttxS7x.png'
        },
        {
            'id': 17,
            'name': 'essence of ashwinder venom',
            'description': 'a highly toxic substance when concentrated',
            'thumbnail': 'https://imgur.com/l69eEFF.png'
        },
        {
            'id': 18,
            'name': 'phoenix feather',
            'description': 'symbolic of fire, rebirth, and healing',
            'thumbnail': 'https://imgur.com/zHW40t3.png'
        },
        {
            'id': 19,
            'name': 'essence of  luminous salamander',
            'description': 'contains protective properties against the sun',
            'thumbnail': 'https://imgur.com/5iv71Rd.png'
        },
        {
            'id': 20,
            'name': 'tortoise shell scales',
            'description': 'tortoise shell scales contain protective properties and are associated with good fortune',
            'thumbnail': 'https://imgur.com/yrfufPA.png'
        },
        {
            'id': 21,
            'name': 'giant squid ink',
            'description': 'due to its ginormous size, the giant squid developed a highly effective ink that has advanced camoflouging capabilities',
            'thumbnail': 'https://imgur.com/F9b0dXK.png'
        },
        {
            'id': 22,
            'name': 'bowtruckle chrysalis',
            'description': 'the bowtruckle chrysalis is a rare find as the creatures are very shy and tend to hide in tall trees. They will also attack viciously if threatened.',
            'thumbnail': 'https://imgur.com/r09jQeT.png'
        },
        {
            'id': 23,
            'name': 'unicorn hair',
            'description': 'symbolic of pure magic, the hair of unicorn can only be collected if offered willingly from the unicorn.',
            'thumbnail': 'https://imgur.com/bSgEUey.png'
        },
        {
            'id': 24,
            'name': 'raven feather',
            'description': 'often associated with death and malice',
            'thumbnail': 'https://imgur.com/QYahZxZ.png'
        },
        {
            'id': 25,
            'name': 'tawny owl feather',
            'description': 'the tawny owl is associated with wisdom and honesty',
            'thumbnail': 'https://imgur.com/WVqFubV.png'
        }
                
    ]

    # Seed potions

    potions = [
        {   'id': 1, 
            'name': 'Amortentia', 
            'correct_ingredients': "1, 6, 16", 
            'description': 'A very potent love potion; can be toxic in high doses',
            'thumbnail': 'https://imgur.com/69a5oJf.png'
        },
        {   'id': 2, 
            'name': 'Potent Furor Poison',
            'correct_ingredients': "1, 7, 17",
            'description': 'A potent poison that induces powerful and potentially dangerous feelings of anger and rage when ingested',
            'thumbnail': 'https://imgur.com/jjoUA4E.png'
        },
        {
            'id': 3, 
            'name': 'Antidote to Common Poisons',
            'correct_ingredients': "3, 7, 23",
            'description': 'Antitode to most common poisons',
            'thumbnail': 'https://imgur.com/GDbe6Kt.png'
        },
        {
            'id': 4,
            'name': 'Elixir of Beauty',
            'correct_ingredients': "4, 15, 23",
            'description': 'Enhances the attractiveness of the drinkers physical appearance',
            'thumbnail': 'https://imgur.com/fnvjLj8.png'
        },
        {
            'id': 5,
            'name': 'Calming Draught',
            'correct_ingredients': "5, 6, 16",
            'description': 'Calms the drinker',
            'thumbnail': 'https://imgur.com/YtWK42H.png'
        },
        {
            'id': 6,
            'name': 'Draught of the Living Dead',
            'correct_ingredients': "3, 10, 24",
            'description': 'Induces a deep, restful sleep',
            'thumbnail': 'https://imgur.com/GDbe6Kt.png'
        },
        {
            'id': 7,
            'name': 'Soliservo Elixer',
            'correct_ingredients': "2, 8, 19",
            'description': 'When ingested, allows the user to withstand direct sunlight(intended for Vampire use only)',
            'thumbnail': 'https://imgur.com/d6rnFwr.png'
        },
        {
            'id': 8,
            'name': 'Ignus Noxa',
            'correct_ingredients': "1, 10, 24",
            'description': 'A simple, yet highly effective damage potion. Inflicts a singing effect on the intended target, causing extreme discomfort',
            'thumbnail': 'https://imgur.com/4yGeRfi.png'
        },
        {
            'id': 9,
            'name': 'Felix Felicis',
            'correct_ingredients': "2, 9, 20",
            'description': 'More commonly known as "Liquid Luck"; makes the drinker lucky for a limited period of time, during which everything they attempt will be successful',
            'thumbnail': 'https://imgur.com/ha4BJzk.png'
        },
        {
            'id': 10,
            'name': 'Dissolution Drought',
            'correct_ingredients': "2, 7, 24",
            'description': 'A malicious drought intended for use on a pair; induces strong feelings of disdain between the two targets',
            'thumbnail': 'https://imgur.com/jjoUA4E.png'
        },
        {
            'id': 11,
            'name': 'Wiggenweld Potion',
            'correct_ingredients': "5, 10, 18",
            'description': 'A very simple, yet potent healing potion that cures a wide variety of ailments and afflictions',
            'thumbnail': 'https://imgur.com/LUUmlOb.png'
        },
        {
            'id': 12,
            'name': 'Invisibility Potion',
            'correct_ingredients': "5, 11, 21",
            'description': 'A potion that makes the drinker invisible for a brief amount of time',
            'thumbnail': 'https://imgur.com/R4mqM7f.png'
        },
        {
            'id': 13,
            'name': 'Polyjuice Potion',
            'correct_ingredients': "4, 12, 22",
            'description': 'A complex and time-consuming concotion, which is best left to highly skilled witches and wizards. Allows the user to assume the physical appearance of another person',
            'thumbnail': 'https://imgur.com/CPo71n0.png'
        },
        {
            'id': 14,
            'name': 'Veritaserum',
            'correct_ingredients': "2, 14, 25",
            'description': 'A very powerful truth serum that forces the drinker to speak the truth',
            'thumbnail': 'https://imgur.com/stFTIGN.png'
        },
        {
            'id': 15,
            'name': 'Wolfsbane Potion',
            'correct_ingredients': "4, 13, 2",
            'description': 'A remedy for the most debilitating symptoms of lycanthropy; allows the drinker to keep their minds during the full moon',
            'thumbnail': 'https://imgur.com/fnvjLj8.png'
        },
    ]

    houses = [
        {
            'id': 1,
            'name': 'Gryffindor',
            'score': '',
        },
        {
            'id': 2,
            'name': 'Hufflepuff',
            'score': '',
        },
        {
            'id': 3,
            'name': 'Ravenclaw',
            'score': '',
        },
        {
            'id': 4,
            'name': 'Slytherin',
            'score': ''
        }
    ]

    users = [
        {
            'id': 1, 
            'username': 'jinxmoon',
            'house': 'Slytherin',
            'score': '150',
            'password': 'luna'
        },
          {
            'id': 2, 
            'username': 'nifflercutie',
            'house': 'Hufflepuff',
            'score': '130',
            'password': 'blanche'
        },
            {
            'id': 3, 
            'username': 'pottergirl13',
            'house': 'Gryffindor',
            'score': '80',
            'password': 'hedwig'
        },
          {
            'id': 4, 
            'username': 'starfire',
            'house': 'Ravenclaw',
            'score': '140',
            'password': 'luna2'
        },
          {
            'id': 5, 
            'username': 'halfbloodprincess',
            'house': 'Slytherin',
            'score': '100',
            'password': 'lordvoldie'
        },
          {
            'id': 6, 
            'username': 'drarrystan1',
            'house': 'Gryffindor',
            'score': '90',
            'password': 'ilovedraco'
        },
          {
            'id': 7, 
            'username': 'greengoddess',
            'house': 'Hufflepuff',
            'score': '40',
            'password': 'ihatepotions'
        },
          {
            'id': 8, 
            'username': 'runepixie',
            'house': 'Ravenclaw',
            'score': '100',
            'password': 'dumbledoresarmy'
        }
    ]


    with app.app_context():
        print('Starting seed...')
        Ingredient.query.delete()
        Potion.query.delete()
        PotionIngredients.query.delete()
        

        # Add ingredients to the database
        for ingredient_data in ingredients:
            ingredient = Ingredient(name=ingredient_data['name'], description=ingredient_data['description'], thumbnail=ingredient_data['thumbnail'])
            db.session.add(ingredient)

        # Add potions to the database
        for potion_data in potions:
            potion = Potion(name=potion_data['name'], correct_ingredients=potion_data['correct_ingredients'], thumbnail=potion_data['thumbnail'] )
            db.session.add(potion)

            # Associate ingredients with potions
            # for ingredient_id in potion_data['correct_ingredients'].split(','):
            #     ingredient = Ingredient.query.get(int(ingredient_id))
            #     if ingredient:
            #         potion.ingredients.append(ingredient)

        # Commit the changes to the database
        db.session.commit()

        print('Seed complete!')
            