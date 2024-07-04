import re
import random

# Responses for different intents
GREETING_RESPONSES = ["Hello, this is Jace, how may I help you?!", "Hi,this is Jace, how may I help you?!", "Hey,this is Jace, how may I help you?!", "Greetings!,this is Jace, how may I help you?"]

RADNOM_RESPONES=["Hello! I am a college inquiry-based chatbot."
                 "I'm here to assist you with your queries about college admissions and related information."
                 "Please note that I am a work-in-progress and my creators are continually working on me to improve my capabilities."
                 "As of now, my data is limited, and I may not have all the answers."
                 "However, my creators are actively working on adding more features and expanding my knowledge base to provide better assistance in the future."
                 "Thank you for your understanding, and I'll do my best to help you with the information I have!"]

COURSE_RESPONSES = ["SRM IST offers various undergraduate and postgraduate courses in engineering, medicine, management, science, humanities, and more.",
                    "The courses offered at SRM IST include engineering, medicine, management, science, humanities, and more.",
                    "SRM IST provides a wide range of undergraduate and postgraduate courses in different fields."]

HOSTEL_RESPONSES = ["SRM IST has separate hostels for boys and girls, providing comfortable accommodation with various amenities.",
                    "The hostels at SRM IST are well-equipped and offer a safe and comfortable stay for students.",
                    "SRM IST provides hostel facilities for both boys and girls, with modern amenities and security measures."]

PLACEMENT_RESPONSES = ["SRM IST has a dedicated placement cell that conducts recruitment drives and connects students with top companies.",
                       "The placement opportunities at SRM IST are robust, with many leading companies visiting the campus for recruitment.",
                       "SRM IST has a strong placement record, with students securing placements in top national and international companies."]

LOCATION_RESPONSES = ["SRM IST is located in Kattankulathur, near Chennai, Tamil Nadu, India.",
                      "SRM IST is situated in Kattankulathur, a suburb of Chennai in Tamil Nadu, India.",
                      "The main campus of SRM IST is in Kattankulathur, near Chennai, Tamil Nadu, India."]

ADMISSION_RESPONSES=["SRM (Sri Ramaswamy Memorial) Institute of Science and Technology is a prestigious private university in India, offering undergraduate, postgraduate, and doctoral programs in various"
                     "fields such as Engineering, Medicine, Science, Management, Arts, and Law."
                      "Admissions at SRM University typically follow a competitive process that involves meeting eligibility criteria, submitting an application,"
                     "appearing for entrance exams, and participating in counseling or interview rounds. Here are the general steps for admissions at SRM:"

"Eligibility Criteria: Candidates must meet the eligibility criteria specified by SRM University for the program they wish to apply for."

                     "This may include minimum educational qualifications, age limits, and other requirements."
                     

"Application: Candidates can apply for SRM admissions through the official website or offline mode, depending on the program."
                     "The application forms are usually available in the months of March to April for most undergraduate programs."

"Entrance Exam: SRM conducts its own entrance exams for various programs, such as SRMJEEE (SRM Joint Engineering Entrance Examination) for B.Tech,"

                "SRMJEEM (SRM Joint Entrance Examination for Management) for MBA, and SRMJEEH (SRM Joint Entrance Examination for Health Sciences) for Medicine, among others."

                "Candidates must prepare for the entrance exams and achieve the minimum cutoff scores to be considered for admission."


"Counseling: Shortlisted candidates based on entrance exam scores are invited for counseling, which may be conducted in person or online."
            "During counseling, candidates need to choose their preferred program and campus based on availability and their rank in the merit list."
             "Document Verification: Candidates need to carry the required documents such as mark sheets, certificates, "
                     "identity proof, and other relevant documents for verification during the counseling process."]

DEPARTMENT_RESPONSES = ["SRM IST has various departments including Engineering, Medicine, Management, Science, Humanities, and more.",
                        "The departments at SRM IST encompass Engineering, Medicine, Management, Science, Humanities, and more.",
                        "SRM IST consists of departments offering diverse disciplines such as Engineering, Medicine, Management, Science, Humanities, and more."
                        "The Engineering and Technology faculty comprises of 7 Schools and 19 Departments."
                        "Each school is headed by a Dean and comprises various Departments of Engineering, clubbed on the basis of their domain expertise."
                        "With students in India seeking more inter-disciplinary program and flexibility in course curriculum, SRMIST addressed this demand by completely leaving "
                        "the option of program path to the students. A student shall have the option of choosing any one of the following pathways:"
                        "(i) Major"
                        "(ii) Major with Specialization"
                        "(iii) Major with Minor or Major with specialization and a Minor."
                        "The core philosophy that is practised in SRMIST as part of teaching-learning process is Inter Disciplinary Experiencial Active Learning (IDEAL)"]

