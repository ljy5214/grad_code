import openai
from openai import OpenAI
import time
import requests

openai.api_key = 'sk-7582699e42240f2433dc64665f380962'
openai.api_base = "https://api.atomecho.cn/v1" # 你的服务ip

def get_oai_completion(prompt):

    try: 
        client = OpenAI(
    api_key='sk-7582699e42240f2433dc64665f380962',
    base_url="https://api.atomecho.cn/v1",
)
        response = client.chat.completions.create(
        model="Atom-7B-Chat",
        messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            
            ],
        temperature=1,
        max_tokens=2048,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
)
        res = response.choices[0].message.content
       
        gpt_output = res
        return gpt_output
    except requests.exceptions.Timeout:
        # Handle the timeout error here
        print("The OpenAI API request timed out. Please try again later.")
        return None
    except openai.error.InvalidRequestError as e:
        # Handle the invalid request error here
        print(f"The OpenAI API request was invalid: {e}")
        return None
    except openai.error.APIError as e:
        if "The operation was timeout" in str(e):
            # Handle the timeout error here
            print("The OpenAI API request timed out. Please try again later.")
#             time.sleep(3)
            return get_oai_completion(prompt)            
        else:
            # Handle other API errors here
            print(f"The OpenAI API returned an error: {e}")
            return None
    except openai.error.RateLimitError as e:
        return get_oai_completion(prompt)

def call_chatgpt(ins):
    success = False
    re_try_count = 15
    ans = ''
    while not success and re_try_count >= 0:
        re_try_count -= 1
        try:
            ans = get_oai_completion(ins)
            success = True
        except:
            time.sleep(5)
            print('retry for sample:', ins)
    return ans

# 测试调用
# if __name__ == '__main__':
#     prompt = "What are the benefits of AI in healthcare?"
#     result = call_chatgpt(prompt)
#     print(result)

# from openai import OpenAI
# # client = OpenAI(
# #     api_key='sk-7582699e42240f2433dc64665f380962',
# #     base_url="https://api.atomecho.cn/v1",
# # )

prompt = "What are the benefits of AI in healthcare?"
client = OpenAI(
api_key='sk-7582699e42240f2433dc64665f380962',
base_url="https://api.atomecho.cn/v1",
)
response = client.chat.completions.create(
model="Atom-7B-Chat",
messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    
    ],
temperature=1,
max_tokens=2048,
top_p=0.95,
frequency_penalty=0,
presence_penalty=0,
stop=None
)
res = response.choices[0].message.content
print(res)
# # print(completion.choices[0].message)
# print(response["choices"][0]["message"])