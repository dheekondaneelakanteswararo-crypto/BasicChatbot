"""
=========================================================
responses.py

Contains all chatbot responses and keyword matching.
=========================================================
"""

import random
from datetime import datetime
from calculator import calculate


greetings = [
    "👋 Hello! Nice to meet you.",
    "Hi! How can I help you today?",
    "Welcome! Hope you're having a great day.",
    "Hello there 😊",
    "Hey! What's up?"
]

happy_responses = [
    "😊 That's wonderful to hear!",
    "Keep smiling and stay positive!",
    "I'm glad you're happy!"
]

sad_responses = [
    "😔 I'm sorry you're feeling that way.",
    "Things will get better. Keep believing in yourself.",
    "Take a short break and don't forget to smile."
]

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why was Python so calm? Because it didn't have too many exceptions.",
    "A SQL query walks into a bar and joins two tables."
]

facts = [
    "Python was created by Guido van Rossum in 1991.",
    "The first computer bug was an actual moth.",
    "Python is one of the world's most popular programming languages.",
    "AI stands for Artificial Intelligence."
]

motivation = [
    "Success is the sum of small efforts repeated every day.",
    "Never stop learning.",
    "Believe in yourself and all that you are.",
    "Your future is created by what you do today.",
    "Consistency beats motivation."
]


def get_response(message):

    message = message.lower().strip()

    # -----------------------------
    # Greetings
    # -----------------------------

    if any(word in message for word in ["hello", "hi", "hey"]):
        return random.choice(greetings)

    elif "good morning" in message:
        return "🌞 Good Morning! Have a productive day."

    elif "good afternoon" in message:
        return "☀️ Good Afternoon!"

    elif "good evening" in message:
        return "🌙 Good Evening!"

    # -----------------------------
    # Feelings
    # -----------------------------

    elif "happy" in message:
        return random.choice(happy_responses)

    elif "sad" in message:
        return random.choice(sad_responses)

    # -----------------------------
    # Programming
    # -----------------------------

    elif "python" in message:
        return (
            "Python is a high-level programming language.\n"
            "It is simple, powerful and widely used for AI,\n"
            "Machine Learning, Automation and Web Development."
        )

    elif "java" in message:
        return (
            "Java is an Object-Oriented Programming language "
            "used for Enterprise and Android Development."
        )

    elif "oop" in message:
        return (
            "OOP stands for Object-Oriented Programming.\n"
            "Main concepts:\n"
            "• Class\n"
            "• Object\n"
            "• Inheritance\n"
            "• Polymorphism\n"
            "• Encapsulation\n"
            "• Abstraction"
        )

    elif "ai" in message:
        return (
            "Artificial Intelligence enables computers to "
            "learn, reason and solve problems like humans."
        )

    elif "machine learning" in message:
        return (
            "Machine Learning is a branch of AI where "
            "computers learn from data."
        )

    # -----------------------------
    # Personal
    # -----------------------------

    elif "your name" in message:
        return "I'm CodeAlpha AI Assistant."

    elif "who created you" in message:
        return (
            "I was developed as part of the "
            "CodeAlpha Python Internship."
        )

    elif "how are you" in message:
        return "I'm doing great! Thanks for asking 😊"

    elif "thank" in message:
        return "You're welcome! Happy Coding ❤️"

    # -----------------------------
    # Date Time
    # -----------------------------

    elif "time" in message:
        return datetime.now().strftime(
            "Current Time : %I:%M:%S %p"
        )

    elif "date" in message:
        return datetime.now().strftime(
            "Today's Date : %d-%m-%Y"
        )

    # -----------------------------
    # Fun
    # -----------------------------

    elif "joke" in message:
        return random.choice(jokes)

    elif "fact" in message:
        return random.choice(facts)

    elif "motivate" in message:
        return random.choice(motivation)

    # -----------------------------
    # Calculator
    # -----------------------------

    elif message.startswith("calculate"):
        expression = message.replace("calculate", "").strip()

        if expression == "":
            return "Example: calculate 25 + 30"

        return calculate(expression)

    # -----------------------------
    # Help
    # -----------------------------

    elif "help" in message:

        return (
            "\nAvailable Commands\n\n"
            "hello\n"
            "how are you\n"
            "python\n"
            "java\n"
            "oop\n"
            "ai\n"
            "machine learning\n"
            "date\n"
            "time\n"
            "fact\n"
            "joke\n"
            "motivate me\n"
            "calculate 20+30\n"
            "bye"
        )

    # -----------------------------
    # Exit
    # -----------------------------

    elif message in ["bye", "exit", "quit"]:
        return "👋 Goodbye! Have a wonderful day."
        # -----------------------------
    # Sports
    # -----------------------------
    elif "cricket" in message:
        return "🏏 Cricket is one of the most popular sports in the world."

    elif "football" in message or "soccer" in message:
        return "⚽ Football is played by millions of people across the globe."

    elif "virat kohli" in message:
        return "Virat Kohli is one of India's greatest batsmen."

    elif "ms dhoni" in message or "dhoni" in message:
        return "MS Dhoni is known as Captain Cool."

    # -----------------------------
    # Movies
    # -----------------------------
    elif "movie" in message:
        return random.choice([
            "🎬 I enjoy science-fiction movies.",
            "Interstellar is an amazing movie.",
            "The Dark Knight is highly recommended.",
            "3 Idiots is a great inspirational movie."
        ])

    elif "avengers" in message:
        return "🦸 Avengers is one of Marvel's most successful movie series."

    elif "iron man" in message:
        return "Iron Man is one of the founders of the Avengers."

    # -----------------------------
    # Coding
    # -----------------------------
    elif "c language" in message:
        return "C is a procedural programming language developed by Dennis Ritchie."

    elif "c++" in message:
        return "C++ supports object-oriented programming."

    elif "html" in message:
        return "HTML is used to structure web pages."

    elif "css" in message:
        return "CSS is used to style web pages."

    elif "javascript" in message:
        return "JavaScript makes web pages interactive."

    elif "sql" in message:
        return "SQL is used to manage relational databases."

    elif "github" in message:
        return "GitHub is a platform for version control and collaboration."

    elif "git" == message:
        return "Git is a distributed version control system."

    # -----------------------------
    # AI & ML
    # -----------------------------
    elif "chatgpt" in message:
        return "ChatGPT is an AI conversational assistant built using large language models."

    elif "deep learning" in message:
        return "Deep Learning uses neural networks with multiple layers."

    elif "neural network" in message:
        return "Neural Networks are inspired by the human brain."

    elif "data science" in message:
        return "Data Science combines statistics, programming, and machine learning."

    # -----------------------------
    # Interview
    # -----------------------------
    elif "interview" in message:
        return random.choice([
            "Prepare your basics before attending interviews.",
            "Practice coding daily.",
            "Confidence is the key to success."
        ])

    elif "tell me about yourself" in message:
        return (
            "Start with your education, skills, projects, "
            "and career goals."
        )

    elif "strength" in message:
        return "One good strength is being a quick learner."

    elif "weakness" in message:
        return "Mention a real weakness and explain how you are improving it."

    # -----------------------------
    # Weather
    # -----------------------------
    elif "weather" in message:
        return (
            "☁️ I can't check live weather, "
            "but I hope it's pleasant where you are."
        )

    elif "rain" in message:
        return "🌧 Don't forget your umbrella."

    elif "summer" in message:
        return "☀️ Stay hydrated during summer."

    # -----------------------------
    # Education
    # -----------------------------
    elif "study" in message:
        return "📚 Consistent study is better than last-minute preparation."

    elif "exam" in message:
        return "Best of luck for your exams! Practice regularly."

    elif "college" in message:
        return "College is a great place to learn and build your skills."

    elif "project" in message:
        return "Building projects is one of the best ways to improve programming skills."

    # -----------------------------
    # Motivation
    # -----------------------------
    elif "success" in message:
        return "🏆 Success comes from consistency and continuous learning."

    elif "failure" in message:
        return "Every failure is an opportunity to learn."

    elif "goal" in message:
        return "Set clear goals and work towards them every day."

    # -----------------------------
    # Technology
    # -----------------------------
    elif "computer" in message:
        return "A computer processes data into useful information."

    elif "internet" in message:
        return "The Internet connects millions of devices worldwide."

    elif "cloud" in message:
        return "Cloud Computing allows you to access computing resources online."

    # -----------------------------
    # Personal Questions
    # -----------------------------
    elif "who are you" in message:
        return "I'm your Rule-Based AI Assistant."

    elif "are you human" in message:
        return "😄 No, I'm a Python chatbot."

    elif "can you help me" in message:
        return "Absolutely! Type 'help' to see what I can do."

    elif "thank you" in message:
        return "😊 You're most welcome!"

    elif "good night" in message:
        return "🌙 Good night! Sleep well."

    elif "goodbye" in message:
        return "👋 Goodbye! Have a fantastic day."

    # -----------------------------
    # Fun Commands
    # -----------------------------
    elif "flip coin" in message:
        return random.choice(["Heads 🪙", "Tails 🪙"])

    elif "roll dice" in message:
        return f"🎲 You rolled {random.randint(1,6)}"

    elif "color" in message:
        return random.choice([
            "Blue",
            "Green",
            "Black",
            "White",
            "Purple"
        ])

    elif "number" in message:
        return f"My lucky number today is {random.randint(1,100)}"

    # -----------------------------
    # Unknown with Suggestions
    # -----------------------------
    elif "?" in message:
        return (
            "🤔 I'm not sure about that.\n\n"
            "Try asking about:\n"
            "• Python\n"
            "• Java\n"
            "• AI\n"
            "• Time\n"
            "• Date\n"
            "• Joke\n"
            "• Motivation\n"
            "• Cricket\n"
            "• Movie\n"
            "• Calculator"
        )
    # -----------------------------
    # Unknown
    # -----------------------------
 # =====================================================
