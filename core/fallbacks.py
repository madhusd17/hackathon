"""
Built-in fallback lessons in English and 5 Indian languages (Hindi, Tamil, Telugu, Marathi, Bengali).
Guarantees that the demo NEVER breaks even if the local LLM fails or times out.
"""

FALLBACK_LESSONS = {
    "python loops": {
        "en": {
            "title": "How a Python Loop Works",
            "level": "beginner",
            "language": "en",
            "topic": "Python Loops",
            "scenes": [
                {
                    "type": "title_card",
                    "heading": "How Does a Python Loop Work?",
                    "subheading": "Repeating actions automatically",
                    "narration": "A loop repeats an instruction for each item in a sequence, saving time and code."
                },
                {
                    "type": "code_walkthrough",
                    "heading": "Step 1: Write the Loop",
                    "code": "for i in range(3):\n    print('Iteration:', i)",
                    "highlight_lines": [1],
                    "output": "Iteration: 0\nIteration: 1\nIteration: 2",
                    "narration": "The for loop iterates through range of three, taking values zero, one, and two."
                },
                {
                    "type": "diagram",
                    "heading": "Step 2: Visualizing Iterations",
                    "items": [
                        {"label": "Pass 1", "value": "i = 0  ->  print"},
                        {"label": "Pass 2", "value": "i = 1  ->  print"},
                        {"label": "Pass 3", "value": "i = 2  ->  print"}
                    ],
                    "narration": "In each pass, the variable i takes the next value and executes the indented print block."
                },
                {
                    "type": "quiz",
                    "heading": "Step 3: Quick Knowledge Check",
                    "question": "What is the final value of i printed by range(3)?",
                    "options": ["1", "2", "3", "0"],
                    "answer": "2",
                    "narration": "Remember that range of three starts from zero and stops before three, so the final number is two."
                }
            ]
        },
        "hi": {
            "title": "पायथन लूप कैसे काम करता है",
            "level": "beginner",
            "language": "hi",
            "topic": "Python Loops",
            "scenes": [
                {
                    "type": "title_card",
                    "heading": "पायथन लूप कैसे काम करता है?",
                    "subheading": "कार्यों को स्वचालित रूप से दोहराना",
                    "narration": "एक लूप किसी क्रम में प्रत्येक आइटम के लिए निर्देशों को दोहराता है।"
                },
                {
                    "type": "code_walkthrough",
                    "heading": "चरण १: लूप कोड लिखना",
                    "code": "for i in range(3):\n    print('Iteration:', i)",
                    "highlight_lines": [1],
                    "output": "Iteration: 0\nIteration: 1\nIteration: 2",
                    "narration": "यह फॉर लूप रेंज तीन के माध्यम से शून्य, एक और दो मान लेता है।"
                },
                {
                    "type": "diagram",
                    "heading": "चरण २: पुनरावृत्ति समझना",
                    "items": [
                        {"label": "पहला फेरा", "value": "i = 0  ->  प्रिंट"},
                        {"label": "दूसरा फेरा", "value": "i = 1  ->  प्रिंट"},
                        {"label": "तीसरा फेरा", "value": "i = 2  ->  प्रिंट"}
                    ],
                    "narration": "हर फेरे में वेरिएबल आई अगला मान लेता है और प्रिंट कमांड चलाता है।"
                },
                {
                    "type": "quiz",
                    "heading": "चरण ३: त्वरित प्रश्न",
                    "question": "range(3) द्वारा प्रिंट किया गया अंतिम मान क्या है?",
                    "options": ["1", "2", "3", "0"],
                    "answer": "2",
                    "narration": "रेंज तीन शून्य से शुरू होकर तीन से पहले रुकती है, इसलिए अंतिम मान दो है।"
                }
            ]
        },
        "ta": {
            "title": "பைதான் லூப் எவ்வாறு செயல்படுகிறது",
            "level": "beginner",
            "language": "ta",
            "topic": "Python Loops",
            "scenes": [
                {
                    "type": "title_card",
                    "heading": "பைதான் லூப் எவ்வாறு செயல்படுகிறது?",
                    "subheading": "செயல்களை தானாக மீண்டும் செய்தல்",
                    "narration": "லூப் என்பது ஒரு வரிசையில் உள்ள ஒவ்வொரு உருப்படிக்கும் வழிமுறைகளை மீண்டும் செய்கிறது."
                },
                {
                    "type": "code_walkthrough",
                    "heading": "படி 1: குறியீட்டை எழுதுங்கள்",
                    "code": "for i in range(3):\n    print('Iteration:', i)",
                    "highlight_lines": [1],
                    "output": "Iteration: 0\nIteration: 1\nIteration: 2",
                    "narration": "இந்த ஃபார் லூப் பூஜ்ஜியம், ஒன்று மற்றும் இரண்டு ஆகிய எண்களை வரிசையாக எடுக்கும்."
                },
                {
                    "type": "diagram",
                    "heading": "படி 2: லூப் இயங்கும் விதம்",
                    "items": [
                        {"label": "சுழற்சி 1", "value": "i = 0  ->  print"},
                        {"label": "சுழற்சி 2", "value": "i = 1  ->  print"},
                        {"label": "சுழற்சி 3", "value": "i = 2  ->  print"}
                    ],
                    "narration": "ஒவ்வொரு சுழற்சியிலும் i அடுத்த மதிப்பை எடுத்து அச்சிடுகிறது."
                },
                {
                    "type": "quiz",
                    "heading": "படி 3: விரைவு வினாடி வினா",
                    "question": "range(3) இல் அச்சிடப்படும் கடைசி மதிப்பு எது?",
                    "options": ["1", "2", "3", "0"],
                    "answer": "2",
                    "narration": "ரேஞ்ச் மூன்று பூஜ்ஜியத்தில் தொடங்கி மூன்றுக்கு முன் முடிவதால் கடைசி மதிப்பு இரண்டு ஆகும்."
                }
            ]
        },
        "te": {
            "title": "పైథాన్ లూప్ ఎలా పనిచేస్తుంది",
            "level": "beginner",
            "language": "te",
            "topic": "Python Loops",
            "scenes": [
                {
                    "type": "title_card",
                    "heading": "పైథాన్ లూప్ ఎలా పనిచేస్తుంది?",
                    "subheading": "పనులను స్వయంచాలకంగా పునరావృతం చేయడం",
                    "narration": "ఒక లూప్ అనేది వరుసలోని ప్రతి అంశానికి సూచనలను పునరావృతం చేస్తుంది."
                },
                {
                    "type": "code_walkthrough",
                    "heading": "దశ 1: కోడ్ రాయడం",
                    "code": "for i in range(3):\n    print('Iteration:', i)",
                    "highlight_lines": [1],
                    "output": "Iteration: 0\nIteration: 1\nIteration: 2",
                    "narration": "ఈ ఫర్ లూప్ సున్నా, ఒకటి మరియు రెండు విలువలను వరుసగా తీసుకుంటుంది."
                },
                {
                    "type": "diagram",
                    "heading": "దశ 2: లూప్ విధానం",
                    "items": [
                        {"label": "రౌండ్ 1", "value": "i = 0  ->  ప్రింట్"},
                        {"label": "రౌండ్ 2", "value": "i = 1  ->  ప్రింట్"},
                        {"label": "రౌండ్ 3", "value": "i = 2  ->  ప్రింట్"}
                    ],
                    "narration": "ప్రతి రౌండ్‌లో i వేరియబుల్ తదుపరి విలువను తీసుకొని ప్రింట్ చేస్తుంది."
                },
                {
                    "type": "quiz",
                    "heading": "దశ 3: క్విజ్",
                    "question": "range(3) లో ప్రింట్ అయ్యే చివరి విలువ ఏమిటి?",
                    "options": ["1", "2", "3", "0"],
                    "answer": "2",
                    "narration": "రేంజ్ మూడు సున్నా నుండి మొదలై మూడుకు ముందు ఆగుతుంది, కాబట్టి చివరి విలువ రెండు."
                }
            ]
        },
        "mr": {
            "title": "पायथन लूप कसे कार्य करते",
            "level": "beginner",
            "language": "mr",
            "topic": "Python Loops",
            "scenes": [
                {
                    "type": "title_card",
                    "heading": "पायथन लूप कसे कार्य करते?",
                    "subheading": "कृती आपोआप पुन्हा करणे",
                    "narration": "लूप प्रत्येक घटकासाठी सूचना पुन्हा पुन्हा कार्यान्वित करतो."
                },
                {
                    "type": "code_walkthrough",
                    "heading": "पायरी १: कोड लिहिणे",
                    "code": "for i in range(3):\n    print('Iteration:', i)",
                    "highlight_lines": [1],
                    "output": "Iteration: 0\nIteration: 1\nIteration: 2",
                    "narration": "हा फॉर लूप शून्य, एक आणि दोन या मूल्यांमधून फिरतो."
                },
                {
                    "type": "diagram",
                    "heading": "पायरी २: लूप फेरे",
                    "items": [
                        {"label": "फेरा १", "value": "i = 0  ->  प्रिंट"},
                        {"label": "फेरा २", "value": "i = 1  ->  प्रिंट"},
                        {"label": "फेरा ३", "value": "i = 2  ->  प्रिंट"}
                    ],
                    "narration": "प्रत्येक फेऱ्यात i पुढील मूल्य घेतो आणि प्रिंट करतो."
                },
                {
                    "type": "quiz",
                    "heading": "पायरी ३: प्रश्नमंजुषा",
                    "question": "range(3) चे अंतिम मुद्रित मूल्य काय आहे?",
                    "options": ["1", "2", "3", "0"],
                    "answer": "2",
                    "narration": "रेंज तीन शून्यापासून सुरू होते आणि तीनच्या आधी थांबते, म्हणून अंतिम मूल्य दोन आहे."
                }
            ]
        },
        "bn": {
            "title": "পাইথন লুপ কীভাবে কাজ করে",
            "level": "beginner",
            "language": "bn",
            "topic": "Python Loops",
            "scenes": [
                {
                    "type": "title_card",
                    "heading": "পাইথন লুপ কীভাবে কাজ করে?",
                    "subheading": "স্বয়ংক্রিয় পুনরাবৃত্তি",
                    "narration": "একটি লুপ কোনো তালিকার প্রতিটি মানের জন্য নির্দেশাবলী বারবার সম্পাদন করে।"
                },
                {
                    "type": "code_walkthrough",
                    "heading": "ধাপ ১: কোড লিখুন",
                    "code": "for i in range(3):\n    print('Iteration:', i)",
                    "highlight_lines": [1],
                    "output": "Iteration: 0\nIteration: 1\nIteration: 2",
                    "narration": "এই ফর লুপটি শূন্য, এক এবং দুই এই মানগুলোর মধ্য দিয়ে আবর্তিত হয়।"
                },
                {
                    "type": "diagram",
                    "heading": "ধাপ ২: প্রতিটি ধাপের প্রবাহ",
                    "items": [
                        {"label": "ধাপ ১", "value": "i = 0  ->  প্রিন্ট"},
                        {"label": "ধাপ ২", "value": "i = 1  ->  প্রিন্ট"},
                        {"label": "ধাপ ৩", "value": "i = 2  ->  প্রিন্ট"}
                    ],
                    "narration": "প্রতিটি ধাপে ভেরিয়েবল i পরবর্তী মান গ্রহণ করে প্রিন্ট নির্দেশ চালায়।"
                },
                {
                    "type": "quiz",
                    "heading": "ধাপ ৩: ছোট প্রশ্ন",
                    "question": "range(3) এর শেষ প্রিন্ট করা মান কোনটি?",
                    "options": ["1", "2", "3", "0"],
                    "answer": "2",
                    "narration": "রেঞ্জ তিন শূন্য থেকে শুরু হয় এবং তিনের আগে থামে, তাই শেষ মান দুই।"
                }
            ]
        }
    },
    "photosynthesis": {
        "en": {
            "title": "Understanding Photosynthesis",
            "level": "beginner",
            "language": "en",
            "topic": "Photosynthesis",
            "scenes": [
                {
                    "type": "title_card",
                    "heading": "What is Photosynthesis?",
                    "subheading": "How plants transform sunlight into energy",
                    "narration": "Photosynthesis is the remarkable process where plants make their own food using sunlight, water, and carbon dioxide."
                },
                {
                    "type": "diagram",
                    "heading": "Step 1: The Key Ingredients",
                    "items": [
                        {"label": "Input 1", "value": "Sunlight (Captured by Chlorophyll)"},
                        {"label": "Input 2", "value": "Water H2O (From the roots)"},
                        {"label": "Input 3", "value": "Carbon Dioxide CO2 (From air)"}
                    ],
                    "narration": "Plants absorb water through roots and take in carbon dioxide through tiny leaf openings called stomata."
                },
                {
                    "type": "diagram",
                    "heading": "Step 2: The Reaction & Output",
                    "items": [
                        {"label": "Output 1", "value": "Glucose (Plant Energy & Growth)"},
                        {"label": "Output 2", "value": "Oxygen O2 (Released for life)"}
                    ],
                    "narration": "Solar energy powers the chemical transformation, producing nourishing glucose and releasing life-giving oxygen into our atmosphere."
                },
                {
                    "type": "summary",
                    "heading": "Step 3: Key Takeaways",
                    "items": [
                        {"label": "Fact 1", "value": "Chlorophyll makes leaves green and traps light"},
                        {"label": "Fact 2", "value": "Produces glucose to feed plants"},
                        {"label": "Fact 3", "value": "Releases oxygen that animals and humans breathe"}
                    ],
                    "narration": "Photosynthesis sustains life on Earth by generating oxygen and forming the base of almost all food chains."
                }
            ]
        },
        "hi": {
            "title": "प्रकाश संश्लेषण की समझ",
            "level": "beginner",
            "language": "hi",
            "topic": "Photosynthesis",
            "scenes": [
                {
                    "type": "title_card",
                    "heading": "प्रकाश संश्लेषण क्या है?",
                    "subheading": "पौधे सूर्य की रोशनी से भोजन कैसे बनाते हैं",
                    "narration": "प्रकाश संश्लेषण वह अद्भुत प्रक्रिया है जिसमें पौधे धूप, पानी और कार्बन डाइऑक्साइड से अपना भोजन बनाते हैं।"
                },
                {
                    "type": "diagram",
                    "heading": "चरण १: मुख्य घटक",
                    "items": [
                        {"label": "घटक १", "value": "सूर्य का प्रकाश (क्लोरोफिल द्वारा)"},
                        {"label": "घटक २", "value": "पानी H2O (जड़ों से अवशोषित)"},
                        {"label": "घटक ३", "value": "कार्बन डाइऑक्साइड CO2 (हवा से)"}
                    ],
                    "narration": "पौधे जड़ों से पानी लेते हैं और पत्तियों के छोटे छिद्रों से कार्बन डाइऑक्साइड सोखते हैं।"
                },
                {
                    "type": "diagram",
                    "heading": "चरण २: रासायनिक क्रिया और परिणाम",
                    "items": [
                        {"label": "उत्पाद १", "value": "ग्लूकोज (पौधों की ऊर्जा)"},
                        {"label": "उत्पाद २", "value": "ऑक्सीजन O2 (जीवन के लिए)"}
                    ],
                    "narration": "सौर ऊर्जा इस क्रिया को शक्ति देती है, जिससे ग्लूकोज बनता है और प्राणदायिनी ऑक्सीजन हवा में निकलती है।"
                },
                {
                    "type": "summary",
                    "heading": "चरण ३: मुख्य बातें",
                    "items": [
                        {"label": "तथ्य १", "value": "क्लोरोफिल पत्तियों को हरा रखता है"},
                        {"label": "तथ्य २", "value": "पौधों के विकास के लिए ग्लूकोज"},
                        {"label": "तथ्य ३", "value": "हमारे सांस लेने के लिए ऑक्सीजन"}
                    ],
                    "narration": "प्रकाश संश्लेषण ऑक्सीजन बनाकर और खाद्य श्रृंखला को आधार देकर पृथ्वी पर जीवन का पोषण करता है।"
                }
            ]
        },
        "ta": {
            "title": "ஒளிச்சேர்க்கை பற்றிய புரிதல்",
            "level": "beginner",
            "language": "ta",
            "topic": "Photosynthesis",
            "scenes": [
                {
                    "type": "title_card",
                    "heading": "ஒளிச்சேர்க்கை என்றால் என்ன?",
                    "subheading": "தாவரங்கள் உணவு தயாரிக்கும் முறை",
                    "narration": "ஒளிச்சேர்க்கை என்பது தாவரங்கள் சூரிய ஒளி, நீர் மற்றும் கார்பன் டை ஆக்சைடைப் பயன்படுத்தி உணவு தயாரிக்கும் செயல்முறையாகும்."
                },
                {
                    "type": "diagram",
                    "heading": "படி 1: முக்கிய கூறுகள்",
                    "items": [
                        {"label": "கூறு 1", "value": "சூரிய ஒளி (பச்சையம் மூலம்)"},
                        {"label": "கூறு 2", "value": "நீர் (வேர்கள் மூலம்)"},
                        {"label": "கூறு 3", "value": "கார்பன் டை ஆக்சைடு"}
                    ],
                    "narration": "வேர்கள் மூலம் நீரை உறிஞ்சி இலைகள் வழியாக கார்பன் டை ஆக்சைடை தாவரங்கள் பெறுகின்றன."
                },
                {
                    "type": "diagram",
                    "heading": "படி 2: உற்பத்தி முடிவுகள்",
                    "items": [
                        {"label": "முடிவு 1", "value": "குளுக்கோஸ் (ஆற்றல்)"},
                        {"label": "முடிவு 2", "value": "ஆக்சிஜன் (சுவாசம்)"}
                    ],
                    "narration": "இந்த செயல்முறை குளுக்கோஸை உருவாக்குகிறது மற்றும் நாம் சுவாசிக்க ஆக்சிஜனை வெளியிடுகிறது."
                },
                {
                    "type": "summary",
                    "heading": "படி 3: முக்கிய குறிப்புகள்",
                    "items": [
                        {"label": "குறிப்பு 1", "value": "பச்சையம் சூரிய ஒளியை ஈர்க்கிறது"},
                        {"label": "குறிப்பு 2", "value": "உணவாக குளுக்கோஸ்"},
                        {"label": "குறிப்பு 3", "value": "பூமிக்கு உயிர் தரும் ஆக்சிஜன்"}
                    ],
                    "narration": "ஒளிச்சேர்க்கை ஆக்சிஜனை உற்பத்தி செய்து பூமியின் அனைத்து உயிர்களையும் பாதுகாக்கிறது."
                }
            ]
        },
        "te": {
            "title": "కిరణజన్య సంయోగక్రియ అవగాహన",
            "level": "beginner",
            "language": "te",
            "topic": "Photosynthesis",
            "scenes": [
                {
                    "type": "title_card",
                    "heading": "కిరణజన్య సంయోగక్రియ అంటే ఏమిటి?",
                    "subheading": "మొక్కలు ఆహారం తయారు చేసుకునే విధానం",
                    "narration": "మొక్కలు సూర్యకాంతి, నీరు మరియు కార్బన్ డయాక్సైడ్ ఉపయోగించి ఆహారాన్ని తయారుచేసే ప్రక్రియే కిరణజన్య సంయోగక్రియ."
                },
                {
                    "type": "diagram",
                    "heading": "దశ 1: ముఖ్య వనరులు",
                    "items": [
                        {"label": "వనరు 1", "value": "సూర్యరశ్మి (క్లోరోఫిల్)"},
                        {"label": "వనరు 2", "value": "నీరు (వేర్ల నుండి)"},
                        {"label": "వనరు 3", "value": "కార్బన్ డయాక్సైడ్ (గాలి నుండి)"}
                    ],
                    "narration": "మొక్కలు వేర్ల ద్వారా నీటిని, ఆకుల ద్వారా కార్బన్ డయాక్సైడ్ గ్రహిస్తాయి."
                },
                {
                    "type": "diagram",
                    "heading": "దశ 2: ఫలితాలు",
                    "items": [
                        {"label": "ఉత్పత్తి 1", "value": "గ్లూకోజ్ (మొక్కల శక్తి)"},
                        {"label": "ఉత్పత్తి 2", "value": "ఆక్సిజన్ (ప్రాణవాయువు)"}
                    ],
                    "narration": "ఈ చర్య ద్వారా మొక్కలకు గ్లూకోజ్ మరియు జీవుల మనుగడకు అవసరమైన ఆక్సిజన్ విడుదలవుతుంది."
                },
                {
                    "type": "summary",
                    "heading": "దశ 3: ప్రధాన అంశాలు",
                    "items": [
                        {"label": "అంశం 1", "value": "క్లోరోఫిల్ కాంతిని గ్రహిస్తుంది"},
                        {"label": "అంశం 2", "value": "గ్లూకోజ్ ఆహారంగా మారుతుంది"},
                        {"label": "అంశం 3", "value": "ఆక్సిజన్ జీవనాన్ని కాపాడుతుంది"}
                    ],
                    "narration": "కిరణజన్య సంయోగక్రియ ప్రాణవాయువును అందించి భూమిపై జీవకోటిని కాపాడుతుంది."
                }
            ]
        },
        "mr": {
            "title": "प्रकाशसंश्लेषण समजून घेऊया",
            "level": "beginner",
            "language": "mr",
            "topic": "Photosynthesis",
            "scenes": [
                {
                    "type": "title_card",
                    "heading": "प्रकाशसंश्लेषण म्हणजे काय?",
                    "subheading": "वनस्पती अन्न कसे तयार करतात",
                    "narration": "प्रकाशसंश्लेषण ही वनस्पतींची सूर्यप्रकाश, पाणी आणि कार्बन डायऑक्साइड वापरून अन्न बनवण्याची प्रक्रिया आहे."
                },
                {
                    "type": "diagram",
                    "heading": "पायरी १: आवश्यक घटक",
                    "items": [
                        {"label": "घटक १", "value": "सूर्यप्रकाश (हरितद्रव्य)"},
                        {"label": "घटक २", "value": "पाणी (मुळांमधून)"},
                        {"label": "घटक ३", "value": "कार्बन डायऑक्साइड (हवेतून)"}
                    ],
                    "narration": "वनस्पती मुळांमधून पाणी आणि पानांमधील छिद्रांमधून कार्बन डायऑक्साइड शोषून घेतात."
                },
                {
                    "type": "diagram",
                    "heading": "पायरी २: उत्पादने",
                    "items": [
                        {"label": "उत्पादन १", "value": "ग्लुकोज (अन्न व ऊर्जा)"},
                        {"label": "उत्पादन २", "value": "ऑक्सिजन (जीवनासाठी)"}
                    ],
                    "narration": "सौर ऊर्जेमुळे रासायनिक प्रक्रिया होऊन ग्लुकोज तयार होते आणि ऑक्सिजन हवेत सोडला जातो."
                },
                {
                    "type": "summary",
                    "heading": "पायरी ३: महत्त्वाचे मुद्दे",
                    "items": [
                        {"label": "मुद्दा १", "value": "हरितद्रव्य प्रकाश शोषून घेते"},
                        {"label": "मुद्दा २", "value": "ग्लुकोज वनस्पतींची वाढ करते"},
                        {"label": "मुद्दा ३", "value": "प्राणवायू ऑक्सिजन मिळतो"}
                    ],
                    "narration": "प्रकाशसंश्लेषण ऑक्सिजन निर्माण करून पृथ्वीवरील जीवसृष्टी टिकवून ठेवते."
                }
            ]
        },
        "bn": {
            "title": "সালোকসংশ্লেষণ বোঝা",
            "level": "beginner",
            "language": "bn",
            "topic": "Photosynthesis",
            "scenes": [
                {
                    "type": "title_card",
                    "heading": "সালোকসংশ্লেষণ কী?",
                    "subheading": "উদ্ভিদের খাদ্য তৈরির প্রক্রিয়া",
                    "narration": "সালোকসংশ্লেষণ হলো এমন একটি প্রক্রিয়া যার মাধ্যমে উদ্ভিদ সূর্যালোক, জল এবং কার্বন ডাই অক্সাইড ব্যবহার করে খাদ্য তৈরি করে।"
                },
                {
                    "type": "diagram",
                    "heading": "ধাপ ১: প্রয়োজনীয় উপাদান",
                    "items": [
                        {"label": "উপাদান ১", "value": "সূর্যালোক (ক্লোরোফিল দ্বারা)"},
                        {"label": "উপাদান ২", "value": "জল (শিকড় দ্বারা সংগৃহীত)"},
                        {"label": "উপাদান ৩", "value": "কার্বন ডাই অক্সাইড (বাতাস থেকে)"}
                    ],
                    "narration": "উদ্ভিদ শিকড় দিয়ে জল শোষণ করে এবং পাতার মাধ্যমে বাতাস থেকে কার্বন ডাই অক্সাইড গ্রহণ করে।"
                },
                {
                    "type": "diagram",
                    "heading": "ধাপ ২: বিক্রিয়ার ফলাফল",
                    "items": [
                        {"label": "উৎপাদ ১", "value": "গ্লুকোজ (উদ্ভিদের শক্তি)"},
                        {"label": "উৎপাদ ২", "value": "অক্সিজেন (প্রাণের জন্য)"}
                    ],
                    "narration": "সূর্যশক্তি এই রাসায়নিক বিক্রিয়া সম্পন্ন করে গ্লুকোজ উৎপন্ন করে এবং বাতাসে অক্সিজেন ছড়িয়ে দেয়।"
                },
                {
                    "type": "summary",
                    "heading": "ধাপ ৩: মূল বিষয়",
                    "items": [
                        {"label": "তথ্য ১", "value": "ক্লোরোফিল আলো আটকে রাখে"},
                        {"label": "তথ্য ২", "value": "উদ্ভিদের পুষ্টির জন্য গ্লুকোজ"},
                        {"label": "তথ্য ৩", "value": "আমাদের শ্বাস নেওয়ার জন্য অক্সিজেন"}
                    ],
                    "narration": "সালোকসংশ্লেষণ অক্সিজেন উৎপাদন করে পৃথিবীর সামগ্রিক পরিবেশ ও জীবনকে সচল রাখে।"
                }
            ]
        }
    },
    "newton's laws": {
        "en": {
            "title": "Newton's Third Law of Motion",
            "level": "beginner",
            "language": "en",
            "topic": "Newton's Third Law",
            "scenes": [
                {
                    "type": "title_card",
                    "heading": "Newton's Third Law of Motion",
                    "subheading": "Action and Reaction Forces",
                    "narration": "For every action force in nature, there is an equal and opposite reaction force."
                },
                {
                    "type": "diagram",
                    "heading": "Step 1: The Force Pair",
                    "items": [
                        {"label": "Action", "value": "Rocket expels gas downward with force F"},
                        {"label": "Reaction", "value": "Gas pushes rocket upward with equal force -F"}
                    ],
                    "narration": "Forces always occur in matched pairs. When a rocket engine pushes fuel downward, the expanding gas pushes the rocket skyward."
                },
                {
                    "type": "summary",
                    "heading": "Step 2: Real-World Examples",
                    "items": [
                        {"label": "Walking", "value": "Foot pushes back on ground; ground pushes you forward"},
                        {"label": "Swimming", "value": "Hands push water backward; water pushes swimmer ahead"},
                        {"label": "Balloon", "value": "Escaping air rushes left; balloon darts right"}
                    ],
                    "narration": "Every step you take and every stroke you swim relies on this universal principle of action and reaction."
                },
                {
                    "type": "quiz",
                    "heading": "Step 3: Concept Check",
                    "question": "If you push a wall with 50 Newtons of force, what force does the wall exert on you?",
                    "options": ["0 Newtons", "25 Newtons", "50 Newtons", "100 Newtons"],
                    "answer": "50 Newtons",
                    "narration": "The wall pushes right back on you with exactly fifty Newtons of force in the opposite direction."
                }
            ]
        },
        "hi": {
            "title": "न्यूटन का गति का तीसरा नियम",
            "level": "beginner",
            "language": "hi",
            "topic": "Newton's Third Law",
            "scenes": [
                {
                    "type": "title_card",
                    "heading": "न्यूटन का गति का तीसरा नियम",
                    "subheading": "क्रिया और प्रतिक्रिया बल",
                    "narration": "प्रत्येक क्रिया के बराबर और विपरीत दिशा में एक प्रतिक्रिया होती है।"
                },
                {
                    "type": "diagram",
                    "heading": "चरण १: बल युग्म",
                    "items": [
                        {"label": "क्रिया", "value": "रॉकेट गैस को नीचे धकेलता है (बल F)"},
                        {"label": "प्रतिक्रिया", "value": "गैस रॉकेट को ऊपर धकेलती है (बल -F)"}
                    ],
                    "narration": "बल हमेशा युग्म में काम करते हैं। जब रॉकेट गैस को नीचे फेंकता है, तो गैस रॉकेट को ऊपर धकेलती है।"
                },
                {
                    "type": "summary",
                    "heading": "चरण २: दैनिक उदाहरण",
                    "items": [
                        {"label": "चलना", "value": "पैर जमीन को पीछे धकेलता है, जमीन हमें आगे"},
                        {"label": "तैरना", "value": "हाथ पानी को पीछे धकेलते हैं, पानी तैराक को आगे"}
                    ],
                    "narration": "हमारा चलना और पानी में तैरना इसी क्रिया-प्रतिक्रिया के नियम पर आधारित है।"
                },
                {
                    "type": "quiz",
                    "heading": "चरण ३: त्वरित प्रश्न",
                    "question": "यदि आप दीवार को 50 न्यूटन बल से धकेलते हैं, तो दीवार आप पर कितना बल लगाएगी?",
                    "options": ["0 न्यूटन", "25 न्यूटन", "50 न्यूटन", "100 न्यूटन"],
                    "answer": "50 न्यूटन",
                    "narration": "दीवार भी आप पर विपरीत दिशा में ठीक पचास न्यूटन का बल लगाती है।"
                }
            ]
        },
        "ta": {
            "title": "நியூட்டனின் மூன்றாம் விதி",
            "level": "beginner",
            "language": "ta",
            "topic": "Newton's Third Law",
            "scenes": [
                {
                    "type": "title_card",
                    "heading": "நியூட்டனின் மூன்றாம் இயக்க விதி",
                    "subheading": "செயலும் எதிர்ச்செயலும்",
                    "narration": "ஒவ்வொரு விசைக்கும் சமமான மற்றும் எதிர் திசையிலான எதிர்விசை உண்டு."
                },
                {
                    "type": "diagram",
                    "heading": "படி 1: விசை இணை",
                    "items": [
                        {"label": "செயல்", "value": "ராக்கெட் வாயுவை கீழே தள்ளுகிறது"},
                        {"label": "எதிர்ச்செயல்", "value": "வாயு ராக்கெட்டை மேலே செலுத்துகிறது"}
                    ],
                    "narration": "ராக்கெட் எரிபொருளை கீழ்நோக்கி உந்தும்போது, எதிர்விசை ராக்கெட்டை வான்நோக்கி செலுத்துகிறது."
                },
                {
                    "type": "summary",
                    "heading": "படி 2: நடைமுறை உதாரணங்கள்",
                    "items": [
                        {"label": "நடப்பது", "value": "கால்கள் தரையை தள்ள, தரை நம்மை முன்னகர்த்துகிறது"},
                        {"label": "நீந்துவது", "value": "கைகள் தண்ணீரை தள்ள, நாம் முன்னேறுகிறோம்"}
                    ],
                    "narration": "நாம் நடப்பதும் நீந்துவதும் இந்த விதியின் அடிப்படையிலேயே நிகழ்கின்றன."
                },
                {
                    "type": "quiz",
                    "heading": "படி 3: கேள்வி",
                    "question": "நீங்கள் சுவரை 50 நியூட்டன் விசையுடன் தள்ளினால் சுவர் உங்கள் மீது செலுத்தும் விசை?",
                    "options": ["0 நியூட்டன்", "25 நியூட்டன்", "50 நியூட்டன்", "100 நியூட்டன்"],
                    "answer": "50 நியூட்டன்",
                    "narration": "சுவரும் சரியாக ஐம்பது நியூட்டன் எதிர்விசையை உங்கள் மீது செலுத்துகிறது."
                }
            ]
        },
        "te": {
            "title": "న్యూటన్ మూడవ గమన నియమం",
            "level": "beginner",
            "language": "te",
            "topic": "Newton's Third Law",
            "scenes": [
                {
                    "type": "title_card",
                    "heading": "న్యూటన్ మూడవ గమన నియమం",
                    "subheading": "చర్య మరియు ప్రతిచర్య బలాలు",
                    "narration": "ప్రతి చర్యకు సమానమైన మరియు వ్యతిరేక దిశలో ప్రతిచర్య ఉంటుంది."
                },
                {
                    "type": "diagram",
                    "heading": "దశ 1: బలాల జత",
                    "items": [
                        {"label": "చర్య", "value": "రాకెట్ వాయువును క్రిందికి నెట్టుతుంది"},
                        {"label": "ప్రతిచర్య", "value": "వాయువు రాకెట్‌ను పైకి నెట్టుతుంది"}
                    ],
                    "narration": "రాకెట్ ఇంధన వాయువును క్రిందికి తోస్తే, ఆ వాయువు రాకెట్‌ను ఆకాశంలోకి నెట్టుతుంది."
                },
                {
                    "type": "summary",
                    "heading": "దశ 2: నిత్యజీవిత ఉదాహరణలు",
                    "items": [
                        {"label": "నడక", "value": "పాదాలు నేలను వెనక్కి నెడితే నేల మనల్ని ముందుకు నెట్టుతుంది"},
                        {"label": "ఈత", "value": "చేతులు నీటిని వెనక్కి నెడితే మనం ముందుకు వెళ్తాము"}
                    ],
                    "narration": "మనం నడవడం, ఈత కొట్టడం అన్నీ ఈ చర్య ప్రతిచర్య నియమంపైనే ఆధారపడి ఉంటాయి."
                },
                {
                    "type": "quiz",
                    "heading": "దశ 3: క్విజ్",
                    "question": "మీరు గోడను 50 న్యూటన్ల బలంతో నెడితే గోడ మీపై చూపే బలం ఎంత?",
                    "options": ["0 న్యూటన్లు", "25 న్యూటన్లు", "50 న్యూటన్లు", "100 న్యూటన్లు"],
                    "answer": "50 న్యూటన్లు",
                    "narration": "గోడ కూడా సరిగ్గా యాభై న్యూటన్ల బలాన్ని మీపై వ్యతిరేక దిశలో చూపుతుంది."
                }
            ]
        },
        "mr": {
            "title": "न्यूटनचा गतीचा तिसरा नियम",
            "level": "beginner",
            "language": "mr",
            "topic": "Newton's Third Law",
            "scenes": [
                {
                    "type": "title_card",
                    "heading": "न्यूटनचा गतीचा तिसरा नियम",
                    "subheading": "क्रिया आणि प्रतिक्रिया बले",
                    "narration": "प्रत्येक क्रियेला समान आणि विरुद्ध प्रतिक्रिया असते."
                },
                {
                    "type": "diagram",
                    "heading": "पायरी १: बल जोडी",
                    "items": [
                        {"label": "क्रिया", "value": "रॉकेट वायू खाली ढकलतो"},
                        {"label": "प्रतिक्रिया", "value": "वायू रॉकेटला वर ढकलतो"}
                    ],
                    "narration": "बले नेहमी जोडीने कार्य करतात. रॉकेट वायू खाली ढकलतो आणि वायू रॉकेटला वर उंचावतो."
                },
                {
                    "type": "summary",
                    "heading": "पायरी २: दैनंदिन उदाहरणे",
                    "items": [
                        {"label": "चालणे", "value": "पाय जमिनीला मागे ढकलतात, जमीन आपल्याला पुढे"},
                        {"label": "पोहणे", "value": "हात पाणी मागे ढकलतात, आपण पुढे जातो"}
                    ],
                    "narration": "चालणे आणि पोहणे ही सर्व न्यूटनच्या याच तिसऱ्या नियमावर अवलंबून आहेत."
                },
                {
                    "type": "quiz",
                    "heading": "पायरी ३: प्रश्न",
                    "question": "भिंतीवर ५० न्यूटन बल लावले तर भिंत किती बल लावेल?",
                    "options": ["० न्यूटन", "२५ न्यूटन", "५० न्यूटन", "१०० न्यूटन"],
                    "answer": "५० न्यूटन",
                    "narration": "भिंत देखील विरुद्ध दिशेने बरोबर पन्नास न्यूटन बल लावते."
                }
            ]
        },
        "bn": {
            "title": "নিউটনের গতির তৃতীয় সূত্র",
            "level": "beginner",
            "language": "bn",
            "topic": "Newton's Third Law",
            "scenes": [
                {
                    "type": "title_card",
                    "heading": "নিউটনের গতির তৃতীয় সূত্র",
                    "subheading": "ক্রিয়া ও প্রতিক্রিয়া বল",
                    "narration": "প্রত্যেক ক্রিয়ারই একটি সমান ও বিপরীত প্রতিক্রিয়া আছে।"
                },
                {
                    "type": "diagram",
                    "heading": "ধাপ ১: বলের জোড়া",
                    "items": [
                        {"label": "ক্রিয়া", "value": "রকেট গ্যাসকে নিচের দিকে ঠেলে"},
                        {"label": "প্রতিক্রিয়া", "value": "গ্যাস রকেটকে উপরের দিকে ঠেলে"}
                    ],
                    "narration": "বল সর্বদা জোড়ায় কাজ করে। রকেট যখন গ্যাস নির্গমন করে, গ্যাস রকেটকে শূন্যে উড়িয়ে নিয়ে যায়।"
                },
                {
                    "type": "summary",
                    "heading": "ধাপ ২: বাস্তব উদাহরণ",
                    "items": [
                        {"label": "হাঁটা", "value": "পা মাটিকে পেছনে ঠেলে, মাটি শরীরকে সামনে ঠেলে"},
                        {"label": "সাঁতার", "value": "হাত জলকে পেছনে ঠেলে, জল সাঁতারুকে এগিয়ে দেয়"}
                    ],
                    "narration": "আমাদের প্রতিটি পদক্ষেপ এবং সাঁতার এই ক্রিয়া ও প্রতিক্রিয়ার প্রাকৃতিক নিয়মে চলে।"
                },
                {
                    "type": "quiz",
                    "heading": "ধাপ ৩: কুইজ",
                    "question": "দেওয়ালে ৫০ নিউটন বল প্রয়োগ করলে দেওয়াল কত বল দেবে?",
                    "options": ["০ নিউটন", "২৫ নিউটন", "৫০ নিউটন", "১০০ নিউটন"],
                    "answer": "৫০ নিউটন",
                    "narration": "দেওয়ালও সমানভাবে বিপরীত দিকে পঞ্চাশ নিউটন বল প্রয়োগ করবে।"
                }
            ]
        }
    }
}

