# Customer & Product Segmentation Analysis

[![DockerHub](https://hub.docker.com/repository/docker/hoanghuy2004/customer-segmentation-app/general)

### Mục tiêu nghiên cứu
- Phân tích các chỉ số cốt lõi: doanh thu, lợi nhuận, chiết khấu, thời gian giao hàng...
- Xây dựng dashboard tương tác bằng **Power BI**.
- Phân cụm khách hàng & sản phẩm bằng **K-Means**, **DBSCAN**.
- Đề xuất chiến lược kinh doanh từ kết quả phân tích.

### Phương pháp & Công cụ
- **Power BI**: trực quan hóa và dashboard phân tích tương tác.
- **Python**: xử lý và phân tích dữ liệu (Jupyter Notebook).
- **Machine Learning**: phân cụm bằng K-Means, DBSCAN để khám phá phân khúc tiềm ẩn.
- **Dữ liệu sử dụng**: [Global Superstore Dataset on Kaggle](https://www.kaggle.com/datasets/apoorvaappz/global-super-store-dataset/data)

## Ứng dụng Web
App Streamlit hiển thị:
- Biểu đồ phân cụm khách hàng (KMeans)
- Biểu đồ phân cụm sản phẩm (DBSCAN)
- Gợi ý chiến lược cho từng cụm
- Visual trực quan bằng Plotly
---
**Demo Local**:
``bash 
docker pull hoanghuy2004/customer-segmentation-app
docker run -p 8501:8501 hoanghuy2004/customer-segmentation-app`` # Sau đó mở trình duyệt tại: http://localhost:8501 

---
Customer & Product Segmentation Analysis/
│
├── data/                           # Dữ liệu gốc và dữ liệu sau phân cụm
│   ├── Global_Superstore2.csv
│   ├── customer_clusters_kmeans.csv
│   └── product_clusters_dbscan.csv
│
├── code/                           # Notebook phân tích
│   └── clustering_analysis.ipynb
│
├── Reports và Dashboard/          # Báo cáo chiến lược và Power BI ( tổng quan , khách hàng , sản phẩm ) 
│   ├── customer_strategy_report.docx
│   ├── product_strategy_report.docx
│   └── Dashboard.pbix
│
├── app/                            # App Streamlit + Docker
│   ├── app.py
│   ├── customer_clusters_kmeans.csv
│   ├── product_clusters_dbscan.csv
│   ├── Dockerfile
│   └── requirements.txt

## Dashboard & Báo cáo
customer_strategy_report.docx: Đề xuất chiến lược nhóm khách hàng
product_strategy_report.docx: Gợi ý xử lý sản phẩm theo cụm
Dashboard.pbix: Dashboard Power BI trực quan tổng quan , khách hàng , sản phẩm 


