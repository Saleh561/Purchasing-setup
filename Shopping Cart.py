

# def discount(amount):
#     if amount > 500:
#         discount = amount * 0.10
#         return discount
#     else:
#         return 0




# print("Items Available")
# total = 0

# item1 = "1. Book 350"
# item2 = "2. Notebook 250"
# item3 = "3. Pen 100"
# item4 = "4. Pencil 70"
# item5 = "0. Exit"

# while(True):
#     print(item1)
#     print(item2)
#     print(item3)
#     print(item4)
#     print(item5)

#     select = int(input("Enter an item to buy "))
#     if(select == 0):
#         break

#     elif(select == 1):
#         total += 350
#         print("Book Added\n Current Total " , total ,"\n")

#     elif(select == 2):
#         total += 250        
#         print("Notebook Added\n Current Total " , total ,"\n")

#     elif(select == 3):
#         total += 100        
#         print("Pen Added\n Current Total " , total, "\n")

#     elif(select == 4):
#         total += 70        
#         print("Pencil Added\n Current Total " , total, "\n")

#     else:
#         print("Invalid Item selected...")         
#         print("Nothing Added\n Current Total " , total , "\n")




# print("\n\nTotal Bill ", total)


# discounted = discount(total)
# final_amount = total - discounted

# print("\nDiscounted Applied ", discounted)
# print("Final Bill ", final_amount)
# print("\nThanks for visiting Us...\n\n")





































import os
import requests

print("Items Available")
total = 0

item1 = "1. Book 350"
item2 = "2. Notebook 250"
item3 = "3. Pen 100"
item4 = "4. Pencil 70"
item5 = "0. Exit"

while(True):
    print(item1)
    print(item2)
    print(item3)
    print(item4)
    print(item5)

    select = int(input("Enter an item to buy "))
    if(select == 0):
        break

    elif(select == 1):
        total += 350
        print("Book Added\n Current Total " , total ,"\n")

    elif(select == 2):
        total += 250        
        print("Notebook Added\n Current Total " , total ,"\n")

    elif(select == 3):
        total += 100        
        print("Pen Added\n Current Total " , total, "\n")

    elif(select == 4):
        total += 70        
        print("Pencil Added\n Current Total " , total, "\n")

    else:
        print("Invalid Item selected...")         
        print("Nothing Added\n Current Total " , total , "\n")


print("\n\nTotal Bill ", total)

# ==========================================
# 🤖 NEW CODE: CALLING THE LLM API AT CHECKOUT
# ==========================================

# 1. Securely fetch the API key from your computer environment
api_key = os.environ.get("MY_AI_API_KEY")

# 2. Check if the key exists before making the web request
if api_key is None:
    print("\n[System Note: AI feature skipped. No API key found in your environment.]")
else:
    print("\nConnecting to AI Assistant for your checkout note...")
    
    # 3. FIXED: Changed back to the official API endpoint URL
    url = "https://openai.com"
    
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json"
    }
    
    # 4. Create the custom prompt telling the AI what the user spent
    ai_prompt = "The customer just spent a total of " + str(total) + " coins at my bookstore. Write a short, single-sentence checkout message thanking them enthusiastically."
    
    # 5. Pack the data into the structure the API expects
    payload = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": ai_prompt}],
        "temperature": 0.7
    }
    
    # 6. Send the request over the internet and handle errors safely
    try:
        response = requests.post(url, json=payload, headers=headers)
        
        # Check if the website responded successfully (Status Code 200)
        if response.status_code == 200:
            response_data = response.json()
            # Excellent fix you made here! This correctly navigates the list.
            ai_message = response_data["choices"][0]["message"]["content"]
            print("\n🤖 AI Note: " + ai_message)
        else:
            print("\n[AI Error: Failed to fetch response. Status code " + str(response.status_code) + "]")
            
    except Exception:
        print("\n[Network Error: Could not connect to the internet to reach the AI.]")

# ==========================================

print("Thanks for visiting Us...")

