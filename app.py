#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 英文文本分析工具 —— Streamlit 网页版
import streamlit as st
import re
from collections import Counter

st.set_page_config(page_title="英文文本分析工具", page_icon="📖")
st.title("📖 英文文本分析工具")
st.markdown("在下方粘贴或输入英文文本，点击分析按钮即可获得统计结果。")

# 文本框
user_text = st.text_area("请输入英文文本：", height=200)

if st.button("🔍 分析文本"):
    if not user_text.strip():
        st.warning("请先输入或粘贴一些英文文本。")
    else:
        # 分析逻辑
        words = re.findall(r'\b\w+\b', user_text.lower())

        total_words = len(words)
        unique_words = len(set(words))
        avg_word_length = round(sum(len(w) for w in words) / total_words, 2) if total_words > 0 else 0
        word_counts = Counter(words)
        common_words = word_counts.most_common(5)

        # 显示结果
        st.success("分析完成！")
        col1, col2, col3 = st.columns(3)
        col1.metric("总词数", total_words)
        col2.metric("不重复词数", unique_words)
        col3.metric("平均词长", f"{avg_word_length} 字母")

        st.subheader("📊 最常见的 5 个词")
        for word, count in common_words:
            st.write(f"- **{word}** : 出现 {count} 次")

