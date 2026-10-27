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


# Additional curated STEM & Computer Science topics
NEW_TOPICS = {'binary search': {'en': {'title': 'How Binary Search Works', 'level': 'beginner', 'language': 'en', 'topic': 'Binary Search', 'scenes': [{'type': 'title_card', 'heading': 'What is Binary Search?', 'subheading': 'Divide and conquer search algorithm', 'narration': 'Binary search finds an item in a sorted list by repeatedly dividing the search space in half.'}, {'type': 'code_walkthrough', 'heading': 'Step 1: Divide and Check', 'code': 'low = 0\nhigh = len(arr) - 1\nmid = (low + high) // 2\nif arr[mid] == target:\n    return mid', 'highlight_lines': [3, 4], 'output': 'Target found at index 2', 'narration': 'We check the middle element. If the target is smaller, we search left; otherwise, we search right.'}, {'type': 'diagram', 'heading': 'Step 2: Halving Search Space', 'items': [{'label': 'Pass 1', 'value': 'Compare mid: 8 items left'}, {'label': 'Pass 2', 'value': 'Discard half: 4 items left'}, {'label': 'Pass 3', 'value': 'Found in O(log n) time'}], 'narration': 'With every comparison, half the remaining elements are eliminated, making it much faster than linear search.'}, {'type': 'quiz', 'heading': 'Step 3: Quick Check', 'question': 'What is strictly required for binary search to work?', 'options': ['Sorted array', 'Small array', 'Only even numbers', 'No requirement'], 'answer': 'Sorted array', 'narration': 'Binary search strictly requires a sorted array so it can determine which half to discard.'}]}, 'hi': {'title': 'बाइनरी सर्च कैसे काम करता है', 'level': 'beginner', 'language': 'hi', 'topic': 'Binary Search', 'scenes': [{'type': 'title_card', 'heading': 'बाइनरी सर्च क्या है?', 'subheading': 'डिवाइड और कॉन्कर तकनीक', 'narration': 'बाइनरी सर्च एक क्रमित सूची में किसी तत्व को खोजने के लिए खोज क्षेत्र को बार-बार आधा करता है।'}, {'type': 'code_walkthrough', 'heading': 'चरण १: मध्य तत्व की जांच', 'code': 'low = 0\nhigh = len(arr) - 1\nmid = (low + high) // 2\nif arr[mid] == target:\n    return mid', 'highlight_lines': [3, 4], 'output': 'Target found at index 2', 'narration': 'हम मध्य इंडेक्स निकालते हैं और तुलना करके तय करते हैं कि बाईं ओर खोजना है या दाईं ओर।'}, {'type': 'diagram', 'heading': 'चरण २: खोज क्षेत्र को आधा करना', 'items': [{'label': 'पहला चरण', 'value': 'मध्य तत्व की तुलना'}, {'label': 'दूसरा चरण', 'value': 'आधा हिस्सा छोड़ना'}, {'label': 'तीसरा चरण', 'value': 'लघुगणकीय समय में लक्ष्य'}], 'narration': 'हर तुलना में आधे तत्व बाहर हो जाते हैं, जिससे यह लीनियर सर्च से कहीं अधिक तेज़ होता है।'}, {'type': 'quiz', 'heading': 'चरण ३: त्वरित प्रश्न', 'question': 'बाइनरी सर्च के लिए अनिवार्य शर्त क्या है?', 'options': ['सॉर्टेड सूची', 'छोटी सूची', 'केवल सम संख्याएं', 'कोई शर्त नहीं'], 'answer': 'सॉर्टेड सूची', 'narration': 'बाइनरी सर्च केवल तभी काम करता है जब सूची पहले से क्रमबद्ध या सॉर्ट की गई हो।'}]}}, 'gravity': {'en': {'title': 'Understanding Gravity', 'level': 'beginner', 'language': 'en', 'topic': 'Gravity', 'scenes': [{'type': 'title_card', 'heading': 'What is Gravity?', 'subheading': 'The universal attractive force', 'narration': 'Gravity is the fundamental force by which all physical objects with mass attract one another.'}, {'type': 'diagram', 'heading': 'Step 1: The Core Principles', 'items': [{'label': 'Mass', 'value': 'Greater mass creates stronger pull'}, {'label': 'Distance', 'value': 'Greater distance rapidly weakens pull'}, {'label': 'Orbits', 'value': 'Balances inertia to hold planets in orbit'}], 'narration': 'Newton showed that gravitational attraction depends directly on mass and inversely on distance squared.'}, {'type': 'summary', 'heading': 'Step 2: Key Takeaways', 'items': [{'label': 'Acceleration', 'value': 'Earth pulls objects at 9.8 meters per second squared'}, {'label': 'Ocean Tides', 'value': "Moon's gravity creates high and low tides"}, {'label': 'Atmosphere', 'value': 'Keeps air and oceans bound to planet Earth'}], 'narration': "Without gravity, the Earth's atmosphere, oceans, and living beings would drift away into space."}]}, 'hi': {'title': 'गुरुत्वाकर्षण बल कैसे काम करता है', 'level': 'beginner', 'language': 'hi', 'topic': 'Gravity', 'scenes': [{'type': 'title_card', 'heading': 'गुरुत्वाकर्षण क्या है?', 'subheading': 'ब्रह्मांडीय आकर्षण बल', 'narration': 'गुरुत्वाकर्षण वह अदृश्य बल है जो द्रव्यमान वाली सभी वस्तुओं को एक-दूसरे की ओर खींचता है।'}, {'type': 'diagram', 'heading': 'चरण १: मुख्य नियम', 'items': [{'label': 'द्रव्यमान', 'value': 'अधिक द्रव्यमान मतलब अधिक खिंचाव'}, {'label': 'दूरी', 'value': 'दूरी बढ़ने पर बल तेजी से घटता है'}, {'label': 'कक्षा', 'value': 'ग्रहों को सूर्य के चारों ओर बांधे रखता है'}], 'narration': 'न्यूटन के अनुसार गुरुत्वाकर्षण द्रव्यमान के समानुपाती और दूरी के वर्ग के व्युत्क्रमानुपाती होता है।'}, {'type': 'summary', 'heading': 'चरण २: मुख्य सारांश', 'items': [{'label': 'पृथ्वी का त्वरण', 'value': 'गिरती वस्तुओं पर 9.8 मीटर प्रति सेकंड वर्ग'}, {'label': 'ज्वार-भाटा', 'value': 'चंद्रमा के खिंचाव से समुद्र में लहरें'}, {'label': 'जीवन रक्षा', 'value': 'वायुमंडल को पृथ्वी की सतह पर बनाए रखना'}], 'narration': 'गुरुत्वाकर्षण के बिना वायुमंडल और महासागर अंतरिक्ष में विलीन हो जाएंगे।'}]}}, 'water cycle': {'en': {'title': 'How the Water Cycle Works', 'level': 'beginner', 'language': 'en', 'topic': 'Water Cycle', 'scenes': [{'type': 'title_card', 'heading': 'The Hydrological Cycle', 'subheading': "Earth's continuous water recycling system", 'narration': "The water cycle describes how water continuously circulates through Earth's oceans, atmosphere, and land."}, {'type': 'diagram', 'heading': 'Step 1: The Three Main Stages', 'items': [{'label': 'Evaporation', 'value': 'Solar heat turns liquid water into rising vapor'}, {'label': 'Condensation', 'value': 'Cooling vapor gathers to form clouds'}, {'label': 'Precipitation', 'value': 'Rain or snow falls back to nourish land'}], 'narration': 'Sunlight evaporates surface water into vapor, which cools into clouds and returns to ground as precipitation.'}, {'type': 'summary', 'heading': 'Step 2: Why It Matters', 'items': [{'label': 'Freshwater', 'value': 'Replenishes rivers, lakes, and drinking water'}, {'label': 'Climate', 'value': 'Transfers heat to regulate global climate'}, {'label': 'Ecosystems', 'value': 'Sustains plant and animal life worldwide'}], 'narration': "The water cycle naturally filters water and distributes rainfall across our planet's ecosystems."}]}, 'hi': {'title': 'जल चक्र कैसे काम करता है', 'level': 'beginner', 'language': 'hi', 'topic': 'Water Cycle', 'scenes': [{'type': 'title_card', 'heading': 'जल चक्र क्या है?', 'subheading': 'प्रकृति की निरंतर जल प्रणाली', 'narration': 'जल चक्र पृथ्वी, महासागरों और वायुमंडल के बीच पानी के निरंतर संचलन की प्रक्रिया है।'}, {'type': 'diagram', 'heading': 'चरण १: चक्र के मुख्य चरण', 'items': [{'label': 'वाष्पीकरण', 'value': 'सूर्य की गर्मी से जल वाष्प बनता है'}, {'label': 'संघनन', 'value': 'ठंडी वाष्प बादलों का रूप लेती है'}, {'label': 'वर्षा', 'value': 'वर्षा की बूंदें जमीन पर लौटती हैं'}], 'narration': 'सूर्य से पानी वाष्प बनकर ऊपर उठता है, बादलों में संघनित होता है, और वर्षा के रूप में धरती पर लौटता है।'}, {'type': 'summary', 'heading': 'चरण २: मुख्य लाभ', 'items': [{'label': 'ताजा पानी', 'value': 'नदियों और भूजल को फिर से भरना'}, {'label': 'मौसम नियंत्रण', 'value': 'धरती के तापमान को संतुलित रखना'}, {'label': 'जीवन रक्षा', 'value': 'कृषि और वन्यजीवों के लिए जीवनदायी'}], 'narration': 'जल चक्र हमारे ग्रह पर शुद्ध पानी उपलब्ध कराता है और पूरे पारिस्थितिकी तंत्र को जीवित रखता है।'}]}}, 'recursion': {'en': {'title': 'Understanding Recursion in Code', 'level': 'beginner', 'language': 'en', 'topic': 'Recursion', 'scenes': [{'type': 'title_card', 'heading': 'What is Recursion?', 'subheading': 'Functions calling themselves to solve problems', 'narration': 'Recursion is a programming technique where a function calls itself to solve smaller pieces of a problem.'}, {'type': 'code_walkthrough', 'heading': 'Step 1: The Factorial Function', 'code': 'def factorial(n):\n    if n <= 1:  # Base Case\n        return 1\n    return n * factorial(n - 1)', 'highlight_lines': [2, 4], 'output': 'factorial(3) = 3 * 2 * 1 = 6', 'narration': 'Every recursive function requires a base case to stop, and a recursive step that shrinks the input.'}, {'type': 'diagram', 'heading': 'Step 2: The Call Stack', 'items': [{'label': 'Call factorial(3)', 'value': 'Waits for factorial(2)'}, {'label': 'Call factorial(2)', 'value': 'Waits for factorial(1)'}, {'label': 'Base Case Reach', 'value': 'Returns 1 and unwinds stack'}], 'narration': 'Each call is pushed onto the stack until the base case returns, then values multiply on the way down.'}]}, 'hi': {'title': 'प्रोग्रामिंग में रिकर्शन कैसे काम करता है', 'level': 'beginner', 'language': 'hi', 'topic': 'Recursion', 'scenes': [{'type': 'title_card', 'heading': 'रिकर्शन क्या है?', 'subheading': 'स्वयं को कॉल करने वाला फंक्शन', 'narration': 'रिकर्शन एक ऐसी तकनीक है जिसमें कोई फंक्शन किसी समस्या को हल करने के लिए खुद को कॉल करता है।'}, {'type': 'code_walkthrough', 'heading': 'चरण १: फैक्टोरियल उदाहरण', 'code': 'def factorial(n):\n    if n <= 1:  # Base Case\n        return 1\n    return n * factorial(n - 1)', 'highlight_lines': [2, 4], 'output': 'factorial(3) = 6', 'narration': 'हर रिकर्सिव फंक्शन में रुकने के लिए एक बेस केस और खुद को कॉल करने वाला स्टेप होता है।'}, {'type': 'diagram', 'heading': 'चरण २: कॉल स्टैक समझना', 'items': [{'label': 'कॉल ३', 'value': 'factorial(2) का इंतज़ार'}, {'label': 'कॉल २', 'value': 'factorial(1) का इंतज़ार'}, {'label': 'बेस केस', 'value': 'मान लौटता है और स्टैक खाली होता है'}], 'narration': 'सभी फंक्शन कॉल्स मेमोरी स्टैक में जमा होते हैं और बेस केस आने पर क्रमिक रूप से हल होते हैं।'}]}}, 'git': {'en': {'title': 'How Git Version Control Works', 'level': 'beginner', 'language': 'en', 'topic': 'Git', 'scenes': [{'type': 'title_card', 'heading': 'What is Git?', 'subheading': 'Distributed version control system', 'narration': 'Git tracks changes in your source code across time, allowing teams to collaborate and rollback mistakes safely.'}, {'type': 'code_walkthrough', 'heading': 'Step 1: Core Workflow', 'code': "git status          # Check files\ngit add .           # Stage changes\ngit commit -m 'feat' # Save snapshot\ngit push origin main # Share with remote", 'highlight_lines': [2, 3], 'output': '[main 4a8b1c] feat: lesson engine ready', 'narration': 'You stage your changes with git add, and record a permanent historical snapshot with git commit.'}, {'type': 'diagram', 'heading': 'Step 2: The Three Git Areas', 'items': [{'label': 'Working Directory', 'value': 'Files you are actively editing'}, {'label': 'Staging Area', 'value': 'Prepared changes for next commit'}, {'label': 'Repository', 'value': 'Permanent commit snapshot history'}], 'narration': 'Code moves from your workspace into the staging area, and is sealed permanently into the repository.'}]}, 'hi': {'title': 'गिट वर्ज़न कंट्रोल कैसे काम करता है', 'level': 'beginner', 'language': 'hi', 'topic': 'Git', 'scenes': [{'type': 'title_card', 'heading': 'गिट क्या है?', 'subheading': 'वितरित वर्ज़न कंट्रोल प्रणाली', 'narration': 'गिट आपके कोड में होने वाले हर बदलाव का इतिहास रखता है ताकि टीम सुरक्षित रूप से काम कर सके।'}, {'type': 'code_walkthrough', 'heading': 'चरण १: मुख्य कमांड्स', 'code': "git status          # बदलाव देखें\ngit add .           # फाइलें स्टेज करें\ngit commit -m 'feat' # स्नैपशॉट सहेजें\ngit push origin main # सर्वर पर भेजें", 'highlight_lines': [2, 3], 'output': '[main 4a8b1c] feat: lesson engine ready', 'narration': 'गिट ऐड से फाइलें स्टेज की जाती हैं और गिट कमिट से उनका स्थायी रिकॉर्ड बन जाता है।'}, {'type': 'diagram', 'heading': 'चरण २: गिट के तीन क्षेत्र', 'items': [{'label': 'वर्किंग डायरेक्टरी', 'value': 'जहां आप फाइलें बदलते हैं'}, {'label': 'स्टेजिंग एरिया', 'value': 'कमिट के लिए तैयार फाइलें'}, {'label': 'कमिट इतिहास', 'value': 'सुरक्षित स्नैपशॉट का टाइमलाइन'}], 'narration': 'गिट कोड को वर्किंग डायरेक्टरी से स्टेजिंग एरिया और फिर कमिट इतिहास में सुरक्षित करता है।'}]}}, 'solar system': {'en': {'title': 'Exploring the Solar System', 'level': 'beginner', 'language': 'en', 'topic': 'Solar System', 'scenes': [{'type': 'title_card', 'heading': 'Our Cosmic Neighborhood', 'subheading': 'The Sun and orbiting planets', 'narration': 'The solar system consists of our central star, the Sun, and all celestial bodies bound to it by gravity.'}, {'type': 'diagram', 'heading': 'Step 1: Planetary Layout', 'items': [{'label': 'Inner Rocky', 'value': 'Mercury, Venus, Earth, and Mars'}, {'label': 'Asteroid Belt', 'value': 'Rocky boundary dividing orbital zones'}, {'label': 'Outer Giants', 'value': 'Jupiter, Saturn, Uranus, Neptune'}], 'narration': 'Four rocky planets orbit closest to the Sun, followed by four massive gas and ice giants.'}, {'type': 'summary', 'heading': 'Step 2: Key Facts', 'items': [{'label': "Sun's Mass", 'value': 'Contains 99.8 percent of all system mass'}, {'label': 'Habitable Zone', 'value': 'Earth is positioned where liquid water can exist'}, {'label': 'Orbital Motion', 'value': 'Gravity keeps all planets in synchronized motion'}], 'narration': "The Sun's enormous gravitational attraction keeps eight planets in stable elliptical orbits."}]}, 'hi': {'title': 'सौरमंडल कैसे काम करता है', 'level': 'beginner', 'language': 'hi', 'topic': 'Solar System', 'scenes': [{'type': 'title_card', 'heading': 'हमारा सौरमंडल', 'subheading': 'सूर्य और परिक्रमा करते ग्रह', 'narration': 'सौरमंडल में हमारे केंद्र में स्थित सूर्य और गुरुत्वाकर्षण से बंधे सभी आठ ग्रह शामिल हैं।'}, {'type': 'diagram', 'heading': 'चरण १: ग्रहों की संरचना', 'items': [{'label': 'आंतरिक ग्रह', 'value': 'बुध, शुक्र, पृथ्वी और मंगल'}, {'label': 'क्षुद्रग्रह पट्टी', 'value': 'चट्टानी पत्थरों का विशाल घेरा'}, {'label': 'बाह्य गैसीय ग्रह', 'value': 'बृहस्पति, शनि, यूरेनस और नेपच्यून'}], 'narration': 'सूर्य के सबसे करीब चार ठोस पथरीले ग्रह हैं, और उसके बाद चार विशाल गैसीय ग्रह स्थित हैं।'}, {'type': 'summary', 'heading': 'चरण २: मुख्य तथ्य', 'items': [{'label': 'सूर्य का भार', 'value': 'सौरमंडल के कुल द्रव्यमान का 99.8 प्रतिशत'}, {'label': 'गोल्डीलॉक्स ज़ोन', 'value': 'पृथ्वी पर तरल पानी और जीवन संभव'}, {'label': 'कक्षा का नियम', 'value': 'गुरुत्वाकर्षण सभी ग्रहों को व्यवस्थित रखता है'}], 'narration': 'सूर्य का शक्तिशाली गुरुत्वाकर्षण सभी ग्रहों को उनकी निर्धारित कक्षाओं में घुमाता है।'}]}}, "ohm's law": {'en': {'title': "Understanding Ohm's Law", 'level': 'beginner', 'language': 'en', 'topic': "Ohm's Law", 'scenes': [{'type': 'title_card', 'heading': "What is Ohm's Law?", 'subheading': 'The foundation of electrical circuits', 'narration': "Ohm's Law states that current through a conductor is proportional to voltage and inversely proportional to resistance."}, {'type': 'diagram', 'heading': 'Step 1: The V = I * R Triangle', 'items': [{'label': 'Voltage (V)', 'value': 'Electrical potential pushing charges (Volts)'}, {'label': 'Current (I)', 'value': 'Rate of electron charge flow (Amperes)'}, {'label': 'Resistance (R)', 'value': 'Opposition to electrical charge flow (Ohms)'}], 'narration': 'Voltage provides the push, current is the electron flow, and resistance opposes that flow.'}, {'type': 'quiz', 'heading': 'Step 2: Circuit Calculation', 'question': 'If Voltage is 10V and Resistance is 5 Ohms, what is Current?', 'options': ['2 Amperes', '50 Amperes', '0.5 Amperes', '5 Amperes'], 'answer': '2 Amperes', 'narration': 'Using the formula I equals V divided by R, ten volts divided by five ohms gives two amperes.'}]}, 'hi': {'title': 'ओम का नियम कैसे काम करता है', 'level': 'beginner', 'language': 'hi', 'topic': "Ohm's Law", 'scenes': [{'type': 'title_card', 'heading': 'ओम का नियम क्या है?', 'subheading': 'विद्युत परिपथ का आधार', 'narration': 'ओम के नियम के अनुसार किसी चालक में प्रवाहित धारा वोल्टेज के समानुपाती और प्रतिरोध के व्युत्क्रमानुपाती होती है।'}, {'type': 'diagram', 'heading': 'चरण १: सूत्र V = I * R', 'items': [{'label': 'वोल्टेज (V)', 'value': 'इलेक्ट्रॉनों को धक्का देने वाला विद्युत विभव'}, {'label': 'धारा (I)', 'value': 'आवेश प्रवाह की दर (एम्पीयर)'}, {'label': 'प्रतिरोध (R)', 'value': 'विद्युत धारा के मार्ग में रुकावट (ओम)'}], 'narration': 'वोल्टेज धक्का देता है, धारा इलेक्ट्रॉनों का प्रवाह है, और प्रतिरोध इस प्रवाह का विरोध करता है।'}, {'type': 'quiz', 'heading': 'चरण २: त्वरित गणना', 'question': 'यदि वोल्टेज 10V और प्रतिरोध 5 ओम है, तो धारा क्या होगी?', 'options': ['2 एम्पीयर', '50 एम्पीयर', '0.5 एम्पीयर', '5 एम्पीयर'], 'answer': '2 एम्पीयर', 'narration': 'सूत्र I बराबर V भाग R से, 10 भाग 5 का परिणाम दो एम्पीयर होता है।'}]}}, 'machine learning': {'en': {'title': 'How Machine Learning Works', 'level': 'beginner', 'language': 'en', 'topic': 'Machine Learning', 'scenes': [{'type': 'title_card', 'heading': 'What is Machine Learning?', 'subheading': 'Computers learning patterns from data', 'narration': 'Machine learning enables computers to learn patterns directly from data to make decisions without explicit programming.'}, {'type': 'diagram', 'heading': 'Step 1: The Learning Pipeline', 'items': [{'label': 'Training Data', 'value': 'Feeding real-world examples to model'}, {'label': 'Pattern Learning', 'value': 'Adjusting internal weights to reduce error'}, {'label': 'Inference', 'value': 'Predicting accurate outputs for new inputs'}], 'narration': 'The model studies thousands of data samples, adjusts its internal weights, and learns to make accurate predictions.'}, {'type': 'summary', 'heading': 'Step 2: Key Takeaways', 'items': [{'label': 'Supervised', 'value': 'Learns from labeled examples with ground truth'}, {'label': 'Unsupervised', 'value': 'Discovers natural clusters in unlabeled data'}, {'label': 'Real World', 'value': 'Powers speech recognition, vision, and healthcare'}], 'narration': 'Machine learning powers modern innovations like voice assistants, recommendation engines, and robotics.'}]}, 'hi': {'title': 'मशीन लर्निंग कैसे काम करती है', 'level': 'beginner', 'language': 'hi', 'topic': 'Machine Learning', 'scenes': [{'type': 'title_card', 'heading': 'मशीन लर्निंग क्या है?', 'subheading': 'डेटा से पैटर्न सीखने वाले कंप्यूटर', 'narration': 'मशीन लर्निंग कंप्यूटर को बिना सीधे कोड किए डेटा से पैटर्न सीखकर निर्णय लेने की क्षमता देती है।'}, {'type': 'diagram', 'heading': 'चरण १: सीखने की प्रक्रिया', 'items': [{'label': 'प्रशिक्षण डेटा', 'value': 'मॉडल को वास्तविक उदाहरण प्रदान करना'}, {'label': 'पैटर्न पहचान', 'value': 'त्रुटि घटाने के लिए भार समायोजित करना'}, {'label': 'अनुमान', 'value': 'नए डेटा पर सटीक परिणाम देना'}], 'narration': 'मॉडल हज़ारों उदाहरणों का अध्ययन करता है और नए इनपुट पर सटीक भविष्यवाणी करना सीख जाता है।'}, {'type': 'summary', 'heading': 'चरण २: मुख्य सारांश', 'items': [{'label': 'सुपरवाइज्ड', 'value': 'लेबल किए गए सही उत्तरों से सीखना'}, {'label': 'अनसुपरवाइज्ड', 'value': 'डेटा में छिपे समूहों की खोज'}, {'label': 'अनुप्रयोग', 'value': 'आवाज़ पहचान और चिकित्सा निदान में उपयोग'}], 'narration': 'मशीन लर्निंग आज वॉयस असिस्टेंट, सिफारिश प्रणाली और आधुनिक तकनीक को शक्ति देती है।'}]}}, 'cell biology': {'en': {'title': 'Understanding Cell Biology', 'level': 'beginner', 'language': 'en', 'topic': 'Cell Biology', 'scenes': [{'type': 'title_card', 'heading': 'The Building Block of Life', 'subheading': 'How living cells function', 'narration': 'Cells are the fundamental microscopic building blocks that carry out all essential biological processes of living things.'}, {'type': 'diagram', 'heading': 'Step 1: Key Cellular Organelles', 'items': [{'label': 'Membrane', 'value': 'Protective barrier controlling transport'}, {'label': 'Nucleus', 'value': 'Command center storing DNA genetic instructions'}, {'label': 'Mitochondria', 'value': 'Cellular powerhouse generating ATP energy'}], 'narration': 'The membrane guards the cell, the nucleus stores genetic instructions, and mitochondria produce essential energy.'}, {'type': 'summary', 'heading': 'Step 2: Key Takeaways', 'items': [{'label': 'Cell Theory', 'value': 'All living organisms are made of one or more cells'}, {'label': 'Energy Creation', 'value': 'Cellular respiration converts glucose into ATP'}, {'label': 'Division', 'value': 'Cells divide through mitosis for growth and repair'}], 'narration': 'Understanding cell biology explains the mechanisms of growth, energy, and life across all organisms.'}]}, 'hi': {'title': 'कोशिका विज्ञान कैसे काम करता है', 'level': 'beginner', 'language': 'hi', 'topic': 'Cell Biology', 'scenes': [{'type': 'title_card', 'heading': 'जीवन की मूल इकाई: कोशिका', 'subheading': 'सजीव कोशिकाओं की कार्यप्रणाली', 'narration': 'कोशिका सभी जीवित प्राणियों की सबसे छोटी और मूलभूत इकाई है जो जीवन की सभी क्रियाएं करती है।'}, {'type': 'diagram', 'heading': 'चरण १: मुख्य कोशिकांग', 'items': [{'label': 'कोशिका झिल्ली', 'value': 'सामग्री के आने-जाने पर नियंत्रण'}, {'label': 'केंद्रक', 'value': 'डीएनए और आनुवंशिक जानकारी का भंडार'}, {'label': 'माइटोकॉन्ड्रिया', 'value': 'ऊर्जा गृह जो एटीपी ऊर्जा बनाता है'}], 'narration': 'झिल्ली रक्षा करती है, केंद्रक में डीएनए सुरक्षित रहता है, और माइटोकॉन्ड्रिया ऊर्जा उत्पन्न करता है।'}, {'type': 'summary', 'heading': 'चरण २: मुख्य सारांश', 'items': [{'label': 'कोशिका सिद्धांत', 'value': 'सभी जीवित प्राणी कोशिकाओं से मिलकर बने हैं'}, {'label': 'श्वसन प्रक्रिया', 'value': 'पोषक तत्वों को ऊर्जा में बदलना'}, {'label': 'कोशिका विभाजन', 'value': 'वृद्धि और मरम्मत के लिए नई कोशिकाएं'}], 'narration': 'कोशिका विज्ञान को समझकर हम जीवन के बुनियादी रहस्यों और स्वास्थ्य को गहराई से समझ सकते हैं।'}]}}}