def get_fallback_lesson(topic: str, language: str = "en", level: str = "beginner") -> dict:
    """Finds the best matching fallback lesson or creates a structured one."""
    topic_clean = topic.lower().strip()
    lang = language.lower().strip()
    if lang not in ["en", "hi", "ta", "te", "mr", "bn"]:
        lang = "en"
    
    # 1. Direct key match
    for k in FALLBACK_LESSONS:
        if k in topic_clean or topic_clean in k:
            if lang in FALLBACK_LESSONS[k]:
                return FALLBACK_LESSONS[k][lang]
            return FALLBACK_LESSONS[k]["en"]
            
    # 2. Check for keywords
    if any(w in topic_clean for w in ["loop", "for", "while", "iteration", "code", "python"]):
        return FALLBACK_LESSONS["python loops"].get(lang, FALLBACK_LESSONS["python loops"]["en"])
    if any(w in topic_clean for w in ["photo", "plant", "leaf", "sun", "chlorophyll", "biology"]):
        return FALLBACK_LESSONS["photosynthesis"].get(lang, FALLBACK_LESSONS["photosynthesis"]["en"])
    if any(w in topic_clean for w in ["newton", "motion", "force", "physics", "action", "reaction"]):
        return FALLBACK_LESSONS["newton's laws"].get(lang, FALLBACK_LESSONS["newton's laws"]["en"])
        
    # 3. Dynamic well-structured generic fallback for any unknown topic
    capitalized_topic = topic.strip().title()
    if lang == "hi":
        return {
            "title": f"{capitalized_topic} की मूल अवधारणा",
            "level": level,
            "language": "hi",
            "topic": capitalized_topic,
            "scenes": [
                {
                    "type": "title_card",
                    "heading": f"{capitalized_topic} क्या है?",
                    "subheading": "सरल और स्पष्ट परिचय",
                    "narration": f"आज हम {capitalized_topic} के बारे में जानेंगे और इसके मुख्य सिद्धांतों को समझेंगे।"
                },
                {
                    "type": "diagram",
                    "heading": "चरण १: मुख्य संरचना",
                    "items": [
                        {"label": "चरण १", "value": "मूल विचार समझना"},
                        {"label": "चरण २", "value": "प्रक्रिया और कार्यप्रणाली"},
                        {"label": "चरण ३", "value": "वास्तविक जीवन में उपयोग"}
                    ],
                    "narration": f"{capitalized_topic} व्यवस्थित चरणों में काम करता है और जटिल समस्याओं को आसान बनाता है।"
                },
                {
                    "type": "summary",
                    "heading": "चरण २: मुख्य सारांश",
                    "items": [
                        {"label": "बिंदु १", "value": "अवधारणा की स्पष्टता"},
                        {"label": "बिंदु २", "value": "क्रमिक प्रगति"},
                        {"label": "बिंदु ३", "value": "व्यावहारिक अनुप्रयोग"}
                    ],
                    "narration": f"संक्षेप में, {capitalized_topic} को समझने से हमें बेहतर परिणाम और अंतर्दृष्टि मिलती है।"
                }
            ]
        }
    else:
        return {
            "title": f"Mastering {capitalized_topic}",
            "level": level,
            "language": "en",
            "topic": capitalized_topic,
            "scenes": [
                {
                    "type": "title_card",
                    "heading": f"Understanding {capitalized_topic}",
                    "subheading": "Core concept simplified",
                    "narration": f"Welcome! Today we explore {capitalized_topic} and discover how it works step by step."
                },
                {
                    "type": "diagram",
                    "heading": "Step 1: The Core Mechanism",
                    "items": [
                        {"label": "Phase 1", "value": "Initial State & Input Setup"},
                        {"label": "Phase 2", "value": "Active Processing Cycle"},
                        {"label": "Phase 3", "value": "Structured Output Delivery"}
                    ],
                    "narration": f"{capitalized_topic} operates in distinct stages, taking input conditions and transforming them smoothly."
                },
                {
                    "type": "summary",
                    "heading": "Step 2: Key Takeaways",
                    "items": [
                        {"label": "Clarity", "value": "Breaks complex problems into simple steps"},
                        {"label": "Efficiency", "value": "Produces predictable and verified results"},
                        {"label": "Foundation", "value": "Applies directly to real-world engineering"}
                    ],
                    "narration": f"By mastering the fundamentals of {capitalized_topic}, you can solve challenging problems with confidence."
                }
            ]
        }