# GREETINGS
# =====================================================

if any(word in message for word in [
    "hello",
    "hi",
    "hey",
    "hii",
    "heyy",
    "hola"
]):
    return random.choice([
        "👋 Hello! Nice to meet you.",
        "Hi! 😊 How can I help you today?",
        "Hey! Welcome back.",
        "Hello there! Hope you're having a wonderful day.",
        "👋 Greetings! What would you like to know?"
    ])

elif "good morning" in message:
    return random.choice([
        "🌞 Good Morning! Have a productive day.",
        "Good Morning! Keep smiling 😊",
        "Morning! Ready to learn something new?"
    ])

elif "good afternoon" in message:
    return random.choice([
        "☀️ Good Afternoon!",
        "Hope your afternoon is going well!",
        "Have a fantastic afternoon!"
    ])

elif "good evening" in message:
    return random.choice([
        "🌙 Good Evening!",
        "Hope you had a wonderful day!",
        "Good Evening! How may I assist you?"
    ])

elif "good night" in message:
    return random.choice([
        "🌙 Good Night!",
        "Sweet dreams 😊",
        "Sleep well and recharge for tomorrow!"
    ])

# =====================================================
# HOW ARE YOU
# =====================================================

elif "how are you" in message:

    return random.choice([
        "😊 I'm doing great. Thanks for asking!",
        "I'm functioning perfectly! What about you?",
        "Everything is running smoothly. How can I help you today?",
        "I'm always ready to assist you!"
    ])

