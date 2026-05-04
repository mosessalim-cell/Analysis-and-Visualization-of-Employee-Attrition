# Employee Attrition Analysis & Data Pipeline	

## Overview

Proyek ini bertujuan untuk menganalisis faktor-faktor yang mempengaruhi employee attrition serta membangun end-to-end data pipeline yang terotomatisasi. Pipeline mencakup proses data ingestion, data cleaning, data validation, hingga visualisasi untuk menghasilkan insight yang dapat mendukung pengambilan keputusan berbasis data.

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

## Project Objectives
Membangun pipeline data yang terautomasi dan terjadwal

Melakukan data cleaning dan memastikan kualitas data

Melakukan validasi data menggunakan Great Expectations

Menyediakan visualisasi interaktif untuk analisis attrition

## Project Output
Clean dataset yang telah divalidasi dengan great expectation
Workflow terotomasi menggunakan Apache Airflow (DAG)
Dashboard visualisasi menggunakan Kibana

## Data
Dataset yang dipakai adalah dataset employee attrition yang berasal dari kaggle

## Method
1. Data Ingestion
Mengambil dataset mentah dan menyimpannya untuk proses lebih lanjut
2. Data Cleaning & Transformation
Membersihkan data dan menyesuaikan format agar siap digunakan
3. Data Validation
Menggunakan Great Expectations untuk memastikan kualitas dan konsistensi data
4. Workflow Orchestration
Menggunakan Apache Airflow untuk menjalankan pipeline secara terjadwal
5. Data Visualization
Menggunakan Kibana untuk membuat dashboard interaktif

## Stacks
Bahasa yang digunakan adalah python dengan libraries seperti pandas, great expectation, elasticsearch dan airflow DAG
