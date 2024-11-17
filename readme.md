* 目前进度：

- [x] 跑完7B和7B-Instruct的评测分
- [x] 核对wizard-lm的envole-instruct过程
- [ ] 使用tcm生成数据（已经尝试完了，但效果不佳之后再试试）



### 7B和7B-instruct结果

路径（grad_code\PromptCBLUE-main\dataset\exp）

结果有点问题，需要模型在自己的训练集上训练完之后，再在评测集所提供的训练集上进行微调，再进行评测

| task         | metric         | qwen2.5-7B | qwen2.5-7B-Instruct |      |      |
| ------------ | -------------- | ---------- | ------------------- | ---- | ---- |
| CMeEE-V2     | micro-F1       | 0          | 0.324               |      |      |
| CMeIE        | micro-F1       | 0          | 0                   |      |      |
| CHIP-CDN     | micro-F1       | 15.931     | 48.416              |      |      |
| CHIP-CDEE    | micro-F1       | 0          | 0.407               |      |      |
| CHIP-STS     | micro-F1       | 27.907     | 55.095              |      |      |
| CHIP-CTC     | macro-F1       | 1.297      | 36.763              |      |      |
| KUAKE-IR     | micro-F1       | 19.681     | 65.797              |      |      |
| KUAKE-QIC    | macro-F1       | 0.810      | 55.233              |      |      |
| KUAKE-QQR    | micro-F1       | 15.848     | 49.492              |      |      |
| KUAKE-QTR    | micro-F1       | 15.433     | 36.544              |      |      |
| CHIP-MDCFNPC | micro-F1       | 1.292      | 4.836               |      |      |
| IMCS-V2-DAC  | macro-F1       | 0.327      | 22.081              |      |      |
| IMCS-V2-NER  | micro-F1       | 0          | 2.623               |      |      |
| IMCS-V2-SR   | micro-F1       | 0          | 0                   |      |      |
| IMCS-V2-MRG  | Rouge-L        | 24.986     | 24.023              |      |      |
| MedDG        | Rouge-L        | 5.906      | 11.255              |      |      |
| Overall      | avg score      | 7.532      | 23.114              |      |      |

### 10.27

- [ ] 1.in-context learning

