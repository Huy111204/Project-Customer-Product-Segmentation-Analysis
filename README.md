# Customer & Product Segmentation Analysis

[![DockerHub](https://img.shields.io/badge/DockerHub-hoanghuy2004%2Fcustomer--segmentation--app-blue?logo=docker)](https://hub.docker.com/repository/docker/hoanghuy2004/customer-segmentation-app/general)
<img width="618" height="615" alt="image" src="https://github.com/user-attachments/assets/60af5b51-b6b0-46a2-9233-8aea1415527c" />

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
# docker pull hoanghuy2004/customer-segmentation-app
# docker run -p 8501:8501 hoanghuy2004/customer-segmentation-app 
3. Truy cập trình duyệt tại: http://localhost:8501
---

## Cấu trúc thư mục dự án

<pre>
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
├── Reports và Dashboard/           # Báo cáo chiến lược và Power BI 
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
│
├── README.md                       # File hiện tại
</pre>


---
## Phân tích tổng quan 
<img width="1535" height="865" alt="image" src="https://github.com/user-attachments/assets/4fa9b6a6-9de0-4ca7-963c-3230ea5003e9" />

### Doanh thu và lợi nhuận:
- Doanh thu đạt **12.64 triệu USD**, lợi nhuận **1.47 triệu USD**, tỷ suất lợi nhuận chỉ **11.61%**.
- Chi phí giao hàng (**1.35 triệu USD**) và chiết khấu cao (**7.33K USD**) là nguyên nhân làm giảm hiệu quả.

### Phân khúc khách hàng:
- **Consumer**: đóng góp **51% lợi nhuận** – nhóm cần được tập trung chăm sóc.
- **Corporate & Home Office**: ít lợi nhuận hơn, nhưng Home Office có tỷ suất lợi nhuận cao nhất.

### Nhóm sản phẩm:
- **Technology** chiếm tỷ trọng lợi nhuận cao nhất (663K USD – 45%).
- **Furniture** doanh thu lớn nhưng lợi nhuận thấp → cần tối ưu.

### Thị trường:
- Doanh thu tập trung tại Bắc Mỹ, châu Âu và châu Á.
- Các thành phố lớn đóng vai trò trung tâm doanh thu.

### Giao hàng:
- **Standard Class** chiếm đa số đơn hàng → tiết kiệm chi phí là ưu tiên.
- **First Class**, **Same Day** ít phổ biến → có thể đẩy mạnh vào nhóm khách hàng cao cấp.

### Tăng trưởng qua các năm:
- Doanh thu tăng từ 2.3M (2011) lên 4.3M (2014).
- Lợi nhuận tăng từ 250K lên 500K USD → ổn định nhưng cần bứt phá.

---
## Phân tích khách hàng
<img width="1539" height="862" alt="image" src="https://github.com/user-attachments/assets/ba01169a-9c99-4634-895e-6e003d139502" />
### Hướng khai thác
- Xác định phân khúc khách hàng chính theo số lượng, doanh thu, lợi nhuận.
- Theo dõi xu hướng tăng trưởng từng phân khúc qua các năm.
- Phân tích **top khách hàng theo giá trị đơn hàng & chiết khấu**.
- Hỗ trợ ra quyết định phân bổ nguồn lực và chiến lược chăm sóc.

### Kết quả nổi bật
- **Consumer** dẫn đầu về số lượng đơn hàng (12.6K/25K), doanh thu (6.5M) và lợi nhuận (0.75M).
- **Home Office** có tỷ suất lợi nhuận cao nhất nhưng quy mô nhỏ.
- Đơn hàng của nhóm Consumer tăng mạnh từ 4.7K (2011) lên gần 9K (2014).
- Chi phí vận chuyển vẫn chiếm tỷ trọng lớn → cần tối ưu logistics.

---
## Phân tích sản phẩm
<img width="1535" height="866" alt="image" src="https://github.com/user-attachments/assets/0e97cf78-57a6-4ebc-a6b3-686d4ee86f2e" />
### Hướng phân tích
- Doanh thu, lợi nhuận, số sản phẩm bán ra theo từng **category**.
- Phân tích **Top 10 sản phẩm** có doanh thu/lợi nhuận cao nhất.
- Theo dõi xu hướng lợi nhuận từng danh mục qua các năm.
- Phân tích tỷ lệ chiết khấu và hiệu suất từng danh mục con.

### Kết quả nổi bật
- **Technology, Office Supplies, Furniture** doanh thu gần tương đương.
- Nhưng **biên lợi nhuận chênh lệch rõ rệt**: Tech và Office Supplies ~14%, Furniture chỉ 7%.
- **Technology** là động lực tăng trưởng mạnh mẽ từ năm 2013 trở đi.
- Top sản phẩm lợi nhuận cao chủ yếu thuộc nhóm công nghệ.

---
## Đề xuất chiến lược

- **Tập trung vào nhóm sản phẩm lợi nhuận cao**
- **Chăm sóc khách hàng trung thành**
- **Tối ưu chi phí giao hàng**
- **Rà soát nhóm sản phẩm kém hiệu quả**
- **Tận dụng thời điểm cao điểm & hành vi theo mùa** 