RESEARCH_RESPONSES =["We are committed to the creation of knowledge through research across all disciplines within the College of Engineering and Technology (CET)."
                      "This stems from the SRMIST’s focus on RESEARCH instilled from the very beginning by the Leadership especially our Founder and Chancellor."
                      "We ensure that aspiring students willing to put in hard work and interested in gaining most fruitful student life experiences will find all the support they need"
                      "to pursue their research interests. They can immensely benefit from advanced labs, equipment, real-life problems being understood and solved by"
                      "experienced research- oriented faculty members and scholars."
                      "We are committed to the creation of knowledge through research across all disciplines within the College of Engineering and Technology (CET)."
                      "This stems from the SRMIST’s focus on RESEARCH instilled from the very beginning by the Leadership especially our Founder and Chancellor."
                      "We ensure that aspiring students willing to put in hard work and interested in gaining most fruitful student life experiences will find all the support"
                      "they need to pursue their research interests. They can immensely benefit from advanced labs, equipment, real-life problems being understood and solved by experienced research-"
                      "oriented faculty members and scholars."]

ENGINEERING_RESPONSES=["SRMIST’s engineering programs endeavor to be at the forefront of innovation. They also foster multi-disciplinary collaborations aimed at solving the most pressing global problems."
                        "Our mission is to seek solutions to global challenges by using the power of engineering principles, techniques and systems."
                       "We believe that engineers should not only possess deep technical excellence, but also nurture creativity, cultural awareness and entrepreneurial skills that come from exposure to science"
                       ", business, medicine and other disciplines – all integral part of the SRM experience."
                        "Our goal is to deliver world class, solutions driven programs that inspire curiosity and generate new knowledge and discoveries."
                       "Our collaboration with over 50 of the world’s best universities and 215 corporates, strengthens our academic and research programs."
                       "SRMIST’s engineering programs endeavor to be at the forefront of innovation. They also foster multi-disciplinary collaborations aimed at solving the most pressing global problems."
                        "Our mission is to seek solutions to global challenges by using the power of engineering principles, techniques and systems."
                       "We believe that engineers should not only possess deep technical excellence, but also nurture creativity, cultural awareness and entrepreneurial skills that come from exposure"
                       "to science, business, medicine and other disciplines – all integral part of the SRM experience."
                       "Our goal is to deliver world class, solutions driven programs that inspire curiosity and generate new knowledge and discoveries."
                       "Our collaboration with over 50 of the world’s best universities and 215 corporates, strengthens our academic and research programs."]

KEYCONTACTSCET_RESPONSES=["Dean"
                            "Faculty of Engineering & Technology"      
                            "SRM Nagar, Kattankulathur,"
                            "Chengalpattu District – 603 203" 
                            "Phone: +91-44 – 27456020"
                            "Fax: +91-44 – 27453903"
                            "Email: dean.cet@srmist.edu.inDean"
                            "Faculty of Engineering & Technology"      
                            "SRM Nagar, Kattankulathur,"
                            "Chengalpattu District – 603 203" 
                            "Phone: +91-44 – 27456020"
                            "Fax: +91-44 – 27453903"
                            "Email: dean.cet@srmist.edu.in"
                          "Enquiries : +91-44-27456020"
                          "Academic Sections: +91-44-27417802"
                          "Administrative Sections: +91-44-27417803"]

COMPUTINGTECHNOLOGIES_RESPONSES=[" The Department of Computing Technologies (CTECH) fosters the future of computing world."
                                 "The Mission of the Department is to advance, evolve, and enhance Computer Science and Engineering fundamentals to build the intellectual capital of society."
                                 "The CTECH Department endeavors to be an important regional, national, and international resource center for the development of computing and its applications."
                                 "The Department is excelling by keeping up with recent trends and evidence of exponential and exhilarating growth. "
                                 "CTECH boasts a vibrant student body of nearly 5000 undergraduates, 50 postgraduate students, 100+ research scholars, and a stellar faculty of Professors."
                                 "During the year 2020-21, around 1200 students of the CTECH Department bagged the placement opportunity in eminent industries like Microsoft, Amazon, Fidelity, etc."
                                 "The students are exposed to a variety of opportunities, such as in-plant training, internships and workshops during the course of the study."
                                  "The department is wide-open to enormously prospective activities such as hackathons, industry-based joint-project development, the semester-abroad Programme,"
                                 "the faculty development program, the NSS, etc., on a regular basis. The International Conference on the Internet of Things is an iconic event being hosted for the"
                                 "third consecutive year for the benefit of the research fraternity with a focus on Sustainable Development Goals."
                                  "The Department of Computing Technologies (CTECH) fosters the future of computing world."
                                 "The Mission of the Department is to advance, evolve, and enhance Computer Science and Engineering fundamentals to build the intellectual capital of society."
                                 "The CTECH Department endeavors to be an important regional, national, and international resource center for the development of computing and its applications."
                                 "The Department is excelling by keeping up with recent trends and evidence of exponential and exhilarating growth."
                                 "CTECH boasts a vibrant student body of nearly 5000 undergraduates, 50 postgraduate students, 100+ research scholars, and a stellar faculty of Professors."
                                 "During the year 2020-21, around 1200 students of the CTECH Department bagged the placement opportunity in eminent industries like Microsoft, Amazon, Fidelity, etc. "
                                 "The students are exposed to a variety of opportunities, such as in-plant training, internships and workshops during the course of the study."
                                  "The department is wide-open to enormously prospective activities such as hackathons, industry-based joint-project development, the semester-abroad Programme,"
                                 "the faculty development program, the NSS, etc., on a regular basis. The International Conference on the Internet of Things is an iconic event being hosted for "
                                 "the third consecutive year for the benefit of the research fraternity with a focus on Sustainable Development Goals."]