FALLBACK_LESSONS.update(NEW_TOPICS)


def get_curated_fallback(topic: str, language: str = "en") -> dict | None:
    """Returns a curated high-quality lesson if topic matches our verified library, else None."""
    topic_clean = topic.lower().strip()
    lang = language.lower().strip()
    if lang not in ["en", "hi", "ta", "te", "mr", "bn"]:
        lang = "en"

    # 1. Direct key match
    for k in FALLBACK_LESSONS:
        if k in topic_clean or topic_clean in k:
            return FALLBACK_LESSONS[k].get(lang, FALLBACK_LESSONS[k].get("en"))

    # 2. Semantic keyword match
    kw_map = [
        (["loop", "while", "iteration", "for loop"], "python loops"),
        (["photo", "chlorophyll", "plant", "leaf"], "photosynthesis"),
        (["newton", "motion", "action reaction", "third law"], "newton's laws"),
        (["binary search", "bsearch", "halving search"], "binary search"),
        (["gravity", "gravitation", "orbit", "planetary pull"], "gravity"),
        (["water cycle", "hydrological", "rain", "evaporation", "cloud"], "water cycle"),
        (["recursion", "recursive", "factorial", "call stack"], "recursion"),
        (["git", "github", "version control", "commit", "branch"], "git"),
        (["solar system", "planet", "jupiter", "mars", "sun"], "solar system"),
        (["ohm", "circuit", "voltage", "resistance", "electric current"], "ohm's law"),
        (["machine learning", "neural", "ai model", "artificial intelligence", "ml"], "machine learning"),
        (["cell", "mitochondria", "organelle", "cell biology", "nucleus"], "cell biology")
    ]
    for keywords, target_key in kw_map:
        if any(w in topic_clean for w in keywords):
            if target_key in FALLBACK_LESSONS:
                return FALLBACK_LESSONS[target_key].get(lang, FALLBACK_LESSONS[target_key].get("en"))

    return None


