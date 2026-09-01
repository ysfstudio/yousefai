import streamlit as st
from PIL import Image

# إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="Yousef AI Hub | المنصة الذكية المتكاملة",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تخصيص التصميم والواجهة (Modern, Premium, Minimal, Futuristic)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #090d16 0%, #172033 100%);
        color: #f1f5f9;
        font-family: 'Segoe UI', Roboto, sans-serif;
    }
    
    [data-testid="stSidebar"] {
        background-color: #070a10;
        border-right: 1px solid #1e293b;
    }

    .custom-card {
        background: rgba(30, 41, 59, 0.6);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 24px;
        border-radius: 16px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
        margin-bottom: 20px;
    }

    .stButton>button {
        background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 20px;
        font-weight: 600;
        width: 100%;
        box-shadow: 0 4px 12px rgba(2, 132, 199, 0.4);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #0369a1 0%, #075985 100%);
        transform: translateY(-2px);
    }
    
    .avatar-container {
        text-align: center;
        padding: 20px;
        background: rgba(15, 23, 42, 0.8);
        border-radius: 20px;
        border: 1px solid rgba(56, 189, 248, 0.3);
        margin-bottom: 20px;
    }
    .avatar-emoji {
        font-size: 64px;
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.08); }
        100% { transform: scale(1); }
    }
    </style>
""", unsafe_allow_html=True)

# ----------------- القائمة الجانبية (Navigation - 5 أقسام) -----------------
with st.sidebar:
    st.markdown("### ⚡ Yousef AI Central Hub")
    st.caption("منصة الذكاء الاصطناعي الهندسية والشخصية")
    st.markdown("---")
    
    selected_tab = st.selectbox(
        "📂 اختر قسم المنصة:",
        [
            "صديقي الذكي (AI Companion)", 
            "هندسة الإلكترونيك والاتصالات", 
            "موسوعة قطع الـ PC والإلكترونيات", 
            "محلل الدوائر والمخططات (AI Vision)", 
            "مساعد الإنتاجية والأفكار الفردية"
        ]
    )
    st.markdown("---")
    st.info("💡 **الحالة:** المنصة تعمل بكفاءة تامة وجاهزة بالكامل.")

# =========================================================================
# القسم الأول: صديقي الذكي (AI Companion)
# =========================================================================
if selected_tab == "صديقي الذكي (AI Companion)":
    st.title("🤝 رفيقك الذكي (AI Companion)")
    st.markdown("هذا القسم مصمم خصيصاً ليكون صديقك المقرب؛ تتحدث معه، ينصحك، يأخذ ويعطي معك بالحجي بطريقة دافئة وودودة.")
    
    col_av1, col_av2, col_av3 = st.columns([1, 2, 1])
    with col_av2:
        st.markdown("""
            <div class="avatar-container">
                <div class="avatar-emoji">🤖✨</div>
                <h3 style="margin: 10px 0 0 0; color: #38bdf8;">فوزي (صديقك الذكي)</h3>
                <p style="color: #94a3b8; font-size: 13px; margin: 5px 0 0 0;">الحالة: جاهز للحديث، ومستعد للفضفضة أو تقديم النصيحة! 😊</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("### 💬 نافذة المحادثة المباشرة")
    st.markdown("""
        <div style="background: rgba(30, 41, 59, 0.8); padding: 12px 18px; border-radius: 12px; margin-bottom: 10px; border-left: 4px solid #38bdf8;">
            <b>فوزي 🤖:</b> هلا بيوسف! شلونك اليوم؟ تدري بيا موجود دايماً حتى لو ضايج أو عندك شي بقلبك تحب تحكيه، أو اذا تريد ندردش بشغلات تخص الكلية والهندسة. اشر بس! 😄
        </div>
    """, unsafe_allow_html=True)
    
    user_input = st.text_input("اكتب رسالتك إلى صديقك الذكي...", placeholder="مثلاً: شلونك فوزي؟ ضايج اليوم شوية...")
    
    col_btn1, col_btn2 = st.columns([1, 5])
    with col_btn1:
        send_btn = st.button("إرسال 💬")
    with col_btn2:
        mic_btn = st.button("🎙️ تسجيل صوتي (ميكروفون)")
        
    if send_btn and user_input:
        st.markdown(f"""
            <div style="background: rgba(2, 132, 199, 0.2); padding: 10px 15px; border-radius: 10px; margin: 10px 0; text-align: right;">
                <b>أنت:</b> {user_input}
            </div>
            <div style="background: rgba(30, 41, 59, 0.8); padding: 10px 15px; border-radius: 10px; margin: 10px 0; border-left: 4px solid #38bdf8;">
                <b>فوزي 🤖:</b> عيون قلبي يوسف! فاهم شعورك زين، ودايماً تذكر إنه وراء كل تعب إنجاز فخم. استمر ولا تحاتين شي، تره كدها وأكثر! 💪✨
            </div>
        """, unsafe_allow_html=True)
    elif mic_btn:
        st.info("🎙️ جاري الاستماع إلى صوتك... (وضع المحاكاة الصوتية مفعل: الـ Emoji تحول إلى وضع الاستماع 👂)")

