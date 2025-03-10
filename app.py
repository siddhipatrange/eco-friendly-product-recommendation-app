import streamlit as st
import pandas as pd
import os
import random
import streamlit.components.v1 as components
from landing_page import show_landing_page  # Import the landing page function

# Set Streamlit page configuration at the very beginning
st.set_page_config(layout="wide", page_title="Eco-Friendly Product Recommender", page_icon="🌱")  # Use full-page width

# Load dataset
df = pd.read_csv("corrected_eco_friendly_products (1).csv")

# User reviews storage
REVIEWS_FILE = "user_reviews.csv"

def load_reviews():
    if os.path.exists(REVIEWS_FILE):
        return pd.read_csv(REVIEWS_FILE)
    return pd.DataFrame(columns=["Product", "User", "Rating", "Review"])

def save_review(product, user, rating, review):
    df_reviews = load_reviews()
    new_review = pd.DataFrame([[product, user, rating, review]], columns=df_reviews.columns)
    df_reviews = pd.concat([df_reviews, new_review], ignore_index=True)
    df_reviews.to_csv(REVIEWS_FILE, index=False)

# Recommendation System
def get_recommendations(product_name, df, n=5):
    product_category = df[df["Name"] == product_name]["Category"].values[0]
    recommended_products = df[df["Category"] == product_category].sort_values(
        by=["Sustainability_Score", "Avg_Rating", "Price"],
        ascending=[False, False, True]
    ).head(n)
    return recommended_products

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #f0f8ff;
    }
    .stApp {
        background: linear-gradient(to right, #a8e6cf, #dcedc1);
    }
    .product-box {
        border: 3px solid #4CAF50;
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        transition: transform 0.3s ease-in-out;
        background-color: #f9f9f9;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.1);
    }
    .product-box:hover {
        transform: scale(1.07);
        box-shadow: 6px 6px 20px rgba(0,0,0,0.3);
        background-color: #e8f5e9;
    }
    .product-image {
        width: 100%;
        height: auto;
        border-radius: 10px;
    }
    .header-title {
        color: #2E7D32;
        text-align: center;
        font-size: 36px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit app
def main():
    # Ensure the button is fully left-aligned
    col1, col2, col3 = st.columns([0.1, 1, 3])  # Left, button, rest of the space
    with col1:
        st.write("")  # Empty space to push button to the left
    with col2:
        if st.button("🏠 Back to Landing Page"):
            st.session_state["page"] = "landing"
            st.rerun()

    
    st.markdown("<h1 class='header-title'>🌱 Eco-Friendly Product Recommendation System 🌍</h1>", unsafe_allow_html=True)

    # Search and Filters in one line
    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
        search_query = st.text_input("🔍 Search for products", "")
    with col2:
        category_filter = st.selectbox("📂 Filter by Category", ["All"] + list(df["Category"].unique()))
    with col3:
        price_sort = st.selectbox("💰 Sort by Price", ["None", "Low to High", "High to Low"])
    
    # Apply filters
    filtered_df = df[df["Name"].str.contains(search_query, case=False, na=False)]
    if category_filter != "All":
        filtered_df = filtered_df[filtered_df["Category"] == category_filter]
    if price_sort == "Low to High":
        filtered_df = filtered_df.sort_values(by="Price")
    elif price_sort == "High to Low":
        filtered_df = filtered_df.sort_values(by="Price", ascending=False)
    
    # Display products in 3-column layout
    cols = st.columns(4)
    for index, row in filtered_df.iterrows():
        col = cols[index % 4]
        with col:
            st.markdown(f"""
            <div class='product-box'>
                <img src='{row["Image_URL"]}' class='product-image' />
                <h4>{row['Name']}</h4>
                <p>💲{row['Price']} | ⭐{row['Avg_Rating']}</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"🔎 View {row['Product_ID']}", key=row['Product_ID']):
                st.session_state["selected_product"] = row.to_dict()
                st.session_state["page"] = "product_detail"
                st.rerun()

# Display product details
def display_product():
    product = st.session_state.get("selected_product", None)
    if not product:
        st.warning("No product selected.")
        return
    
    # Back button
    if st.button("⬅️ Back to Products"):
        st.session_state["page"] = "main"
        st.rerun()
        
    col1, col2 = st.columns([1, 2])
    with col1: 
        st.image(product["Image_URL"], width=400)
        
    with col2: 
        st.write(f"### {product['Name']}")
        st.write(f"**💰 Price:** ${product['Price']}")
        st.write(f"**⭐ Rating:** ${product['Price']}")
        st.write(f"**📂 Category:** {product['Category']}")
        st.write(f"**🌿 Material:** {product['Material']}")
        st.write(f"**✅ Eco Certifications:** {product['Eco_Certifications']}")
        st.write(f"**🌍 Sustainability Score:** {product['Sustainability_Score']}")
        st.write(f"**💨 Carbon Footprint:** {product['Carbon_Footprint (kg CO2)']} kg CO2")
        st.write(f"**♻️ Biodegradability:** {product['Biodegradability (%)']}%")
        st.write(f"**💧 Water Usage:** {product['Water_Usage (L)']} L")
        st.write(f"**⚡ Energy Consumption:** {product['Energy_Consumption (kWh)']} kWh")
    
    # Reviews section
    st.write("### 📝 Customer Reviews")
    df_reviews = load_reviews()
    product_reviews = df_reviews[df_reviews["Product"] == product["Name"]]
    if not product_reviews.empty:
        for _, row in product_reviews.iterrows():
            with st.container():
                st.markdown(f"**{row['User']}** rated *{row['Product']}* ⭐ {row['Rating']}/5")
                st.markdown(f"💬 {row['Review']}")
                st.write("---")
    else:
        st.info("No reviews yet. Be the first to write one!")
        
    # Write a Review
    st.write("### ✍️ Write a Review")
    user_name = st.text_input("👤 Your Name")
    rating = st.slider("⭐ Rating (1-5)", 1, 5, 3)
    review_text = st.text_area("💬 Your Review")
    if st.button("✅ Submit Review"):
        if user_name and review_text:
            save_review(product["Name"], user_name, rating, review_text)
            st.success("✅ Review submitted successfully!")
            st.rerun()
        else:
            st.warning("⚠️ Please fill in all fields.")
    
    # Recommendations
    st.write("### 🔎 You may also like:")
    recommended_products = get_recommendations(product['Name'], df)
    cols = st.columns(len(recommended_products))
    for col, (_, row) in zip(cols, recommended_products.iterrows()):
        with col:
            st.image(row["Image_URL"], caption=row["Name"], use_container_width=True)
            st.markdown(f"**{row['Name']}**")
            st.markdown(f"⭐ {row['Avg_Rating']}/5")
            st.markdown(f"💰 ${row['Price']}")
    
if __name__ == "__main__":
    if "page" not in st.session_state:
        st.session_state["page"] = "landing"  # Start with the landing page
    
    if st.session_state["page"] == "landing":
        show_landing_page()  # Call the function from landing_page.py
    elif st.session_state["page"] == "main":
        main()  # Function to display the main product page
    else:
        display_product()  # Function to show the selected product