import json
import pandas as pd
from bs4 import BeautifulSoup
from openai import OpenAI

API_KEY = ''
client = OpenAI(api_key=API_KEY)

def load_html(file_path):
    """Load HTML file and parse with BeautifulSoup."""
    with open(file_path, encoding='utf-8') as file:
        return BeautifulSoup(file, "html.parser")

def extract_text_elements(soup, tag, attributes):
    """Extract text elements from HTML based on tag and attributes."""
    elements = soup.find_all(tag, attributes)
    return [element.text for element in elements if element.text]


def generate_json_prompt(input_list):
    """Generate JSON conversion prompt for OpenAI API."""
    return f"""Convert the following list into a JSON object with each records based on this \
            JSON record schema:
            {{
                "name": "Bill Kim Ramen Bar",
                "rating": "3.2",
                "reviews": "45",
                "price": "$$",
                "category": "Ramen",
                "location": "916 W Fulton Market",
                "hours": "Open - Closes 9PM",
                "services": [
                    "Dine-in",
                    "Takeout",
                    "Delivery"
                ],
                "actions": [
                    "Order online"
                ]
            }}
            You will reply only with the JSON itself, and no other descriptive or explanatory text
            ---
            Input:
            {str(input_list)}
            """


def get_openai_response(client, prompt):
    """Get response from OpenAI API."""
    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        model="gpt-4o",
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.1
    )
    return response.choices[0].message.content.strip('```json\n').rstrip('```')


def main():
    # Load and parse HTML
    soup = load_html("maps.html")
    results = extract_text_elements(soup, 'div', {'jsaction': True})

    # Save raw extracted text elements to a file
    with open("raw_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"Saved {len(results)} raw text elements to raw_results.json")


    # Process text elements in batches
    recordset = []
    batch_size = 35
    for i in range(0, 100, batch_size):
        input_list = results[i:i + batch_size]
        prompt = generate_json_prompt(input_list)

        print('running...')
        response_content = get_openai_response(client, prompt)
        data = json.loads(response_content)

        print(len(data))
        recordset.extend(data)

    # Save to CSV
    df = pd.DataFrame(recordset)
    df.to_csv('bakery_gpt4o.csv', encoding='utf-8-sig', index=False)

if __name__ == "__main__":
    main()
