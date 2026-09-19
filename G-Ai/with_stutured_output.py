from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typedict import TYpeDict,Annotated

load_dotenv()
model=ChatOpenAI()
class Review(TypeDict):
    summary:Annotated[str,"A brief summary of the review"]
    sentiment:Annotated[int,"Return sentiment as an integer: 1 for positive, 0 for neutral, -1 for negative"]
    pros:Annotated[list[str],"List of pros mentioned in the review"]
    cons:Annotated[list[str],"List of cons mentioned in the review"]
    
sturctured_output=with_stutured_output(Review)  
result=model_invoke("What do you think about the movie Inception?", output_format=sturctured_output)
print(result.summary)
print(result.sentiment)