# =====================================================
# USER FEELINGS
# =====================================================

elif any(word in message for word in [
    "happy",
    "excited",
    "great",
    "awesome"
]):
    return random.choice([
        "😊 That's wonderful!",
        "I'm happy to hear that.",
        "Keep smiling!",
        "Great! Positive energy is always welcome."
    ])

elif any(word in message for word in [
    "sad",
    "depressed",
    "upset",
    "cry"
]):
    return random.choice([
        "😔 I'm sorry you're feeling that way.",
        "Remember, tough times don't last forever.",
        "Take a deep breath. Better days are ahead.",
        "You're stronger than you think."
    ])

elif any(word in message for word in [
    "angry",
    "mad",
    "frustrated"
]):
    return random.choice([
        "Take a short break and relax.",
        "Sometimes a little rest helps.",
        "Try listening to your favorite music.",
        "Stay calm. Everything will be okay."
    ])

elif any(word in message for word in [
    "bored",
    "boring"
]):
    return random.choice([
        "Maybe learn a new Python concept today!",
        "How about solving a coding problem?",
        "Want to hear a joke? Type 'joke'.",
        "Let's make today productive!"
    ])

# =====================================================
# THANK YOU
# =====================================================

elif any(word in message for word in [
    "thanks",
    "thank you",
    "thx"
]):
    return random.choice([
        "You're welcome! 😊",
        "Happy to help!",
        "Anytime!",
        "Glad I could help."
    ])

# =====================================================
# COMPLIMENTS
# =====================================================

elif any(word in message for word in [
    "good bot",
    "nice",
    "awesome",
    "amazing",
    "excellent"
]):
    return random.choice([
        "😊 Thank you so much!",
        "That means a lot!",
        "I'm happy you liked it.",
        "Thanks! I appreciate your feedback."
    ])

# =====================================================
# APOLOGY
# =====================================================

elif any(word in message for word in [
    "sorry",
    "my mistake"
]):
    return random.choice([
        "No worries 😊",
        "It's completely okay.",
        "Everyone makes mistakes.",
        "No problem at all!"
    ])

# =====================================================
# PERSONAL QUESTIONS
# =====================================================

elif "who are you" in message:
    return (
        "🤖 I'm CodeAlpha AI Assistant.\n"
        "A Rule-Based Chatbot built using Python."
    )

elif "your name" in message:
    return "My name is CodeAlpha AI Assistant."

elif "who created you" in message:
    return (
        "I was developed as a project for the "
        "CodeAlpha Python Programming Internship."
    )

elif "where are you from" in message:
    return (
        "I live inside this Python program 😊"
    )

elif "are you real" in message:
    return (
        "I'm not a human.\n"
        "I'm a Rule-Based AI Chatbot written in Python."
    )

elif "are you human" in message:
    return (
        "No 😊 I'm software created using Python."
    )

elif "what can you do" in message:
    return (
        "I can help you with:\n\n"
        "• Programming Questions\n"
        "• AI Concepts\n"
        "• Motivation\n"
        "• Jokes\n"
        "• Facts\n"
        "• Calculator\n"
        "• Date & Time\n"
        "• Career Guidance"
    )

# =====================================================
# SMALL TALK
# =====================================================

elif "what's up" in message or "whats up" in message:
    return random.choice([
        "Just helping people learn Python 😊",
        "Everything is going great!",
        "Ready to answer your questions."
    ])

elif "how is your day" in message:
    return (
        "Every day is a great day when I'm helping users 😊"
    )

elif "can we be friends" in message:
    return (
        "Of course! 😊 I'm always here to help."
    )

elif "i love you" in message:
    return (
        "❤️ Thank you! I'm happy to help you learn and grow."
    )

elif "do you know me" in message:
    return (
        "I know what you tell me during our conversation."
    )

elif "miss you" in message:
    return (
        "😊 I'm always here whenever you need me."
    )

# =====================================================
# GOODBYE
# =====================================================

elif any(word in message for word in [
    "bye",
    "goodbye",
    "see you",
    "exit",
    "quit"
]):
    return random.choice([
        "👋 Goodbye! Have a wonderful day.",
        "See you soon! Keep coding.",
        "Take care! Happy Learning.",
        "Goodbye 😊 Stay safe."
    ])
    # =====================================================
# PROGRAMMING LANGUAGES
# =====================================================

elif "python" in message:
    return random.choice([
        "🐍 Python is a high-level, interpreted programming language known for its simplicity and readability.",
        "Python is widely used in AI, Machine Learning, Data Science, Automation, and Web Development.",
        "Python supports multiple programming paradigms including Object-Oriented, Functional, and Procedural Programming."
    ])

elif "java" in message:
    return random.choice([
        "☕ Java is an Object-Oriented Programming language developed by Sun Microsystems (now Oracle).",
        "Java follows the principle: Write Once, Run Anywhere (WORA).",
        "Java is widely used for enterprise software, Android apps, and backend systems."
    ])

elif "c language" in message or message == "c":
    return random.choice([
        "C is a procedural programming language developed by Dennis Ritchie.",
        "C is considered the foundation for many modern programming languages.",
        "C provides low-level memory access and is widely used in system programming."
    ])

elif "c++" in message or "cpp" in message:
    return random.choice([
        "C++ extends C by adding Object-Oriented Programming features.",
        "C++ supports classes, objects, inheritance, polymorphism, and templates.",
        "C++ is commonly used in game development and high-performance applications."
    ])

# =====================================================
# WEB DEVELOPMENT
# =====================================================

