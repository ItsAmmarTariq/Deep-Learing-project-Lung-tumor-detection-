
###START

import random
import nltk

# Import necessary NLTK modules
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Set up stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.tag import pos_tag

stop_words = set(stopwords.words('english'))

# Preprocessing function
def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [token for token in tokens if token.isalpha() and token not in stop_words]
    return tokens

# Process user input
def process_user_input(user_input):
    # Tokenize user input
    user_tokens = preprocess_text(user_input)

    # Provide information about different topics based on user input
    if any(token in ['diet', 'nutrition'] for token in user_tokens):
        return "Maintaining a healthy diet is essential during lung tumor cancer treatment..."

    if any(token in ['smoking', 'quit', 'cigarettes'] for token in user_tokens):
        return "Smoking is a significant risk factor for developing lung tumor cancer..."

    if any(token in ['cancer'] for token in user_tokens):
        return "Cancer is a complex disease characterized by the uncontrolled growth of abnormal cells..."

        # Provide information about diet
    if any(token in ['diet', 'nutrition'] for token in user_tokens):
        return "Maintaining a healthy diet is essential during lung tumor cancer treatment. A well-balanced diet rich in fruits, vegetables, whole grains, lean proteins, and healthy fats can help support overall health and well-being. However, specific dietary recommendations may vary for individuals based on their condition and treatment plan. It's recommended to consult a healthcare professional or a registered dietitian for personalized dietary guidance."

        # Provide information about smoking and cancer
    if any(token in ['smoking', 'quit', 'cigarettes'] for token in user_tokens):
        return "Smoking is a significant risk factor for developing lung tumor cancer. The majority of lung tumor cancer cases are caused by smoking, including both active and passive smoking (secondhand smoke). Quitting smoking is one of the most crucial steps in reducing the risk of lung tumor cancer. It can also improve overall health and decrease the risk of other smoking-related diseases. There are various smoking cessation methods and resources available, including medications, counseling, support groups, and behavioral therapies. Seeking assistance from healthcare professionals or smoking cessation programs can greatly increase the chances of successfully quitting smoking."

        # Provide information about cancer
    if any(token in ['cancer'] for token in user_tokens):
        return "Cancer is a complex disease characterized by the uncontrolled growth of abnormal cells. Lung tumor cancer specifically refers to cancer that originates in the lungs. There are two main types of lung tumor cancer: benign and malignant. Benign tumors are non-cancerous and do not spread to other parts of the body, while malignant tumors are cancerous and can invade nearby tissues and spread to other organs through a process called metastasis."

        # Provide information about cancer stages
    if any(token in ['stages', 'stage'] for token in user_tokens):
        return "The stages of lung tumor cancer are typically classified using the TNM staging system, which considers the size of the tumor (T), the involvement of lymph nodes (N), and the presence of distant metastasis (M). The stages range from Stage 0 (carcinoma in situ) to Stage IV (advanced cancer with distant metastasis). Each stage helps determine the treatment approach and provides insights into the prognosis. It's important to consult with healthcare professionals to understand the specific stage and its implications for your case."

        # Provide information about instructions
    if any(token in ['instructions', 'guidance'] for token in user_tokens):
        return "During lung tumor cancer treatment, it's essential to follow the instructions provided by healthcare professionals. These instructions may include taking prescribed medications as directed, attending scheduled appointments, undergoing recommended tests and procedures, managing side effects, and making necessary lifestyle modifications. It's important to communicate openly with your healthcare team and seek clarification if you have any questions or concerns about the instructions."

        # Provide information about myths
    if any(token in ['myths', 'misconceptions'] for token in user_tokens):
        return "There are several myths and misconceptions associated with lung tumor cancer. Some common myths include believing that only smokers can develop lung tumor cancer, or that a single exposure to secondhand smoke can cause it. It's important to rely on accurate information from credible sources such as healthcare professionals, medical organizations, and reputable research studies. If you have specific myths or misconceptions in mind, feel free to ask for clarification."

        # Provide information about medication
    if any(token in ['medicine', 'medication'] for token in user_tokens):
        return "Treatment for lung tumor cancer may involve different types of medications, such as chemotherapy drugs, targeted therapy, immunotherapy, or palliative care medications. The specific medications prescribed depend on factors like the stage of cancer, genetic mutations, overall health, and individualized treatment plans. It's important to note that treatment plans are personalized, and medications are prescribed based on a patient's specific condition. Consulting with healthcare professionals will provide accurate information about medications and their role in treatment."

        # Provide information about curability
    if any(token in ['cure', 'curable'] for token in user_tokens):
        return "The potential for cure in lung tumor cancer depends on various factors, including the stage at diagnosis, the presence of metastasis, the type of cancer, and individual characteristics. Early detection and treatment increase the chances of a positive outcome. In cases where the cancer is localized and hasn't spread significantly, curative treatment options such as surgery, radiation therapy, or a combination of treatments may be considered. However, it's important to note that each case is unique, and prognosis can vary. Healthcare professionals can provide more detailed information based on individual circumstances."

        # Provide information about malignant tumors
    if any(token in ['malignant', 'malignancy'] for token in user_tokens):
        return "Malignant tumors are cancerous growths that can invade nearby tissues and spread to other parts of the body. In the context of lung tumor cancer, malignant tumors refer to cancer cells that originate in the lungs and have the potential to metastasize. The treatment approach for malignant lung tumor cancer depends on various factors, including the stage of cancer, the presence of metastasis, and individual patient characteristics."

        # Provide information about benign tumors
    if any(token in ['benign'] for token in user_tokens):
        return "Benign tumors are non-cancerous growths that do not invade nearby tissues or spread to other parts of the body. In the context of lung tumor cancer, benign tumors refer to non-cancerous abnormalities in lung tissues. Unlike malignant tumors, benign lung tumors typically do not require aggressive treatment, unless they cause symptoms or interfere with normal lung function."

        # Provide information about diagnosis
    if any(token in ['diagnosis', 'diagnose'] for token in user_tokens):
        return "Diagnosing lung tumor cancer usually involves a combination of medical history evaluation, physical examination, imaging tests (such as CT scan or MRI), and biopsy. Medical professionals will consider symptoms, risk factors, and imaging findings to determine the need for a biopsy, which involves obtaining a tissue sample for laboratory analysis. The biopsy results help confirm the presence of lung tumor cancer and provide additional information about the specific type and characteristics of the cancer."

        # Provide information about CT scan
    if any(token in ['ct', 'scan'] for token in user_tokens):
        return "A CT (computed tomography) scan is a common imaging test used in the diagnosis and monitoring of lung tumor cancer. It uses a combination of X-rays and computer technology to create detailed cross-sectional images of the lungs. CT scans can help identify the presence of tumors, determine their size and location, and assess the extent of cancer spread. They are valuable tools in the initial diagnosis, staging, and ongoing monitoring of lung tumor cancer."

        # Provide information about symptoms
    if any(token in ['symptoms'] for token in user_tokens):
        return "Symptoms of lung tumor cancer can vary depending on the stage and location of the tumor. Common symptoms may include persistent cough, chest pain, shortness of breath, coughing up blood, fatigue, unexplained weight loss, recurrent respiratory infections, and hoarseness. However, it's important to note that some individuals with lung tumor cancer may not experience noticeable symptoms, particularly in the early stages. If you have concerns about symptoms or potential risk factors, it's advisable to consult with healthcare professionals for further evaluation."

        # Provide information about expenses
    if any(token in ['expenses', 'costs', 'financial'] for token in user_tokens):
        return "The expenses associated with lung tumor cancer can vary depending on various factors, including the type and stage of cancer, treatment approach, healthcare facility, geographic location, insurance coverage, and individual circumstances. The costs may include diagnostic tests, consultations, treatment procedures (such as surgery, chemotherapy, radiation therapy), medications, follow-up appointments, and supportive care services. It's advisable to discuss the financial aspects with healthcare professionals and insurance providers to understand the potential costs and explore available resources for financial assistance or support."

        # Provide information about treatment duration
    if any(token in ['time', 'duration', 'treatment'] for token in user_tokens):
        return "The duration of lung tumor cancer treatment can vary depending on factors such as the type and stage of cancer, the treatment approach, individual response to treatment, and overall health. Treatment plans may involve a combination of surgery, radiation therapy, chemotherapy, targeted therapy, immunotherapy, or palliative care. The treatment duration can range from a few weeks to several months or longer. It's important to discuss the treatment timeline and expectations with healthcare professionals who can provide more specific information based on the individual case."

        # Provide information about survival rates
    if any(token in ['survival', 'kill', 'ratio', 'prognosis'] for token in user_tokens):
        return "The survival rates and prognosis for lung tumor cancer depend on various factors, including the stage at diagnosis, the type and characteristics of cancer, individual response to treatment, overall health, and other individualized factors. It's important to note that survival rates are statistical estimates based on large populations and may not reflect the outcome for an individual patient. The healthcare team can provide more personalized information about prognosis and survival rates based on the specific case."
    if any(token in ['smok', 'smoking'] for token in user_tokens):
        return "Smoking is a significant risk factor for developing lung tumor cancer..."

    if any(token in ['cancer', 'death'] for token in user_tokens):
        return "Cancer is a life-threatening disease that can have high mortality rates..."

    if any(token in ['x-ray', 'radiation', 'imaging'] for token in user_tokens):
        return "X-ray imaging is commonly used in the diagnosis and monitoring of lung tumor cancer..."

    if any(token in ['cell', 'growth'] for token in user_tokens):
        return "Uncontrolled cell growth is a key characteristic of cancer..."

    if any(token in ['age', 'ageing'] for token in user_tokens):
        return "Age can be a risk factor for developing lung tumor cancer, with increased incidence among older individuals..."

    if any(token in ['minimal', 'minimum', 'youngest', 'age'] for token in user_tokens):
        return "There is no specific minimal age for developing lung tumor cancer, as it can affect individuals of all ages..."

    # Add more topic-specific responses here...

    # Add more topic-specific responses here...

    # Return a random response if no specific topic is identified
    responses = [
        "I'm sorry, but I couldn't understand your question...",
        "I'm sorry, I don't have information on that specific topic...",
        "I'm here to provide information about lung tumor cancer. If you have any specific questions, feel free to ask...",
        "Could you please provide more details or rephrase your question? I'm here to assist you with information about lung tumor cancer..."
    ]
    return random.choice(responses)

# Generate multiple responses
def generate_responses(user_input, num_responses=3):
    responses = []
    for _ in range(num_responses):
        response = process_user_input(user_input)
        responses.append(response)
    return responses

# Chat function
def chat(user_input):
    user_input = user_input.strip()
    if user_input.lower() == 'bye':
        return "Goodbye! Take care."
    else:
        responses = generate_responses(user_input, num_responses=1)
        return responses

# Main function
def main():
    print("DoctorBot: Hello! I'm here to provide information about lung tumor cancer...")
    print("DoctorBot: Feel free to ask me any questions you have. If you want to exit, just type 'bye'.")

    while True:
        user_input = input("You: ")
        bot_responses = chat(user_input)
        for bot_response in bot_responses:
            print("DoctorBot:", bot_response)

if __name__ == '__main__':
    main()
