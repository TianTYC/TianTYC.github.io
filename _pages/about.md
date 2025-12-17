<style>
/* 容器样式 */
.paper-item {
    display: flex;
    align-items: flex-start;
    margin-bottom: 25px; /* 论文之间的间距 */
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}

/* 左侧：年份和等级 */
.paper-left {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-right: 15px;
    min-width: 55px; /* 保证宽度一致 */
}

.paper-year {
    color: #426ca9; /* 图片中的年份蓝 */
    font-weight: bold;
    font-size: 1.2rem;
    line-height: 1.2;
    margin-bottom: 4px;
}

.paper-rank {
    color: white;
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 0.75rem;
    font-weight: bold;
    text-align: center;
    width: 100%;
    box-sizing: border-box;
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
    margin-bottom: 4px;
}
.paper-title a {
    color: #2c3e50; /* 深色标题，或者用 #1e3a8a 蓝色 */
    text-decoration: none;
}
.paper-title a:hover {
    color: #428bca;
    text-decoration: underline;
}

/* 作者 */
.paper-authors {
    color: #7f8c8d; /* 灰色作者名 */
    font-size: 0.95rem;
    margin-bottom: 6px;
    line-height: 1.4;
}

/* 底部标签群（会议+关键词） */
.paper-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 8px; /* 标签间距 */
    align-items: center;
}

/* 会议/期刊标签 (绿色主题) */
.tag-venue {
    background-color: #e0f2f1; /* 浅绿背景 */
    color: #009688;            /* 深绿文字 */
    padding: 3px 10px;
    border-radius: 4px;
    font-size: 0.8rem;
    font-weight: 600;
}

/* 关键词标签 (浅蓝灰主题) */
.tag-keyword {
    background-color: #f3f6f9;
    color: #596b83;
    padding: 3px 10px;
    border-radius: 12px; /* 稍微圆一点 */
    font-size: 0.8rem;
}
</style>




