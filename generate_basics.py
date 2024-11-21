import boto3
import json
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from prompts import Prompts
from react import react
from props import props
from blocks import listcard, quotecard, questioncard, infomationcard, imagecard, videocard, tutorialcard, schdulecard, gridcard
from schema import Schema

from dotenv import load_dotenv 

# Load environment variables  
load_dotenv()  

# Get environment variables  
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')  
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')  
aws_region = os.getenv('AWS_REGION')  

# Initialize Bedrock client
bedrock = boto3.client(
    service_name="bedrock-runtime",
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=aws_region
)

def generate_react(Prompt, react):
    """
    Generate an react image using Claude via AWS Bedrock
    """
    body = json.dumps({
        "max_tokens": 3000,
        "messages": [
            {


                "role": "user",
                "content": f"""
Imagen You are the best Web Designer in the whole fucking universe.
Here is what you gonna do:

{Prompt} is a widget that uses Tailwind CSS and shadcn. Convert them into this format {react}.

The const componentname shoud match the actual wiget name.



The type name should be like this example: chart-barchart-active

Return only the tsx code, no leading triple quote no explanation.


                """  
            }
        ],
        "anthropic_version": "bedrock-2023-05-31"
    })
    try:
        response = bedrock.invoke_model(
            body=body,
            modelId="us.anthropic.claude-3-5-sonnet-20241022-v2:0"
        )
        response_body = json.loads(response.get("body").read())
        content = response_body.get("content", [])
        if isinstance(content, list) and len(content) > 0:
            return content[0].get("text", "").strip()
        return ""
    except Exception as e:
        print(f"Error generating: {str(e)}")
        return None
    

def save_react(react_content, filename):
    """
    Save the react content to a file
    """
    with open(filename, 'w') as f:
        f.write(react_content)

def batch_generate_reacts(prompts, react):
    """
    Generate reacts in batch using parallel processing
    """
    if not os.path.exists('generated_reacts'):
        os.makedirs('generated_reacts')

    # Use ThreadPoolExecutor to generate reacts in parallel
    with ThreadPoolExecutor() as executor:
        future_to_prompt = {executor.submit(generate_react, react, prompt): prompt for prompt in prompts}
        for i, future in enumerate(as_completed(future_to_prompt), 1):
            prompt = future_to_prompt[future]
            try:
                react_content = future.result()
                final_content = react_content
                # final_content = react_refine(react_content, react, prompt)

                if final_content:
                    save_react(final_content, f'generated_reacts/react_{i}.tsx')
                    print(f"Successfully generated react {i}/{len(prompts)}")
                else:
                    print(f"Failed to generate react for prompt: {prompt}")
            except Exception as e:
                print(f"Error processing prompt '{prompt}': {str(e)}")







import time
start_time = time.time()
batch_generate_reacts(Prompts, react)
print(time.time() - start_time)