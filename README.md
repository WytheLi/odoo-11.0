[![Build Status](http://runbot.odoo.com/runbot/badge/flat/1/11.0.svg)](http://runbot.odoo.com/runbot)
[![Tech Doc](http://img.shields.io/badge/11.0-docs-875A7B.svg?style=flat&colorA=8F8F8F)](http://www.odoo.com/documentation/11.0)
[![Help](http://img.shields.io/badge/11.0-help-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/forum/help-1)
[![Nightly Builds](http://img.shields.io/badge/11.0-nightly-875A7B.svg?style=flat&colorA=8F8F8F)](http://nightly.odoo.com/)

Odoo
----

Odoo is a suite of web based open source business apps.

The main Odoo Apps include an <a href="https://www.odoo.com/page/crm">Open Source CRM</a>,
<a href="https://www.odoo.com/page/website-builder">Website Builder</a>,
<a href="https://www.odoo.com/page/e-commerce">eCommerce</a>,
<a href="https://www.odoo.com/page/warehouse">Warehouse Management</a>,
<a href="https://www.odoo.com/page/project-management">Project Management</a>,
<a href="https://www.odoo.com/page/accounting">Billing &amp; Accounting</a>,
<a href="https://www.odoo.com/page/point-of-sale">Point of Sale</a>,
<a href="https://www.odoo.com/page/employees">Human Resources</a>,
<a href="https://www.odoo.com/page/lead-automation">Marketing</a>,
<a href="https://www.odoo.com/page/manufacturing">Manufacturing</a>,
<a href="https://www.odoo.com/page/purchase">Purchase Management</a>,
<a href="https://www.odoo.com/#apps">...</a>

Odoo Apps can be used as stand-alone applications, but they also integrate seamlessly so you get
a full-featured <a href="https://www.odoo.com">Open Source ERP</a> when you install several Apps.


Getting started with Odoo
-------------------------
For a standard installation please follow the <a href="https://www.odoo.com/documentation/11.0/setup/install.html">Setup instructions</a>
from the documentation.

Then follow <a href="https://www.odoo.com/documentation/11.0/tutorials.html">the developer tutorials</a>


-------------------------
### 二次开发修改自odoo 11.0版本 [源码地址](https://github.com/odoo/odoo/tree/11.0)


#### 运行项目
```
./odoo-bin -c /etc/odoo/odoo.conf -d testdb2 --dev=all
```

#### 配置文件
```sh
vim /etc/odoo/odoo.conf

[options]
addons_path = /home/willi/Desktop/odoo-11.0/odoo/addons, /home/willi/Desktop/odoo-11.0/addons, /home/willi/Desktop/odoo-11.0/my_modules
```


#### 使用脚手架创建模块模板
```sh
./odoo-bin scaffold bug-manage my_modules
```