ELIGIBILITYBTECH_RESPONES=["(a) Nationality and Age"

"Resident Indian or Non-Resident Indian (NRI), holder of PIO or OCI card issued by Government of India are eligible to apply for SRMJEEE (UG)."

"note: NRIs, holders of PIO or OCI card issued by Government of India who has not taken the SRMJEEE (UG) must apply under International student category only."

"Should have attained the age of 16 years and 6 months on the 31st July of the calendar year in which the 12th Board examination is to be held (source)."

"(b) Qualifying Examination:"

"All B.Tech programmes :"

"Minimum 50% aggregate in PCM"

"(i) Passed in Higher secondary examination (10+2 pattern ) or appearing in Higher Secondary examination in the current academic year"
"with Physics and Mathematics as compulsory subjects along with one of the Chemistry/ Biotechnology/ Biology/ Technical Vocational subject"
"/ Computer Science/ Information Technology/ Informatics Practices/ Agriculture/ Engineering Graphics/ Business Studies as major subjects in regular stream from any state board within India,"
"CBSE, ISCE, Matriculation, or NIOS"

"Note: Students who have completed +2 under NIOS must have completed the 10th standard from regular schooling or vice-versa."

"(ii) GCE A-level or International Baccalaureate(IB) diploma or IB certificate with Physics and Mathematics as"
"compulsory subjects along with one of the Chemistry/ Biotechnology/ Biology/ Technical Vocational subject/"
"Computer Science/ Information Technology/ Informatics Practices/ Agriculture/ Engineering Graphics/"
"Business Studies as major subjects (equivalent to Advanced Placement level in each subject) in any International schools within India."

"(c) SRMJEEE (UG)"

"Candidates who have attempted Physics, Chemistry, Mathematics, English & Aptitude in SRMJEEE(UG) are eligible for all the B.Tech Degree Programs"

"(d) Direct Admission"

"To encourage and support students of exemplary talent, SRM Institute of Science and Technology (formerly known as SRM University) offers direct admission and "
"scholarships to first rank students of all the central and state boards in India, top 10,000 rankers in IIT JEE, top rankers in each district of Tamil Nadu"
"and exemplary sports persons at National and International level."

"(e) Nationality and Age"

"Resident Indian or Non-Resident Indian (NRI), holder of PIO or OCI card issued by Government of India are eligible to apply for SRMJEEE (UG)."

"Note: NRIs, holders of PIO or OCI card issued by Government of India who has not taken the SRMJEEE (UG) must apply under International student category only."

"Should have attained the age of 16 years and 6 months on the 31st July of the calendar year in which the 12th Board examination is to be held."

"(f) Qualifying Examination:"

"All B.Tech programmes :"

"Minimum 50% aggregate in PCM"

"(i) Passed in Higher secondary examination (10+2 pattern ) or appearing in Higher Secondary examination in the current academic"
"year with Physics and Mathematics as compulsory subjects along with one of the Chemistry/ Biotechnology/ Biology/ Technical Vocational subject"
"/ Computer Science/ Information Technology/ Informatics Practices/ Agriculture/ Engineering Graphics/ Business Studies as major subjects in regular"
"stream from any state board within India, CBSE, ISCE, Matriculation, or NIOS"

"Note: Students who have completed +2 under NIOS must have completed the 10th standard from regular schooling or vice-versa."

"(ii) GCE A-level or International Baccalaureate(IB) diploma or IB certificate with Physics and Mathematics as compulsory subjects along with one of the Chemistry/ Biotechnology/ Biology/ Technical Vocational subject/ Computer Science/ Information Technology/ Informatics Practices/ Agriculture/ Engineering Graphics/ Business Studies as major subjects (equivalent to Advanced Placement level in each subject) in any International schools within India"
"(c) SRMJEEE (UG)"

"Candidates who have attempted Physics, Chemistry, Mathematics, English & Aptitude in SRMJEEE(UG) are eligible for all the B.Tech Degree Programs"

"(d) Direct Admission"

"To encourage and support students of exemplary talent, SRM Institute of Science and Technology (formerly known as SRM University) offers direct admission and scholarships to first rank students of all the central and state boards in India, top 10,000 rankers in IIT JEE, top rankers in each district of Tamil Nadu and exemplary sports persons at National and International level."]



