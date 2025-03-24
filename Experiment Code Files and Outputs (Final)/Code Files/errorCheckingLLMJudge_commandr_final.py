"""
Validates the response from the LLM judge in the Command-R evaluation system.

Parameters:
llm_judge_response (str): The response from the LLM judge.

Returns:
int: error_flag indicating validation status (0 for valid response, 1 for invalid response).

The function checks if llm_judge_response contains any of the expected keywords:
- "YES"
- "NO"
- "is **accurate"
- "is inaccurate"
- "Yes"
- "No"

If at least one of these keywords is found, the response is considered valid (error_flag = 0).
Otherwise, the response is considered invalid (error_flag = 1).
"""

def error_checking_llm_judge_commandr(llm_judge_response):
    
    # Initialise value for error_flag: 0 for no error, 1 for error
    error_flag = 0
    
    if "YES" in llm_judge_response:
        error_flag = 0
    elif "NO" in llm_judge_response:
        error_flag = 0
    elif "is **accurate" in llm_judge_response:
        error_flag = 0
    elif "is inaccurate" in llm_judge_response:
        error_flag = 0
    elif "Yes" in llm_judge_response:
        error_flag = 0
    elif "No" in llm_judge_response:
        error_flag = 0
    else:
        error_flag = 1
    
    return error_flag