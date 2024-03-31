# %%
from lxml import etree, html

with open('data/recommend_20240331.html', 'rt', encoding='utf-8') as f:
    html_text = f.read()

source_code = html.fromstring(html_text)
len(source_code.xpath('div/div'))

# source_code.xpath('div/div')[0].text_content()
# source_code.xpath('div/div')[0].to_string()
# '/html/body/div[2]/div[2]/div/div[1]/div/div/div/div[2]/div'
# a = soup.find_all('div', class_='row')
# a[0].find('div', class_='info-company') 
# print(a[0])

# %%
div_element = source_code.xpath('div/div')[0]  # assuming this is the div element you're interested in
print(etree.tostring(div_element, pretty_print=True).decode())
# %%
print(div_element.xpath('@description')[0])

#%%
div_element = source_code.xpath('div/div/div/text()')[0]  # assuming this is the div element you're interested in
print(div_element)
div_element = source_code.xpath('div/div/div/div/div/div/a/text()')[0]  # assuming this is the div element you're interested in
print(div_element)
div_element = source_code.xpath('div/div/div/div/div[1]/div[2]/span/text()')[0]  # assuming this is the div element you're interested in
print(div_element)
div_element = source_code.xpath('div/div/div/div/div/div[2]/a/text()')[0]  # assuming this is the div element you're interested in
print(div_element)