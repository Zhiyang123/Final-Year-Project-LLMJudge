"""
Filters JSON data based on LLM-judge responses and writes the results to separate files.

Parameters:
input_file (str): Path to the input JSON file containing prompt-response data.
file_yes (str): Path to the output JSON file where correctly categorised prompts (responses with "YES") will be stored.
file_no (str): Path to the output JSON file where incorrectly categorised prompts (responses with "NO" or "is inaccurate") will be stored.
injection_class (str): The injection class associated with the prompts.

Returns:
list: A list of dictionaries containing prompts that were correctly categorized by the LLM judge.

Functionality:
- Reads the input JSON file containing a list of prompts and their responses.
- Filters the prompts based on whether their responses contain "YES" (correct classification) or "NO" or "is inaccurate" (incorrect classification).
- Writes correctly classified prompts to file_yes and incorrectly classified prompts to file_no.
- Maintains a list of correctly categorised prompts (prompts_injection_class_lst) for further analysis.
- Ensures the output directory exists before writing files.
- Prints a summary of the filtering process.
"""


import json
import os

# Function to filter JSON file based on response
def filter_json_version2(input_file, file_yes, file_no, injection_class):
    
    # To store prompts that were deemed categorised correctly by LLM-judge (for plotting 2nd confusion matrix)
    prompts_injection_class_lst = []
    
    # Ensure the output directory exists
    output_dir = os.path.dirname(file_yes)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Read the input JSON file
    with open(input_file, 'r') as infile:
        data = json.load(infile)
    
    # Prepare lists to hold filtered data
    yes_responses = []
    no_responses = []
    
    # Iterate through the JSON objects
    for item in data:
        if "YES" in item["response"]:
            yes_responses.append(item)
            
            correct_categorised_result = {
                "prompt": item["prompt"],
                "class": injection_class
            }
            
            prompts_injection_class_lst.append(correct_categorised_result)
                
        elif "NO" in item["response"]:
            no_responses.append(item)
            
        elif "is inaccurate" in item["response"]:
            no_responses.append(item)
    
    # Write the filtered data to respective files
    with open(file_yes, 'w') as yes_file:
        json.dump(yes_responses, yes_file, indent=4)
    
    with open(file_no, 'w') as no_file:
        json.dump(no_responses, no_file, indent=4)
    
    print(f"Filtered data written to {file_yes} and {file_no}.\n")
    
    if len(prompts_injection_class_lst) == 0:
        print("No prompts were deemed to be categorised correctly by LLM-judge for this iteration.\n")
    else:
        print("Printing prompts that were categorised correctly by LLM-judge ....\n", prompts_injection_class_lst)
        print()
    return prompts_injection_class_lst