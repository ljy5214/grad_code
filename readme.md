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
 https://aistudio.baidu.com/datasetdetail/205651/0
* 灾害应对：遇到火灾，地震等一系列自然灾害时的灾害应急步骤、避难策略选择、应急资源分配模拟