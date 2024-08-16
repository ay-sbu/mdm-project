from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    return render(request, 'index.html')

def show_firebase_js(request):
    data = '''
    // Import the functions you need from the SDKs you need
        import { initializeApp } from "https://www.gstatic.com/firebasejs/10.13.0/firebase-app.js";
        import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.13.0/firebase-analytics.js";
        // TODO: Add SDKs for Firebase products that you want to use
        // https://firebase.google.com/docs/web/setup#available-libraries
      
        // Your web app's Firebase configuration
        // For Firebase JS SDK v7.20.0 and later, measurementId is optional
        const firebaseConfig = {
          apiKey: "AIzaSyAelj0_dJWBx0JQUatpd2fvZSxH4KjwH98",
          authDomain: "mdm-project-4e5b6.firebaseapp.com",
          projectId: "mdm-project-4e5b6",
          storageBucket: "mdm-project-4e5b6.appspot.com",
          messagingSenderId: "984723582484",
          appId: "1:984723582484:web:ff332bcf3795e75c510101",
          measurementId: "G-QJY3J9ELE1"
        };
      
        // Initialize Firebase
        const app = initializeApp(firebaseConfig);
        const analytics = getAnalytics(app);
    '''
    
    return HttpResponse(data, content_type='text/javascript')

def notification_page_view(request):
    return render(request, "notification_page.html")