elif "html" in message:
    return (
        "🌐 HTML (HyperText Markup Language) is used to create the structure of web pages."
    )

elif "css" in message:
    return (
        "🎨 CSS (Cascading Style Sheets) is used to style HTML elements."
    )

elif "javascript" in message or message == "js":
    return (
        "⚡ JavaScript makes web pages interactive and dynamic."
    )

elif "react" in message:
    return (
        "⚛ React is a JavaScript library used to build modern user interfaces."
    )

elif "node" in message:
    return (
        "🟢 Node.js allows JavaScript to run outside the browser."
    )

# =====================================================
# DATABASE
# =====================================================

elif "sql" in message:
    return (
        "SQL (Structured Query Language) is used to manage relational databases."
    )

elif "mysql" in message:
    return (
        "MySQL is one of the most popular relational database management systems."
    )

elif "mongodb" in message:
    return (
        "MongoDB is a NoSQL database that stores data in JSON-like documents."
    )

# =====================================================
# GIT
# =====================================================

elif message == "git":
    return (
        "Git is a distributed version control system used for tracking code changes."
    )

elif "github" in message:
    return (
        "GitHub is a cloud platform for hosting Git repositories and collaborating on projects."
    )

elif "git clone" in message:
    return (
        "git clone <repository_url>\n"
        "downloads a remote repository to your computer."
    )

elif "git add" in message:
    return (
        "git add .\n"
        "adds all modified files to the staging area."
    )

elif "git commit" in message:
    return (
        'git commit -m "message"\n'
        "creates a snapshot of your staged changes."
    )

elif "git push" in message:
    return (
        "git push origin main\n"
        "uploads your local commits to GitHub."
    )

# =====================================================
# OOP
# =====================================================

elif "oop" in message or "object oriented programming" in message:
    return (
        "Object-Oriented Programming (OOP) is based on:\n\n"
        "• Class\n"
        "• Object\n"
        "• Inheritance\n"
        "• Encapsulation\n"
        "• Polymorphism\n"
        "• Abstraction"
    )

elif "class" in message:
    return (
        "A Class is a blueprint used to create objects."
    )

elif "object" in message:
    return (
        "An Object is an instance of a class."
    )

elif "inheritance" in message:
    return (
        "Inheritance allows one class to inherit properties and methods from another class."
    )

elif "polymorphism" in message:
    return (
        "Polymorphism allows one interface to represent different implementations."
    )

elif "encapsulation" in message:
    return (
        "Encapsulation hides internal data and exposes only required functionality."
    )

elif "abstraction" in message:
    return (
        "Abstraction hides implementation details and shows only essential features."
    )

# =====================================================
# DSA
# =====================================================

elif "array" in message:
    return (
        "An Array stores multiple elements of the same data type in contiguous memory."
    )

elif "linked list" in message:
    return (
        "A Linked List stores nodes connected using pointers."
    )

elif "stack" in message:
    return (
        "Stack follows the LIFO (Last In First Out) principle."
    )

elif "queue" in message:
    return (
        "Queue follows the FIFO (First In First Out) principle."
    )

elif "tree" in message:
    return (
        "A Tree is a hierarchical data structure consisting of nodes."
    )

elif "graph" in message:
    return (
        "A Graph consists of vertices (nodes) connected by edges."
    )

elif "binary search" in message:
    return (
        "Binary Search works on sorted arrays with O(log n) time complexity."
    )

elif "sorting" in message:
    return (
        "Popular sorting algorithms include Bubble, Selection, Merge, Quick, and Heap Sort."
    )

# =====================================================
# PYTHON LIBRARIES
# =====================================================

elif "numpy" in message:
    return (
        "NumPy provides fast numerical computations using multidimensional arrays."
    )

elif "pandas" in message:
    return (
        "Pandas is a powerful Python library for data analysis and manipulation."
    )

elif "matplotlib" in message:
    return (
        "Matplotlib is used for creating charts and data visualizations."
    )

elif "flask" in message:
    return (
        "Flask is a lightweight Python web framework used for building APIs and web applications."
    )

elif "django" in message:
    return (
        "Django is a high-level Python web framework that follows the MTV architecture."
    )

# =====================================================
# API
# =====================================================

elif "api" in message:
    return (
        "API (Application Programming Interface) allows different software applications to communicate."
    )

elif "json" in message:
    return (
        "JSON (JavaScript Object Notation) is a lightweight format used to exchange data."
    )

# =====================================================
# DEBUGGING
# =====================================================

elif "error" in message:
    return (
        "Errors help identify issues in a program. Read the traceback carefully to locate the problem."
    )

elif "bug" in message:
    return (
        "🐞 A bug is an error or flaw in a program that causes unexpected behavior."
    )

# =====================================================
# CAREER
# =====================================================

elif "internship" in message:
    return (
        "Internships help you gain practical experience, improve your resume, and build industry skills."
    )

elif "resume" in message:
    return (
        "A good resume should include your education, skills, projects, certifications, and achievements."
    )

elif "project" in message:
    return (
        "Projects demonstrate your practical knowledge. Build real-world applications and upload them to GitHub."
    )

elif "interview" in message:
    return (
        "Practice DSA, OOP, DBMS, Operating Systems, and Computer Networks for technical interviews."
    )
    # =====================================================
# ARTIFICIAL INTELLIGENCE
# =====================================================

elif "artificial intelligence" in message or message == "ai":
    return random.choice([
        "🤖 Artificial Intelligence (AI) enables computers to simulate human intelligence and decision-making.",
        "AI is used in chatbots, self-driving cars, recommendation systems, and healthcare.",
        "Artificial Intelligence combines algorithms, data, and computing power to solve complex problems."
    ])

