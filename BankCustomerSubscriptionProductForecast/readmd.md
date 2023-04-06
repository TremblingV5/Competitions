# 天池 - 金融数据分析赛题1：银行客户认购产品预测

[TOC]

## 赛题背景

赛题以银行产品认购预测为背景，想让你来预测下客户是否会购买银行的产品。在和客户沟通的过程中，我们记录了和客户联系的次数，上一次联系的时长，上一次联系的时间间隔，同时在银行系统中我们保存了客户的基本信息，包括：年龄、职业、婚姻、之前是否有违约、是否有房贷等信息，此外我们还统计了当前市场的情况：就业、消费信息、银行同业拆解率等。

## 字段

age	    年龄

job	    职业：admin, unknown, unemployed, management…

marital	婚姻：married, divorced, single

default	信用卡是否有违约: yes or no

housing	是否有房贷: yes or no

contact	联系方式：unknown, telephone, cellular

month	上一次联系的月份：jan, feb, mar, …

day_of_week	上一次联系的星期几：mon, tue, wed, thu, fri

duration	上一次联系的时长（秒）

campaign	活动期间联系客户的次数

pdays	上一次与客户联系后的间隔天数

previous	在本次营销活动前，与客户联系的次数

poutcome	之前营销活动的结果：unknown, other, failure, success

emp_var_rate	就业变动率（季度指标）

cons_price_index	消费者价格指数（月度指标）

cons_conf_index	消费者信心指数（月度指标）

lending_rate3m	银行同业拆借率 3个月利率（每日指标）

nr_employed	雇员人数（季度指标）

subscribe	客户是否进行购买：yes 或 no