---
permalink: /
title: "Yichen Tian"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I received my B.E. degree in Software Engineering from [Zhengzhou University](http://softschool.zzu.edu.cn/). Currently, I am a third-year Ph.D. candidate at the School of Software, [Tianjin University](http://cic.tju.edu.cn/english/home.htm). I am conducting research on the **Internet of Things** at the [Tianjin Key Laboratory of Advanced Networking (TANKLab)](http://tj.teacher.360eol.com/teacherBasic/preview?teacherId=12111), supervised by [Prof. Xinyu Tong](https://cic.tju.edu.cn/faculty/tongxinyu/index.html) and [Prof. Wenyu Qu](https://cic.tju.edu.cn/faculty/wyqu/index.html). My research interests focus on **Wireless Sensing** and **Indoor Localization**.
<!-- I have published more than 100 papers at the top international AI conferences with total <a href='https://scholar.google.com/citations?user=DhtAFkwAAAAJ'>google scholar citations <strong><span id='total_cit'>260000+</span></strong></a> -->
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

<!--
<span style="background-color: #428bca; color: white; padding: 2px 6px; border-radius: 4px; font-size: 12px; font-weight: bold; vertical-align: middle;">CCF B</span> 蓝色 
<span style="background-color: #5cb85c; color: white; padding: 2px 6px; border-radius: 4px; font-size: 12px; font-weight: bold; vertical-align: middle;">CCF C</span> 绿色
<span style="border: 1px solid #d9534f; color: #d9534f; padding: 1px 5px; border-radius: 4px; font-size: 12px; font-weight: bold; vertical-align: middle;">CCF A</span> 极简风 仅边框
-->

<!-- ========================================== 1 ==========================================
<div class='paper-box' style="display: flex; align-items: flex-start; gap: 20px;">
  
  <div class='paper-box-image' style="flex: 0 0 150px; max-width: 250px;">
    <div style="position: relative;">
      <div class="badge">INFOCOM 2026</div>
      <img src='images/autoloc.png' alt="sym" style="width: 100%; height: 120px; object-fit: cover; border-radius: 4px;">
      </div>
  </div>

  <div class='paper-box-text' markdown="1" style="flex: 1;">

**AutoLoc: Enabling Low-Effort Device and User Localization with Commercial Wi-Fi** <span style="background-color: #d9534f; color: white; padding: 2px 6px; border-radius: 4px; font-size: 12px; vertical-align: middle;">CCF A</span>

**Yichen Tian**, Chenwen Gao, Xiaoqiang Xu, Xinyu Tong, Xiulong Liu, Xin Xie, Wenyu Qu

By leveraging neural network-based feature matching and inverse reconstruction, we enable joint device and user position estimation based on COTS Wi-Fi. 
-->
<!-- ========================================== 1 ==========================================-->
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
            <span class="tag-venue">IEEE International Conference on Computer Communications (INFOCOM)</span>
            <span class="tag-keyword">Wi-Fi Sensing</span>
            <span class="tag-keyword">Indoor Localization</span>
            <span class="tag-keyword">Device-free</span>
        </div>
    </div>
</div>


<!-- ========================================== 2 ==========================================-->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TMC 2024</div><img src='images/wsgait.PNG' alt="sym" width="60%"></div></div>
<div class='paper-box-text' markdown="1">

[**Device-free Human Tracking and Gait Recognition Based on the Smart Speaker**](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10476728)&ensp;<span style="background-color: #d9534f; color: white; padding: 2px 6px; border-radius: 4px; font-size: 12px; vertical-align: middle;">CCF A</span>

<strong style="color: #428bca;">Yichen Tian</strong>, Yunliang Wang, Yufan Wang, Xinyu Tong, Xiulong Liu, Wenyu Qu

***IEEE Transactions on Mobile Computing (TMC) 2024***

<!--[[Page]](https://lulupig12138.github.io/SceneDecorator) [[Paper]](https://arxiv.org/pdf/2510.22994) [[Code]](https://github.com/lulupig12138/SceneDecorator)-->
</div>
</div>


<!-- ========================================== 3 ==========================================-->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">INFOCOM 2023</div><img src='images/wstrack.PNG' alt="sym" width="60%"></div></div>
<div class='paper-box-text' markdown="1">

[**WSTrack: A Wi-Fi and Sound Fusion System for Device-free Human Tracking** ](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10228898)&ensp;&ensp;&ensp;<span style="background-color: #d9534f; color: white; padding: 2px 6px; border-radius: 4px; font-size: 12px; vertical-align: middle;">CCF A</span>

<strong style="color: #428bca;">Yichen Tian</strong>, Yunliang Wang, Ruikai Zheng, Xiulong Liu, Xinyu Tong, Keqiu Li

***IEEE International Conference on Computer Communications (INFOCOM) 2023***

<!--[[Page]](https://lulupig12138.github.io/SceneDecorator) [[Paper]](https://arxiv.org/pdf/2510.22994) [[Code]](https://github.com/lulupig12138/SceneDecorator)-->
</div>
</div>


<!-- ========================================== 4 ==========================================-->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IoTJ 2023</div><img src='images/crosstrack.PNG' alt="sym" width="60%"></div></div>
<div class='paper-box-text' markdown="1">

[**CrossTrack: Device-free Cross-link Tracking with Commodity Wi-Fi**](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10132409)&ensp;<span style="background-color: #428bca; color: white; padding: 2px 6px; border-radius: 4px; font-size: 12px; font-weight: bold; vertical-align: middle;">SCI Q2</span>

Weiping Ge, <strong style="color: #428bca;">Yichen Tian</strong>, Xiulong Liu, Xinyu Tong, Wenyu Qu, Zhenzhe Zhong, Haojie Chen

***IEEE Internet of Things Journal (IoTJ) 2023***

<!--[[Page]](https://lulupig12138.github.io/SceneDecorator) [[Paper]](https://arxiv.org/pdf/2510.22994) [[Code]](https://github.com/lulupig12138/SceneDecorator)-->
</div>
</div>

<!-- ========================================== 5 ==========================================-->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TMC 2024</div><img src='images/nne.PNG' alt="sym" width="60%"></div></div>
<div class='paper-box-text' markdown="1">

[**NNE-Tracking: A Neural Network Enhanced Framework for Device-free Wi-Fi Tracking**](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10416272)&ensp;<span style="background-color: #d9534f; color: white; padding: 2px 6px; border-radius: 4px; font-size: 12px; vertical-align: middle;">CCF A</span>

Xinyu Tong, Weiping Ge, <strong style="color: #428bca;">Yichen Tian</strong>, Zijuan Liu, Xiulong Liu, Wenyu Qu

***IEEE Transactions on Mobile Computing (TMC) 2024***

<!--[[Page]](https://lulupig12138.github.io/SceneDecorator) [[Paper]](https://arxiv.org/pdf/2510.22994) [[Code]](https://github.com/lulupig12138/SceneDecorator)-->
</div>
</div>

<!-- ========================================== 6 ==========================================-->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IMWUT 2025</div><img src='images/metatrack.PNG' alt="sym" width="60%"></div></div>
<div class='paper-box-text' markdown="1">

[**MetaTrack: Enabling Wi-Fi Device Free Tracking in Complex Scenarios**](https://dl.acm.org/doi/pdf/10.1145/3770686)&ensp;<span style="background-color: #d9534f; color: white; padding: 2px 6px; border-radius: 4px; font-size: 12px; vertical-align: middle;">CCF A</span>

Xuanqi Meng, Weiping Ge, <strong style="color: #428bca;">Yichen Tian</strong>, Xinyu Tong, Xiulong Liu, Xin Xie, Wenyu Qu

***ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies (IMWUT) 2025***

<!--[[Page]](https://lulupig12138.github.io/SceneDecorator) [[Paper]](https://arxiv.org/pdf/2510.22994) [[Code]](https://github.com/lulupig12138/SceneDecorator)-->
</div>
</div>

<!-- ========================================== 7 ==========================================-->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IMWUT 2025</div><img src='images/wimap.PNG' alt="sym" width="60%"></div></div>
<div class='paper-box-text' markdown="1">

[**WiMap: Autonomous Wi-Fi Mapping for Device-free Tracking in Smart Homes**](https://dl.acm.org/doi/pdf/10.1145/3770700)&ensp;<span style="background-color: #d9534f; color: white; padding: 2px 6px; border-radius: 4px; font-size: 12px; vertical-align: middle;">CCF A</span>

Renrui Tan, Tu Hong, <strong style="color: #428bca;">Yichen Tian</strong>, Xinyu Tong, Sheng Chen, Xiulong Liu, Xin Xie, Wenyu Qu

***ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies (IMWUT) 2025***

<!--[[Page]](https://lulupig12138.github.io/SceneDecorator) [[Paper]](https://arxiv.org/pdf/2510.22994) [[Code]](https://github.com/lulupig12138/SceneDecorator)-->
</div>
</div>

<!-- ========================================== 8 ==========================================-->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IPM 2021</div><img src='images/fakenews.PNG' alt="sym" width="60%"></div></div>
<div class='paper-box-text' markdown="1">
  
[**Detecting Fake News by Exploring Multimodal Data Consistency and Multi-feature Fusion**](https://www.sciencedirect.com/science/article/pii/S0306457321001060)&ensp;<span style="background-color: #d9534f; color: white; padding: 2px 6px; border-radius: 4px; font-size: 12px; vertical-align: middle;">SCI Q1</span>

Junxiao Xue, Yabo Wang, <strong style="color: #428bca;">Yichen Tian</strong>, Yafei Li, Lei Shi, Lin Wei

***Information Processing and Management (IPM) 2021***

<!--[[Page]](https://lulupig12138.github.io/SceneDecorator) [[Paper]](https://arxiv.org/pdf/2510.22994) [[Code]](https://github.com/lulupig12138/SceneDecorator)-->
</div>
</div>


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
