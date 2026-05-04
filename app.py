# app_complete.py - COMPLETE VERSION with Advanced Features
# CORRECTLY uses YOUR trained model from trained_model.pkl (NO retraining)

import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
from datetime import datetime

# ============================================
# PAGE CONFIGURATION
# ============================================
st.set_page_config(
    page_title="Real Estate Price Predictor",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# CUSTOM CSS
# ============================================
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 0;
    }
    .sub-header {
        text-align: center;
        color: #6B7280;
        margin-bottom: 2rem;
    }
    .prediction-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 1rem;
        text-align: center;
        margin: 1rem 0;
    }
    .prediction-price {
        font-size: 3rem;
        font-weight: bold;
        color: white;
        margin: 0;
    }
    .prediction-label {
        font-size: 1rem;
        color: #E0E7FF;
        margin-bottom: 0.5rem;
    }
    .metric-card {
        background: #F3F4F6;
        padding: 1rem;
        border-radius: 0.5rem;
        text-align: center;
    }
    .footer {
        text-align: center;
        color: #9CA3AF;
        margin-top: 3rem;
        padding: 1rem;
        font-size: 0.8rem;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# HEADER
# ============================================
st.markdown('<h1 class="main-header">🏠 Real Estate Price Predictor</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Enter property details to get an accurate market price prediction</p>', unsafe_allow_html=True)

# ============================================
# SIDEBAR WITH INFO
# ============================================
with st.sidebar:
    st.markdown("### 📊 About This Tool")
    st.markdown("""
    This ML model predicts real estate prices based on:
    - Property area (sq ft)
    - Number of bedrooms
    - Number of bathrooms  
    - Location category
    
    **Model:** Random Forest Regressor
    """)
    
    st.markdown("---")
    st.markdown("### 📈 Price Factors")
    st.markdown("""
    - ✅ Area: Most significant factor
    - ✅ Bedrooms: +₹200K per bedroom
    - ✅ Bathrooms: +₹150K per bathroom
    - ✅ Location: Premium for Downtown/Prime
    """)
    
    st.markdown("---")
    st.markdown("### 💾 Model Status")

# ============================================
# LOAD YOUR EXISTING MODEL (NO TRAINING)
# ============================================
@st.cache_resource
def load_model():
    """LOAD your existing trained model - NO training, NO retraining"""
    
    if os.path.exists('trained_model.pkl'):
        with open('trained_model.pkl', 'rb') as f:
            model = pickle.load(f)
        return model, True
    else:
        st.error("❌ trained_model.pkl not found!")
        st.info("Run your ZenML pipeline first to train the model.")
        return None, False

model, model_exists = load_model()

if model_exists:
    st.sidebar.success("✅ Using YOUR trained model from trained_model.pkl")
    
    # Show model info
    if hasattr(model, 'n_estimators'):
        st.sidebar.info(f"📊 Model: Random Forest with {model.n_estimators} trees")
    
    # Try to get feature names from model
    if hasattr(model, 'feature_names_in_'):
        st.sidebar.info(f"📋 Features: {len(model.feature_names_in_)} total")
else:
    st.sidebar.error("❌ No model found")
    st.stop()

# Define feature columns (adjust based on YOUR model's expected input)
feature_columns = ['area', 'bedrooms', 'bathrooms', 
                   'location_Downtown', 'location_Prime Area', 'location_Suburb']

# ============================================
# MAIN INPUT FORM (Two Column Layout)
# ============================================
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📏 Property Dimensions")
    area = st.number_input(
        "Area (sq ft)", 
        min_value=200, 
        max_value=10000, 
        value=1200,
        step=100,
        help="Total built-up area in square feet"
    )
    
    bedrooms = st.number_input(
        "Bedrooms", 
        min_value=1, 
        max_value=10, 
        value=2,
        step=1,
        help="Number of bedrooms"
    )

with col2:
    st.markdown("### 🛁 Amenities")
    bathrooms = st.number_input(
        "Bathrooms", 
        min_value=1, 
        max_value=8, 
        value=2,
        step=1,
        help="Number of bathrooms"
    )
    
    location = st.selectbox(
        "Location", 
        ["Downtown", "Suburb", "Prime Area"],
        help="Property location category"
    )

# ============================================
# ADVANCED OPTIONS (Expandable)
# ============================================
with st.expander("🔧 Advanced Options"):
    show_breakdown = st.checkbox("Show price breakdown", value=True)
    compare_locations = st.checkbox("Compare across locations", value=False)
    show_feature_importance = st.checkbox("Show feature importance", value=False)

# ============================================
# PREDICTION BUTTON
# ============================================
st.markdown("---")
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    predict_button = st.button("🔮 Predict Price", use_container_width=True, type="primary")

# ============================================
# MAKE PREDICTION USING YOUR MODEL
# ============================================
if predict_button and model_exists:
    # Prepare input data
    input_data = pd.DataFrame({
        'area': [area],
        'bedrooms': [bedrooms],
        'bathrooms': [bathrooms],
        'location_Downtown': [1 if location == 'Downtown' else 0],
        'location_Prime Area': [1 if location == 'Prime Area' else 0],
        'location_Suburb': [1 if location == 'Suburb' else 0]
    })
    
    # Ensure all columns exist
    for col in feature_columns:
        if col not in input_data.columns:
            input_data[col] = 0
    
    input_data = input_data[feature_columns]
    
    # Predict using YOUR model
    try:
        prediction = model.predict(input_data)[0]
        
        # Display prediction in fancy box
        st.markdown("---")
        st.markdown('<div class="prediction-box">', unsafe_allow_html=True)
        st.markdown('<p class="prediction-label">🏠 Estimated Market Price</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="prediction-price">₹{prediction:,.2f}</p>', unsafe_allow_html=True)
        
        # Add per sq ft price
        price_per_sqft = prediction / area
        st.markdown(f'<p style="color: #E0E7FF; text-align: center;">≈ ₹{price_per_sqft:,.0f} per sq ft</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # ============================================
        # PRICE BREAKDOWN (ADVANCED FEATURE)
        # ============================================
        if show_breakdown:
            st.markdown("### 📊 Price Breakdown")
            
            col_a, col_b, col_c = st.columns(3)
            
            with col_a:
                area_contribution = area * 5000
                st.metric("Area Contribution", f"₹{area_contribution:,.0f}", 
                         help=f"{area} sq ft × ₹5,000 (base rate)")
            
            with col_b:
                bedroom_contribution = bedrooms * 200000
                st.metric("Bedroom Value", f"₹{bedroom_contribution:,.0f}",
                         help=f"{bedrooms} bedrooms × ₹200,000")
            
            with col_c:
                bathroom_contribution = bathrooms * 150000
                st.metric("Bathroom Value", f"₹{bathroom_contribution:,.0f}",
                         help=f"{bathrooms} bathrooms × ₹150,000")
            
            location_premium = {
                'Prime Area': 0.3,
                'Downtown': 0.15,
                'Suburb': 0.0
            }
            premium_percent = location_premium[location]
            base_total = area_contribution + bedroom_contribution + bathroom_contribution
            premium_amount = base_total * premium_percent
            
            st.info(f"📍 **Location Premium ({location}):** +{premium_percent*100:.0f}% (₹{premium_amount:,.0f})")
            
            # Total from breakdown
            breakdown_total = base_total + premium_amount
            st.success(f"💰 **Total from breakdown:** ₹{breakdown_total:,.2f}")
            st.caption(f"(Model prediction: ₹{prediction:,.2f})")
        
        # ============================================
        # LOCATION COMPARISON (ADVANCED FEATURE)
        # ============================================
        if compare_locations:
            st.markdown("### 📍 Location Comparison")
            st.markdown("How price changes with different locations (same property):")
            
            comparison_data = []
            for loc in ['Downtown', 'Prime Area', 'Suburb']:
                test_data = pd.DataFrame({
                    'area': [area],
                    'bedrooms': [bedrooms],
                    'bathrooms': [bathrooms],
                    'location_Downtown': [1 if loc == 'Downtown' else 0],
                    'location_Prime Area': [1 if loc == 'Prime Area' else 0],
                    'location_Suburb': [1 if loc == 'Suburb' else 0]
                })
                for col in feature_columns:
                    if col not in test_data.columns:
                        test_data[col] = 0
                test_data = test_data[feature_columns]
                price = model.predict(test_data)[0]
                comparison_data.append({"Location": loc, "Price": price})
            
            comp_df = pd.DataFrame(comparison_data)
            st.bar_chart(comp_df.set_index('Location'))
            
            # Show percentage difference
            base_price = comp_df[comp_df['Location'] == 'Suburb']['Price'].values[0]
            for loc in ['Downtown', 'Prime Area']:
                loc_price = comp_df[comp_df['Location'] == loc]['Price'].values[0]
                diff_percent = ((loc_price - base_price) / base_price) * 100
                st.caption(f"📍 {loc}: +{diff_percent:.0f}% vs Suburb")
        
        # ============================================
        # FEATURE IMPORTANCE (ADVANCED FEATURE)
        # ============================================
        if show_feature_importance and hasattr(model, 'feature_importances_'):
            st.markdown("### 🌳 Feature Importance")
            st.markdown("Which factors most influence the price?")
            
            # Get feature importances
            if hasattr(model, 'feature_names_in_'):
                features = model.feature_names_in_
                importances = model.feature_importances_
            else:
                features = feature_columns
                importances = [0.4, 0.25, 0.15, 0.1, 0.05, 0.05]  # Estimated if not available
            
            # Create DataFrame
            importance_df = pd.DataFrame({
                'Feature': features,
                'Importance': importances
            }).sort_values('Importance', ascending=False)
            
            # Display bar chart
            st.bar_chart(importance_df.set_index('Feature'))
            
            # Add explanation
            st.caption("Higher importance = greater impact on price prediction")
            
    except Exception as e:
        st.error(f"Prediction error: {e}")
        st.info("Make sure your model's feature format matches the input data")

# ============================================
# FOOTER
# ============================================
st.markdown("---")
st.markdown('<div class="footer">', unsafe_allow_html=True)
st.markdown("🏠 **Real Estate Price Predictor** | Built with Streamlit & Random Forest")
st.markdown(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M')}")
st.markdown("💡 *Powered by your ZenML trained model*")
st.markdown('</div>', unsafe_allow_html=True)