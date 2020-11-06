import json, fastjsonschema
from fastjsonschema import JsonSchemaException
#from exceptions import JsonSchemaException, JsonSchemaDefinitionException
# Do task_1

with open('data_schema.json') as json_file: 
    json_schema = json.load(json_file) # загружаем схему в объект (dictionary)
with open('input_text.txt') as input_text:
    #print(input_text)
    pass

#exception fastjsonschema.JsonSchemaException(message, value=None, name=None, definition=None, rule=None)
#print(fastjsonschema.validate({'type': 'string'}, '12345'))
#code = fastjsonschema.compile_to_code({'type': 'string'})
#print(code)

NoneType = type(None)
data = 12354
def validate(data):
    if not isinstance(data, (str)):
        raise JsonSchemaException("data must be string", value=data, name="data", definition={'type': 'string'}, rule='type')
    return data

#print(validate(data))

!pip install nba_api

