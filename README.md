# TSC-Management
Pre-release for TSC Website. 

OS: Windows10 or Windows11

# Odoo Basic
📄 Tutorial https://www.odoo.com/documentation/15.0/developer/howtos.html

## Programing Language
- Python version 3.9 and later.

## DBMS
- PostgreSQL version 10.0 and later.

## IDE
PyCharm Community: https://www.jetbrains.com/pycharm/download/#section=windows

## Resource

**Installation**
- 📄 Odoo installation docs: https://www.odoo.com/documentation/15.0/administration/install.html
- 🎥 Install Odoo15 on Windows 10 or Windows 11: https://www.youtube.com/watch?v=eD12tbz6BC4&t=740s

**Programming**
- 🎥 How to build custom module in Odoo15: https://www.youtube.com/watch?v=TiJ__I77CyE
- 🎥 Odoo Web Controller | Tutorial with Rest API & qWeb Templates: https://www.youtube.com/watch?v=eb83AeNHzWo&t=259s
- 🎥 Dynamic Web Controller in odoo: https://www.youtube.com/watch?v=q6Dp9ObPRqM&t=203s

## Running Odoo
```bash
C:\odoo\odoo> python odoo-bin -d <mydbname> -r <dbuser> -w <dbpassword>
```

## Scaffolding
In administrator mode
```bash
C:\odoo\odoo> python odoo-bin scaffold <module_name> addons\
```
Add custom addons path
- Go to location: C:\odoo\odoo\odoo.conf
- Add path in that file: addons_path = C:\odoo\odoo\odoo\addons,C:\odoo\odoo\addons

Add PostgreSQL bin for Backup or Restore Database
- Go to location: C:\odoo\odoo\odoo.conf
- Add path in that file: pg_path = C:\Program Files\PostgreSQL\version\bin

## Files path
```
tsc
├── __init__.py
├── __manifest__.py
├── controllers
|   ├── __init__.py
|   ├── controllers.py
├── demo
|   ├── demo.xml
├── models
|   ├── __init__.py
|   ├── TSC_Career_Model.py
|   ├── TSC_Organization_Model.py
|   ├── TSC_Team_Model.py
├── security
|   ├── ir.model.access.csv
├── static
|   ├── description
|       ├── icon.ong
|   ├── src
|       ├── img
|           ├── avatar.jpeg
|       ├── scss
|           ├── team_style.scss 
├── views
    ├── TSC_Career_views.xml
    ├── TSC_menu.xml
    ├── TSC_Organization_views.xml
    ├── TSC_Team_views.xml
    ├── TSC_templates.xml

## Files description
    - Module name: tsc
    - __init__.py คือ ไฟล์ที่เอาไว้ import ไฟล์ controllers และ models 
    - __manifest__.py คือ ไฟล์ที่มีไว้ตั้งค่ารายละเอียดของ module รวมทั้งเอาไว้เพิ่ม path file ของ data ด้วย
    - โฟลเดอร์ controllers ประกอบไปด้วย
        - __init__.py เป็นไฟล์ที่เอาไว้ import ไฟล์ในโฟลเดอร์ controllers ทั้งหมด
        - controllers.py เป็นไฟล์ที่เอาไว้ควบคุมการทำงานระหว่าง models และ views
    - โฟลเดอร์ demo มีไว้เพื่อจำรองข้อมูล (ไม่ได้ใช้งาน)
    - โฟลเดอร์ models คือโฟลเดอร์ที่เอาไว้เก็บไฟล์ของการสร้างโมเดล ประกอบไปด้วย
        - __init__.py คือไฟล์ที่เอาไว้ import ชื่อไฟล์ในโฟลเดอร์ model ทั้งหมด
        - TSC_Career_Model.py คือไฟล์ที่เอาสร้างโมเดลของ careers
        - TSC_Organization_Model.py คือไฟล์ที่เอาไว้สร้างโมเดลของ organization
        - TSC_Team_Model.py คือไฟล์ที่เอาไว้สร้างโมเดลของ profile team
    - โฟลเดอร์ security ประกอบไปด้วย ir.model.access.csv เป็นไฟล์ที่มีไว้เพื่ออนุญาติว่า group user สามารถทำอะไรได้บ้าง (ได้ 1 ไม่ได้ 0)
    - โฟลเดอร์ static คือโฟลเดอร์ที่เอาไว้เก็บ source อื่น ๆ เช่น รูป, js, scss ประกอบไปด้วย
        - โฟลเดอร์ description เอาไว้เก็บ icon ที่แสดงบน web browser
        - โฟลเดอร์ src ประกอบไปด้วย
            - โฟลเดอร์ img เอาไว้เก็บรูปต่าง ๆ
            - โฟลเดอร์ scss เอาไว้เก็บไฟล์ scss
    - โฟลเดอร์ views คือโฟลเดอร์ที่เอาไว้เก็บไฟล์ xml ต่าง ๆ ประกอบไปด้วย
        - TSC_Career_views.xml เป็นไฟล์ที่เอาไว้สร้าง form ของ career ใน backend
        - TSC_menu.xml เป็นไฟล์ที่เอาไว้รวมเมนูของ Team, Organization และ Careers ใน backend
        - TSC_Organization_views.xml เป็นไฟล์ที่เอาไว้สร้าง form ของ organization ใน backend
        - TSC_Team_views.xml เป็นไฟล์ที่เอาไว้สร้าง form ของ Profile team ใน backend
        - TSC_templates.xml เป็นไฟล์ที่แสดงผลบนเว็บไซต์ และดึงข้อมูลจาก backend ผ่าน controllers
        
    
    
