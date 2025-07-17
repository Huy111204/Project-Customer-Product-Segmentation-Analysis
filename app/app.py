import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import plotly.express as px

st.set_page_config(layout="wide")
st.title("Customer & Product Segmentation")

# Load data
@st.cache_data
def load_data():
    df_customer = pd.read_csv("customer_clusters_kmeans.csv")
    df_product = pd.read_csv("product_clusters_dbscan.csv")
    return df_customer, df_product

df_customer, df_product = load_data()

# Sidebar
st.sidebar.header("📂 Select Segmentation Type")
option = st.sidebar.selectbox("Choose a segmentation:", ["Customer Segmentation (KMeans)", "Product Segmentation (DBSCAN)"])

# -------------------------------
# Customer Segmentation
# -------------------------------
if option == "Customer Segmentation (KMeans)":
    st.header("🧑‍💼 Customer Segmentation using KMeans")

    st.subheader("1️⃣ Heatmap of RFM Features")
    features_rfm = ['Recency', 'Frequency', 'Monetary']
    fig, ax = plt.subplots()
    sns.heatmap(df_customer[features_rfm].corr(), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

    st.subheader("2️⃣ PCA Visualization (2D Projection)")
    pca = PCA(n_components=2)
    components = pca.fit_transform(df_customer[features_rfm])
    df_customer['PCA1'], df_customer['PCA2'] = components[:, 0], components[:, 1]

    fig = px.scatter(
        df_customer,
        x='PCA1', y='PCA2',
        color=df_customer['Cluster_KMeans'].astype(str),
        title="Customer Segments (PCA View)",
        color_discrete_sequence=px.colors.qualitative.Set2,
        labels={"color": "Cluster"}
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("3️⃣ Cluster Distribution")
    fig = px.pie(df_customer, names='Cluster_KMeans', title='Customer Cluster Distribution')
    st.plotly_chart(fig)

    st.subheader("4️⃣ Cluster Data Preview")
    selected_cluster = st.selectbox("Select a cluster to view data:", sorted(df_customer['Cluster_KMeans'].unique()))
    st.dataframe(df_customer[df_customer['Cluster_KMeans'] == selected_cluster].head(10))

# -------------------------------
# Product Segmentation
# -------------------------------
elif option == "Product Segmentation (DBSCAN)":
    st.header("📦 Product Segmentation using DBSCAN")

    st.subheader("1️⃣ Feature Correlation Heatmap")

    # Dùng các cột thực tế có trong file
    feature_cols = ['TotalSales', 'AvgPrice', 'OrderCount', 'TotalQuantity', 'TotalProfit']

    if not all(col in df_product.columns for col in feature_cols):
        st.error(f"❌ Missing expected columns in df_product. Found columns: {list(df_product.columns)}")
        st.stop()

    fig, ax = plt.subplots()
    sns.heatmap(df_product[feature_cols].corr(), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

    st.subheader("2️⃣ PCA Projection for DBSCAN Clusters")
    pca = PCA(n_components=2)
    components_prod = pca.fit_transform(df_product[feature_cols])
    df_product['PCA1'], df_product['PCA2'] = components_prod[:, 0], components_prod[:, 1]

    fig = px.scatter(
        df_product,
        x='PCA1', y='PCA2',
        color=df_product['Cluster_DBSCAN'].astype(str),
        title="Product Segments (PCA View)",
        color_discrete_sequence=px.colors.qualitative.Bold,
        labels={"color": "Cluster"}
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("3️⃣ Cluster Distribution Pie Chart")
    fig = px.pie(df_product, names='Cluster_DBSCAN', title='Product Cluster Distribution')
    st.plotly_chart(fig)

    st.subheader("4️⃣ Cluster Data Preview")
    selected_cluster = st.selectbox("Select a cluster to view products:", sorted(df_product['Cluster_DBSCAN'].unique()))
    st.dataframe(df_product[df_product['Cluster_DBSCAN'] == selected_cluster].head(10))
