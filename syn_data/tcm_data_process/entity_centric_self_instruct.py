import openai
import json
import sys
import random
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
# openai.api_key = "sk-xxx"  # you must provide your OpenAI API key before crawling

if not openai.api_key:
    raise ValueError("OpenAI API key not provided. Please set the 'openai.api_key' variable.")


def return_random_prompt(kg_file=None):
    system_prompt = "你需要尽可能给出多样化的，与中医(中国传统医学),中药等相关的，任务指令和对应的回答。我们将用于人工评估ChatGPT模型对指令的完成情况。要求:\n"

    # generate random topics
    entity_list = []
    with open(kg_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip().split("	")
            # print(line)
            for w in line:
                w = w.strip()
                if "symmap_chemical" in w:
                    continue
                if "chemical_" in w:
                    continue
                if "SMIT" in w:
                    continue

                # print(w)
                entity_list.append(w)

    # system_prompt += "1. 主题多样化，涵盖各个领域，例如：" + "、".join(random.sample(topic_list, 10)) + "等。\n"
    system_prompt += "1. 主题多样化，涵盖不同的中医实体，例如：" + "、".join(
        random.sample(entity_list, 10)
    ) + "等。\n"

    # generate random tasks
    task_list = ["开放式生成", "分类", "问答", "编辑", "摘要",
                 "写作", "分析", "常识推理", "写文献",
                 "抽取", "推荐", "问诊", "文献标题生成", "诊断", "方剂推荐", "治疗推荐"]
    system_prompt += "2. 表述多样化，结合真实问题；指令类型多样化，例如：" + "、".join(random.sample(task_list, 10)) + "等。\n"

    # other requirements
    system_prompt += "3. 如果遇到无法处理的指令（只靠文本无法回答），给出无法处理的回复。\n"
    system_prompt += "4. 除非特别要求，请使用中文，指令可以是命令句、疑问句、或其他合适的类型。\n"
    system_prompt += "5. 为指令生成一个适当且涉及真实情况的<input>，不应该只包含简单的占位符。<input>应提供实质性的内容，具有挑战性。字数不超过" + str(
        random.randint(80, 120)) + "字。\n"
    system_prompt += "6. <output>应该是对指令的适当且真实的回应，不能只回复答应或拒绝请求。如果需要额外信息才能回复时，请努力预测用户意图并尝试回复。<output>的内容应少于" + str(
        512) + "字。\n\n"

    system_prompt += "请给出满足条件的5条JSON格式数据：\n"

    print(system_prompt)
    return system_prompt

def get_response(model,prompt,tokenizer):
    # model_name = '../model/qwen/Qwen2.5-7B-Instruct'

    # model = AutoModelForCausalLM.from_pretrained(
    #     model_name,
    #     torch_dtype="auto",
    #     device_map="auto"
    # )
    # tokenizer = AutoTokenizer.from_pretrained(model_name)

    # prompt = "给我讲一个笑话"
    messages = [
        {"role": "system", "content": "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ]
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )
    model_inputs = tokenizer([text], return_tensors="pt").to(model.device)
    torch.backends.cuda.enable_mem_efficient_sdp(False)
    torch.backends.cuda.enable_flash_sdp(False)
    generated_ids = model.generate(
        **model_inputs,
        max_new_tokens=512,
    )
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]

    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return response

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python crawl_prompt.py <input_kg_file> <output_file>")
        exit(1)

    kg_file = sys.argv[1]
    output_file = open(sys.argv[2], 'w', encoding="utf-8")
    model_name = '../model/qwen/Qwen2.5-7B-Instruct'
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype="auto",
        device_map="auto"
    )
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    MAX_EPOCHS = 10  # number of data to generate (each prompt contains 20 JSON-formatted data)
    for k in range(MAX_EPOCHS):
        # response = openai.ChatCompletion.create(
        #     model="gpt-3.5-turbo",  # here we use `gpt-3.5-turbo` model, while Stanford-Alpaca uses `text-davinci-003`
        #     messages=[
        #         {"role": "user", "content": return_random_prompt(kg_file=kg_file)},
        #     ]
        # )
        # print(response["choices"])
        # output_file.write(response["choices"][0]["message"]["content"] + '\n')
        response = get_response(model, return_random_prompt(kg_file=kg_file),tokenizer)
        output_file.write(response + '\n')

    output_file.close()


