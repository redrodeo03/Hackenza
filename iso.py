from pyiso4.ltwa import Abbreviate

# Create an abbreviator (using the default LTWA)
abbreviator = Abbreviate.create()

# Abbreviate a journal title
abbreviation = abbreviator('International Journal of Child-Computer Interaction', remove_part=True)
print(abbreviation)
