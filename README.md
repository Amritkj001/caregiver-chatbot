# Care Kaki - support for caegivers of the elderly
 - [Background](#Background)
 - [Problem Statement](#Problem-Statement)
 - [Approach](#Approach)
 - [Technical & Task Based Evaluation](#Technical-&-Task-Based-Evaluation)
 - [Conclusion](#Conclusion)
 
## Background
![Caring Hands](images/caring-hands-and-logo.jpg)

### Caregiving for the Elderly in Singapore

With Singapore's population ageing rapidly, caregiving for the elderly has become a significant national issue. By 2030, nearly one in four Singaporeans will be aged 65 or older, placing immense pressure on families, communities, and healthcare systems. 

#### Trends in Elderly Caregiving

Over recent decades, caregiving in Singapore has gained increasing importance due to higher life expectancy and declining birth rates. More elderly individuals are living longer, often with chronic conditions requiring extended care. Currently, approximately 210,000 caregivers in Singapore provide support for elderly family members, with the majority being middle-aged women balancing caregiving responsibilities with employment and other family duties, heightening the risk of stress and burnout.

#### Challenges Caregivers Face

One of the foremost challenges caregivers encounter is the **emotional and physical toll** caregiving takes. Many caregivers report feelings of isolation, exhaustion, and anxiety, particularly when caring for elderly individuals with dementia or other complex health issues. This strain can lead to a decline in the caregiver's own health and well-being over time.

Caregiving also brings **financial stress**, as the cost of medical care, professional services, and home adaptations can be significant. Many caregivers are forced to cut back on work or dip into personal savings to cover expenses, adding to the already substantial financial burden.

## Problem Statement

Despite government initiatives, **lack of awareness of exisiting resources** is one of the barriers that continuse to prevent caregivers from receiving help that can alleviate the mental, physical and financial toll that comes from caregiivng. As a result, caregivers frequently feel unsupported and overwhelmed by their duties.

## Approach

**How might we use machine learning to address this awareness gap?**

We will follow the data science process to create a solution.
1. Define the problem
2. Gather & clean the data
3. Explore the data
4. Model the data
5. Evaluate the model
6. Answer the problem

### Dataset
The dataset used for machine learning contains two columns; "Question" and "Answer", and a total of 69 rows. 

The dataset contains information on grants and schemes to support the elderly, as well as resources for caregivers themselves. The data was selected, manually scrapped and curated from government websites such as LifeSG and Agency for Integrated Care. 

The information in the dataset is accurate as of 11/11/2024.

### Machine Learning

In building the chatbot, Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), and OpenAI models are used to provide accurate and contextually relevant responses to users, especially caregivers seeking support. 

**Large Language Models (LLMs)** such as OpenAI's GPT-4, are powerful tools capable of understanding and generating human-like text. The key advantage of LLMs is their ability to:

- Understand complex queries and respond with natural language output.
- Process vast amounts of pre-existing knowledge, which is crucial for generating insightful and relevant responses in various caregiving scenarios.
- Handle conversational nuances, making them particularly suited for a chatbot that needs to interact with users empathetically and dynamically.

By using LLMs, the chatbot can engage with users meaningfully, addressing both the informational and emotional aspects of caregiving.

**Retrieval-Augmented Generation (RAG)** is a technique that combines the power of LLMs with an external knowledge base to improve accuracy and relevancy. The process involves:

- Retrieving relevant information from an external knowledge base or database based on user queries.
- Generating responses that combine the retrieved data with the LLM’s natural language capabilities.

This is particularly useful for the chatbot, as caregivers often require precise information about resources, government schemes, and support services. RAG ensures that the chatbot can access and provide up-to-date information, which may not be part of the LLM's internal knowledge.

**OpenAI Models** such as GPT-4 and GPT-4 Turbo models were used due to their robust conversational abilities, high-quality outputs, and cost-efficiency. OpenAI models provide:

- Scalable, powerful performance in generating natural, contextually rich conversations.
- Flexibility to handle real-world deployment scenarios, with GPT-4 Turbo offering faster and more cost-efficient interactions.

OpenAI models help achieve the goal of making the chatbot both intelligent and responsive, ensuring that it can answer user queries with depth and accuracy.

**Why This Approach?**

By integrating LLMs, RAG, and OpenAI models, the chatbot:

- Provides accurate and relevant information by retrieving real-time resources.
- Maintains conversational quality and empathy, crucial in supporting caregivers.
- Is scalable and efficient, ensuring a seamless user experience even during long, detailed interactions.

This approach allows the chatbot to fulfil its role effectively as a resource for caregivers, offering both information and emotional support tailored to individual needs.

## Conclusion

XXX