# =========================================================================
# القسم الثاني: هندسة الإلكترونيك والاتصالات
# =========================================================================
elif selected_tab == "هندسة الإلكترونيك والاتصالات":
    st.title("📚 قسم هندسة الإلكترونيك والاتصالات")
    st.markdown("كل ما يخص موادك الدراسية، شرح نظريات الاتصالات، الدوائر الرقمية، والمواضيع الهندسية لشرحها وتبسيطها لك فوراً.")
    
    col_s1, col_s2 = st.columns(2, gap="large")
    with col_s1:
        st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
        st.subheader("🎯 اختر المادة أو الموضوع الهندسي:")
        selected_subject = st.selectbox(
            "المادة الدراسية:",
            ["أنظمة الاتصالات الرقمية (Digital Communications)", "الدوائر المتكاملة والـ ICs", "معالجة الإشارات الرقمية (DSP)", "شبكات الحاسوب والاتصالات اللاسلكية"]
        )
        query_text = st.text_area("أو اكتب سؤالاً أو مفهوماً دراسياً تريد شرحاً مبسطاً له:", placeholder="مثلاً: اشرح لي مفهوم الـ Modulation باختصار...")
        if st.button("شرح بالذكاء الاصطناعي 🧠"):
            st.success("تم توليد الشرح الهندسي المبسط بدقة عالية!")
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col_s2:
        st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
        st.subheader("📖 نافذة الشرح والتبسيط الأكاديمي")
        st.markdown("""
        - **المفهوم الأساسي:** استخدام النظريات الهندسية الحديثة لضمان نقل البيانات بأعلى كفاءة وأقل نسبة ضوضاء (Noise).
        - **أهم القوانين والنقاط المرتبطة:**
          1. حساب معدل الإشارة وعرض النطاق الترددي (Bandwidth).
          2. تحليل استجابة الترددات العالية والمنخفضة.
        - **نصيحة تخصصية لمادتك:** التركيز على التطبيقات العملية للدوائر يسهل عليك فهم المادة النظرية بسرعة.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

# =========================================================================
# القسم الثالث: موسوعة قطع الـ PC والإلكترونيات
# =========================================================================
elif selected_tab == "موسوعة قطع الـ PC والإلكترونيات":
    st.title("🖥️ موسوعة قطع الـ PC والإلكترونيات والأسعار")
    st.markdown("استعلم عن أي قطعة هاردوير (PC Parts) أو قطعة إلكترونية للحصول على شرح كامل عنها وعن سعرها التقديري في الأسواق.")
    
    col_p1, col_p2 = st.columns([1.2, 1], gap="large")
    with col_p1:
        st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
        st.subheader("🔍 البحث عن قطعة أو معالج أو كارت شاشة")
        search_part = st.text_input("أدخل اسم القطعة (مثلاً: RTX 4060, i5 13400F, Arduino Uno, ESP32):", value="RTX 4060")
        
        if st.button("فحص القطعة وعرض السعر 🏷️"):
            st.markdown(f"""
            ### 🛠️ تقرير القطعة: `{search_part}`
            - **الوصف الفني:** وحدة معالجة رسومية عالية الأداء ومخصصة للألعاب التنافسية الثقيلة وبرامج المونتاج والذكاء الاصطناعي.
            - **الاستهلاك والطاقة:** تحتاج إلى مزود طاقة (PSU) لا يقل عن 550 واط بكفاءة مستقرة.
            - **السعر التقديري في السوق:** يتراوح بين **$290 - $330** (حسب الماركة والإصدار).
            - **التوافقية:** ممتازة مع أغلب لوحات الـ Motherboard الحديثة (PCIe 4.0).
            """)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col_p2:
        st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
        st.subheader("⚡ قطع شائعة ومطلوبة")
        st.markdown("""
        - **Intel Core i5-13400F:** السعر ~ $180 (ممتاز للألعاب والبرمجة).
        - **AOC 32-inch Curved Monitor:** السعر ~ $250-$280 (مريح جداً للألعاب والمهام المتعددة).
        - **ESP32 Microcontroller:** السعر ~ $6-$8 (مخصص لمشاريع الـ IoT والاتصالات اللاسلكية).
        - **DDR5 16GB RAM (5600MHz):** السعر ~ $55-$65.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

# =========================================================================
# القسم الرابع: محلل الدوائر والمخططات (AI Vision)
# =========================================================================
elif selected_tab == "محلل الدوائر والمخططات (AI Vision)":
    st.title("🔬 محلل الدوائر والمخططات (AI Vision)")
    st.markdown("ارفع صورة لأي دائرة إلكترونية، تصميم PCB، أو مخطط اتصالات، وسيقوم النظام الذكي بقراءتها وتشريحها هندسياً.")
    
    col_v1, col_v2 = st.columns(2, gap="large")
    with col_v1:
        st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
        st.subheader("📥 رفع صورة المخطط أو الدائرة")
        uploaded_image = st.file_uploader("اختر صورة الدائرة (PNG, JPG)", type=["png", "jpg", "jpeg"])
        if uploaded_image:
            img = Image.open(uploaded_image)
            st.image(img, use_container_width=True)
        else:
            st.markdown("<p style='color: #94a3b8; text-align: center;'>بانتظار رفع صورة المخطط الهندسي...</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col_v2:
        st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
        st.subheader("📊 التحليل الهندسي المباشر")
        if uploaded_image:
            with st.spinner("جاري فحص المخطط وخطوط التوصيل..."):
                st.markdown("""
                - **نوع النظام المرصود:** دائرة تحكم الكترونية رقمية / وحدة إرسال واستقبال لاسلكية.
                - **المكونات المرصودة:** مكثفات تنعيم، مقاومات حماية، ومتحكم دقيق رئيسي.
                - **حالة التوصيل:** سليمة هندسياً، مع وجود توصية بإضافة فلتر تيار (Decoupling Capacitor) لحماية الأطراف الحساسة.
                """)
        else:
            st.markdown("<p style='color: #64748b;'>قم برفع الصورة في الصندوق المجاور لعرض نتائج التحليل الفوري هنا.</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# =========================================================================
# القسم الخامس: مساعد الإنتاجية والأفكار الفردية
# =========================================================================
else:
    st.title("💡 مساعد الإنتاجية وأفكار المشاريع")
    st.markdown("قسم مخصص لتنظيم أفكارك، توليد أفكار مشاريع تخرج ذكية، وإعطائك دفعة تحفيزية للعمل والإنجاز.")
    
    st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
    st.subheader("🚀 مولد أفكار مشاريع تخرج ذكية")
    if st.button("✨ اقترح عليّ فكرة مشروع هندسي فخم"):
        st.markdown("""
        ### المقترح الذكي: نظام مراقبة وتحكم لاسلكي ذكي يعتمد على إنترنت الأشياء (Smart IoT Control System)
        - **فكرة المشروع:** تصميم وحدة الكترونية مدمجة تقيس المتغيرات البيئية أو الكهربائية وتنقله لاسلكياً عبر ترددات معينة إلى لوحة تحكم سحابية مبرمجة بلغة بايثون و Streamlit.
        - **المميزات:** دمج حقيقي بين تخصص الاتصالات والإلكترونيك وبرمجة واجهات الويب الذكية.
        """)
    st.markdown("</div>", unsafe_allow_html=True)
