from urllib import request

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.sites import requests
from django.core.checks import messages
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
import json
from django.shortcuts import render, redirect
import requests as req
from django.views.decorators.csrf import csrf_exempt

from tensorflow import keras
from keras.models import load_model
import numpy as np
import cv2


# Create your views here.
def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def service(request):
    return render(request, 'service.html')


def contact(request):
    return render(request, 'contact.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass1')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'patient.html', {'fname': username})
        else:
            return HttpResponse('Invalid username or password.')
    else:
        return render(request, 'sign-in.html')

def signup(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')

        username = request.POST.get('username')

        email = request.POST.get('email')
        phone = request.POST.get('phone')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if User.objects.filter(username=username):
            return HttpResponse(" USER ALRAEDY EXIST TRY AGAIN")
        if User.objects.filter(email=email).exists():
            return HttpResponse(" EMAIL ALREADY EXIST M TRY AGAIN")

        if pass1 != pass2:
            return HttpResponse(" PASSWORD NOT MATCH TRY AGAIN")

        myuser = User.objects.create_user(username, email, pass1)

        myuser.save()
        return HttpResponse(" account created successfully!")
    return render(request, 'sign up.html')


def forgetpassword(request):
    return render(request, 'forget.html')


def data_processing(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('my_file', None)
        model = load_model('lungs_tumor_model.h5')

        if not uploaded_file:
            return HttpResponse('No file uploaded!')

        # Preprocess the image (resize, normalize, etc.)
        img = preprocess_image(uploaded_file)

        # Predict the class of the image
        prediction = model.predict(img)
        class_names = ['benign', 'malignant', 'normal']
        predicted_class = class_names[prediction.argmax()]

        # Render the result page with the predicted class
        return render(request, 'result.html', {'predicted_class': predicted_class})

    else:
        return HttpResponse('Invalid request method')


def preprocess_image(file):
    # Load the image using OpenCV
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_GRAYSCALE)
    print(img.shape)


    IMG_SIZE = 256
    img_resized = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    print(img_resized.shape)

    # Normalize the pixel values to be between 0 and 1
    img_normalized = img_resized / 255.0

    # Add an extra dimension for the channel (required by the model)
    img_processed = np.expand_dims(img_normalized, axis=-1)
    img_processed = np.expand_dims(img_processed, axis=0)

    return img_processed

from django.shortcuts import render
from django.http import JsonResponse
import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Set up stopwords
stop_words = set(stopwords.words('english'))

def process_chat(request):
    if request.method == 'POST':
        user_input = request.POST.get('user-input')
        print(user_input)

        # Check if user input is None
        if user_input is None:
            return JsonResponse({'error': 'No user input received'})

        # Preprocess user input
        tokens = nltk.word_tokenize(user_input.lower())
        user_tokens = [token for token in tokens if token.isalpha() and token not in stop_words]
        print("User Tokens:", user_tokens)  # Print the user tokens for debugging purposes

        # Check if the user tokens are correctly generated
        if not user_tokens:
            response = "User tokens not generated properly"
        elif any(token in ['diet', 'nutrition'] for token in user_tokens):
            response = "Maintaining a healthy diet is essential during lung tumor cancer treatment."
        elif any(token in ['causes', 'benign', 'malignant'] for token in user_tokens):
            response = "Benign tumors are non-cancerous growths that do not invade nearby tissues or spread to other parts of the body. They are usually not life-threatening. On the other hand, malignant tumors are cancerous growths that can invade nearby tissues and spread to other parts of the body. They have the potential to be life-threatening if not treated."

        elif any(token in ['affects'] for token in user_tokens):
            response = "The effects of tumors depend on their location, size, and whether they are benign or malignant. Benign tumors generally cause fewer symptoms and have a lower risk of complications. Malignant tumors can cause various symptoms depending on the affected organ or tissue, such as pain, changes in organ function, weight loss, fatigue, and more."

        elif any(token in ['diagnose', 'how'] for token in user_tokens):
            response = "The diagnosis of tumors involves various methods, including medical history evaluation, physical examination, imaging tests (such as X-rays, CT scans, MRI scans), laboratory tests (such as blood tests, biopsy), and sometimes genetic testing. These diagnostic procedures help healthcare professionals determine the presence, type, location, and characteristics of the tumor."

        elif any(token in ['symptoms'] for token in user_tokens):
            response = "The symptoms of tumors can vary depending on the type, location, and size. Common symptoms may include pain, swelling, lumps, changes in bowel or bladder habits, unexplained weight loss, fatigue, changes in skin appearance, persistent cough, difficulty swallowing, and more. However, it's important to note that some tumors may not cause noticeable symptoms in the early stages."

        elif any(token in ['price'] for token in user_tokens):
            response = "The price of treating tumors, whether benign or malignant, can vary depending on various factors such as the type of tumor, stage, location, treatment approach, and healthcare system. The cost can include diagnostic tests, surgery, radiation therapy, chemotherapy, targeted therapy, immunotherapy, and follow-up care. The specific treatment and cost details can be discussed with a healthcare provider or medical specialist."

        elif any(token in ['cure'] for token in user_tokens):
            response = "Curing tumors, especially malignant ones, depends on several factors such as the type of tumor, stage, location, and individual patient characteristics. Treatment approaches for tumors can include surgery, radiation therapy, chemotherapy, targeted therapy, immunotherapy, and other specialized treatments. The goal of treatment is to remove or destroy the tumor cells and achieve long-term remission or cure. The specific treatment plan should be discussed with a healthcare provider or medical specialist."

        elif any(token in ['treatment'] for token in user_tokens):
            response = "Treatments for tumors can vary depending on the type, location, and stage. Common treatment options include surgery, radiation therapy, chemotherapy, targeted therapy, immunotherapy, and palliative care. The choice of treatment depends on factors such as tumor characteristics, patient's overall health, and individual preferences. A healthcare provider or medical specialist can provide a tailored treatment plan based on the specific tumor and patient's needs."

        elif any(token in ['medicine'] for token in user_tokens):
            response = "There are various medicines used in the treatment of tumors, including chemotherapy drugs, targeted therapy drugs, immunotherapy drugs, hormone therapy drugs, and supportive medications. The specific medicine prescribed depends on the type of tumor, stage, and individual patient factors. Medications may be used alone or in combination with other treatment modalities. It's important to consult with a healthcare provider or medical specialist to determine the appropriate medicines for tumor treatment."

        elif any(token in ['smoking', 'quit', 'cigarettes'] for token in user_tokens):
            response = "Smoking is a significant risk factor for developing lung tumor cancer. If you are thinking about quitting smoking, there are many resources available to help you. You can talk to your doctor, a smoking cessation counselor, or a support group. There are also many medications that can help you quit smoking."
        elif any(token in ['cancer'] for token in user_tokens):
            response = "Cancer is a complex disease characterized by the uncontrolled growth of abnormal cells. There are many different types of cancer, and each type is treated differently. If you have been diagnosed with cancer, it is important to talk to your doctor about your treatment options. There are many resources available to help you, including the American Cancer Society and the National Cancer Institute."
        else:
            response = random.choice([
                "I'm sorry, but I couldn't understand your question...",
                "I'm sorry, I don't have information on that specific topic...",
                "I'm here to provide information about lung tumor cancer. If you have any specific questions, feel free to ask...",
                "Could you please provide more details or rephrase your question? I'm here to assist you with information about lung tumor cancer..."
            ])

        return JsonResponse({'response': response})

    else:
        return JsonResponse({'error': 'Invalid request method'})



def render_chat(request):
    return render(request, 'chat.html')