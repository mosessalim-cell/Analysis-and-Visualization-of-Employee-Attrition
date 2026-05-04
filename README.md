# Visualisation of Employee Attrition

## Repository Outline
images - berisi hasil dari visualisasi menggunakan kibana
P2M3_Moses_Imanuel_Salim_DAG_graph.jpg - Berisi graph dari DAG yang telah dibuat
P2M3_Moses_Imanuel_Salim_DAG.py - berisi DAG yang telah dibuat untuk menjalankan workflow secara terschedule
P2M3_Moses_Imanuel_Salim_data_clean.csv - dataset yang telah diclean
P2M3_Moses_Imanuel_Salim_data_raw.csv - dataset yang raw yang berasal dari kaggle
P2M3_Moses_Imanuel_Salim_ddl.txt - Berisi DDL dan DDM yang telah dilakukan untuk membuat table dan menginsert data ke dalam table
P2M3_Moses_Imanuel_Salim_GX.ipynb - Data Validasi dengan great expectation
P2M3_Moses_Imanuel_Salim_conceptual.txt - berisi pertanyaan konsepsual yang perlu dijawab dalam project ini
description.md - Berisi penjelasan singkat mengenai project ini

## Problem Background
Employee attrition merupakan salah satu tantangan yang banyak perusahaan alami. Tingginya tingkat karyawan keluar dapat berdampak yang negatif bagi perusahaan. Menurut https://kumparan.com/dunia-karier/attrition-pengertian-penyebab-dan-dampaknya-untuk-perusahaan-24wIrFRVwZj/full, employee attrition dapat berdampak buruk bagi reputasi perusahaan. Keluarnya karyawan juga dapat mengganggu project yang sedang berjalan dikarenakan employee baru perlu waktu yang tidak cepat untuk menggantikan posisi tersebut. Biaya yang dikeluarkan oleh perusahaan juga tidak sedikit untuk merekrut karyawan barunya

## Project Output
Dataset yang telah diclean dan di validasi dengan great expectation
DAG yang berjalan dengan terschedule
Visualisasi dengan Kibana

## Data
Dataset yang dipakai adalah dataset employee attrition yang berasal dari kaggle

## Method
Projek ini menggunakan apache airflow untuk menjalankan DAG yang sudah ditentukan, Kibana untuk melakukan visualisasi, dan great expectation untuk data validasi

## Stacks
Bahasa yang digunakan adalah python dengan libraries seperti pandas, great expectation, elasticsearch dan airflow DAG