def get_dynamic_fallback(topic: str, language: str = "en", level: str = "beginner") -> dict:
    """Intelligently generates topic-specific educational scenes for any novel topic."""
    capitalized_topic = topic.strip().title()
    topic_lower = topic.lower().strip()
    lang = language.lower().strip()
    if lang not in ["en", "hi", "ta", "te", "mr", "bn"]:
        lang = "en"

    is_cs = any(k in topic_lower for k in [
        "code", "program", "algorithm", "data", "tree", "graph", "hash", "sql", "linux",
        "docker", "api", "crypto", "stack", "queue", "function", "array", "compiler",
        "pointer", "oop", "class", "sort", "search", "variable", "string", "database", "web", "server"
    ])
    is_physics = any(k in topic_lower for k in [
        "physics", "quantum", "black hole", "force", "energy", "motion", "thermo", "heat",
        "relativity", "magnet", "wave", "light", "optics", "sound", "velocity", "atom", "nuclear"
    ])
    is_bio_chem = any(k in topic_lower for k in [
        "bio", "biology", "chem", "cell", "dna", "gene", "protein", "enzyme", "plant", "animal",
        "human", "body", "organ", "heart", "brain", "reaction", "acid", "base", "molecule", "eco", "evolution", "virus"
    ])

    if lang == "hi":
        if is_cs:
            return {
                "title": f"{capitalized_topic} कैसे काम करता है",
                "level": level,
                "language": "hi",
                "topic": capitalized_topic,
                "scenes": [
                    {
                        "type": "title_card",
                        "heading": f"{capitalized_topic} क्या है?",
                        "subheading": "संगणक विज्ञान की महत्वपूर्ण अवधारणा",
                        "narration": f"{capitalized_topic} सॉफ्टवेयर इंजीनियरिंग में डेटा और प्रक्रियाओं को प्रबंधित करने की महत्वपूर्ण तकनीक है।"
                    },
                    {
                        "type": "diagram",
                        "heading": "चरण १: प्रक्रियात्मक प्रवाह",
                        "items": [
                            {"label": "१. इनपुट डेटा", "value": f"{capitalized_topic} के लिए इनपुट प्राप्त करना"},
                            {"label": "२. लॉजिक निष्पादन", "value": "नियमों के अनुसार डेटा प्रोसेस करना"},
                            {"label": "३. सटीक आउटपुट", "value": "सत्यापित और सुरक्षित परिणाम देना"}
                        ],
                        "narration": f"{capitalized_topic} में प्रत्येक निर्देश को क्रमिक रूप से निष्पादित किया जाता है ताकि सही परिणाम प्राप्त हो सके।"
                    },
                    {
                        "type": "summary",
                        "heading": "चरण २: मुख्य सारांश",
                        "items": [
                            {"label": "दक्षता", "value": "समय और मेमोरी की बचत"},
                            {"label": "विश्वसनीयता", "value": "त्रुटियों को कम करना"},
                            {"label": "व्यावहारिक उपयोग", "value": "आधुनिक सॉफ्टवेयर में आवश्यक"}
                        ],
                        "narration": f"संक्षेप में, {capitalized_topic} को समझने से जटिल सॉफ्टवेयर समस्याओं को आसानी से हल किया जा सकता है।"
                    }
                ]
            }
        elif is_physics:
            return {
                "title": f"{capitalized_topic} का भौतिक विज्ञान",
                "level": level,
                "language": "hi",
                "topic": capitalized_topic,
                "scenes": [
                    {
                        "type": "title_card",
                        "heading": f"{capitalized_topic} क्या है?",
                        "subheading": "प्रकृति के भौतिक नियम",
                        "narration": f"{capitalized_topic} ब्रह्मांड में ऊर्जा और पदार्थ के बीच होने वाले व्यवहार को समझाने वाला महत्वपूर्ण सिद्धांत है।"
                    },
                    {
                        "type": "diagram",
                        "heading": "चरण १: भौतिक प्रक्रिया",
                        "items": [
                            {"label": "१. मूल कारण", "value": f"{capitalized_topic} को सक्रिय करने वाले बल"},
                            {"label": "२. ऊर्जा हस्तांतरण", "value": "ऊर्जा का एक रूप से दूसरे में रूपांतरण"},
                            {"label": "३. अंतिम प्रभाव", "value": "प्रकृति में दिखने वाला संतुलन"}
                        ],
                        "narration": "इस सिद्धांत में ऊर्जा का रूपांतरण होता है और वस्तुएं निश्चित भौतिक नियमों के अनुसार व्यवहार करती हैं।"
                    },
                    {
                        "type": "summary",
                        "heading": "चरण २: मुख्य सारांश",
                        "items": [
                            {"label": "नियम", "value": "सार्वभौमिक रूप से लागू"},
                            {"label": "संरक्षण", "value": "ऊर्जा और संवेग का संरक्षण"},
                            {"label": "उपयोग", "value": "आधुनिक तकनीक और अंतरिक्ष विज्ञान"}
                        ],
                        "narration": f"{capitalized_topic} के नियमों को जानकर हम प्राकृतिक घटनाओं और उन्नत तकनीक को समझ सकते हैं।"
                    }
                ]
            }
        elif is_bio_chem:
            return {
                "title": f"{capitalized_topic} की वैज्ञानिक संरचना",
                "level": level,
                "language": "hi",
                "topic": capitalized_topic,
                "scenes": [
                    {
                        "type": "title_card",
                        "heading": f"{capitalized_topic} क्या है?",
                        "subheading": "जीवन और रसायन का विज्ञान",
                        "narration": f"{capitalized_topic} सजीवों में होने वाली रासायनिक और जैविक प्रक्रियाओं को संचालित करने का माध्यम है।"
                    },
                    {
                        "type": "diagram",
                        "heading": "चरण १: जैविक चक्र",
                        "items": [
                            {"label": "१. प्रारंभिक अणु", "value": f"{capitalized_topic} के लिए आवश्यक घटक"},
                            {"label": "२. जैव-रासायनिक क्रिया", "value": "एंजाइम और उत्प्रेरक द्वारा रूपांतरण"},
                            {"label": "३. जीवनदायी उत्पाद", "value": "शरीर के लिए आवश्यक ऊर्जा व वृद्धि"}
                        ],
                        "narration": "यह प्रक्रिया आवश्यक घटकों को उपयोगी ऊर्जा और संरचनात्मक अणुओं में परिवर्तित करती है।"
                    },
                    {
                        "type": "summary",
                        "heading": "चरण २: मुख्य सारांश",
                        "items": [
                            {"label": "जैविक महत्व", "value": "कोशिकाओं और जीवन के लिए अनिवार्य"},
                            {"label": "संतुलन", "value": "शरीर में समस्थिति बनाए रखना"},
                            {"label": "अनुसंधान", "value": "चिकित्सा और स्वास्थ्य विज्ञान में आधार"}
                        ],
                        "narration": f"{capitalized_topic} का अध्ययन स्वास्थ्य, चिकित्सा और प्राकृतिक जीवन को समझने की कुंजी है।"
                    }
                ]
            }
        else:
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
                            {"label": "१. आधार", "value": f"{capitalized_topic} के मूलभूत सिद्धांत"},
                            {"label": "२. कार्यविधि", "value": "प्रणाली की मुख्य कार्यप्रणाली"},
                            {"label": "३. अनुप्रयोग", "value": "वास्तविक जीवन में उपयोग"}
                        ],
                        "narration": f"{capitalized_topic} व्यवस्थित चरणों में काम करता है और व्यावहारिक जीवन में उपयोगी समाधान देता है।"
                    },
                    {
                        "type": "summary",
                        "heading": "चरण २: मुख्य सारांश",
                        "items": [
                            {"label": "स्पष्टता", "value": "जटिल अवधारणाओं का सरलीकरण"},
                            {"label": "उपयोग", "value": "दैनिक समस्याओं का वैज्ञानिक समाधान"},
                            {"label": "निष्कर्ष", "value": "बेहतर समझ और नवाचार"}
                        ],
                        "narration": f"संक्षेप में, {capitalized_topic} को समझने से हमें बेहतर परिणाम और रचनात्मक अंतर्दृष्टि मिलती है।"
                    }
                ]
            }
    else:
        # English dynamic fallback
        if is_cs:
            return {
                "title": f"How {capitalized_topic} Works",
                "level": level,
                "language": "en",
                "topic": capitalized_topic,
                "scenes": [
                    {
                        "type": "title_card",
                        "heading": f"Understanding {capitalized_topic}",
                        "subheading": "Core concept in computer science",
                        "narration": f"{capitalized_topic} is an essential computing concept used to organize data and execute operations reliably."
                    },
                    {
                        "type": "diagram",
                        "heading": "Step 1: The Execution Flow",
                        "items": [
                            {"label": "1. Input Data", "value": f"Receive and validate inputs for {capitalized_topic}"},
                            {"label": "2. Core Logic", "value": "Execute deterministic algorithmic instructions"},
                            {"label": "3. Validated Output", "value": "Return optimal computed result"}
                        ],
                        "narration": f"{capitalized_topic} processes inputs through structured computational steps to produce predictable, error-free results."
                    },
                    {
                        "type": "summary",
                        "heading": "Step 2: Key Takeaways",
                        "items": [
                            {"label": "Efficiency", "value": "Minimizes time and memory consumption"},
                            {"label": "Modularity", "value": "Enables scalable software architectures"},
                            {"label": "Application", "value": "Found across web, operating systems, and databases"}
                        ],
                        "narration": f"Mastering {capitalized_topic} empowers developers to build efficient, scalable, and resilient software."
                    }
                ]
            }
        elif is_physics:
            return {
                "title": f"The Physics of {capitalized_topic}",
                "level": level,
                "language": "en",
                "topic": capitalized_topic,
                "scenes": [
                    {
                        "type": "title_card",
                        "heading": f"Exploring {capitalized_topic}",
                        "subheading": "Fundamental laws of the physical universe",
                        "narration": f"{capitalized_topic} describes how energy, forces, and matter interact across time and space."
                    },
                    {
                        "type": "diagram",
                        "heading": "Step 1: The Physical Mechanism",
                        "items": [
                            {"label": "1. Underlying Force", "value": f"Initial forces driving {capitalized_topic}"},
                            {"label": "2. Energy Exchange", "value": "Dynamic transfer between potential and kinetic states"},
                            {"label": "3. Equilibrium", "value": "Stable physical state reached in nature"}
                        ],
                        "narration": f"Through {capitalized_topic}, physical forces transfer energy until the system reaches a natural equilibrium."
                    },
                    {
                        "type": "summary",
                        "heading": "Step 2: Key Takeaways",
                        "items": [
                            {"label": "Conservation", "value": "Energy and momentum remain strictly conserved"},
                            {"label": "Universality", "value": "Applies across Earth and deep cosmological space"},
                            {"label": "Engineering", "value": "Enables aerospace, robotics, and energy systems"}
                        ],
                        "narration": f"The principles of {capitalized_topic} form the cornerstone of modern engineering and astrophysics."
                    }
                ]
            }
        elif is_bio_chem:
            return {
                "title": f"Understanding {capitalized_topic}",
                "level": level,
                "language": "en",
                "topic": capitalized_topic,
                "scenes": [
                    {
                        "type": "title_card",
                        "heading": f"What is {capitalized_topic}?",
                        "subheading": "Biological and chemical processes of life",
                        "narration": f"{capitalized_topic} is a vital scientific mechanism that regulates cellular function and biological chemistry."
                    },
                    {
                        "type": "diagram",
                        "heading": "Step 1: The Biological Pathway",
                        "items": [
                            {"label": "1. Raw Precursors", "value": f"Essential compounds required for {capitalized_topic}"},
                            {"label": "2. Catalytic Action", "value": "Enzymatic reaction driving the transformation"},
                            {"label": "3. Vital Products", "value": "Yields energy and building blocks for organisms"}
                        ],
                        "narration": f"{capitalized_topic} converts precursor molecules into functional biological products to sustain living systems."
                    },
                    {
                        "type": "summary",
                        "heading": "Step 2: Key Takeaways",
                        "items": [
                            {"label": "Homeostasis", "value": "Maintains chemical balance inside organisms"},
                            {"label": "Vitality", "value": "Drives growth, cellular repair, and respiration"},
                            {"label": "Medicine", "value": "Crucial for therapeutics, vaccines, and health"}
                        ],
                        "narration": f"Understanding {capitalized_topic} gives us profound insights into medicine, genetics, and the origin of life."
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
                            {"label": "1. Foundation", "value": f"Fundamental premise behind {capitalized_topic}"},
                            {"label": "2. Operation", "value": "Active mechanism driving the system"},
                            {"label": "3. Application", "value": "Practical outcomes in real-world environments"}
                        ],
                        "narration": f"{capitalized_topic} operates in distinct stages, taking input conditions and transforming them smoothly."
                    },
                    {
                        "type": "summary",
                        "heading": "Step 2: Key Takeaways",
                        "items": [
                            {"label": "Clarity", "value": "Breaks complex problems into simple steps"},
                            {"label": "Efficiency", "value": "Produces predictable and verified results"},
                            {"label": "Impact", "value": "Applies directly to modern science and engineering"}
                        ],
                        "narration": f"By mastering the fundamentals of {capitalized_topic}, you can solve challenging problems with confidence."
                    }
                ]
            }


def get_fallback_lesson(topic: str, language: str = "en", level: str = "beginner") -> dict:
    """Finds best matching curated fallback or builds a dynamic topic-tailored lesson."""
    curated = get_curated_fallback(topic, language=language)
    if curated:
        return curated
    return get_dynamic_fallback(topic, language=language, level=level)