elif "machine learning" in message or message == "ml":
    return random.choice([
        "Machine Learning is a branch of AI where computers learn patterns from data.",
        "ML algorithms improve their performance by learning from experience instead of explicit programming.",
        "Common ML algorithms include Linear Regression, Decision Trees, SVM, and Random Forest."
    ])

elif "deep learning" in message:
    return (
        "🧠 Deep Learning is a subset of Machine Learning that uses multi-layer neural networks."
    )

elif "neural network" in message:
    return (
        "Neural Networks are inspired by the human brain and are used for image recognition, NLP, and speech processing."
    )

elif "computer vision" in message:
    return (
        "👁 Computer Vision enables computers to understand and analyze images and videos."
    )

elif "natural language processing" in message or "nlp" in message:
    return (
        "💬 NLP helps computers understand and generate human language."
    )

elif "large language model" in message or "llm" in message:
    return (
        "Large Language Models (LLMs) are AI models trained on massive text datasets to understand and generate language."
    )

# =====================================================
# DATA SCIENCE
# =====================================================

elif "data science" in message:
    return (
        "📊 Data Science combines statistics, programming, machine learning, and visualization to extract insights from data."
    )

elif "data analyst" in message:
    return (
        "A Data Analyst collects, cleans, analyzes, and visualizes data to support decision-making."
    )

elif "data engineer" in message:
    return (
        "A Data Engineer builds and manages data pipelines, databases, and infrastructure."
    )

elif "big data" in message:
    return (
        "Big Data refers to extremely large datasets processed using technologies like Hadoop and Spark."
    )

# =====================================================
# CLOUD COMPUTING
# =====================================================

elif "cloud computing" in message or message == "cloud":
    return (
        "☁ Cloud Computing provides computing resources like servers, storage, and databases over the internet."
    )

elif "aws" in message:
    return (
        "Amazon Web Services (AWS) is the world's leading cloud computing platform."
    )

elif "azure" in message:
    return (
        "Microsoft Azure offers cloud services for computing, storage, networking, and AI."
    )

elif "google cloud" in message or "gcp" in message:
    return (
        "Google Cloud Platform (GCP) provides scalable cloud infrastructure and AI services."
    )

# =====================================================
# CYBER SECURITY
# =====================================================

elif "cyber security" in message or "cybersecurity" in message:
    return (
        "🔐 Cybersecurity protects systems, networks, and data from cyber attacks."
    )

elif "ethical hacking" in message:
    return (
        "Ethical Hackers legally identify vulnerabilities to improve system security."
    )

elif "phishing" in message:
    return (
        "🎣 Phishing is a cyber attack where attackers trick users into revealing sensitive information."
    )

elif "malware" in message:
    return (
        "🦠 Malware is malicious software such as viruses, ransomware, worms, and spyware."
    )

elif "virus" in message:
    return (
        "A Computer Virus is malicious software that spreads by infecting files or programs."
    )

# =====================================================
# OPERATING SYSTEM
# =====================================================

elif "operating system" in message or message == "os":
    return (
        "🖥 An Operating System manages computer hardware and software resources."
    )

elif "linux" in message:
    return (
        "Linux is a free and open-source operating system widely used on servers."
    )

elif "windows" in message:
    return (
        "Microsoft Windows is one of the most popular desktop operating systems."
    )

# =====================================================
# NETWORKING
# =====================================================

elif "computer network" in message or "networking" in message:
    return (
        "🌐 Computer Networking allows devices to communicate and share resources."
    )

elif "ip address" in message:
    return (
        "An IP Address uniquely identifies a device on a network."
    )

elif "http" in message:
    return (
        "HTTP stands for HyperText Transfer Protocol and is used to transfer web pages."
    )

elif "https" in message:
    return (
        "HTTPS is the secure version of HTTP that encrypts communication using SSL/TLS."
    )

# =====================================================
# DATABASE THEORY
# =====================================================

elif "dbms" in message:
    return (
        "📂 DBMS (Database Management System) is software used to create, manage, and organize databases."
    )

elif "normalization" in message:
    return (
        "Normalization organizes database tables to reduce redundancy and improve data integrity."
    )

elif "primary key" in message:
    return (
        "A Primary Key uniquely identifies each record in a database table."
    )

elif "foreign key" in message:
    return (
        "A Foreign Key links one table with another by referencing the Primary Key."
    )

# =====================================================
# SOFTWARE ENGINEERING
# =====================================================

elif "software engineering" in message:
    return (
        "Software Engineering is the systematic approach to designing, developing, testing, and maintaining software."
    )

elif "agile" in message:
    return (
        "Agile is an iterative software development methodology focused on collaboration and continuous delivery."
    )

elif "scrum" in message:
    return (
        "Scrum is an Agile framework that organizes work into short iterations called sprints."
    )

elif "testing" in message:
    return (
        "Software Testing verifies that an application works correctly and meets requirements."
    )

# =====================================================
# CAREER GUIDANCE
# =====================================================

elif "software developer" in message:
    return (
        "A Software Developer designs, builds, tests, and maintains software applications."
    )

elif "full stack" in message:
    return (
        "A Full Stack Developer works with both frontend and backend technologies."
    )

elif "backend" in message:
    return (
        "Backend development focuses on servers, databases, and APIs."
    )

elif "frontend" in message:
    return (
        "Frontend development focuses on user interfaces using HTML, CSS, JavaScript, and frameworks like React."
    )

elif "roadmap" in message:
    return (
        "📚 Learning Roadmap:\n"
        "1. Programming Fundamentals\n"
        "2. Data Structures & Algorithms\n"
        "3. Git & GitHub\n"
        "4. Databases\n"
        "5. Web Development\n"
        "6. Projects\n"
        "7. Internship Preparation"
    )
    # =====================================================