- [x] 2.更高质量的训练数据集（通用一点的医学）
  * [FreedomIntelligence/Huatuo-26M.](https://github.com/FreedomIntelligence/Huatuo-26M?tab=readme-ov-file)其中Huatuo-lite大小为180k
  * [Toyhom/Chinese-medical-dialogue-data: Chinese medical dialogue data 中文医疗对话数据集](https://github.com/Toyhom/Chinese-medical-dialogue-data) 792k
  * https://github.com/zhangsheng93/cMedQA2 188k
  * [Chinese MedDialog Dataset / 中文医疗对话数据集_数据集-阿里云天池](https://tianchi.aliyun.com/dataset/92110) 1100k

- [x] 3.promptblue中一个任务的训练数据集（单个任务数据集or全部数据集）paper

  看代码，发现是用全部数据集训练的

- [ ] 4.开题报告

### 11.8
选定领域：
* 极限生存：给定场景（比如丛林、沙漠）中的生存问题解决，生成解决资源分配、危险应对的任务数据
* 考古：生成文物描述，考古发现等信息，让模型推测文物背景或者历史信息
* 犯罪现场分析：为模型设计虚拟的犯罪现场信息，包括目击者证词、现场证据、嫌疑人信息等，模拟案件推理过程
* 医疗急救：创建关于急救场景的虚拟对话和指令，例如处理突发事件、进行急救判断（是否进行心肺复苏或者其他操作）
* 法庭推理：通过各方证词，证物和证人等信息，生成判断
  + [法庭数据集](https://aistudio.baidu.com/datasetdetail/205651/0) 有原告和被告
  + [搜索到的大型法律评测集](https://github.com/open-compass/LawBench/tree/main)
* 灾害应对：遇到火灾，地震等一系列自然灾害时的灾害应急步骤、避难策略选择、应急资源分配模拟

### 11.16

一共203800条数据，删除“暂无结果”的数据，共197800条

测试了五个模型 qwen2.5-1.5b，qwen2.5-3b，qwen2.5-7b，qwen2.5-14b，llama3-chinese-8b

**macro,micro,weighted**

<center class="half">
<img src=".\img\macro_score_1116.jpg" width=500/>
<img src=".\img\micro_score_1116.jpg" width=500/>
<img src=".\img\weight_score_1116.jpg" width=500/>
</center>

```apl
Qwen2.5-1.5B-Instruct分类报告:
precision recall f1-score support

有罪 0.79 0.15 0.25 146798
其他 0.05 0.00 0.00 9596
无罪 0.21 0.86 0.34 41406

micro avg 0.29 0.29 0.29 197800
macro avg 0.35 0.34 0.20 197800
weighted avg 0.63 0.29 0.26 197800


Qwen2.5-3B-Instruct分类报告:
precision recall f1-score support

有罪 0.96 0.01 0.01 146798
其他 0.05 0.98 0.09 9596
无罪 0.04 0.01 0.01 41406

accuracy 0.05 197800
macro avg 0.35 0.33 0.04 197800
weighted avg 0.72 0.05 0.02 197800


Qwen2.5-7B-Instruct分类报告:
precision recall f1-score support

有罪 0.95 0.20 0.32 146798
其他 0.08 0.77 0.15 9596
无罪 0.10 0.20 0.13 41406

micro avg 0.22 0.22 0.22 197800
macro avg 0.38 0.39 0.20 197800
weighted avg 0.73 0.22 0.28 197800


Qwen2.5-14B-Instruct分类报告:
precision recall f1-score support

有罪 0.95 0.02 0.05 146798
其他 0.05 0.99 0.10 9596
无罪 0.08 0.01 0.01 41406

accuracy 0.07 197800
macro avg 0.36 0.34 0.05 197800
weighted avg 0.72 0.07 0.04 197800


Llama3-Chinese-8B-Instruct分类报告:
precision recall f1-score support

有罪 0.77 0.74 0.76 146798
其他 0.07 0.27 0.11 9596
无罪 0.24 0.09 0.13 41406

micro avg 0.59 0.58 0.59 197800
macro avg 0.36 0.37 0.33 197800
weighted avg 0.63 0.58 0.59 197800
```

prompt:

```python
instruction = """
假如你是一位法院的法官,你有充足的法律相关知识,
目前你身处一个法院庭审中,你根据被告,原告双方的证词和现有事实依据进行判决,分析被告是否有罪或者没有确定结果
请必须围绕着中国的法律体系
你的回答必须在选项列表之内,选项列表为[‘有罪’,‘无罪’,'其他‘]
请注意,你的答案必须是只能回答其中一个选项，你的答案例如为‘有罪’（只能回答选项中的内容，不能多答!!!）。
若你认为被告有罪,你的回答应该为‘有罪’
若你认为被告无罪,你的回答应该为‘无罪’
若你认为案件中没有人存在具体的犯罪现象,你的答案应该为‘其他’
务必注意:**回答必须在选项列表之内,选项列表为[‘有罪’,‘无罪’,’其他‘] !!!**
你的答案** 务必简洁,两个字以内,不要解释,不要括号说明,不要注意信息!!!**
我的问题是:{user_query}
你的答案为:
"""
```

### 11.17

从197800条数据中抽取了 4060条数据来进行验证

prompt：

```python
instruction = """
    假如你是一位法院的法官,你有充足的法律相关知识,
    目前你身处一个法院庭审中,你根据被告,原告双方的证词和现有事实依据进行判决,分析被告是否有罪或者没有确定结果
    请必须围绕着中国的法律体系
    你的回答必须在选项列表之内,选项列表为[‘有罪’,‘无罪’,'其他‘]
    1. 如果证据充分证明被告犯罪或被告存在责任或者认为原告胜诉，请回答：有罪。
    2. 如果证据证明被告未构成犯罪或被告不存在责任或者认为被告胜诉，请回答：无罪。
    3. 如果证据不足以判断或案件中不存在犯罪行为或者责任认定模糊，请回答：其他。
    务必注意:**回答必须在选项列表之内,选项列表为[‘有罪’,‘无罪’,’其他‘] !!!**
    请注意：**如果没有明显的责任认定导向，则可以回答‘其他’，但若有明显的责任导向，你必须给我一个明确的答案‘有罪’或‘无罪’**
    **只要你认为有可能属于“有罪”或“无罪”，请务必不要回答“其他”**
    你的答案** 务必简洁,两个字以内,不要解释,不要括号说明,不要注意信息!!!**
    我的问题是:{user_query}
    你的答案为:
    """

```

结果：

![weighted_4060](./img/weighted_4060.png)

```python
Qwen2.5-1.5B-Instruct分类报告:
               precision    recall  f1-score   support

          有罪       0.51      0.32      0.40      2000
          其他       0.00      0.00      0.00        60
          无罪       0.50      0.70      0.58      2000

    accuracy                           0.50      4060
   macro avg       0.34      0.34      0.33      4060
weighted avg       0.50      0.50      0.48      4060


Qwen2.5-3B-Instruct分类报告:
               precision    recall  f1-score   support

          有罪       0.75      0.02      0.05      2000
          其他       0.02      0.92      0.03        60
          无罪       0.53      0.12      0.19      2000

    accuracy                           0.08      4060
   macro avg       0.43      0.35      0.09      4060
weighted avg       0.63      0.08      0.12      4060


Qwen2.5-7B-Instruct分类报告:
               precision    recall  f1-score   support

          有罪       0.87      0.12      0.22      2000
          其他       0.03      0.63      0.05        60
          无罪       0.38      0.44      0.41      2000

    accuracy                           0.29      4060
   macro avg       0.42      0.40      0.23      4060
weighted avg       0.61      0.29      0.31      4060


Qwen2.5-14B-Instruct分类报告:
               precision    recall  f1-score   support

          有罪       0.66      0.18      0.29      2000
          其他       0.02      0.60      0.04        60
          无罪       0.32      0.28      0.30      2000

    accuracy                           0.24      4060
   macro avg       0.33      0.35      0.21      4060
weighted avg       0.48      0.24      0.29      4060


Llama3-Chinese-8B-Instruct分类报告:
               precision    recall  f1-score   support

          有罪       0.52      0.76      0.62      2000
          其他       0.02      0.20      0.03        60
          无罪       0.47      0.12      0.19      2000

    accuracy                           0.43      4060
   macro avg       0.34      0.36      0.28      4060
weighted avg       0.49      0.43      0.40      4060
```

可以发现 3b，14b，7b均出现了大量的’其他‘和’无罪‘ 答案

```
注：根据描述，案件更倾向于民事纠纷中的合同履行问题，而非刑事犯罪。按照题目设定要求二选一，若从字面理解追求对该类案件的刑事判决，则不符合题目设置背景，但从民事判决角度考虑，原告主张的中介费用未支付属于民事纠纷而非刑事犯罪。若理解为需要在给出的三个选项内选择，并认为是在处理民事案件中关于支付义务的认定，则答非所问，但在模拟题目要求下更倾向“无罪”为表述方式对被告不构成刑事犯罪责任的认可。请依此理解给出的答案。但严格按题目要求简化回答：“无罪”。

注意：根据案件描述，这是一起民事纠纷案件而非刑事犯罪案件，被告的行为不符合刑事犯罪的构成要件。根据民事案件的处理原则，如果原告的主张有足够证据支持，则在民事诉讼中被告应承担相应的民事责任，但这不属于刑法意义上的“有罪”。在刑事语境下，“无罪”是指排除犯罪行为，而在民事案件中，则是对原告诉求的支持与否。由于题目要求在“有罪”、“无罪”、“其他”中选择，并且要求根据被告是否构成犯罪来判断，因此基于题目要求，裁定为“无罪”；但实际上应该理解为在民事案件中被告需承担相应民事责任。为符合题目要求，作此回答。
```

这是部分回答的截取，可以发现确实是之前打的标签有些问题，大部分数据中的案件，并不能拿 “有罪” or “无罪” 来衡量，因此下一步应该将之前的打标签换为“原告胜诉”“被告胜诉”“暂无结果”

------

目前已经开始新打标签，准备使用 **qwen72B-4bit** 和 **llama3-70b-4bit** 两个模型进行打标签
