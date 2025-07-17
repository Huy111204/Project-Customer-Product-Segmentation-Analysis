# Customer & Product Segmentation Analysis

[![DockerHub](https://img.shields.io/badge/DockerHub-hoanghuy2004%2Fcustomer--segmentation--app-blue?logo=docker)](https://hub.docker.com/repository/docker/hoanghuy2004/customer-segmentation-app/general)

### Mục tiêu nghiên cứu
- Phân tích các chỉ số cốt lõi: doanh thu, lợi nhuận, chiết khấu, thời gian giao hàng,...
- Xây dựng dashboard tương tác bằng **Power BI**.
- Phân cụm khách hàng & sản phẩm bằng **K-Means**, **DBSCAN**.
- Tạo ứng dụng web bằng **Streamlit** để trực quan hóa kết quả.
- Đề xuất chiến lược kinh doanh từ kết quả phân tích và phân cụm.

### Phương pháp & Công cụ
- **Power BI**: trực quan hóa dữ liệu & xây dựng dashboard.
- **Python (Jupyter Notebook)**: xử lý dữ liệu, phân tích, mô hình hóa.
- **Machine Learning**: phân cụm bằng KMeans và DBSCAN để phát hiện nhóm khách hàng & sản phẩm.
- **Plotly + Streamlit**: trực quan hóa tương tác.
- **Docker**: đóng gói và triển khai app dễ dàng.
- **Dataset**: [Global Superstore Dataset (Kaggle)](https://www.kaggle.com/datasets/apoorvaappz/global-super-store-dataset/data)

## Ứng dụng Web
Ứng dụng cung cấp:
- Phân cụm khách hàng bằng **KMeans**.
- Phân cụm sản phẩm bằng **DBSCAN**.
- Trực quan hóa phân cụm bằng **PCA**, **Heatmap**, **Scatter Plot**,...
- Đưa ra **gợi ý chiến lược kinh doanh** dựa trên mỗi nhóm khách hàng/sản phẩm.

## Dashboard & Báo cáo
| File | Nội dung |
|------|----------|
| `customer_strategy_report.docx` | Báo cáo đề xuất chiến lược cho từng nhóm khách hàng |
| `product_strategy_report.docx`  | Chiến lược xử lý nhóm sản phẩm theo kết quả phân cụm |
| `Dashboard.pbix`               | Power BI Dashboard gồm: Tổng quan, Khách hàng, Sản phẩm |

---
**Demo Local (sử dụng Docker)**:
## 🚀 Demo Local (sử dụng Docker)

### 🔧 Hướng dẫn triển khai

1. Mở **Terminal** hoặc **Command Prompt**
2. Thực hiện 2 lệnh sau:
docker pull hoanghuy2004/customer-segmentation-app
docker run -p 8501:8501 hoanghuy2004/customer-segmentation-app 
3. Truy cập trình duyệt tại: 👉 http://localhost:8501
---

## 📁 Cấu trúc thư mục dự án

Customer & Product Segmentation Analysis/
│
├── data/ # Dữ liệu gốc và dữ liệu sau phân cụm
│ ├── Global_Superstore2.csv
│ ├── customer_clusters_kmeans.csv
│ └── product_clusters_dbscan.csv
│
├── code/ # Notebook phân tích
│ └── clustering_analysis.ipynb
│
├── Reports và Dashboard/ # Báo cáo chiến lược và Power BI
│ ├── customer_strategy_report.docx
│ ├── product_strategy_report.docx
│ └── Dashboard.pbix
│
├── app/ # App Streamlit + Docker
│ ├── app.py
│ ├── customer_clusters_kmeans.csv
│ ├── product_clusters_dbscan.csv
│ ├── Dockerfile
│ └── requirements.txt

---


