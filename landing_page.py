import streamlit as st
import pandas as pd
import plotly.express as px

def show_landing_page():
    st.markdown(
        """
        <style>
            .header {
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 10px 20px;
                background: linear-gradient(to right, #0D47A1, #1976D2);
                color: white;
                border-radius: 8px;
            }
            .logo-title {
                display: flex;
                align-items: center;
                gap: 10px;
            }
            .nav-links {
                display: flex;
                gap: 20px;
            }
            .nav-links a {
                color: white;
                text-decoration: none;
                font-size: 18px;
                font-weight: bold;
            }
            .welcome-section {
                text-align: center;
                padding: 80px 20px;
                background: linear-gradient(to bottom, #E3F2FD, #BBDEFB);
                border-radius: 10px;
                margin-top: 20px;
            }
            .get-started-container {
                display: flex;
                justify-content: center;
                margin-top: 20px;
            }
            .features-section {
                text-align: center;
                margin-top: 40px;
            }
        </style>
        <div class='header'>
            <div class='logo-title'>
                <h2>EcoShop 🌿</h2>
            </div>
            <div class='nav-links'>
                <a href='#'>Home</a>
                <a href='#'>Products</a>
                <a href='#'>About Us</a>
                <a href='#'>Contact</a>
                <a href='#' style='background: white; color: #0D47A1; padding: 8px 12px; border-radius: 5px;'>Log In</a>
                <a href='#' style='background: white; color: #0D47A1; padding: 8px 12px; border-radius: 5px;'>Sign Up</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class='welcome-section'>
            <h1>Welcome to EcoShop 🌱</h1>
            <p>Discover sustainable, eco-friendly products for a greener future.</p>
            <div class='get-started-container'>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
   
    # Centered and Funky Streamlit Button
    st.markdown(
        """
        <style>
            .stButton > button {
                background: linear-gradient(135deg, #0D47A1, #1976D2);
                color: white;
                font-size: 20px;
                font-weight: bold;
                padding: 15px 30px;
                border-radius: 12px;
                cursor: pointer;
                transition: all 0.3s ease;
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
                display: block;
                margin: 20px auto;
            }
            .stButton > button:hover {
                background: linear-gradient(135deg, #1565C0, #42A5F5);
                transform: scale(1.05);
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    if st.button("🚀 Get Started"):
        st.session_state["page"] = "main"
        st.rerun()

    st.markdown(
    """
    <style>
        .features-section {
            text-align: center;
            margin-top: 40px;
        }
        .features-section h2 {
            font-size: 28px;
            color: #0D47A1;
        }
        .features-box {
            background: linear-gradient(135deg, #E3F2FD, #BBDEFB);
            border-radius: 12px;
            padding: 15px;
            margin: 10px auto;
            width: 60%;
            font-size: 18px;
            font-weight: bold;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 2px 4px 10px rgba(0, 0, 0, 0.2);
            border-left: 5px solid #0D47A1;
        }
    </style>
    
    <div class='features-section'>
        <h2>Why Choose EcoShop?</h2>
        <div class='features-box'>✅ Find eco-friendly alternatives easily</div>
        <div class='features-box'>✅ Get product sustainability ratings</div>
        <div class='features-box'>✅ Smart recommendations for greener choices</div>
        <div class='features-box'>✅ Learn about carbon footprint and biodegradability</div>
        <div class='features-box'>✅ Contribute to a sustainable future</div>
    </div>
    """,
    unsafe_allow_html=True
)


    # Load dataset and create visuals
    df = pd.read_csv("corrected_eco_friendly_products (1).csv")

    # Eco-Friendly Trends Bar Chart
    st.markdown("## 📊 Eco-Friendly Trends")
    trend_fig = px.bar(
        df, x='Category', y='Sustainability_Score', 
        title='🌱 Eco-Friendly Product Trends',
        color='Category', 
        color_discrete_sequence=px.colors.qualitative.Pastel,  # More colorful palette
        text_auto=True
    )
    trend_fig.update_traces(marker_line_width=1.5, marker_line_color="black")
    trend_fig.update_layout(
        template="plotly_white",  # Light theme for contrast
        title_font=dict(size=22, family="Arial Black"),
        xaxis_title="Product Category",
        yaxis_title="Sustainability Score",
        hovermode="x unified"
    )
    st.plotly_chart(trend_fig, use_container_width=True)

    # Explanation
    st.markdown("""
    📌 **What does this graph tell us?**  
    This bar chart showcases how different product categories perform in terms of sustainability. A higher score means the product is more environmentally friendly.  
    It helps users choose **greener** options while shopping! 🌿
    """)

    # Usage of Eco-Friendly Products - Pie Chart
    st.markdown("## 🌍 Usage of Eco-Friendly Products")
    usage_fig = px.pie(
        df, names='Category', values='Biodegradability (%)',
        title='♻️ Usage Distribution of Eco-Friendly Products',
        color='Category',
        color_discrete_sequence=px.colors.qualitative.Bold,  # Bright colors
        hole=0.4  # Donut effect for a modern look
    )
    usage_fig.update_layout(
        template="plotly_white",
        title_font=dict(size=22, family="Arial Black"),
        annotations=[dict(text="Eco Usage", x=0.5, y=0.5, font_size=18, showarrow=False)]
    )
    st.plotly_chart(usage_fig, use_container_width=True)

    # Explanation
    st.markdown("""
    📌 **Why is this important?**  
    This chart shows the **percentage of biodegradable products** across categories. The higher the percentage, the better the product is for reducing waste and pollution.  
    Use this to identify the most eco-friendly choices! 🌎♻️
    """)

    # Benefits of Eco-Friendly Products - Stylish Bar Chart
    st.markdown("## 🌱 Benefits of Eco-Friendly Products")
    benefits_fig = px.bar(
        df, x='Category', y='Carbon_Footprint (kg CO2)',
        title='🌎 Environmental Benefits by Product Category',
        color='Category',
        color_discrete_sequence=px.colors.qualitative.Set1,  # More vibrant
        text_auto=True
    )
    benefits_fig.update_traces(marker_line_width=1.5, marker_line_color="black")
    benefits_fig.update_layout(
        template="plotly_white",
        title_font=dict(size=22, family="Arial Black"),
        xaxis_title="Product Category",
        yaxis_title="Carbon Footprint (kg CO2) (Lower is Better)",
        hovermode="x unified"
    )
    st.plotly_chart(benefits_fig, use_container_width=True)

    # Explanation
    st.markdown("""
    📌 **What does this tell us?**  
    This chart measures the **carbon footprint** of different product categories. A lower value means the product produces less CO2, making it a better choice for the planet. 🌍  
    **Tip:** Choose items with the lowest carbon footprint to reduce environmental impact!
    """)

