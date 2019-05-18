import modulesConverters
from modulesConverters import lbs_to_kg

#  imported modules are objects so we refer to the function with the module.function_name()
print(modulesConverters.kg_to_lbs(12))
#  when importing separate functions from classes (shown with Ctr+Space) you can address the function directly
print(lbs_to_kg(35))