# MOVIES
# =====================================================

elif "movie" in message or "movies" in message:
    return random.choice([
        "🎬 I enjoy science fiction movies.",
        "Interstellar is a fantastic sci-fi movie.",
        "3 Idiots is one of the best inspirational movies.",
        "The Dark Knight is a masterpiece.",
        "Watching movies is a great way to relax!"
    ])

elif "marvel" in message:
    return "🦸 Marvel is famous for superheroes like Iron Man, Spider-Man, Thor, and Captain America."

elif "avengers" in message:
    return "⚡ Avengers: Endgame is one of the highest-grossing movies ever."

elif "iron man" in message:
    return "❤️ Iron Man (Tony Stark) is one of Marvel's most loved superheroes."

elif "spiderman" in message:
    return "🕷 Spider-Man believes that 'With great power comes great responsibility.'"

elif "batman" in message:
    return "🦇 Batman protects Gotham City without any superpowers."

# =====================================================
# SPORTS
# =====================================================

elif "cricket" in message:
    return random.choice([
        "🏏 Cricket is one of the most popular sports in India.",
        "A cricket team has 11 players.",
        "The ICC organizes international cricket tournaments."
    ])

elif "virat kohli" in message:
    return "🇮🇳 Virat Kohli is regarded as one of the greatest modern batsmen."

elif "ms dhoni" in message or "dhoni" in message:
    return "🏆 MS Dhoni led India to the 2011 Cricket World Cup victory."

elif "football" in message:
    return "⚽ Football is the world's most popular sport."

elif "ronaldo" in message:
    return "🇵🇹 Cristiano Ronaldo is one of the greatest football players in history."

elif "messi" in message:
    return "🇦🇷 Lionel Messi won the FIFA World Cup with Argentina in 2022."

# =====================================================
# MUSIC
# =====================================================

elif "music" in message:
    return random.choice([
        "🎵 Music helps people relax and focus.",
        "Listening to music can improve your mood.",
        "Everyone has a different taste in music."
    ])

elif "song" in message:
    return "🎶 I don't play songs, but I love talking about music."

elif "favorite singer" in message:
    return "🎤 I don't have favorites, but many people enjoy Arijit Singh, Taylor Swift, and Ed Sheeran."

# =====================================================
# FOOD
# =====================================================

elif "food" in message:
    return random.choice([
        "🍕 Pizza is loved worldwide.",
        "🥗 Healthy food keeps your body energetic.",
        "🍎 Eating fruits daily is a good habit."
    ])

elif "pizza" in message:
    return "🍕 Pizza is one of the most popular fast foods."

elif "biryani" in message:
    return "🍛 Biryani is one of India's most loved dishes."

elif "coffee" in message:
    return "☕ Coffee helps many programmers stay awake while coding."

elif "tea" in message:
    return "🍵 Tea is one of the most consumed beverages in the world."

# =====================================================
# TRAVEL
# =====================================================

elif "travel" in message:
    return "✈ Traveling helps you experience new cultures and places."

elif "india" in message:
    return "🇮🇳 India is famous for its rich culture, history, and diversity."

elif "taj mahal" in message:
    return "🕌 The Taj Mahal is one of the Seven Wonders of the World."

elif "hyderabad" in message:
    return "🏙 Hyderabad is famous for Charminar and Hyderabadi Biryani."

# =====================================================
# BOOKS
# =====================================================

elif "book" in message:
    return random.choice([
        "📚 Reading books improves knowledge and vocabulary.",
        "Books are a great source of inspiration.",
        "Developing a reading habit is beneficial."
    ])

elif "python book" in message:
    return "📘 'Python Crash Course' is a great book for beginners."

# =====================================================
# HOBBIES
# =====================================================

elif "hobby" in message:
    return "🎨 Popular hobbies include reading, coding, painting, gaming, and music."

elif "gaming" in message:
    return "🎮 Gaming can be fun when balanced with studies and work."

elif "coding" in message:
    return "💻 Coding improves problem-solving and logical thinking."

# =====================================================
# GENERAL KNOWLEDGE
# =====================================================

elif "capital of india" in message:
    return "🇮🇳 New Delhi is the capital of India."

elif "largest planet" in message:
    return "🪐 Jupiter is the largest planet in our Solar System."

elif "fastest animal" in message:
    return "🐆 The Cheetah is the fastest land animal."

elif "largest ocean" in message:
    return "🌊 The Pacific Ocean is the largest ocean on Earth."

elif "national animal of india" in message:
    return "🐅 The Bengal Tiger is the national animal of India."

elif "national bird of india" in message:
    return "🦚 The Indian Peacock is the national bird of India."

# =====================================================
# TECHNOLOGY FACTS
# =====================================================

elif "computer" in message:
    return "💻 A computer processes data into useful information."

elif "internet" in message:
    return "🌐 The Internet connects billions of devices worldwide."

elif "wifi" in message:
    return "📶 Wi-Fi allows devices to connect wirelessly to the internet."

# =====================================================
# RANDOM FACTS
# =====================================================

elif "fact" in message:
    return random.choice([
        "🐙 Octopuses have three hearts.",
        "🍯 Honey never spoils.",
        "🌍 Earth revolves around the Sun.",
        "🧠 The human brain contains around 86 billion neurons.",
        "🐬 Dolphins sleep with one eye open.",
        "🦒 Giraffes have the same number of neck bones as humans."
    ])

# =====================================================
# JOKES
# =====================================================

