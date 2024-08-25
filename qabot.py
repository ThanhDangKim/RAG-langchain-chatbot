from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain_community.llms.ctransformers import CTransformers
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain_community.vectorstores import FAISS
import vectorquery as vt

# Load model 
model_name = "model/vinallama-7b-chat_q5_0.gguf"

def load_model():
    llm = CTransformers(
        model = model_name,
        model_type = 'llama',
        max_new_token = 1024,
        temperature = 0.2
    )
    return llm

def create_prompt_template(template):
    prompt = PromptTemplate(template = template, input_variables = ['context', 'question'])
    return prompt

def create_qa(llm, prompt):
    llm_chain = RetrievalQA.from_chain_type(
        llm = llm,
        chain_type = 'stuff',
        retriever = vt.VectorDB().get_retriever(),
        return_source_documents = False,
        chain_type_kwargs = {'prompt': prompt}
    )
    return llm_chain

llm = load_model()

template = """<|im_start|>system\nSử dụng thông tin sau đây để trả lời câu hỏi. Nếu bạn không biết câu trả lời, hãy nói không biết, đừng cố tạo ra câu trả lời\n
    {context}<|im_end|>\n<|im_start|>user\n{question}<|im_end|>\n<|im_start|>assistant"""
prompt = create_prompt_template(template)

qa_chain = create_qa(llm, prompt)

#test
question = 'Sinh viên tốt nghiệp ngành công nghệ kỹ thuật Điện-Điện Tử (Điện công nghiệp) có thể làm những công việc gì?'
output = qa_chain.invoke({'query': question})
print(output)

