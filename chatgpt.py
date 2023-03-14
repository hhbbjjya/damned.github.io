import openai
openai.api_key = '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'
def qus(x):
    #x = str(input("請問有甚麼問題?"))
    response = openai.Completion.create(
    engine = "text-davinci-003",    # select model
    prompt = x,     
    max_tokens = 512,               # response tokens
    temperature = 1,                # diversity related
    top_p = 0.75,                   # diversity related
    n = 1,                          # num of response
)

    completed_text = response["choices"][0]["text"]
    return(completed_text)
    print(completed_text)