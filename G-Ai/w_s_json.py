from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typedict import TypeDict,Annotated,Optionai,Literal
from pydantic import BaseModel,Field,EmailStr

load_dotenv()
model=ChatOpenAI()
#schema
{
    "title":"Student",
    "description":"schema_student",
    "type":"object",
    "properties":{
        "name":{
            "type":"string",
            "description":"Name of the student"
        }
    }
}
sturctured_output=Review
result=model.invoke("What do you think about the movie Inception?", output_format=sturctured_output)
print(result.summary)
print(result.sentiment)