# Function to extract intent and entities from user input
def extract_intent_entities(user_input):
    cleaned_input = user_input.lower().strip()
    intent = None
    entities = []
    if re.search(r'\b(hi|hello|hey|greetings)\b', cleaned_input):
        intent = "greeting"
        
    elif re.search(r'\b(course|courses)\b', cleaned_input):
        intent = "course"
        
    elif re.search(r'\b(hostel|hostels)\b', cleaned_input):
        intent = "hostel"
        
    elif re.search(r'\b(placement|placements)\b', cleaned_input):
        intent = "placement"
        
    elif re.search(r'\b(location|address)\b', cleaned_input):
        intent = "location"

    elif re.search(r'\b(WHO ARE YOU?| who are you?|describe yourself!| introduce yourself|this is not the answer i wanted|nope|no|nah|not the right answer)\b', cleaned_input):
        intent = "random"
        
    elif re.search(r'\b(department|departments)\b', cleaned_input):
        intent = "department"
        
    elif re.search(r'\b(admission|admissions)\b', cleaned_input):
        intent = "admission"
        
    elif re.search(r'\b(research|how is research|what about research here?|tell me about research in SRM)\b', cleaned_input):
        intent="research"
        
    elif re.search(r'\b( CSE|cse|Cse|CsE|how is cse engineering |computer science|tell me about Computer science engg in SRM|ctech)\b', cleaned_input):
        intent="computingtechnologies"
        
    elif re.search(r'\b(Engineering |Engineering department|what about the engineering based department here?|tell me about Engineering dept in SRM)\b', cleaned_input):
        intent="engineering"

    elif re.search(r'\b(contact details|help for Engineering| dean contact number|helpdesk number|contact|help)\b', cleaned_input):
        intent="keycontactscet"
        
    elif re.search(r'\b(eligibility|criteria|engineering criteria|criteria for engineering|eligibility for engineering btech|btech|admission for btech)\b', cleaned_input):
        intent="eligibiltybtech"


        
    else:
        intent = "unknown"
    entities = re.findall(r'\b([a-zA-Z]+)\b', cleaned_input)
    return intent, entities

# Function to generate chatbot response based on intent and entities
def chatbot_response(intent, entities):
    if intent == "greeting":
        response = random.choice(GREETING_RESPONSES)
    elif intent=="admission":
         response=random.choice(ADMISSION_RESPONSES)

    elif intent == "course":
        response = random.choice(COURSE_RESPONSES)
    
    elif intent == "random":
        response = random.choice(RANDOM_RESPONSES)


    elif intent == "hostel":
        if entities:
            response = f"SRM IST has separate hostels for {', '.join(entities)}, providing comfortable accommodation with various amenities."
        else:
            response = random.choice(HOSTEL_RESPONSES)

    elif intent == "placement":
        response = random.choice(PLACEMENT_RESPONSES)

    elif intent == "location":
        response = random.choice(LOCATION_RESPONSES)

    elif intent == "research":
        response = random.choice(RESEARCH_RESPONSES)

    elif intent == "computingtechnologies":
        response = random.choice(COMPUTINGTECHNOLOGIES_RESPONSES)

    elif intent == "engineering":
        response = random.choice(ENGINEERING_RESPONSES)

    elif intent == "keycontactcet":
        response = random.choice(KEYCONTACTSCET_RESPONSES)

    elif intent == "eligibilitybtech":
        response = random.choice(ELIGIBILITYBTECH_RESPONSES)
    
    else:
        response = "I'm sorry, I am not able to provide information on that topic. Please ask me something else."

    return response










# Main loop for user interaction
while True:
    user_input = input("You: ")
    if re.search(r'\b(bye|exit)\b', user_input):
        print("Chatbot: Goodbye!")
        break
    intent, entities = extract_intent_entities(user_input)
    response = chatbot_response(intent, entities)
    print("Chatbot:", response)

