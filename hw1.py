
# coding: utf-8

# In[1]:

import mediacloud, datetime


# In[2]:

mc = mediacloud.api.MediaCloud('9161674c95b57926bdbfee32ac62556983f678a7a45b51249e571aa3c3fae200')


# In[3]:

res = mc.sentenceCount('( dog)', solr_filter=[mc.publish_date_query( datetime.date( 2015, 8, 1), datetime.date( 2015, 8, 31) ), 'media_sets_id:1' ])


# In[4]:

print res['count']


# In[5]:

res = mc.sentenceCount('( cat)', solr_filter=[mc.publish_date_query( datetime.date( 2015, 8, 1), datetime.date( 2015, 8, 31) ), 'media_sets_id:1' ])


# In[6]:

print res['count']


# In[7]:

print('dogs are way popular than cats')


# In[ ]:



