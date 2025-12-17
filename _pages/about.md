---
permalink: /
title: "Yichen Tian"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<style>
/* 容器样式 */
.paper-item {
    display: flex;
    align-items: flex-start;
    margin-bottom: 25px;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    padding-bottom: 15px;
    border-bottom: 1px dashed #eee; /* 可选：加个淡淡的分隔线 */
}
.paper-item:last-child {
    border-bottom: none;
}

/* 左侧：年份和等级 */
.paper-left {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-right: 15px;
    min-width: 60px; /* 稍微宽一点以容纳长标签 */
}

.paper-year {
    color: #426ca9;
    font-weight: bold;
    font-size: 1.2rem;
    line-height: 1.2;
    margin-bottom: 6px;
}

.paper-rank {
    color: white;
    padding: 3px 6px;
    border-radius: 4px;
    font-size: 0.75rem;
    font-weight: bold;
    text-align: center;
    width: 100%;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

/* 等级颜色定义 */
.rank-red { background-color: #ee3f4d; }   /* CCF A / SCI Q1 */
.rank-blue { background-color: #428bca; }  /* CCF B / SCI Q2 */
.rank-orange { background-color: #f0ad4e; } /* CCF C / SCI Q3 */

/* 右侧：主要内容 */
.paper-content {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

/* 标题 */
.paper-title {
    font-size: 1.1rem;
    font-weight: bold;
    color: #1a1a1a;
    line-height: 1.4;
    margin-bottom: 6px;
}
.paper-title a {
    color: #2c3e50;
    text-decoration: none;
}
.paper-title a:hover {
    color: #428bca;
    text-decoration: underline;
}

/* 作者 */
.paper-authors {
    color: #666;
    font-size: 0.95rem;
    margin-bottom: 8px;
    line-height: 1.5;
}

/* 标签群 */
.paper-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    align-items: center;
}

/* 会议/期刊标签 (绿色主题) */
.tag-venue {
    background-color: #e0f2f1;
    color: #00897b;
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 0.75rem;
    font-weight: 700;
    border: 1px solid #b2dfdb;
}

/* 关键词标签 (浅蓝灰主题) */
.tag-keyword {
    background-color: #f1f3f5;
    color: #495057;
    padding: 2px 10px;
    border-radius: 12px;
    font-size: 0.75rem;
    border: 1px solid #dee2e6;
}
</style>

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I received my B.E. degree in Software Engineering from [Zhengzhou University](http://softschool.zzu.edu.cn/). Currently, I am a third-year Ph.D. candidate at the School of Software, [Tianjin University](http://cic.tju.edu.cn/english/home.htm). I am conducting research on the **Internet of Things** at the [Tianjin Key Laboratory of Advanced Networking (TANKLab)](http://tj.teacher.360eol.com/teacherBasic/preview?teacherId=12111), supervised by [Prof. Xinyu Tong](https://cic.tju.edu.cn/faculty/tongxinyu/index.html) and [Prof. Wenyu Qu](https://cic.tju.edu.cn/faculty/wyqu/index.html). My research interests focus on **Wireless Sensing** and **Indoor Localization**.

<a href='https://scholar.google.com/citations?user=67hHKAEAAAAJ&hl=zh-CN'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>

## 🎓 Education
* 2017-2021 &ensp; B.E. in Software Engineering, Zhengzhou University (Rank:1/713)
* 2021-2023 &ensp; M.S. in Computer Science, Tianjin University
* 2023- Now &ensp; Ph.D. in Software Engineering, Tianjin University


## 🔥 News
- *2025.12*: 🎉 One paper is accepted by **INFOCOM 2026**!
- *2025.11*: 🎉 Awarded the **Third Prize** of MobiCom 2025 SSC Competition!
- *2025.08*: 🎉 Two papers are accepted by **IMWUT/UbiComp 2025**!
- *2024.03*: 🎉 Two papers are accepted by **TMC**!
- *2023.05*: 🎉 One paper is accepted by **IoTJ**!
- *2022.12*: 🎉 One paper is accepted by **INFOCOM 2023**!
- *2021.06*: 🎓 Acquired my B.E. degree from Zhengzhou University as an outstanding graduate.
- *2021.05*: 🎉 One paper is accepted by **IPM**!
- *2019.12*: 🏅 Awarded a national scholarship.
- *2018.12*: 🏅 Awarded a national scholarship.


# 📝 Publications 

<div class="paper-item">
    <div class="paper-left">
        <div class="paper-year">2026</div>
        <div class="paper-rank rank-red">CCF A</div>
    </div>
    <div class="paper-content">
        <div class="paper-title">
            <a href="https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10228898">
                AutoLoc: Enabling Low-Effort Device and User Localization with Commercial Wi-Fi
            </a>
        </div>
        <div class="paper-authors">
            <strong style="color: #428bca;">Yichen Tian</strong>, Chenwen Gao, Xiaoqiang Xu, Xinyu Tong, Xiulong Liu, Xin Xie, Wenyu Qu
        </div>
        <div class="paper-tags">
            <span class="tag-venue">INFOCOM</span>
            <span class="tag-keyword">Wi-Fi Sensing</span>
            <span class="tag-keyword">Indoor Localization</span>
            <span class="tag-keyword">Device-free</span>
        </div>
    </div>
</div>

<div class="paper-item">
    <div class="paper-left">
        <div class="paper-year">2025</div>
        <div class="paper-rank rank-red">CCF A</div>
    </div>
    <div class="paper-content">
        <div class="paper-title">
            <a href="https://dl.acm.org/doi/pdf/10.1145/3770686">
                MetaTrack: Enabling Wi-Fi Device Free Tracking in Complex Scenarios
            </a>
        </div>
        <div class="paper-authors">
            Xuanqi Meng, Weiping Ge, <strong style="color: #428bca;">Yichen Tian</strong>, Xinyu Tong, Xiulong Liu, Xin Xie, Wenyu Qu
        </div>
        <div class="paper-tags">
            <span class="tag-venue">IMWUT / UbiComp</span>
            <span class="tag-keyword">Complex Scenarios</span>
            <span class="tag-keyword">Meta-Learning</span>
        </div>
    </div>
</div>

<div class="paper-item">
    <div class="paper-left">
        <div class="paper-year">2025</div>
        <div class="paper-rank rank-red">CCF A</div>
    </div>
    <div class="paper-content">
        <div class="paper-title">
            <a href="https://dl.acm.org/doi/pdf/10.1145/3770700">
                WiMap: Autonomous Wi-Fi Mapping for Device-free Tracking in Smart Homes
            </a>
        </div>
        <div class="paper-authors">
            Renrui Tan, Tu Hong, <strong style="color: #428bca;">Yichen Tian</strong>, Xinyu Tong, Sheng Chen, Xiulong Liu, Xin Xie, Wenyu Qu
        </div>
        <div class="paper-tags">
            <span class="tag-venue">IMWUT / UbiComp</span>
            <span class="tag-keyword">Wi-Fi Mapping</span>
            <span class="tag-keyword">Smart Homes</span>
            <span class="tag-keyword">Autonomous</span>
        </div>
    </div>
</div>

<div class="paper-item">
    <div class="paper-left">
        <div class="paper-year">2024</div>
        <div class="paper-rank rank-red">CCF A</div>
    </div>
    <div class="paper-content">
        <div class="paper-title">
            <a href="https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10476728">
                Device-free Human Tracking and Gait Recognition Based on the Smart Speaker
            </a>
        </div>
        <div class="paper-authors">
            <strong style="color: #428bca;">Yichen Tian</strong>, Yunliang Wang, Yufan Wang, Xinyu Tong, Xiulong Liu, Wenyu Qu
        </div>
        <div class="paper-tags">
            <span class="tag-venue">IEEE TMC</span>
            <span class="tag-keyword">Gait Recognition</span>
            <span class="tag-keyword">Acoustic Sensing</span>
            <span class="tag-keyword">Smart Speaker</span>
        </div>
    </div>
</div>

<div class="paper-item">
    <div class="paper-left">
        <div class="paper-year">2024</div>
        <div class="paper-rank rank-red">CCF A</div>
    </div>
    <div class="paper-content">
        <div class="paper-title">
            <a href="https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10416272">
                NNE-Tracking: A Neural Network Enhanced Framework for Device-free Wi-Fi Tracking
            </a>
        </div>
        <div class="paper-authors">
            Xinyu Tong, Weiping Ge, <strong style="color: #428bca;">Yichen Tian</strong>, Zijuan Liu, Xiulong Liu, Wenyu Qu
        </div>
        <div class="paper-tags">
            <span class="tag-venue">IEEE TMC</span>
            <span class="tag-keyword">Neural Network</span>
            <span class="tag-keyword">Wi-Fi Tracking</span>
            <span class="tag-keyword">Framework</span>
        </div>
    </div>
</div>

<div class="paper-item">
    <div class="paper-left">
        <div class="paper-year">2023</div>
        <div class="paper-rank rank-red">CCF A</div>
    </div>
    <div class="paper-content">
        <div class="paper-title">
            <a href="https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10228898">
                WSTrack: A Wi-Fi and Sound Fusion System for Device-free Human Tracking
            </a>
        </div>
        <div class="paper-authors">
            <strong style="color: #428bca;">Yichen Tian</strong>, Yunliang Wang, Ruikai Zheng, Xiulong Liu, Xinyu Tong, Keqiu Li
        </div>
        <div class="paper-tags">
            <span class="tag-venue">INFOCOM</span>
            <span class="tag-keyword">Multi-modal Fusion</span>
            <span class="tag-keyword">Wi-Fi + Sound</span>
            <span class="tag-keyword">Tracking</span>
        </div>
    </div>
</div>

<div class="paper-item">
    <div class="paper-left">
        <div class="paper-year">2023</div>
        <div class="paper-rank rank-blue">SCI Q2</div>
    </div>
    <div class="paper-content">
        <div class="paper-title">
            <a href="https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10132409">
                CrossTrack: Device-free Cross-link Tracking with Commodity Wi-Fi
            </a>
        </div>
        <div class="paper-authors">
            Weiping Ge, <strong style="color: #428bca;">Yichen Tian</strong>, Xiulong Liu, Xinyu Tong, Wenyu Qu, Zhenzhe Zhong, Haojie Chen
        </div>
        <div class="paper-tags">
            <span class="tag-venue">IEEE IoTJ</span>
            <span class="tag-keyword">Cross-link</span>
            <span class="tag-keyword">Commodity Wi-Fi</span>
        </div>
    </div>
</div>

<div class="paper-item">
    <div class="paper-left">
        <div class="paper-year">2021</div>
        <div class="paper-rank rank-red">SCI Q1</div>
    </div>
    <div class="paper-content">
        <div class="paper-title">
            <a href="https://www.sciencedirect.com/science/article/pii/S0306457321001060">
                Detecting Fake News by Exploring Multimodal Data Consistency and Multi-feature Fusion
            </a>
        </div>
        <div class="paper-authors">
            Junxiao Xue, Yabo Wang, <strong style="color: #428bca;">Yichen Tian</strong>, Yafei Li, Lei Shi, Lin Wei
        </div>
        <div class="paper-tags">
            <span class="tag-venue">IPM</span>
            <span class="tag-keyword">Fake News Detection</span>
            <span class="tag-keyword">Multi-feature Fusion</span>
        </div>
    </div>
</div>

<br>

# 🏅 Honors and Awards
- *2025.11* &ensp; ACM MobiCom 2025 SDP Sensing Challenge (SSC), Global 10th place (10/305)
- *2023.10* &ensp; First-Class Scholarship
- *2021.10* &ensp; Special Scholarship 
- *2021.06* &ensp; Outstanding Graduate of Henan Province and Zhengzhou University
- *2020.09* &ensp; First-Class Scholarship 
- *2019.12* &ensp; Merit Student Award of Henan Province
- *2019.12* &ensp; National Scholarship
- *2018.12* &ensp; National Scholarship 


# 💬 Presentations
- *2024.09*, 'Optimization of passive indoor positioning system based on Wi-Fi signal', oral presentation at the 18th CWSN 2024. 
- *2023.05*, 'WSTrack: A Wi-Fi and Sound Fusion System for Device-free Human Tracking', oral presentation at INFOCOM 2023. 


# ✏️ Academic Service
- Reviewer of IEEE Internet of Things Journal(IoTJ), ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies (IMWUT).
    
<div id="footer1">
		<h2> </h2>
		<div align="center">
		  <small>This page has been visited for
			<a href="https://www.easycounter.com/">
			<img src="https://www.easycounter.com/counter.php?tyc" border="0" alt="HTML Hit Counter"></a>

	
  <p>
	<center>
	<div align="center" style="width:20%">
	  <script type="text/javascript" id="clstr_globe" src="//clustrmaps.com/globe.js?d=qiU-RdfzQ5M0yLNi5rDZWbDZB2ulHFNhMw_1-YiP1pg"></script>
	</div>        
	</center>
  </p>
