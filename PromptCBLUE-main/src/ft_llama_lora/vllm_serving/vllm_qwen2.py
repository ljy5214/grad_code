# vllm_model.py
from vllm import LLM, SamplingParams
from transformers import AutoTokenizer
import os
import json
import time

# 自动下载模型时，指定使用modelscope。不设置的话，会从 huggingface 下载
# os.environ['VLLM_USE_MODELSCOPE']='True'

def get_completion(prompts, model, tokenizer=None, max_tokens=512, temperature=0.8, top_p=0.95, max_model_len=2048):
    stop_token_ids = [151329, 151336, 151338]
    # 创建采样参数。temperature 控制生成文本的多样性，top_p 控制核心采样的概率
    sampling_params = SamplingParams(temperature=temperature, top_p=top_p, max_tokens=max_tokens, stop_token_ids=stop_token_ids)
    # 初始化 vLLM 推理引擎
    llm = LLM(model=model, tokenizer=tokenizer, max_model_len=max_model_len,trust_remote_code=True)
    outputs = llm.generate(prompts, sampling_params)
    return outputs

# def get_data():



if __name__ == "__main__":    
    # 初始化 vLLM 推理引擎
    model='/root/autodl-tmp/Qwen2.5-7B-Instruct' # 指定模型路径
    # model="qwen/Qwen2-7B-Instruct" # 指定模型名称，自动下载模型
    tokenizer = None
    # 加载分词器后传入vLLM 模型，但不是必要的。
    # tokenizer = AutoTokenizer.from_pretrained(model, use_fast=False) 
    f_out = open("src/web_services/test_examples/test_preds_0.json", "a", encoding="utf-8", buffering=1)
    with open("data/promptcblue/test_a_open_0/dev.json", "r", encoding="utf-8") as f:

        for line in f:
            line = line.strip()
            if not line:
                continue

            line = json.loads(line)

            t0 = time.time()
            result = get_completion([line['prompt']], model, tokenizer=tokenizer, max_tokens=512, temperature=1, top_p=1, max_model_len=2048)
            t1 = time.time()
            print("time cost: ", t1 - t0)

            f_out.write(
                json.dumps(result, ensure_ascii=False) + "\n"
            )
    
    # text = ["你好，帮我介绍一下什么时大语言模型。",
    #         "可以给我将一个有趣的童话故事吗？"]*100
    # messages = [
    #     {"role": "system", "content": "你是一个有用的助手。"},
    #     {"role": "user", "content": prompt}
    # ]
    # 作为聊天模板的消息，不是必要的。
    # text = tokenizer.apply_chat_template(
    #     messages,
    #     tokenize=False,
    #     add_generation_prompt=True
    # )

    # outputs = get_completion(text, model, tokenizer=tokenizer, max_tokens=512, temperature=1, top_p=1, max_model_len=2048)

    # 输出是一个包含 prompt、生成文本和其他信息的 RequestOutput 对象列表。
    # 打印输出。
    for output in outputs[:2]:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
