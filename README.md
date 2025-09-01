# Customer & Product Segmentation Analysis

[![DockerHub](https://img.shields.io/badge/DockerHub-hoanghuy2004%2Fcustomer--segmentation--app-blue?logo=docker)](https://hub.docker.com/repository/docker/hoanghuy2004/customer-segmentation-app/general)
<img width="618" height="615" alt="image" src="https://github.com/user-attachments/assets/60af5b51-b6b0-46a2-9233-8aea1415527c" />

### Objectives
Examine key performance indicators—revenue, profit, discount, delivery time.

Develop an interactive Power BI dashboard.

Segment customers via K-Means and products via DBSCAN.

Deploy results through a Streamlit web app with Docker.

Propose business strategies based on cluster analysis.

Underlying dataset: Global Superstore from Kaggle ([Global Superstore Dataset (Kaggle)](https://www.kaggle.com/datasets/apoorvaappz/global-super-store-dataset/data))


## Web App
Clusters customers using K-Means.

Clusters products using DBSCAN.

Visualizes clusters via PCA, heatmaps, and scatter plots.

Links analytics with strategic business recommendations.

## Dashboard & Báo cáo
| File | Includes |
|------|----------|
| `customer_strategy_report.docx` | Custom strategy per customer segment |
| `product_strategy_report.docx`  | Tailored product segment tactics |
| `Dashboard.pbix`               | Power BI overview |

---
**Docker**:


### To use

open **Terminal** 
##### docker pull hoanghuy2004/customer-segmentation-app
##### docker run -p 8501:8501 hoanghuy2004/customer-segmentation-app 
 http://localhost:8501
---

## Repo Structure

<pre>
Project-Customer-Product-Segmentation-Analysis/
├── data/                # Raw and clustered data files
├── code/                # Analysis notebooks
├── Reports and Dashboard/ # Strategy reports & Power BI dashboard
├── app/                 # Streamlit app with Dockerfile
└── README.md            
</pre>


---
## Key Insights
<img width="1535" height="865" alt="image" src="https://github.com/user-attachments/assets/4fa9b6a6-9de0-4ca7-963c-3230ea5003e9" />

### Revenue & Profit: ~$12.64M revenue vs. ~$1.47M profit → low net margin (~11.6%); high discounts and logistics costs erode gains.

### Customer Segmentation: 'Consumer' segment dominates volume, revenue ($6.5M), and profit ($0.75M). 'Home Office' yields highest margin, but limited in scale.

### Product Analysis: Technology leads profits (~$663K, 45% margin); Furniture generates high revenue but suffers from low margin (7%)

### Growth Patterns: Revenue grew from $2.3M (2011) to $4.3M (2014), profit from $0.25M to $0.5M—steady, yet plainly unspectacular. Urgent need for revitalization.


---
## Customer Analysis
<img width="1539" height="862" alt="image" src="https://github.com/user-attachments/assets/ba01169a-9c99-4634-895e-6e003d139502" />


---
## Product Analysis
<img width="1535" height="866" alt="image" src="https://github.com/user-attachments/assets/0e97cf78-57a6-4ebc-a6b3-686d4ee86f2e" />



---
## Strategic Recommendations

Prioritize high-margin categories (Tech, Home Office).

Cultivate the Consumer segment—most lucrative and scalable.

Optimize logistics and reduce discount expenses.

Reevaluate low-performance segments and product lines.

Leverage seasonal behavior and target timing for promotions
