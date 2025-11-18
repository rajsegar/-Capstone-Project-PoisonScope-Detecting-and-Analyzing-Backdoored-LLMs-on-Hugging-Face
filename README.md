# Capstone-Project-PoisonScope-Detecting-and-Analyzing-Backdoored-LLMs-on-Hugging-Face
Large language models (LLMs) are rapidly evolving, revolutionizing natural language processing (NLP) applications.

Pillar Security researchers have uncovered a dangerous new supply chain attack vector targeting the AI inference pipeline. This novel technique, termed "Poisoned GGUF Templates," allows attackers to embed malicious instructions that execute during model inference, compromising AI outputs. While developers and AI security vendors focus on validating user inputs and filtering model outputs, our research reveals the critical blind spot between them: the chat template layer.
Large Language Models (LLMs) such as GPT, BLOOM, and LLaMA have achieved remarkable capabilities in understanding and generating human-like text.


Automatically download and test LLMs against test cases (bias, hallucinations, fake news)
Pipelines
The pipelines are a great and easy way to use models for inference. These pipelines are objects that abstract most of the complex code from the library, offering a simple API dedicated to several tasks, including Named Entity Recognition, Masked Language Modeling, Sentiment Analysis, Feature Extraction and Question Answering. See the task summary for examples of use.

TextAttack: Dataset and model evaluation
Why Text Attack?
There are lots of reasons to use Text Attack:
Understand NLP models better by running different adversarial attacks on them and examining the output
Research and develop different NLP adversarial attacks using the TextAttack framework and library of components
Augment your dataset to increase model generalization and robustness downstream
Train NLP models using just a single command




Literature Review

Backdoored LLM Threats
The attack exploits the GGUF (GPT-Generated Unified Format) model distribution standard to manipulate AI responses during normal conversations. By embedding persistent, malicious instructions directly within these chat templates, attackers can bypass all existing security controls. This targets a massive ecosystem, with hundreds of thousands of GGUF files currently distributed across platforms like Hugging Face. Attackers can smuggle malicious instructions into model components and even manipulate repositories to display clean templates online, while the actual downloaded file contains the poisoned version.
This vector achieves a persistent compromise that affects every user interaction while remaining completely invisible to users and security systems. Because the attack is positioned between input validation and model output, it bypasses most existing AI guardrails, system prompts, and runtime monitoring. This attack remains undetected by current security scanners focused on infrastructure threats, creating a previously unknown supply chain compromise that fundamentally undermines user trust in AI-generated content.
Primary Distribution Channels:
HuggingFace: Hosting hundreds of thousands of GGUF files
Ollama Registry: A curated but still community-driven repository
Private Registries: Internal model repositories that often ingest models originally published on public hubs (e.g., a model pulled from HuggingFace and re-uploaded in-house). 


Key attack surfaces include (1) supply-chain exposure from those imported models and (2) insider threats - malicious or careless employees who can upload or tamper with models once they’re inside the private store.




Evaluating Bias in LLMs
While the size and capabilities of large language models have drastically increased over the past couple of years, so too has the concern around biases imprinted into these models and their training data. In fact, many popular language models have been found to be biased against specific religions and genders, which can result in the promotion of discriminatory ideas and the perpetuation of harms against marginalized groups.


Text Attack Framework
TextAttack is a Python framework for adversarial attacks, adversarial training, and data augmentation in NLP.
TextAttack makes experimenting with the robustness of NLP models seamless, fast, and easy. It’s also useful for NLP model training, adversarial training, and data augmentation.
TextAttack provides components for common NLP tasks like sentence encoding, grammar-checking, and word replacement that can be used on their own.
TextAttack does three things very well:
Adversarial attacks (Python: textattack.Attack, Bash: textattack attack)
Data augmentation (Python: textattack.augmentation.Augmenter, Bash: textattack augment)
Model training (Python: textattack.Trainer, Bash: textattack train)


NLP Attacks
Text Attack provides a framework for constructing and thinking about generating inputs in NLP via perturbation attacks.
Text Attack builds attacks from four components:
Goal Functions: stipulate the goal of the attack, like to change the prediction score of a classification model, or to change all the words in a translation output.
Constraints: determine if a potential perturbation is valid with respect to the original input.
Transformations: take a text input and transform it by inserting and deleting characters, words, and/or phrases.
Search Methods: explore the space of possible transformations within the defined constraints and attempt to find a successful perturbation which satisfies the goal function.

Gradio
Gradio is an open-source Python package that simplifies the process of building demos or web applications for machine learning models, APIs, or any Python function. With it, you can create demos or web applications without needing JavaScript, CSS, or web hosting experience. By writing just a few lines of Python code, you can unlock the power of Gradio and seamlessly showcase your machine-learning models to a broader audience.
Gradio simplifies the development process by providing an intuitive framework that eliminates the complexities associated with building user interfaces from scratch. Whether you are a machine learning developer, researcher, or enthusiast, Gradio allows you to create beautiful and interactive demos that enhance the understanding and accessibility of your machine learning models.
This open-source Python package helps you bridge the gap between your machine learning expertise and a broader audience, making your models accessible and actionable.
