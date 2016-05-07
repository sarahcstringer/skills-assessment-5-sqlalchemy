"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

# from model import *

from model import *
from sqlalchemy import or_

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.

# print Brand.query.get(8) #returns a Brand object

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.

# print Model.query.filter_by(brand_name='Chevrolet', name='Corvette').all()

# Get all models that are older than 1960.

# print Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.

# print Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".

# print Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.

# print Brand.query.filter(Brand.founded == 1903, Brand.discontinued.is_(None)).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded 
# before 1950.

# print Brand.query.filter(or_(Brand.discontinued.isnot(None), Brand.founded < 1950)).all()

# Get any model whose brand_name is not Chevrolet.

# print Model.query.filter(Model.brand_name != 'Chevrolet').all()


# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    model_info = Model.query.filter(Model.year == year).all()

    for model in model_info:
        #handles null values for brand (ex: Fillmore model)
        if model.brand == None:
            print "Model: {}; Brand Name: None; Headquarters: None".format(
                                                        model.name)
        else:
            print "Model: {}; Brand Name: {}; Headquarters: {}".format(
                                        model.name, model.brand_name, 
                                        model.brand.headquarters)
    return

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''
    
    brands_summary = Brand.query.all()

    for brand in brands_summary:
        print "Brand: {}".format(brand.name)
        for model in brand.models:
            print "\tModel: {}; Year: {}".format(model.name, model.year)    

# get_model_info(1960)
# get_brands_summary()
# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# A query object, which could then have .first(), .add(), or .all() added to complete
# the query and get an object matching those criteria.

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?



# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    
    return Brand.query.filter(Brand.name.like('%'+mystr+'%')).all()


def get_models_between(start_year, end_year):
    
    return Model.query.filter(Model.year >= start_year, Model.year < end_year).all()
