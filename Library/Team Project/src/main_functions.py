#Simple functions (5)

def normalize_crime_category(category: str) -> str:
    '''
    Normalize crime category names to a standardized format

    Args:
        category: Raw crime category string
    
    Returns:
        str: normalized category name in title case
    
    Raises:
        ValueError: If category is empty or None
    '''
    if not category:
        raise ValueError("Crime category cannot be empty or none")
    
    return category.strip().title()

def is_violent_crime(crime_type: str) -> bool:
    '''
    Checks if a crime type is classified as violent

    Args:
        crime_type: the type of crime to be checked
    
    Returns:
        bool: True = violent crime, False = not violent
    
    Raises:
        TypeError: if crime_type is not a string
    '''

    if not isinstance(crime_type, str):
        raise TypeError(f"Crime type must be a string, got {type(crime_type)}")
    
    violent_crimes = {'assault', 'robbery', 'homicide', 'murder', 'rape', 'kidnapping'}
    
    return crime_type.lower() in violent_crimes

def calculate_crime_rate(incidents: int, population: int) -> float:
    '''
    Calculate the rate of crime per 100,000 people

    Args:
        incidents: number of crime incidents
        population: total population
    
    Returns:
        float: crime rate per 100,000 people
    
    Raises:
        ValueError: if population is 0 or negative, if incidents is negative
    
    '''
    if population <= 0:
        raise ValueError("Population must be greater than 0")
    if incidents < 0:
        raise ValueError("incidents must not be negative")
    
    return (incidents / population) * 100000
#Medium functions (5)


#Complex functions (5)

