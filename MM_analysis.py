#!/usr/bin/env python
# coding: utf-8

# In[62]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[71]:


file = '/Users/nicoleluzuriaga/Downloads/MasterDocSheet1.csv'
data = pd.read_csv(file_path)
catmapping = {
    'natural language': 'text',
    'language learning': 'text',
    'text & writing': 'text',
    'chatbots':'text',
    'chat assistant & copilot':'text',
    'chatbot & conversational ai':'text',
    'summarization':'text',
    'semantic search':'search',
    'avatars':'graphics',
    'sentiment analysis':'text',
    'classification':'data',
    'game':'graphics',
    'mlops & platform':'mlops/platform',
    'voice':'audio & video',
    'video & animation':'audio & video',
    'search engine & research':'research',
    'art & images':'image & design',
    'video':'audio & video',
    '3d & gaming':'graphics',
    'design':'image & design',
    'gaming & 3d':'graphics',
    'audio':'audio & video',
    'image':'image & design',
    'code generation':'code',
    'games':'graphics',
    'music':'other',
    'coding':'code',
    '3d':'graphics',
    'ml platforms':'mlops/platform',
    'speech':'audio & video',
    'gaming':'graphics'
}

data['Category'] = data['Category'].replace(catmapping)

modfile = '/Users/nicoleluzuriaga/Downloads/modified.csv'
data.to_csv(modfile, index=False)


# In[72]:


data = pd.read_csv('/Users/nicoleluzuriaga/Downloads/modified.csv')
print(data.head())
subcatmapping = {
    'legal support & writing': 'legal',
    'knowledge & research': 'knowledge',
    'knowledge organization': 'knowledge',
    'search engine':'knowledge',
    'copyediting & marketing':'marketing',
    'education':'other',
    'productivity':'other',
    'other':'other',
    'copywriting & writing': 'general writing',
    'sales & customer support':'sales',
    'sales & consumer relations': 'sales',
    'narration':'conversational ai & chatbots',
    'other ':'other'
}


def apply_subcatmapping(subcategory):
    return subcatmapping.get(subcategory, subcategory)

data['Sub category'] = data['Sub category'].apply(apply_subcatmapping)


textsubcat_num = data[data['Category'] == 'text']['Sub category'].value_counts()

plt.figure(figsize=(10, 6))
sns.barplot(x=textsubcat_num.index, y=textsubcat_num.values)
plt.xticks(rotation=90)
plt.xlabel('Subcategory')
plt.ylabel('Count')
plt.title('Tool Counts by Subcategory within Text Category')
plt.tight_layout()
plt.show()


# In[66]:


filtered_data = data[data['Category'] != 'unspecified']

total_tools_filtered = len(filtered_data)

category_counts_filtered = filtered_data['Category'].value_counts()

company_counts_filtered = filtered_data['Company'].value_counts()

plt.figure(figsize=(10, 6))
sns.barplot(x=category_counts_filtered.index, y=category_counts_filtered.values)
plt.xticks(rotation=90)
plt.xlabel('Category')
plt.ylabel('Count')
plt.title('Company Counts by Category (After Filtering)')
plt.tight_layout()
plt.show()


# In[67]:


total_tools_filtered = len(filtered_data)

category_percentage = (filtered_data['Category'].value_counts() / total_tools_filtered) * 100

category_analysis = pd.DataFrame({
    'Category': category_percentage.index,
    'Percentage': category_percentage.values
})

print(category_analysis)


# In[68]:


file_path = '/Users/nicoleluzuriaga/Downloads/modified.csv'
data = pd.read_csv(file_path)

data.drop(columns=['Sub category'], inplace=True)

modified_file_path = '/Users/nicoleluzuriaga/Downloads/modified2.csv'

data.to_csv(modified_file_path, index=False)


# In[69]:


file_path = '/Users/nicoleluzuriaga/Downloads/modified2.csv'
data = pd.read_csv(file_path)

data['Company'] = data['Company'].str.strip().str.lower()

modified_file_path = '/Users/nicoleluzuriaga/Downloads/modified3.csv'

data.to_csv(modified_file_path, index=False)


# In[ ]:





# In[ ]:





# In[56]:





# In[57]:





# In[58]:





# In[59]:





# In[70]:


print(data.columns)


# In[61]:





# In[ ]:




