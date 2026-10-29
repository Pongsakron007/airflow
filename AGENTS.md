# Project Rules & Guidelines (`AGENTS.md`)

เอกสารนี้เป็นไฟล์ Rule สำหรับ Agent (Antigravity) ในการทำงานกับโปรเจกต์ **Gold Price ETL** 
ระบบจะโหลดข้อกำหนดในไฟล์นี้มาใช้เป็นแนวทางและบริบทพื้นฐานโดยอัตโนมัติในทุก Session

---

## 1. ข้อมูลภาพรวมของโปรเจกต์ (Project Overview)
- **โปรเจกต์:** Airflow ETL สำหรับดึงและจัดเก็บข้อมูลราคาทองคำ
- **Stack หลัก:** Python, Apache Airflow, PostgreSQL, Docker / Docker Compose
- **โครงสร้างโฟลเดอร์หลัก:**
  - `airflow/`: บันทึก DAGs, plugins, และ configurations ของ Airflow
  - `utils/`: สคริปต์ช่วยเหลือและการทดสอบ API (เช่น `check_api.py`)
  - `docker-compose.yml`: จัดการ container ของ Airflow services และ PostgreSQL

---

## 2. กฎการเขียนโค้ดและพัฒนา (Development Guidelines)
- **ภาษาและสไตล์:** ใช้ Python 3 ตามมาตรฐาน PEP 8 พร้อมเขียน Type Hints และ Docstrings ในฟังก์ชันสำคัญ
- **Docker & Services:** การเปลี่ยนแปลง service หรือ environment ต้องสอดคล้องกับ `docker-compose.yml`
- **Airflow DAGs:** 
  - ออกแบบ DAG ให้ idempotent (รันซ้ำแล้วผลลัพธ์เหมือนเดิม ไม่เกิดข้อมูลซ้ำซ้อน)
  - แยก logic การประมวลผลและการโหลดข้อมูลออกเป็น Task หรือ Plugin ย่อยอย่างชัดเจน
- **ความปลอดภัย (Security):**
  - ห้าม Hardcode Credentials หรือ API Keys ลงในโค้ดโดยตรง
  - ให้เรียกค่าจาก Environment Variables (`.env`) เสมอ
  - ห้าม commit ข้อมูลความลับลง Git

---

## 3. รูปแบบการสื่อสารและการทำงาน (Agent Behavior)
- สื่อสารและอธิบายแนวทางการทำงานเป็นภาษาไทยอย่างกระชับและเข้าใจง่าย
- ก่อนแก้ไขไฟล์หลัก ให้สรุปสิ่งที่จะทำและตรวจสอบผลกระทบต่อระบบ ETL ก่อนเสมอ

