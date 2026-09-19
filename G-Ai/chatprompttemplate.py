from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessagePromptTemplate, HumanMessagePromptTemplate,AIMessagePromptTemplate

chat_template=ChatPromptTemplate([
     ('system','You are a helpful{domain} assistant'),
        ('human','Explainin simple terms{input}'),
])

prompt=chat_template.invoke({'domain':' programming','input':' what is a variable?'})
print(prompt)