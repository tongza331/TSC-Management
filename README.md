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
- Add path in that file: pg_path = C:\Program Files\PostgreSQL\\<version>\bin

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
