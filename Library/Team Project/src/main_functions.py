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
#Medium functions (5)


#Complex functions (5)