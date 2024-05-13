# Just runs .complete to make sure the LLM is listening
from llama_index.llms.ollama import Ollama

from llama_index.core import SimpleDirectoryReader
from cleantext import clean
from llama_index.core import Document
from llama_index.core.program import LLMTextCompletionProgram
from documentSchema import Candidate
from llama_index.core.output_parsers import PydanticOutputParser

def clean_document_text(document : Document):
    ''' Clean the text attribute of a Document object and return a new Document object.'''
    cleaned_text = clean(document.text, \
        lower=False, fix_unicode=True, no_line_breaks=True,no_urls=False, no_emails=False, no_phone_numbers=False, no_numbers=False, no_digits=False, no_currency_symbols=False, no_punct=False, no_emoji=True)
    # Assuming Document has an attribute 'text' and other attributes remain the same
    document.text = cleaned_text
    return document

def read_cvs(root_folder):
    ''' Load the CVs from the root folder. Loads docx, pdf, txt files. '''

    cvs_folder = root_folder + "/cvs"
    cvs = SimpleDirectoryReader(cvs_folder).load_data()
    cvs_cleaned = list(map(clean_document_text, cvs))    
    return cvs_cleaned

llm = Ollama(model="llama3:instruct", temperature=.2, request_timeout=90, context_window=10000)

prompt_template_str = """
You will be given below CV, your job is to Extract the information from CV in the given JSON format.
CV - {cv}
"""
program = LLMTextCompletionProgram.from_defaults(
    output_cls=Candidate,
    prompt_template_str=prompt_template_str,
    verbose=True,
    llm=llm
)
cv = read_cvs("chatbot")
data = cv[0].text
output = program(cv=data)
print(output.json())