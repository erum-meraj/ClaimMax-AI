from flask import Flask, request, jsonify
import flask_cors
import os
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv


load_dotenv()

os.environ["GOOGLE_API_KEY"] = "AIzaSyD5z7xZDxC4rIw1PPbTVlHMP1ps_XecQQ8"
app = Flask(__name__)
flask_cors.CORS(app)

def get_pdf_text(file_path):
    text = ""
    pdf_reader = PdfReader(file_path)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

def get_conversational_chain():
    prompt_template = """
    You are a helpful Tax Assistant who tells the user what all extra investments that the user can make to be eligible for tax deductions they are not currently eligible for based on multiple contexts given to you.
   the user data would be given in the form of a json object. Suggest the relavent sections that they can apply under after making the new investments and steps.
    Reply "I'll advice to connect to our support team" if relavent information is not there in the given file. 
    Context:\n{context}\n
    User Data: \n{question}\n
    Answer:
    """

    model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.3)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain

def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = vector_store.similarity_search(user_question)

    chain = get_conversational_chain()
    response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)

    return response


raw_text = get_pdf_text("DeductionsunderChapterVIA.pdf")
text_chunks = get_text_chunks(raw_text)
get_vector_store(text_chunks)



model = genai.GenerativeModel('gemini-2.0-flash')


def suggest_investments(user_data):
    
    user_question = user_data
    print(user_question)
    response = user_input(user_question)
    # print()
    message = {"answer": response["output_text"]}
    return message["answer"]



if __name__ == "__main__":
    user_data = '''{'age': 'below60', 'disability': 'yes', 'donations': 'yes', 'health_insurance': ['parents'], 'income': 894848484.0, 'interest': ['savings', 'fd'], 'investments': 'no', 'loan': ['home', 'ev'], 'name': 'Erum', 'occupation': 'salaried'}'''
    print(suggest_investments(user_data))


