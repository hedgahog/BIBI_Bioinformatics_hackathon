from gemini_function import json_to_dict, SNP_to_genai

rs = "6311"

# get json data and put into python dict
python_dict = json_to_dict(rs)

# dump dict into json and load into genai
summary = SNP_to_genai(python_dict)
print(summary)
