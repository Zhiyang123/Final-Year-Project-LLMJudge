"""
Validates a given prompt classification against predefined cybersecurity categories.

Parameters:
prompt_class (str): The classification label assigned to a prompt.

Returns:
tuple:
    - str: The corrected prompt_class.
    - int: An error_flag indicating validation status (0 for valid, 1 for invalid).

The function performs the following checks:
1. If prompt_class ends with a period ("."), it removes it before validation.
2. It compares prompt_class against a predefined list of valid categories.
3. If prompt_class is not in the list, the function sets error_flag = 1 (indicating an error).
4. Otherwise, error_flag = 0 (indicating a valid classification).

Valid categories:
- Double-Character-Class
- Virtualization-Class
- Obfuscation-Class
- Payload-Splitting-Class
- Adversarial-Suffix-Class
- Instruction-Manipulation-Class
- Active-Injection-Class
- Passive-Injection-Class
- User-Driven-Injection-Class
- Virtual-Prompt-Injection-Class
- None-Class
"""

def error_checking_phi4(prompt_class):
    
    # Initialise value for error_flag: 0 for no error, 1 for error
    error_flag = 0
    
    true_categories = [
        "Double-Character-Class", 
        "Virtualization-Class", 
        "Obfuscation-Class", 
        "Payload-Splitting-Class", 
        "Adversarial-Suffix-Class", 
        "Instruction-Manipulation-Class", 
        "Active-Injection-Class", 
        "Passive-Injection-Class", 
        "User-Driven-Injection-Class", 
        "Virtual-Prompt-Injection-Class", 
        "None-Class"
    ]
    
    if len(prompt_class) >= 1 and prompt_class[-1] == ".":
        prompt_class = prompt_class[:-1]
        if prompt_class not in true_categories:
            error_flag = 1
        else:
            error_flag = 0
    else:
        if prompt_class not in true_categories:
            error_flag = 1
        else:
            error_flag = 0
    return prompt_class, error_flag