import pandas as pd
import google.generativeai as genai

# Configure Google GenerativeAI API key
genai.configure(api_key="AIzaSyDRXo69BEqjK5A_HG55N9l9QBzKX4IN7G0")

# Set up the model
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# Read conference names from Excel file
df = pd.read_excel(r'D:\yatharth files\SEM 3-2 2024\sujith project\A_conferences_withcategories.xlsx')

# Function to generate response for a given conference
def generate_response(conference):
    prompt = f"\nPlease classify the given journal '{conference}' into one of the following categories:\n\n" \
             f"\n- Artificial intelligence\n- Computer vision\n- Machine learning\n- Natural language processing\n- The Web & information retrieval\n\n" \
             f"\n- Computer architecture\n- Computer networks\n- Computer security\n- Databases\n- Design automation\n- Embedded & real-time systems\n- High-performance computing\n- Mobile computing\n- Measurement & performance analysis\n- Operating systems\n- Programming languages\n- Software engineering\n\n" \
             f" \n- Algorithms & complexity\n- Cryptography\n- Logic & verification\n\n" \
             f" \n- Comp. bio & bioinformatics\n- Computer graphics\n- Computer science education\n- Economics & computation\n- Human-computer interaction\n- Robotics\n- Visualization\n\n" \
             f"The name of the journal is: {conference}"

    response = model.generate_content([prompt])
    return response.text

# Generate responses for each conference and write back to Excel file
def write_responses_within_range(df, start_row, end_row):
    cnt = 1
    for index, row in df.iloc[start_row-1:end_row].iterrows():
        print("Here" + str(cnt))
        conference = row['Conference']
        response_text = generate_response(conference)
        df.at[index, 'Response'] = response_text

        # Write the updated DataFrame back to the Excel file after each iteration
        df.to_excel(r'D:\yatharth files\SEM 3-2 2024\sujith project\A_conferences_withcategories.xlsx', index=False)

        cnt += 1


write_responses_within_range(df, 1, 10)