elif "joke" in message:
    return random.choice([
        "😂 Why do programmers prefer dark mode? Because light attracts bugs!",
        "😂 Why was the computer cold? It left its Windows open.",
        "😂 Why do Java developers wear glasses? Because they don't C#.",
        "😂 Why did the programmer quit his job? Because he didn't get arrays."
    ])

# =====================================================
# QUOTES
# =====================================================

elif "quote" in message:
    return random.choice([
        "🌟 Success is the sum of small efforts repeated every day.",
        "🌟 Believe you can and you're halfway there.",
        "🌟 Dream big. Work hard. Stay humble.",
        "🌟 Consistency beats talent when talent doesn't work hard."
    ])
    # =====================================================
# CAREER GUIDANCE
# =====================================================

elif "career" in message:
    return random.choice([
        "🚀 Choose a career that matches your interests and continuously improve your skills.",
        "Success comes from learning, building projects, and staying consistent.",
        "Focus on problem-solving, communication, and practical experience."
    ])

elif "software engineer" in message:
    return (
        "💻 A Software Engineer designs, develops, tests, and maintains software applications."
    )

elif "software developer" in message:
    return (
        "A Software Developer writes code, fixes bugs, and develops software solutions."
    )

elif "full stack developer" in message:
    return (
        "🌐 Full Stack Developers work with both Frontend (HTML, CSS, JavaScript, React) "
        "and Backend (Python, Node.js, Java, Databases)."
    )

elif "frontend" in message:
    return (
        "Frontend Development focuses on user interfaces using HTML, CSS, JavaScript, and React."
    )

elif "backend" in message:
    return (
        "Backend Development handles servers, APIs, databases, and business logic."
    )

# =====================================================
# INTERNSHIP
# =====================================================

elif "internship" in message:
    return (
        "🎓 Internships provide practical experience, improve your resume, "
        "and help you understand industry workflows."
    )

elif "codealpha" in message:
    return (
        "CodeAlpha provides internships where students complete practical Python, "
        "Web Development, AI, and other technical projects."
    )

# =====================================================
# RESUME
# =====================================================

elif "resume" in message or "cv" in message:
    return (
        "📄 A professional resume should include:\n\n"
        "• Contact Information\n"
        "• Career Objective\n"
        "• Education\n"
        "• Technical Skills\n"
        "• Projects\n"
        "• Certifications\n"
        "• Internships\n"
        "• Achievements"
    )

# =====================================================
# PROJECTS
# =====================================================

elif "project" in message:
    return random.choice([
        "Projects demonstrate your practical programming skills.",
        "Upload projects to GitHub to build your portfolio.",
        "Build real-world applications instead of only small programs."
    ])

elif "github project" in message:
    return (
        "Push your projects to GitHub with a proper README, LICENSE, and screenshots."
    )

# =====================================================
# GITHUB
# =====================================================

elif "github profile" in message:
    return (
        "Maintain an active GitHub profile by uploading projects regularly."
    )

elif "github repository" in message:
    return (
        "Each project should have:\n"
        "• README.md\n"
        "• LICENSE\n"
        "• requirements.txt\n"
        "• Source Code\n"
        "• Screenshots"
    )

# =====================================================
# INTERVIEW PREPARATION
# =====================================================

elif "interview" in message:
    return (
        "🎯 Prepare these subjects:\n\n"
        "• Python\n"
        "• OOP\n"
        "• DBMS\n"
        "• Operating System\n"
        "• Computer Networks\n"
        "• Data Structures & Algorithms\n"
        "• SQL\n"
        "• Projects"
    )

elif "tell me about yourself" in message:
    return (
        "Introduce yourself with:\n\n"
        "• Name\n"
        "• Education\n"
        "• Technical Skills\n"
        "• Projects\n"
        "• Internship Experience\n"
        "• Career Goals"
    )

elif "strength" in message:
    return (
        "Example Strength:\n"
        "'I am a quick learner and enjoy solving programming problems.'"
    )

elif "weakness" in message:
    return (
        "Example Weakness:\n"
        "'Sometimes I focus too much on details, but I'm learning to manage my time better.'"
    )

elif "hr interview" in message:
    return (
        "HR interviews evaluate communication skills, confidence, teamwork, and attitude."
    )

elif "technical interview" in message:
    return (
        "Technical interviews focus on coding, algorithms, OOP, DBMS, OS, and projects."
    )

# =====================================================
# STUDY TIPS
# =====================================================

elif "study" in message:
    return random.choice([
        "📚 Study consistently instead of only before exams.",
        "Practice coding daily to improve your skills.",
        "Revise concepts regularly."
    ])

elif "exam" in message:
    return (
        "Best of luck for your exams! Practice previous papers and revise important topics."
    )

elif "time management" in message:
    return (
        "⏰ Divide your day into study sessions with short breaks for better productivity."
    )

elif "productivity" in message:
    return (
        "🚀 Avoid distractions, set daily goals, and complete one task at a time."
    )

# =====================================================
# CERTIFICATIONS
# =====================================================

elif "certificate" in message:
    return (
        "Certificates add value to your resume, especially when combined with practical projects."
    )

elif "linkedin" in message:
    return (
        "Create a professional LinkedIn profile and regularly share your projects, internships, and certifications."
    )

# =====================================================
# MOTIVATION
# =====================================================

elif "motivate me" in message:
    return random.choice([
        "🌟 Don't stop until you're proud.",
        "Small progress every day leads to big success.",
        "Success comes to those who never give up.",
        "Believe in yourself and keep learning.",
        "Consistency is more important than perfection."
    ])

elif "success" in message:
    return (
        "🏆 Success is achieved through consistency, hard work, and continuous learning."
    )

elif "failure" in message:
    return (
        "Failure is not the opposite of success; it is a part of the journey."
    )

# =====================================================
# GOALS
# =====================================================

elif "goal" in message:
    return (
        "🎯 Set SMART goals:\n"
        "• Specific\n"
        "• Measurable\n"
        "• Achievable\n"
        "• Relevant\n"
        "• Time-bound"
    )

elif "dream" in message:
    return (
        "Dream big, stay focused, and work hard every day."
    )
    # =====================================================
# PROGRAMMING JOKES
# =====================================================

elif "joke" in message:

    jokes = [
        "😂 Why do programmers prefer dark mode? Because light attracts bugs.",
        "😂 Why did the Python developer wear glasses? Because they couldn't C.",
        "😂 Why do Java developers wear glasses? Because they don't C#.",
        "😂 Why was the computer cold? It left its Windows open.",
        "😂 There are only 10 kinds of people: those who understand binary and those who don't.",
        "😂 A SQL query walks into a bar and asks: 'Can I JOIN you?'",
        "😂 Why was the programmer broke? Because he used all his cache.",
        "😂 Debugging: Being the detective in a crime movie where you're also the criminal.",
        "😂 Why did the programmer quit? He didn't get arrays.",
        "😂 Keyboard not found... Press F1 to continue."
    ]

    return random.choice(jokes)

# =====================================================
# RANDOM FACTS
# =====================================================

elif "fact" in message:

    facts = [

        "🐙 Octopuses have three hearts.",

        "🐧 Penguins can't fly but they're excellent swimmers.",

        "🧠 The human brain has about 86 billion neurons.",

        "🍯 Honey never spoils.",

        "🌍 Earth revolves around the Sun once every 365 days.",

        "⚡ Lightning is five times hotter than the Sun's surface.",

        "🐬 Dolphins sleep with one eye open.",

        "🦒 Giraffes have the same number of neck bones as humans.",

        "🚀 The Moon moves about 3.8 cm away from Earth every year.",

        "💧 Water covers about 71% of Earth's surface."

    ]

    return random.choice(facts)

# =====================================================
# MOTIVATION
# =====================================================

elif "motivate" in message:

    motivation = [

        "🌟 Dream big. Start small. Act now.",

        "🚀 Every expert was once a beginner.",

        "💪 Success comes from consistency.",

        "📚 Learn something new every day.",

        "🔥 Believe in yourself.",

        "🏆 Hard work beats talent when talent doesn't work hard.",

        "🎯 Small daily improvements lead to remarkable results.",

        "💻 Practice coding every day.",

        "🌱 Growth starts outside your comfort zone.",

        "⭐ Never stop learning."

    ]

    return random.choice(motivation)

# =====================================================
# QUOTES
# =====================================================

elif "quote" in message:

    quotes = [

        "The best way to predict the future is to create it.",

        "Success is not final. Failure is not fatal.",

        "Stay hungry. Stay foolish.",

        "Knowledge is power.",

        "Learning never exhausts the mind.",

        "Code is like humor. When you have to explain it, it's bad.",

        "Programming isn't about what you know; it's about what you can figure out."

    ]

    return random.choice(quotes)

# =====================================================
# ROCK PAPER SCISSORS
# =====================================================

elif message.startswith("play"):

    game = message.replace("play", "").strip()

    if game in ["rock", "paper", "scissors"]:

        bot = random.choice(["rock", "paper", "scissors"])

        if bot == game:
            return f"I chose {bot}. 🤝 It's a Draw!"

        elif (
            (game == "rock" and bot == "scissors") or
            (game == "paper" and bot == "rock") or
            (game == "scissors" and bot == "paper")
        ):
            return f"I chose {bot}. 🎉 You Win!"

        else:
            return f"I chose {bot}. 😄 I Win!"

    else:

        return (
            "Example:\n"
            "play rock\n"
            "play paper\n"
            "play scissors"
        )

# =====================================================
# GUESS NUMBER
# =====================================================

elif message.startswith("guess"):

    try:

        number = int(message.split()[1])

        secret = random.randint(1,10)

        if number == secret:
            return "🎉 Amazing! You guessed correctly."

        elif number > secret:
            return f"Too High! Number was {secret}"

        else:
            return f"Too Low! Number was {secret}"

    except:

        return "Example: guess 5"

# =====================================================
# COLOR
# =====================================================

elif "favorite color" in message:

    return random.choice([
        "💙 Blue",
        "💚 Green",
        "💜 Purple",
        "🖤 Black",
        "❤️ Red"
    ])

# =====================================================
# RANDOM NUMBER
# =====================================================

elif "lucky number" in message:

    return f"🍀 Your lucky number today is {random.randint(1,100)}"

# =====================================================
# RANDOM PASSWORD
# =====================================================

elif "password" in message:

    import string

    chars = string.ascii_letters + string.digits + "@#$%"

    password = "".join(random.choice(chars) for _ in range(10))

    return f"🔐 Suggested Password : {password}"

# =====================================================
# HELP
# =====================================================

elif message == "help":
    return """
Available Commands

Greetings
---------
hello
hi

Programming
-----------
python
java

Exit
----
bye
exit
quit
"""

# =====================================================
# SMART DEFAULT RESPONSE
# =====================================================
else:

    suggestions = [

        "Try asking about Python.",
        "Ask me a programming question.",
        "Type 'help' to see available commands.",
        "Try 'fact' for an interesting fact.",
        "Type 'joke' to hear a programming joke.",
        "Ask about AI or Machine Learning.",
        "Try 'calculate 25+30'.",
        "Ask for interview tips.",
        "Type 'motivate' for motivation.",
        "Play a game using 'play rock'."

    ]

    return (
        "🤔 Sorry, I couldn't understand that.\n\n"
        + random.choice(suggestions)
    )