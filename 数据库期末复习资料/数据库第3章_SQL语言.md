# 数据库第3章 - SQL语言

> 整理自数据库期末复习PPT

---

## 3.1 SQL概述.pptx


### 幻灯片 1

数据库原理


### 幻灯片 2

第三章    结构化查询语言SQL

	3.1 SQL概述
	3.2 数据定义语句
	3.3 查询
        3.4 数据更新
	3.5 视图


### 幻灯片 3

3.1 SQL概述
3.1.1 SQL语言的发展
SQL(Structured Query Language)结构化查询语言，1974年Boyce和Chamberlin提出，首先在IBM公司的关系数据库系统System R上实现。
特点：功能丰富、使用方便、灵活、语言简洁易学，应用系统范围广，统一标准。
1986年，ANSI数据库委员会 X3H2 批准了 SQL 作为数据库语言的美国标准，ISO随后也通过这一标准，使得 SQL 成为数据库领域的主流语言。
有关标准：SQL/86、SQL/89、SQL/92、SQL99、SQL2003、 SQL2006、 SQL2008、SQL2011、 SQL2016
现状:大部分DBMS产品都支持SQL，成为数据库的标准语言，是一个通用的、功能极强的关系数据库语言。


### 幻灯片 4

3.1 SQL概述
3.1.2 SQL语言的特点
一. 综合统一
       集数据定义语言DDL、数据操纵语言DML 和数据控制语言DCL 于一体，语言风格统一，可以独立完成数据库生命周期中的全部活动。
数据定义（DDL）
定义、删除、修改关系模式
定义、删除视图（View）
定义、删除索引（Index）
数据操纵（DML）
数据查询
数据增、删、改
数据控制（DCL）
用户访问权限的授予、收回


### 幻灯片 5

3.1 SQL概述
3.1.2 SQL语言的特点
二. 高度非过程化
     用户只需提出“做什么”，至于“怎么做”由DBMS解决；用户无需了解存取路径，存取路径的选择以及SQL语句的操作过程由系统自动完成。

三. 面向集合的操作方式
  每一个SQL的操作对象是一个或多个关系，操作的结果也是关系。

四. 以同一种语法结构提供两种使用方式
      即可独立使用，又可嵌入到高级语言中使用，具有自主型和嵌入型两种特点，且在两种使用方式下，SQL语言的语法结构基本一致。


### 幻灯片 6

3.1 SQL概述
3.1.2 SQL语言的特点
五. 语言简捷、易学易用
     核心功能只有9个动词，语法简单，接近英语。

**表格内容：**

SQL功能 | 操作符
数据查询 | SELECT
数据定义 | CREATE，DROP，ALTER
数据操纵 | INSERT，UPDATE，DELETE
数据控制 | GRANT，REVOKE


### 幻灯片 7

3.1 SQL概述
3.1.3 SQL语言的基本概念
－支持关系数据库的三级模式结构


### 幻灯片 8

小结
SQL语言的发展
SQL语言的特点
SQL语言的基本概念
谢谢观看！

---

## 3.2 数据定义语句(MySQL).pptx


### 幻灯片 1

数据库原理


### 幻灯片 2

第三章    结构化查询语言SQL

	3.1 SQL概述
	3.2 数据定义语句
	3.3 查询
        3.4 数据更新
	3.5 视图


### 幻灯片 3

3.2 数据定义语句

**表格内容：**

操作
对象 | 操作方式 |  | 
 | 创建 | 删除 | 修改
表 | CREAT TABLE | DROP TABLE | ALTER TABLE
视图 | CREAT VIEW | DROP VIEW | 
索引 | CREAT INDEX | DROP INDEX | 
SQL的数据定义语句
注：SQL通常不提供修改视图定义和索引定义的操作。


### 幻灯片 4

3.2 数据定义语句
补充：数据库的定义
数据库定义语句：
CREATE DATABASE <数据库名>


### 幻灯片 5

3.2 数据定义语句
补充：数据库的定义
CREATE DATABASE SampleDB;
电力抢修工程数据库的数据库名为SampleDB，建立电力抢修工程数据库的命令：
删除数据库语句：
DROP DATABASE <数据库名>
DROP DATABASE SampleDB;


### 幻灯片 6

3.2 数据定义语句
3.2.1 基本表的定义
CREATE TABLE <表名>
 (  <列名><数据类型>[列级完整性约束条件]
     [, <列名><数据类型>[列级完整性约束条件]]
        …
    [,表级完整性约束条件] );
注：若完整性约束条件涉及多个属性列，则必须定义在表级上，否则即可定义在列级也可定义在表级。
<列级完整性约束条件>：涉及相应属性列的完整性约束条件。
<表级完整性约束条件>：涉及一个或多个属性列的完整性约束条件


### 幻灯片 7

3.2 数据定义语句
3.2.1 基本表的定义
定义表的各个属性时需要指明其数据类型及长度。要注意，不同的RDBMS支持的数据类型不完全相同。


### 幻灯片 8

3.2 数据定义语句
3.2.1 基本表的定义
SQL创建表语句中常用完整性约束：
主码约束：  PRIMARY  KEY
唯一性约束：UNIQUE
非空值约束：NOT NULL
参照完整性约束: FOREIGN KEY REFERENCES 引用表名（引用列）
检查约束：CHECK(检查表达式) 
默认值约束：DEFAULT 默认值


### 幻灯片 9

3.2 数据定义语句
3.2.1 基本表的定义
【例3.1】建立 “抢修工程计划表”表Salvaging。
     Salvaging(prj_num, prj_name, start_date, end_date, prj_status）

        CREATE TABLE Salvaging
       (  prj_num char(8)  PRIMARY KEY ,  
            /* 列级完整性约束，prj_num是主码*/
	        prj_name varchar(50) ,
	        start_date datetime ,
	        end_date datetime ,
	        prj_status bit 
       );
各属性含义如下：
  工程项目编号：prj_num
  工程项目名称：prj_name
  开始日期：start_date
  结束日期：end_date
  是否按期完成：prj_status
本章所有例子均来自电力抢修工程数据库，该数据库包括三个表。


### 幻灯片 10

3.2 数据定义语句
3.2.1 基本表的定义
【例3.2】建立一个“配电物资库存记录表”表Stock。
    Stock(mat_num, mat_name, speci, warehouse, amount, unit,total）

CREATE TABLE Stock
(   mat_num char(4)  PRIMARY KEY, 	
    mat_name varchar(50)  NOT NULL, 	
    speci varchar(20)  NOT NULL, 	
    warehouse char(20) NULL ,
    amount  int NULL check(amount>0),
    unit decimal(18, 2) ,  
    CHECK(mat_num like'[m][0-9][0-9][0-9]'),
);
各属性含义如下：
  物资编号：mat_num
  物资名称：mat_name
  规格：speci
  仓库名称：warehouse
  数量：amount
  单价：unit
  总金额：total


### 幻灯片 11

3.2 数据定义语句
3.2.1 基本表的定义
【例3.3】建立一个“配电物资领料出库表”表Out_stock。
Out_stock(prj_num, mat_num, amount, get_date, department）

CREATE TABLE Out_stock
(   prj_num char(8) ,
	  mat_num char(4) ,
	  amount int ,
	  get_date datetime default NOW(),
	  department char(20) ,
    PRIMARY KEY(prj_num,mat_num),  
/* 主码由两个属性构成，必须作为表级完整性约束 */
    FOREIGN KEY (prj_num) REFERENCES Salvaging(prj_num),
    FOREIGN KEY (mat_num) REFERENCES Stock(mat_num)
);
各属性含义如下：
    工程项目编号：prj_num
    物资编号：mat_num
    领取数量：amount
    领料日期：get_date
    领料部门：department


### 幻灯片 12

3.2 数据定义语句
3.2.2 基本表的修改
ALTER TABLE <表名>
[ADD <新列名><数据类型> | [完整性约束]]
[DROP COLUMN <列名>  | <完整性约束名>]
[MODIFY COLUMN <列名>  <数据类型> <完整性约束>]
其中：ADD－增加新列和新的完整性约束条件；
          DROP－删除指定列或者完整性约束条件；
          MODIFY －修改原有的列定义，包括修改列名和数据类型。
注意：修改原有的列定义有可能会破坏已有数据。


### 幻灯片 13

3.2 数据定义语句
3.2.2 基本表的修改
【例3.4】向抢修工程计划表Salvaging增加“工程项目负责人”列，数据类型为字符型。
ALTER TABLE Salvaging ADD prj_director VARCHAR(10);
注意：不论基本表中原来是否已有数据，新增加的列一律为空值。
问题：若表salvaging中已有若干记录，再执行如下命令：
   ALTER TABLE salvaging ADD prj_director  VARCHAR(10) not null;        
  会成功吗？

问题：若表salvaging中已有若干记录，再执行如下命令：
ALTER TABLE Salvaging ADD prj_director  VARCHAR(10) not null  default  '张三' ;        
   会成功吗？


### 幻灯片 14

3.2 数据定义语句
3.2.2 基本表的修改
【例3.5】删除抢修工程计划表Salvaging中“工程项目负责人”的属性列。
ALTER TABLE Salvaging DROP COLUMN prj_director;
注意：修改原有的列定义有可能会破坏已有数据。
【例3.6】将配电物资领料出库表Out_stock中领取部门的数据类型改为可变长度字符类型。
ALTER TABLE Out_stock 
MODIFY COLUMN department varchar(20) NOT NULL;


### 幻灯片 15

3.2 数据定义语句
3.2.2 基本表的删除
DROP TABLE <表名>
如：DROP TABLE Out_stock;
DANGER：基本表一旦删除，则表中的数据，以及在其基础上建立的索引和视图都将自动删除。
注意：基本表的删除是有限制条件的，欲删除的基本表不能被其他表的约束所引用。如果存在这些依赖该表的对象，则此表不能被删除。

若执行：DROP TABLE Stock;
因为表stock被表out_stock外键引用
系统将会弹出提示,不能删除stock表


### 幻灯片 16

3.2 数据定义语句
3.2.4 约束的添加与删除
基本表的约束有：主键约束、外键约束、非空约束、唯一性约束、用户自定义的约束等，可以在创建表时创建（列级约束还可以在修改表的结构时创建），也可以在表已经创建完成后再添加或删除约束。

其一般格式为：
ALTER TABLE <表名> [ADD CONSTRAINT  <约束名>  <约束表达式>]
                                     [DROP CONSTRAINT  <约束名>];
【例3.8】 假设创建out_stock表时没有同时创建外键，可以再添加外键约束。
ALTER TABLE  out_stock 
                     ADD  CONSTRAINT  FK_Salvaging_Out_stock
                    FOREIGN KEY (prj_num)    REFERENCES  salvaging (prj_num);


### 幻灯片 17

3.2 数据定义语句
3.2.4 约束的添加与删除
【例3.9】删除out_stock表中的外键约束
      ALTER TABLE  out_stock  
                               DROP  CONSTRAINT  FK_Salvaging_Out_stock ;
或
      ALTER TABLE  out_stock 
                             DROP  FOREIGN KEY  FK_Salvaging_Out_stock ;
【例3.10】给表stock添加一个check约束：amount>0 。
ALTER TABLE stock  ADD  CONSTRAINT  CK_amount CHECK(amount>0);

【例3.11】给表salvaging的列prj_name添加一个唯一性约束。
      ALTER TABLE salvaging ADD CONSTRAINT  un_prj_name  UNIQUE(prj_name);


### 幻灯片 18

小结
基本表的定义
基本表的修改
基本表的删除
谢谢观看！

---

## 3.3.1 单表查询(MySQL).pptx


### 幻灯片 1

数据库原理


### 幻灯片 2

第三章    结构化查询语言SQL

	3.1 SQL概述
	3.2 数据定义语句
	3.3 查询
        3.4 数据更新
	3.5 视图


### 幻灯片 3

3.3 查询
查询是对现有的基本表和视图进行数据查询，并不改变数据本身，是数据库的核心操作。
一般格式：
   SELECT [ALL|DISTINCT]<目标列表表达式>
   FROM <表名或视图名>
   [WHERE <条件表达式>]
   [GROUP BY <列名1>[HAVING <条件表达式>]]
   [ORDER BY <列名2>[ASC|DESC]];


### 幻灯片 4

执行过程：
(1) 读取FROM子句中基本表、视图的数据,执行笛卡儿积操作;
(2) 选取满足WHERE子句中给出的条件表达式的元组;
(3) 按GROUP子句中指定列的值分组,同时提取满足HAVING子句中组条件表达式的那些组;
(4) 按SELECT子句中给出的列名或列表达式求值输出;
(5) ORDER子句对输出的目标表进行排序,可选择升序或降序。
3.3 查询


### 幻灯片 5

Select语句的含义
对 From 子句中的各关系，作笛卡儿积(×);
对 Where 子句中的逻辑表达式进行选择（σ）运算，找出符合条件的元组;
Select 子句中的属性列表，对上述结果作投影（π）操作.
结果集
 查询操作的对象是关系，结果还是一个关系，是一个结果集，而且是一个动态数据集。
等价于：∏a1 , a2 , … , an(p(R1  R2  …  Rm))
3.3 查询


### 幻灯片 6

Select语句的含义
对 From 子句中的各关系，作笛卡儿积(×);
对 Where 子句中的逻辑表达式进行选择（σ）运算，找出符合条件的元组;
Select 子句中的属性列表，对上述结果作投影（π）操作.
结果集
 查询操作的对象是关系，结果还是一个关系，是一个结果集，而且是一个动态数据集。
等价于：∏a1 , a2 , … , an(p(R1  R2  …  Rm))
3.3 查询


### 幻灯片 7

3.3 查询
我们以电力抢修工程数据库为例说明SELECT语句的各种用法。
(a) stock表
(b) salvaging表


### 幻灯片 8

3.3 查询
(c) out_stock表


### 幻灯片 9

3.3.1 单表查询
3.3 查询
【例3.12】查询所有配电物资的物资编号、物资名称、规格。
    SELECT  
    FROM
1. 选择表中若干列
       选择表中的全部列或部分列，即关系代数的投影运算。
1) 查询指定的列
【例3.13】查询所有配电物资的物资名称、物资编号、规格和所在仓库名称。
   SELECT 
   FROM Stock;
注：<目标列表达式>中各个列的先后顺序可以与表中的顺序不一致，用户可以根据应用的需要改变列的显示顺序。
mat_num, mat_name, speci
  Stock;
mat_name, mat_num, speci, warehouse


### 幻灯片 10

3.3.1 单表查询
3.3 查询
【例3.14】查询所有配电物资的记录。
   SELECT * 
   FROM Stock

   等价于：
    SELECT mat_num, mat_name, speci, warehouse, amount, unit, total
    FROM Stock
2) 查询全部列
注：用*，则列的显示顺序与基本表一致。


### 幻灯片 11

3.3.1 单表查询
3.3 查询
【例3.15】查询所有抢修工程的抢修天数。

SELECT prj_name, start_date, end_date, datediff(end_date,start_date)
FROM Salvaging;
3) 查询经过计算的值


### 幻灯片 12

3.3.1 单表查询
3.3 查询
MySQL  提供时间函数，可以对日期和时间输入值执行操作，并返回一个字符串、数字或日期和时间值，如下表所示 :

**表格内容：**

函    数 | 功    能
now() | 返回系统当前的日期和时间
year(d) | 返回日期d中的年份
month(d) | 返回日期d中的月份
dayofmonth(d) | 计算日期d是本月的第几天
datediff(d1,d2) | 返回d1和d2之间相隔的天数
adddate(d,n) | 返回起始日期d加上n天的日期
subdate(d,n) | 返回起始日期d减去n天的日期


### 幻灯片 13

3.3.1 单表查询
3.3 查询
【例3.16】查询所有抢修工程的抢修天数，并在实际抢修天数列前加入一个列，此列的每行数据均为‘抢修天数’常量值。

SELECT prj_name 项目名称, start_date 开始日期, end_date 结束日期,'抢修天数',
            datediff(end_date,start_date) 抢修天数
FROM Salvaging;
注：<目标表达式>不仅可以是属性列，也可以是算术表达式，还可以是字符串常量、函数等。


### 幻灯片 14

3.3.1 单表查询
3.3 查询
用户可以通过指定别名来改变查询结果的列标题，语法格式为：
           列名|表达式 [AS] 列标题    
      或：列标题=列名|表达式
SELECT prj_name 项目名称, start_date 开始日期, end_date 结束日期,
            datediff(end_date,start_date)抢修天数
FROM salvaging;


### 幻灯片 15

3.3.1 单表查询
3.3 查询
【例3.17】在配电物资库存记录表中查询出所有的仓库名称,并去掉结果表中的重复行。
  SELECT warehouse
  FROM Stock;
2. 选择表中若干元组
1）消除取值重复的行
SELECT DISTINCT warehouse
  FROM stock;
注：如果没有指定DISTINCT短语，则默认为ALL，即保留结果表中取值重复的行。


### 幻灯片 16

3.3.1 单表查询
3.3 查询
2） 查询满足条件的元组（WHERE）

**表格内容：**

 | 
 | 


### 幻灯片 17

3.3.1 单表查询
3.3 查询
【例3.18】查询供电局1#仓库存放的所有物资编号、物资名称、规格以及数量。

SELECT mat_num, mat_name, speci,amount
FROM stock
WHERE warehouse ='供电局1#仓库'
（1）比较大小


### 幻灯片 18

3.3.1 单表查询
3.3 查询
【例3.19】查询所有单价小于80的物资名称、数量及其单价。

    SELECT mat_name, amount,unit       
    FROM stock                  
   WHERE unit <80;                         
或：
   SELECT mat_name, amount,unit
   FROM stock
   WHERE NOT unit >=80;


### 幻灯片 19

3.3.1 单表查询
3.3 查询
【例3.20】查询单价在50~100之间的物资名称、数量及其单价。
   SELECT mat_name, amount, unit
   FROM stock
   WHERE unit BETWEEN 50 AND 100;
等价于：
   SELECT mat_name, amount, unit
   FROM stock
   WHERE unit >=50 AND unit <=100;
（2）确定范围(between… and…, not between… and…)


### 幻灯片 20

3.3.1 单表查询
3.3 查询
【例3.21】查询单价不在50~100之间的物资名称、数量及其单价。

   SELECT mat_name, amount, unit
   FROM Stock
   WHERE unit NOT BETWEEN 50 AND 100;

等价于：
   SELECT mat_name, amount, unit 
   FROM Stock
   WHERE unit<50 OR unit >100;


### 幻灯片 21

3.3.1 单表查询
3.3 查询
【例3.22】查询存放在供电局1#仓库和供电局2#仓库的物资名称、规格及其数量。
   SELECT mat_name, speci, amount
   FROM stock
   WHERE warehouse IN('供电局1#仓库','供电局2#仓库')
等价于：
   SELECT mat_name, speci, amount
  FROM stock
  WHERE warehouse ='供电局1#仓库'    
         OR warehouse ='供电局2#仓库'
（3）确定集合(in, not in)


### 幻灯片 22

3.3.1 单表查询
3.3 查询
【例3.23】查询既没有存放在供电局1#仓库，也没有存放在供电局2#仓库的物资名称、规格及其数量。
  SELECT mat_name, speci, amount
  FROM stock
  WHERE warehouse NOT IN ('供电局1#仓库','供电局2#仓库')
等价于：
  SELECT mat_name, speci, amount
  FROM stock
  WHERE warehouse !='供电局1#仓库' 
      AND warehouse !='供电局2#仓库'


### 幻灯片 23

3.3.1 单表查询
3.3 查询
（4）字符匹配(like,not like，模糊查询)
找出满足给定匹配条件的字符串，其格式为：
[NOT] LIKE  ‘<匹配串>’[ESCAPE ‘<换码字符>’]
匹配规则：
    “%” ：代表任意长度（0个或多个）字符串。例如a%b表示以a开头，以b结尾的任意长度的字符串。
    “_”：代表任意单个字符。例如a_b表示以a开头，以b结尾的长度为3的任意字符串。
     escape ：定义换码字符，以去掉特殊字符的特定含义，使其被作为普通字符看待。如escape ‘\’，定义了 \ 作为换码字符，则可用\%去匹配%，用\＿去匹配＿，用\ \去匹配 \ 。


### 幻灯片 24

3.3.1 单表查询
3.3 查询
【例3.24】查询存放在供电局1#仓库的物资的详细情况。

   SELECT *                               
  FROM stock                  
  WHERE warehouse LIKE '供电局1#仓库'    
等价于：
  SELECT *
  FROM stock
  WHERE warehouse ='供电局1#仓库'
注：如果LIKE后面的匹配串中不含通配符，则可以用“=”（等于）运算符取代LIKE谓词，用“!=”或“<>”（不等于）运算符取代NOT LIKE 谓词。


### 幻灯片 25

3.3.1 单表查询
3.3 查询
【例3.25】查询所有绝缘电线的物资编号、名称和规格。
    SELECT mat_num , mat_name, speci
   FROM stock                  
   WHERE mat_name LIKE '%绝缘电线'

【例3.26】查询物资名称中第三、四个字为“绝缘”的物资编号、名称和规格。
    SELECT mat_num , mat_name, speci
   FROM stock                  
   WHERE mat_name LIKE '__绝缘%'


### 幻灯片 26

3.3.1 单表查询
3.3 查询
【例3.27】查询所有不带绝缘两个字的物资编号、名称和规格。
    SELECT mat_num , mat_name, speci
    FROM stock                  
    WHERE mat_name NOT LIKE '%绝缘%'

【例3.28】查询物资名称含有“户外_真空”字样的物资信息。     
    SELECT *
    FROM Stock                  
    WHERE mat_name LIKE '%户外/_真空%' ESCAPE '/';

 说明：ESCAPE’\’短语表示“\”为换码字符，这样匹配串中紧跟在“\”后面的字符“_”不再具有通配符的含义，转义为普通的“_”字符。


### 幻灯片 27

3.3.1 单表查询
3.3 查询
判断取值为空的语句格式为：  列名 IS NULL
判断取值不为空的语句格式为：列名 IS NOT NULL

【例3.29】查询无库存单价的物资编号及其名称。
   SELECT mat_num , mat_name
   FROM stock                  
   WHERE unit IS NULL

注意：这里的“IS”不能用等号（=）代替。
（5）涉及空值的查询(is null, is not null)


### 幻灯片 28

3.3.1 单表查询
3.3 查询
【例3.30】查询规格为BVV-120的护套绝缘电线的物资编号、库存数量及库存地点。

SELECT mat_num,warehouse,amount  
FROM stock 
WHERE mat_name='护套绝缘电线'  
  AND speci='BVV-120'
（6）多重条件查询(and, or)
 AND的优先级高于OR
 可以用括号改变优先级


### 幻灯片 29

3.3.1 单表查询
3.3 查询
【例3.31】查询“护套绝缘电线”的物资编号及其单价，查询结果按单价降序排列。

     SELECT mat_name,unit
     FROM stock
     WHERE mat_name='护套绝缘电线' 
     ORDER BY unit DESC
3. 对查询结果排序(order by <列名>[ASC|DESC])
 可以按一个或多个属性列排序
 ASC表示升序，DESC 表示降序，缺省值为升序


### 幻灯片 30

3.3.1 单表查询
3.3 查询
【例3.32】查询所有物资的信息，查询结果按所在仓库名降序排列，同一仓库的物资按库存量升序排列。
SELECT * 
FROM stock
ORDER BY warehouse DESC , amount
注：
 1）当指定多个排序列时，首先按最前面的列进行排序，如果排序后存在两个或两个以上列值相同的记录，则对这些值相同的记录再按排在第二位的列进行排序，依次类推。
 2）空值是最小的。


### 幻灯片 31

3.3.1 单表查询
3.3 查询
4. LIMIT子句的用法
LIMIT 显示记录数量：从第一条记录开始，显示指定条数的记录；
LIMIT 初始位置，显示记录数量：从指定的初始位置开始显示指定条数的记录。

【例3.33】显示stock表中库存量最大的两条记录。
    SELECT *  
   FROM Stock 
   ORDER BY amount DESC
   LIMIT 2;


### 幻灯片 32

3.3.1 单表查询
3.3 查询
【例3.34】显示Stock表中的5条记录，指定从第3条记录开始显示。
      SELECT *  
      FROM Stock 
      LIMIT 3,5;


### 幻灯片 33

3.3.1 单表查询
3.3 查询
5. 聚集函数
COUNT([DISTINCT|ALL] *)      统计元组个数 
COUNT([DISTINCT|ALL] <列名>) 统计一列中值的个数
SUM([DISTINCT|ALL] <列名>) 计算一列值的总和（此列必须是数值型）
AVG([DISTINCT|ALL] <列名>) 计算一列值的平均（此列必须是数值型）
MAX([DISTINCT|ALL] <列名>) 求一列值中的最大值
MIN([DISTINCT|ALL] <列名>) 求一列值中的最小值
注：如果指定DISTINCT，表示计算时取消该列中的重复值；缺省为ALL，即计算时不取消重复值。


### 幻灯片 34

3.3.1 单表查询
3.3 查询
【例3.35】 统计领取了物资的抢修工程项目数。
SELECT COUNT (DISTINCT prj_num)
FROM out_stock;

【例3.36】 查询使用m001号物资的抢修工程的最高领取数量、最低领取数量以及平均领取数量。
SELECT MAX(amount), MIN(amount), AVG(amount)
FROM  out_stock
WHERE mat_num = 'm001';

注意：聚集函数中除COUNT外，其他函数在计算过程中均忽略NULL值；
          WHERE子句中是不能使用聚集函数作为条件表达式的。


### 幻灯片 35

3.3.1 单表查询
3.3 查询
6. 开窗函数
数据分析和统计中经常需要用到开窗函数，通常和聚集函数联合使用。
开窗函数：满足某种条件的记录集合上执行的特殊函数。
对于每条记录都要在此窗口内执行函数，有的函数随着记录不同，窗口大小都是固定的，这种属于静态窗口；有的函数则相反，不同的记录对应着不同的窗口，这种动态变化的窗口叫滑动窗口。
开窗函数的本质还是聚合运算，只不过它更具灵活性，它对数据的每一行，都使用与该行相关的行进行计算并返回计算结果。
聚合函数是将多条记录聚合为一条；而开窗函数是每条记录都会执行，有几条记录执行完还是几条。


### 幻灯片 36

3.3.1 单表查询
3.3 查询
【例3.37】查询每种物资按时间顺序的累计订单金额。
select *,sum(amount) over(partition by mat_num order by get_date) sum_amount
from out_stock;


### 幻灯片 37

3.3.1 单表查询
3.3 查询

**表格内容：**

函数名 | 函数功能
CUME_DIST() | 计算一组值中一个值的累计分布
DENSE_RANK() | 根据该order by 子句为分区中的每一行分配一个等级，它将相同的等级分配给具有相等值得行。如果两行或更多行具有相同得排名，则排名值序列中将没有间隙
FIRST_VALUE() | 返回相对于窗口框架第一行得指定表达式得值
LAG() | 返回分区中当前行之前的第N行得值。如果不存在前一行，则返回NULL
LAST_VALUE() | 返回相对于窗口框架最后一行得指定表达式得值
LEAD() | 返回分区中当前行之后的第N行得值。如果不存在后续行，则返回NULL
NTH_VALUE() | 从窗口框架的第N行返回参数的值
NTILE() | 将每个窗口分区的行分配到指定数量的排名组中
PERCENT_RANK() | 计算分区或结果集中行的百分数等级
RANK() | 与DENSE_RANK()相似，不同之处在于当两行或多行具有相同的等级时，等级值序列中存在间隙
ROW_NUMBER() | 为分区中的每一行分配一个顺序整数


### 幻灯片 38

3.3.1 单表查询
3.3 查询
【例3.38】查询每种物资使用数量最高的前2条出库情况。
select *
from ( select *,
row_number() over(partition by mat_num order by amount desc) as row_num
	  from out_stock) as t
where row_num<=2;


### 幻灯片 39

3.3.1 单表查询
3.3 查询
7. 对查询结果分组(group by)
GROUP BY子句可以将查询结果表按一列或多列取值相等的原则进行分组。
分组的目的：为了细化集函数的作用对象。如果未对查询结果分组，集函数将作用于整个查询结果，即整个查询结果只有一个函数值。如果用GROUP分了组，集函数将作用于每一个组，即每一组都有一个函数值。


### 幻灯片 40

3.3.1 单表查询
3.3 查询
【例3.39】 查询每个抢修工程项目号及使用的物资种类。

SELECT prj_num 项目号, COUNT(*) 物资种类
FROM out_stock
GROUP BY prj_num;


### 幻灯片 41

3.3.1 单表查询
3.3 查询
HAVING
可以针对集函数的结果值进行筛选，它是作用于分组计算的结果集；
跟在Group By子句的后面，有GROUP BY才有HAVING。
【例3.40】 查询使用了2种以上物资的抢修工程项目号。
SELECT prj_num 项目号, COUNT(*) 物资种类
FROM out_stock
GROUP BY prj_num
HAVING COUNT(*)>=2;
注：
（1）WHERE作用于基本表或视图，从中选择满足条件的元组；
（2）HAVING作用于组，从中选择满足条件的组。


### 幻灯片 42

3.3.1 单表查询
3.3 查询
【例3.41】按工程部门及物资编号统计其抢修的项目个数以及对应的领取总量。
SELECT department, mat_num, count(distinct prj_num) 项目个数 , sum(amount) 领取总量
FROM Out_stock
GROUP BY department,mat_num
GROUP BY子句的分组字段也可包含多个属性列名。


### 幻灯片 43

3.3.1 单表查询
3.3 查询
【例3.42】按工程部门及物资编号统计其抢修的项目个数以及对应的领取总量，要求带ROLLUP关键字。
 
SELECT department, mat_num,count(distinct prj_num) 项目个数 , sum(amount) 领取总量
FROM Out_stock
GROUP BY department,mat_num
WITH ROLLUP
ROLLUP：按照分组顺序，先对第一个分组字段分组，在组内进行统计，最后给出合计。


### 幻灯片 44

3.3.1 单表查询
3.3 查询
8. 正则表达式查询
正则表达式通常用于检索或替换那些符合某个模式的文本内容，根据指定的匹配模式匹配文本中符合要求的特殊字符串。
查询能力比通配字符的查询能力更强，而且更加灵活。
在MySQL中可以使用REGEXP关键字指定正则表达式的字符串匹配模式，基本语法如下： 列名   REGEXP  '匹配方式'
其中：列名表示需要查询的字段名称；匹配方式表示以哪种方式进行匹配查询。


### 幻灯片 45

3.3.1 单表查询
3.3 查询

**表格内容：**

模式字符 | 说明
^ | 匹配字符串开始的部分
$ | 匹配字符串结束的部分
. | 代表字符串中的任意一个字符，包括回车和换行
[字符集合] | 匹配“字符集合”中的任何一个字符
[^字符集合] | 匹配除了“字符集合”以外的任何一个字符
S1|S2|S3 | 匹配S1、S2、S3中的任意一个字符串
* | 匹配0个或多个在它前面的字符
+ | 匹配前面的字符1次或多次
字符串{N} | 字符串出现N次
字符串{M,N} | 字符串出现至少M次，最多N次
正则表达式的模式字符


### 幻灯片 46

3.3.1 单表查询
3.3 查询
【例3.43】查询项目名称中包含“西丽”、“明珠”的项目信息。
SELECT *
FROM Salvaging
WHERE prj_name REGEXP '西丽|明珠'
【例3.44】查询项目名称中包含“2”至少1次，最多2次的项目信息。
SELECT *
FROM Salvaging
WHERE prj_name REGEXP '2{1,2}'


### 幻灯片 47

小结
选择表中若干列
选择表中若干元祖
对查询结果排序
LIMIT子句的用法
聚集函数
对查询结果分组
谢谢观看！

---

## 3.3.2 连接查询(MySQL).pptx


### 幻灯片 1

数据库原理


### 幻灯片 2

第三章    结构化查询语言SQL

	3.1 SQL概述
	3.2 数据定义语句
	3.3 查询
        3.4 数据更新
	3.5 视图


### 幻灯片 3

3.3 查询
3.3.2 连接查询
在查询中，同时涉及两个或两个以上的表，要根据表中数据的情况作连接查询。
连接两个表的条件称为连接条件或连接谓词。
一般格式为：
[<表名1>.]<列名1> <比较运算符> [<表名2>.]<列名2>
或
[<表名1>.]<列名1> BETWEEN [<表名2>.]<列名2> AND  [<表名2>.]<列名3>
其中比较运算符主要有：=、>、<、>=、<=、!=（或<>）。


### 幻灯片 4

3.3 查询
3.3.2 连接查询
连接操作的执行过程：
 首先在表1中找到第一个元组，从头开始扫描表2，逐一查找满足连接条件的元组，找到后将表1中的第一个元组与该元组拼接起来，形成结果表中一个元组；
 表2全部查找完后，再找表1中第二个元组，然后再从头开始扫描表2，逐一查找满足连接条件的元组，找到后就将表1中的第二个元组与该元组拼接起来，形成结果表中一个元组；
 重复上述操作，直到表1中的全部元组都处理完毕 。


### 幻灯片 5

3.3 查询
3.3.2 连接查询
1. 等值与非等值连接查询
连接运算符为=则为等值连接，其他为非等值连接。
连接条件中的连接字段类型必须可比，但不必相同。
【例3.45】查询每个抢修工程及其领料出库的情况。
    SELECT Salvaging.*, Out_stock.*
    FROM Salvaging, Out_stock
    WHERE Salvaging.prj_num=Out_stock.prj_num


### 幻灯片 6

3.3 查询
3.3.2 连接查询
【例3.46】 对例3.45用自然连接完成。

SELECT Salvaging.prj_num,prj_name,start_date, end_date,Prj_status, mat_num,amount,get_date, department
FROM Salvaging, Out_stock
WHERE Salvaging.prj_num=Out_stock.prj_num
注：任何子句中引用表1和表2中同名属性时，都必须加表名前缀；若属性名在参加连接的表中是唯一的，则可以省略表名前缀。
连接谓词


### 幻灯片 7

3.3 查询
3.3.2 连接查询
广义笛卡尔积：
SELECT Salvaging.prj_num,prj_name,start_date, end_date,Prj_status, mat_num,amount,get_date, department
FROM Salvaging, Out_stock
112行记录


### 幻灯片 8

3.3 查询
3.3.2 连接查询
2. 内连接查询
使用INNER JOIN或者JOIN连接，重点是要有查询条件，条件使用ON引导。
【例3.47】 对例3.45用内连接完成。
SELECT salvaging.prj_num,prj_name,start_date,end_date,prj_status, mat_num,
amount,get_date,department
FROM salvaging INNER JOIN out_stock ON salvaging.prj_num=out_stock.prj_num
隐性连接：在FROM过程中对所有表进行笛卡儿积，最终通过WHERE条件过滤。
   显性连接：在每一次表连接时通过ON过滤，筛选后的结果集再和下一个表做笛卡儿积，以此循环。
即：显性连接最终得到笛卡儿积的数量可能会远远小于隐性连接所要扫描的数量，所以同样是等值连接，显性连接的效率更高。


### 幻灯片 9

3.3 查询
3.3.2 连接查询
3. 外连接查询
与普通连接的区别
  普通连接操作只输出满足连接条件的元组；
  外连接操作以指定某表为连接主体，将主体表中不满足连接条件的元组一并输出。
分类：
     左外连接：LEFT OUTER JOIN … ON …，列出左边关系中所有元组。
 
     右外连接：RIGHT OUTER JOIN … ON …，列出右边关系中所有元组。

    全外连接：FULL OUTER JOIN … ON …，列出左边关系和右边关系中所有元组。
外连接：把舍弃的元组也保存在结果关系中，而在其他属性上填空值。


### 幻灯片 10

3.3 查询
3.3.2 连接查询
【例3.48】把例3.45中的等值连接改为左外连接。
SELECT Salvaging.prj_num,prj_name,start_date, end_date,prj_status, mat_num,amount,get_date, department
FROM Salvaging LEFT OUTER JOIN Out_stock ON  Salvaging.prj_num = Out_stock.prj_num


### 幻灯片 11

3.3 查询
3.3.2 连接查询
【例3.49】 查询项目号为“20100015”抢修项目所使用的物资编号、物资名称、规格和使用数量。
SELECT Out_stock.mat_num, mat_name,speci, Out_stock.amount
FROM  Stock join Out_stock on 
Stock.mat_num=Out_stock.mat_num  
Where  prj_num='20100015'
4. 复合条件连接查询
       －WHERE子句中包含多个连接条件。
连接谓词
其他限定条件


### 幻灯片 12

3.3 查询
3.3.2 连接查询
【例3.50】 查询使用了护套绝缘电线的所有抢修项目编号及名称。

SELECT out_stock.prj_num,prj_name
FROM  (stock INNER JOIN out_stock ON stock.mat_num=out_stock.mat_num) 
INNER JOIN salvaging ON salvaging.prj_num=out_stock.prj_num
WHERE mat_name='护套绝缘电线'


### 幻灯片 13

3.3 查询
3.3.2 连接查询
5. 自身连接查询
连接操作是一个表与其自己进行的。
【例3.51】查询同时使用了物资编号为m001和m002的抢修工程的工程号。
SELECT A.prj_num
FROM Out_stock A, Out_stock B
WHERE A.prj_num =B.prj_num 
  AND A.mat_num='m001' 
  AND B.mat_num='m002'; 
SELECT A.prj_num
FROM Out_stock A inner join  Out_stock B  on  A.prj_num =B.prj_num 
 where A.mat_num='m001'    AND B.mat_num='m002';
必须给表起别名以示区别，且由于所有属性都是同名属性，则必须加前缀。


### 幻灯片 14

3.3 查询
3.3.2 连接查询
Out_stock: A
Out_stock:B
SELECT A.*,B.*
FROM Out_stock A, Out_stock B
WHERE A.prj_num =B.prj_num
A.mat_num='m001' AND B.mat_num='m002';


### 幻灯片 15

3.3.2 连接查询－练习
练习：4个表:
  Student(Sno , Sname , Ssex , Sage , Sclass)
  Teacher(Tno,Tname,Tsex,Tage, Tprof, Tdept)
  Course(Cno , Cname ,Tno)
  SC(Sno , Cno , Grade)


### 幻灯片 16

3.3.2 连接查询－练习
1. 查询所有选课学生的姓名、课程号和成绩。
2. 查询95033班同学所选各门课程的课号及平均分。
Select  Sname, Cno, Grade
From  Student join SC
on Student.Sno=SC.Sno;
Select Cno, AVG(Grade)
From   Student join SC on Student.Sno=SC.Sno
Where Sclass='95033' GROUP BY Cno;


### 幻灯片 17

3.3.2 连接查询－练习
3. 查询选修“3-105”号课程的成绩高于“109”号同学的所有同学记录。
Select  X.Sno, X.Cno, X.Grade
From  SC X, SC Y
Where X.Cno='3-105' 
            AND X.Grade>Y.Grade
            AND Y.Sno='109' 
            AND Y.Cno= '3-105';


### 幻灯片 18

小结
等值与非等值连接查询
内连接查询
外连接查询
复合条件连接查询
自身连接查询
谢谢观看！

---

## 3.3.3 嵌套查询(MySQL).pptx


### 幻灯片 1

数据库原理


### 幻灯片 2

第三章    结构化查询语言SQL

	3.1 SQL概述
	3.2 数据定义语句
	3.3 查询
        3.4 数据更新
	3.5 视图


### 幻灯片 3

3.3 查询
3.3.3 嵌套查询
在一个select-from-while语句的where子句或having短语中，又出现了另一个select语句，这种查询称为嵌套查询。
如：SELECT prj_name 
       FROM Salvaging
       WHERE prj_num IN
            (  SELECT prj_num 
               FROM Out_stock
               WHERE mat_num='m003'
             );


### 幻灯片 4

3.3 查询
3.3.3 嵌套查询
SQL允许多层嵌套查询，层层嵌套方式反映了 SQL语言的结构化；
子查询的限制：不能使用ORDER BY子句，即order by只能对最终结果排序；
有些嵌套查询可以用连接运算替代。


### 幻灯片 5

3.3 查询
3.3.3 嵌套查询
【例3.52】 查询与规格为“BVV-120”的“护套绝缘电线”在同一个仓库存放的物资名称、规格和数量。
（1）确定规格为“BVV-120”的“护套绝缘电线”的物资所存放仓库名称：
  SELECT warehouse
  FROM Stock
  WHERE speci ='BVV-120'  AND mat_name ='护套绝缘电线';

     结果：
1. 带谓词IN的嵌套查询
－子查询的结果是一个集合。


### 幻灯片 6

3.3 查询
3.3.3 嵌套查询
② 查找存放在供电局1#仓库的物资：
SELECT mat_name, speci, amount
FROM Stock
WHERE warehouse ='供电局1#仓库';

查询结果为：
将第1步查询嵌入到第2步查询的条件中，构造嵌套查询，SQL语句如下：

SELECT mat_name, speci, amount
FROM Stock
WHERE warehouse IN
       ( SELECT warehouse
         FROM Stock
         WHERE speci ='BVV-120' 
           AND mat_name ='护套绝缘电线');


### 幻灯片 7

3.3 查询
3.3.3 嵌套查询
本例中的查询也可以用自身连接来完成：
SELECT s1.mat_name, s1.speci, s1.amount
FROM Stock s1,Stock s2
WHERE s1.warehouse=s2.warehouse 
   and s2.speci ='BVV-120' and s2.mat_name ='护套绝缘电线';
不相关子查询
        －子查询的查询条件不依赖于父查询。
求解方法：由里向外逐层处理
        即每个子查询在上一级查询处理之前求解，子查询的结果用于建立其父查询的查找条件。


### 幻灯片 8

3.3 查询
3.3.3 嵌套查询
【例3.47】 查询工程项目为“观澜站光缆抢修”抢修所使用的物资编号和名称。
(  SELECT mat_num
   FROM Out_stock
    WHERE prj_num IN
SELECT mat_num, mat_name 
FROM Stock
WHERE mat_num IN
(   SELECT prj_num 
    FROM Salvaging 
    WHERE prj_name ='观澜站光缆抢修'));
① 在Salvaging 表中确定观澜站光缆抢修的项目编号：20110003
③ 在stock关系中查询其mat_num和mat_name
②在out_stock表中找出20110003号工程使用的物资编号：m001、m003


### 幻灯片 9

3.3 查询
3.3.3 嵌套查询
SELECT Stock.mat_num, mat_name                          
FROM Stock,Out_stock, Salvaging                                                 
WHERE Stock.mat_num = Out_stock.mat_num 
    AND  Out_stock.prj_num= Salvaging.prj_num
    AND  prj_name ='观澜站光缆抢修';
也可用连接查询实现：


### 幻灯片 10

3.3 查询
3.3.3 嵌套查询
【例3.54】查询出库存量超过该仓库物资平均库存量的物资编号、名称、规格及数量。

       SELECT mat_num, mat_name,speci,amount
       FROM Stock  
       WHERE amount>( 


                                    );
2. 带有比较运算符的子查询
－确定子查询返回的是单值，则子查询与父查询之间可用比较运算符连接。
SELECT avg(amount)
 FROM Stock  
 WHERE
s1
s2
s2.warehouse=s1.warehouse
相关子查询


### 幻灯片 11

3.3 查询
3.3.3 嵌套查询
执行过程：
   ① 从外层查询中取出Stock表的一个元组s1，将元组s1的warehouse值（供电局1#仓库）传送给内层查询。
 SELECT avg(amount)
 FROM stock  s2
 WHERE s2.warehouse='供电局1#仓库'
② 执行内层查询，得到值125，用该值代替内层查询，得到外层查询：
SELECT mat_num,mat_name,speci,amount
FROM stock  s1
WHERE amount > 125 and s1.warehouse='供电局1#仓库'
③ 执行这个查询：


### 幻灯片 12

3.3 查询
3.3.3 嵌套查询
相关子查询
        －子查询的查询条件依赖于父查询。
求解方法：
1）首先取外层查询中表的第一个元组，根据它与内层查询相关的属性值处理内层查询，若WHERE子句返回值为真，则取此元组放入结果表；
2）然后再取外层表的下一个元组；
3）重复这一过程，直至外层表全部检查完为止。


### 幻灯片 13

3.3 查询
3.3.3 嵌套查询
3. 带有ANY或ALL谓词的子查询
－必须同时使用比较运算符

**表格内容：**

>ANY | 大于子查询结果中某个值 | >ALL | 大于子查询结果中所有值
<ANY | 小于 | <ALL | 小于
>=ANY | 大于等于 | >=ALL | 大于等于
<=ANY | 小于等于 | <=ALL | 小于等于
=ANY | 等于 | =ALL | 等于
!=ANY
<>ANY | 不等于 | !=ALL
<>ALL | 不等于


### 幻灯片 14

3.3 查询
3.3.3 嵌套查询
【例3.49】 查询其他仓库中比供电局1#仓库的某一物资库存量少的物资名称、规格和数量。
SELECT mat_name, speci, amount 
FROM Stock
WHERE warehouse <> '供电局1#仓库'
         AND amount < ANY
                  ( 


                  );
SELECT amount
FROM Stock
WHERE warehouse = '供电局1#仓库'


### 幻灯片 15

3.3 查询
3.3.3 嵌套查询
也可用集函数MAX()实现：
SELECT mat_name, speci, amount 
FROM Stock
WHERE warehouse <> '供电局1#仓库'
         AND amount < 
                   (SELECT MAX (amount)
                    FROM Stock
                    WHERE warehouse = '供电局1#仓库');


### 幻灯片 16

3.3 查询
3.3.3 嵌套查询
【例 】 查询其他仓库中比供电局1#仓库的所有物资库存量少的物资名称、规格和数量。
SELECT mat_name, speci, amount 
FROM Stock
WHERE warehouse <> '供电局1#仓库'
         AND amount < ALL
                  ( SELECT amount
                     FROM Stock
                     WHERE warehouse = '供电局1#仓库');


### 幻灯片 17

3.3 查询
3.3.3 嵌套查询
也可用集函数MIN()实现：
SELECT mat_name, speci, amount 
FROM Stock
WHERE warehouse <> '供电局1#仓库'
         AND amount < 
                   (SELECT MIN (amount)
                    FROM Stock
                    WHERE warehouse = '供电局1#仓库');


### 幻灯片 18

3.3 查询
3.3.3 嵌套查询
注：使用集函数比使用ANY、ALL效率高，因为能减少比较次数。

**表格内容：**

 | = | != | < | <= | > | >=
ANY | IN |  | <MAX | <=MAX | >MIN | >=MIN
ALL |  | NOT IN | <MIN | <=MIN | >MAX | >=MAX
ANY和ALL谓词有时可以用聚集函数实现:


### 幻灯片 19

3.3 查询
3.3.3 嵌套查询
3. 带有EXISTS谓词的子查询
－EXISTS代表存在量词  ，不返回任何数据，只产生逻辑真(true)或逻辑假(false)。
若内层查询结果非空，则返回真值
若内层查询结果为空，则返回假值
－由EXISTS引出的子查询，其目标列表达式通常都用 * ，因为带EXISTS的子查询只返回真值或假值，给出列名无实际意义。


### 幻灯片 20

3.3 查询
3.3.3 嵌套查询
【例3.56】 查询使用了m001号物资的工程项目名称。
SELECT prj_name
FROM Salvaging
WHERE EXISTS
       (SELECT *
        FROM Out_stock
        WHERE prj_num=Salvaging.prj_num 
              AND mat_num ='m001' );


### 幻灯片 21

3.3 查询
3.3.3 嵌套查询
【例3.57】 查询没有使用m001号物资的工程项目编号及名称。

SELECT prj_num, prj_name
FROM Salvaging
WHERE NOT EXISTS
       (SELECT *
        FROM Out_stock
        WHERE prj_num=Salvaging.prj_num 
              AND mat_num ='m001' );
相关子查询


### 幻灯片 22

3.3 查询
3.3.3 嵌套查询
不同形式的查询间的替换：
 所有带IN谓词、比较运算符、ANY和ALL谓词的子查询都能用带EXISTS谓词的子查询等价替换；
 一些带EXISTS或NOT EXISTS谓词的子查询不能被其他形式的子查询等价替换。
若内层查询结果为空，则返回真值
若内层查询结果非空，则返回假值
NOT EXISTS谓词：


### 幻灯片 23

3.3 查询
3.3.3 嵌套查询
用EXISTS/NOT EXISTS实现全称量词
SQL语言中没有全称量词； 
可以把带有全称量词的谓词转换为等价的带有存在量词的谓词：
       　 (x)P
≡ (x(P))


### 幻灯片 24

3.3 查询
3.3.3 嵌套查询
【例3.59】查询被所有的抢修工程项目都使用了的物资编号及物资名称、规格。
分析：查询这样的物资，没有一个抢修工程没有使用过它。
SELECT mat_num,mat_name, speci
FROM Stock
WHERE
NOT EXISTS
         (  SELECT *
            FROM Out_stock
            WHERE  mat_num= Stock.mat_num  
                 AND   prj_num = Salvaging.prj_num));
NOT EXISTS
  (  SELECT *
     FROM Salvaging
     WHERE


### 幻灯片 25

3.3 查询
3.3.3 嵌套查询
F
F
F
F
F
F 
F
T
F


### 幻灯片 26

3.3 查询
3.3.3 嵌套查询
用EXISTS/NOT EXISTS实现逻辑蕴涵(难点)
SQL语言中没有逻辑蕴涵运算；
可以利用谓词演算将逻辑蕴涵谓词等价转换为：
                   p  q
≡  p∨q


### 幻灯片 27

3.3 查询
3.3.3 嵌套查询
【例3.60】查询所用物资包含抢修工程20100016所用物资的抢修工程号。
解题思路：
 用逻辑蕴涵表达：查询抢修工程号为x的工程，对所有的物资y，只要20100016号工程项目使用了物资y，则x也使用了y。
 形式化表示：
	用p表示谓词 “抢修工程20100016使用了物资y”
	用q表示谓词 “抢修工程x使用了物资y”
  则上述查询为: (y) (p  q)
等价变换：(y)(p  q) ≡   (y ((p  q ))
                                    ≡   (y (( p∨ q)
                                     ≡   y(p∧q)
变换后语义：不存在这样的物资 y，抢修工程20100016使用了物资 y，而抢修工程 x 没有使用物资 y。


### 幻灯片 28

3.3 查询
3.3.3 嵌套查询
SELECT DISTINCT prj_num
FROM Out_stock  sx
WHERE
NOT EXISTS
           ( SELECT *
             FROM Out_stock  sy
             WHERE sy.prj_num = '20100016'  
                   AND
NOT EXISTS
      (  SELECT *
          FROM Out_stock  sz
          WHERE  sz.mat_num= sy.mat_num  
             AND   sz.prj_num = sx.prj_num));
不存在这样的物资，抢修工程20100016使用了，而抢修工程 x 没有使用。


### 幻灯片 29

3.3 查询
3.3.3 嵌套查询
F
T
F
F
T
F


### 幻灯片 30

小结
带谓词IN的嵌套查询
带有比较运算符的子查询
带有ANY或ALL谓词的子查询
带有EXISTS谓词的子查询
谢谢观看！

---

## 3.3.4 集合查询(MySQL).pptx


### 幻灯片 1

数据库原理


### 幻灯片 2

第三章    结构化查询语言SQL

	3.1 SQL概述
	3.2 数据定义语句
	3.3 查询
        3.4 数据更新
	3.5 视图


### 幻灯片 3

3.3 查询
3.3.4 集合查询
Select语句的结果是一个元组的集合，多个Select语句的结果可以进行集合操作。
集合操作种类：
 并操作(UNION)
 交操作(INTERSECT)
 差操作(EXCEPT)
注：参加集合操作的结果集必须是相容的：
 属性个数及对应的数据类型必须一致；
 属性名无关，最后结果集采用第一个结果的属性名；
 缺省为自动去除重复元组；
 只能在整个语句的最后使用一次Order By。


### 幻灯片 4

3.3 查询
3.3.4 集合查询
【例3.61】 查询存放在供电局1#仓库的物资或者单价不大于50的物资。 

    SELECT *
    FROM Stock
    WHERE warehouse='供电局1#仓库'
    UNION
    SELECT *
    FROM Stock
    WHERE unit<=50;
或：
SELECT  DISTINCT  *
FROM Stock
 WHERE warehouse = '供电局1#仓库'
        OR unit <=50;
all
注: UNION操作自动去除重复元组，如果要保留重复元组的话，必须使用all关键词。


### 幻灯片 5

3.3 查询
3.3.4 集合查询
【例3.62】查询使用了物资编号为m001或m002的抢修工程的工程号。
SELECT prj_num
FROM Out_s tock
WHERE mat_num ='m001'
UNION
SELECT prj_num
FROM Out_stock
WHERE mat_num ='m002';
或：
SELECT  DISTINCT prj_num
FROM Out_stock
WHERE mat_num ='m001'
       OR  mat_num ='m002'


### 幻灯片 6

3.3 查询
3.3.5 通过中间表查询
【例3.63】查询使用的抢修物资数量前3名的抢修工程编号。
select prj_num
from  (select prj_num,sum(amount) as sum_amount
        from out_stock 
	   group by prj_num)  as S
 order by sum_amount  DESC
limit 3;


### 幻灯片 7

3.3 查询
3.3.5 通过中间表查询
【例3.64】查询每个抢修工程的抢修工程编号、名称及使用的抢修物资总数量
Select  salvaging.prj_num,prj_name,sum_amount
From salvaging inner join 
         (select prj_num,sum(amount) as sum_amount
           from out_stock 
           group by prj_num) as S
on salvaging.prj_num=S.prj_num


### 幻灯片 8

小结
并操作
交操作
差操作
谢谢观看！

---

## 3.4 数据更新(MySQL).pptx


### 幻灯片 1

数据库原理


### 幻灯片 2

第三章    结构化查询语言SQL

	3.1 SQL概述
	3.2 数据定义语句
	3.3 查询
        3.4 数据更新
	3.5 视图


### 幻灯片 3

3.4 数据更新
3.4.1 插入数据
1. 插入单个元组
功能: 将新元组插入指定表中。
语句格式为：
INSERT
INTO <表名> [(<属性列1>[，<属性列2 >…)]
VALUES (<常量1> [，<常量2>]    …   );


### 幻灯片 4

3.4 数据更新
3.4.1 插入数据
INTO子句
 指定要插入数据的表名及属性列；
 指定属性列的顺序可与表定义中的顺序不一致；
 没有指定属性列：表示要插入的是一条完整的元组，且属性列属性与表定义中的顺序一致；
 指定部分属性列：插入的元组在其余属性列上取空值，要求非空的属性列必须指定，不能为空。
VALUES子句
 提供的值必须与INTO子句匹配:
值的个数
值的类型


### 幻灯片 5

3.4 数据更新
3.4.1 插入数据
【例3.65】 将新的配电物资（物资编号：m020；物资名称：架空绝缘导线；规格：10KV-100；仓库名称：供电局1#仓库；单价：12.8；库存数量：50）插入配电物资库存记录表Stock中。
   INSERT 
   INTO Stock(mat_num,mat_name,speci,warehouse, unit,amount)
   VALUES ('m020','架空绝缘导线','10KV-100','供电局1#仓库', 12.8,50);
【例3.66】 将新的抢修工程（20110011，观澜站电缆接地抢修，2011-2-3 0:00:00，2011-2-5 12:00:00，1）插入到抢修工程计划表 Salvaging中。
   INSERT 
   INTO Salvaging
   VALUES ('20110011','观澜站电缆接地抢修','2011-2-3 0:00:00','2011-2-5 12:00:00',1);


### 幻灯片 6

3.4 数据更新
3.4.1 插入数据
功能:基本用法同插入单行元祖类似，但是允许将多条数据记录用逗号隔开，放在关键字VALUES的后面，插入数据表中。
语句格式:
INSERT 
INTO <表名> [<属性列1>[,<属性列2>…]]
VALUES (<常量1_1>[,<常量1_2>]…),
             (<常量2_1>[,<常量2_2>]…)
                   …
             (<常量n_1>[,<常量n_2>]…);
2. 插入多行元组


### 幻灯片 7

3.4 数据更新
3.4.1 插入数据
【例3.67】 将多行数据记录插入领料出库表 Out_stock中。
 
   INSERT 
   INTO Out_stock
   VALUES ('20110006','m001',2,'2011-3-9','工程4部'),
                ('20110006','m002',3,'2011-3-9','工程4部');


### 幻灯片 8

3.4 数据更新
3.4.1 插入数据
功能: 将子查询结果插入指定表中。
语句格式:
INSERT
INTO <表名> [(<属性列1>[，<属性列2 >…)]
子查询;
3. 插入子查询结果


### 幻灯片 9

3.4 数据更新
3.4.1 插入数据
INTO子句(与插入单条元组类似)
指定要插入数据的表名及属性列
属性列的顺序可与表定义中的顺序不一致
没有指定属性列：表示要插入的是一条完整的元组
指定部分属性列：插入的元组在其余属性列上取空值，要求非空的属性列必须指定，不能为空。
子查询
SELECT子句目标列必须与INTO子句匹配:
 值的个数
 值的类型


### 幻灯片 10

3.4 数据更新
3.4.1 插入数据
【例3.68】对每一抢修工程项目，求其所用物资的总费用，并把结果存入数据库。
第一步：建表
CREATE TABLE Prj_cost
(    prj_num char(8)  PRIMARY KEY ,    	 
     cost decimal(18, 2),
);
第二步：插入数据
INSERT
INTO Prj_cost
  SELECT prj_num, SUM (out_stock.amount*unit)
  FROM Out_stock,Stock
  WHERE Out_stock.mat_num=Stock.mat_num 
  GROUP BY prj_num


### 幻灯片 11

3.4 数据更新
3.4.2 修改数据
功能: 修改指定表中满足where子句条件的元组，并由set重新赋值；如果省略WHERE子句，表示要修改表中的所有元组。
语句格式:

UPDATE <表名>
SET <列名>=<表达式>[,<列名>=<表达式>]…
[ WHERE <条件> ];


### 幻灯片 12

3.4 数据更新
3.4.2 修改数据
【例3.69】 将编号为“m020”的物资单价改为44.5。
UPDATE Stock
SET unit =44.5
WHERE mat_num ='m020';
1. 修改单个元组的值
【例3.70】 将所有物资的单价增加1。
UPDATE Stock
SET unit=unit+1;
2. 修改多个元组的值
注：where缺省表示要修改表中所有元组.


### 幻灯片 13

3.4 数据更新
3.4.2 修改数据
【例3.71】将供电局1#仓库所有物资的领取数量置零。
3. 带子查询的修改语句
update Out_stock
    set amount =0
   where mat_num in 
                           ( select mat_num    from Stock
                             where warehouse ='供电局1#仓库');
Update out_stock, stock
       Set  out_stock.amount =0
       Where stock. mat_num = out_stock. mat_num 
            and warehouse ='供电局1#仓库';
该语句还可以写为：


### 幻灯片 14

3.4 数据更新
3.4.3 删除数据
功能: 从指定表中删除满足where子句条件的所有元组，若where缺省则删除表中所有元组；只删除表的数据，不删表的定义。
语句格式:

    DELETE 
    FROM <表名>
    [ WHERE <条件> ];


### 幻灯片 15

3.4 数据更新
3.4.3 删除数据
【例3.72】删除项目号为“20110001”的抢修工程领取编号为“m001”的物资出库记录。
DELETE
    FROM Out_stock
    WHERE prj_num ='20110001' AND mat_num ='m001';
1. 删除单个元组的值
2. 删除多个元组的值
【例3.73】 删除所有抢修工程的领料出库记录。
DELETE 
FROM Out_stock;


### 幻灯片 16

3.4 数据更新
3.4.3 删除数据
3. 带子查询的删除语句
【例3.74】删除观澜站光缆抢修工程项目的所有领料出库记录。
Delete  
From Out_stock
Where prj_num in
    (select prj_num 
    from Salvaging
    where prj_name ='观澜站光缆抢修');
delete 
From out_stock, salvaging
 Where salvaging. prj_num = out_stock.prj_num and prj_name ='观澜站光缆抢修';
思考：这语句正确么？
错误！


### 幻灯片 17

小结
插入数据
修改数据
删除数据
谢谢观看！

---

## 3.5 视图.pptx [(MySQL)].pptx


### 幻灯片 1

数据库原理


### 幻灯片 2

第三章    结构化查询语言SQL

	3.1 SQL概述
	3.2 数据定义语句
	3.3 查询
        3.4 数据更新
	3.5 视图


### 幻灯片 3

3.5 视图
视图的特点:
虚表，是从一个或几个基本表（或视图）导出的表；
只存放视图定义，不存放数据，因此不会出现数据冗余；
基表中的数据一旦发生变化，从视图中查询出的数据也随之改变；
用户可通过视图这样的窗口，看到数据库中感兴趣的数据。
基于视图的操作：
 查询
 删除
 受限更新
 定义基于该视图的新视图


### 幻灯片 4

3.5 视图
3.5.1 视图的定义与删除
语句格式:
CREATE VIEW <视图名>[(<列名>[,<列名>]…)] 
AS <子查询>
[ WITH CHECK OPTION];
1. 定义视图
注：视图是用一个查询块的结果定义的，但子查询中通常不允许含有Order by子句和Distinct短语。
       WITH CHECK OPTION表示用视图进行UPDATE、INSERT和DELETE操作时要保证更新、插入或删除的元组满足视图定义中的谓词条件（即子查询中的条件表达式）。


### 幻灯片 5

3.5 视图
3.5.1 视图的定义与删除
组成视图的属性列名：
全部省略：由子查询中SELECT目标列中的各个字段组成。
全部指定：以下情况必须明确指定视图的所有列名:
   (1) 某个目标列是集函数或列表达式；
   (2) 多表连接时选出了几个同名列作为视图的属性名；
   (3) 需要在视图中为某个列启用新的更合适的名字。


### 幻灯片 6

3.5 视图
3.5.1 视图的定义与删除
【例3.75】建立供电局1#仓库所存放物资的视图。
CREATE VIEW s1_stock
AS
行列子集视图： 从单个基本表导出的，只是去掉了基本表的某些行和某些列，但保留了码的视图。
建立在单个基本表上的视图
SELECT mat_num,mat_name,speci,amount,unit
 FROM Stock
 WHERE warehouse ='供电局1#仓库';


### 幻灯片 7

3.5 视图
3.5.1 视图的定义与删除
注：DBMS执行CREATE VIEW语句时只是把视图的定义存入数据字典，并不执行其中的SELECT语句。只是在对视图进行查询时，才按视图的定义从基本表中将数据查出。
SELECT * FROM s1_stock


### 幻灯片 8

3.5 视图
3.5.1 视图的定义与删除
【例3.76】建立供电局1#仓库所存放物资的视图，并要求进行修改和插入操作时仍需保证该视图只有供电局1#仓库所存放的物资。
CREATE VIEW s2_stock
AS
 SELECT mat_num,mat_name,speci,amount,unit
 FROM Stock
 WHERE warehouse ='供电局1#仓库'
 WITH CHECK OPTION
注意：以后对该视图进行插入、修改和删除操作时，DBMS会自动检查或加上warehouse ='供电局1#仓库'的条件。


### 幻灯片 9

3.5 视图
3.5.1 视图的定义与删除
建立在多个基本表上的视图
【例3.77】 建立由抢修工程项目名称（prj_name）、出库物资名称（mat_name）、规格（speci）及领取数量（amount）的视图。
CREATE VIEW s1_outstock
AS
SELECT prj_name, mat_name,speci, out_stock.amount
   FROM Stock inner join  Out_stock
      on Stock.mat_num = Out_stock.mat_num 
       inner join Salvaging 
      on Salvaging.prj_num = Out_stock.prj_num;


### 幻灯片 10

3.5 视图
3.5.1 视图的定义与删除
基于视图的视图
【例3.78】建立供电局1#仓库所存放物资库存数量不少于50的视图。
CREATE VIEW s3_stock
AS
SELECT mat_num,mat_name,speci,amount
   FROM s1_stock
   WHERE amount>=50;


### 幻灯片 11

3.5 视图
3.5.1 视图的定义与删除
带表达式的视图
【例3.79】建立一个体现抢修工程项目实际抢修天数的视图。
CREATE VIEW s1_salvaging
AS
－带虚拟列（基本表上并不实际存在的列）的视图。
注意：本例中由于SELECT子句的目标列中含有表达式，因此必须在CREATE VIEW的视图名后面明确说明视图的各个属性列名。
SELECT prj_name, start_date, end_date,   datediff(day,start_date,end_date )
  FROM Salvaging;
(prj_name, start_date, end_date,days)


### 幻灯片 12

3.5 视图
3.5.1 视图的定义与删除
建立分组视图
－用带集函数和Group by子句的查询来定义的视图。
【例3.80】将仓库名称与其仓库内所存放物资的种类定义为一个视图。
CREATE VIEW s4_stock
AS
SELECT warehouse, COUNT(mat_num) 
  FROM Stock
  GROUP BY warehouse;
(warehouse,counts)


### 幻灯片 13

3.5 视图
3.5.1 视图的定义与删除
一类不易扩充的视图
－以 SELECT * 方式创建的视图可扩充性差，应尽可能避免。
【例3.81】将所有已按期完成的抢修工程定义为一个视图。
CREATE VIEW s2_salvaging (prj_num,prj_name,start_date,end_date,prj_status)
AS
  SELECT * 
  FROM Salvaging
  WHERE prj_status=1;


### 幻灯片 14

3.5 视图
3.5.1 视图的定义与删除
语句格式:
         DROP VIEW <视图名> ;
注： 1）该语句从数据字典中删除指定的视图定义；
   2）由该视图导出的其他视图定义仍在数据字典中，但已不能使用，必须显式删除;
   3）删除基表时，由该基表导出的所有视图定义均已不能使用，都必须显式删除。
2. 删除视图
【例3.82】删除视图S1_Stock。
DROP VIEW S1_Stock;
DROP VIEW S3_Stock;
注：由于s1_stock视图上还导出了s3_stock视图，虽然s3_stock视图的定义仍在数据字典中，但已无法使用，所以需要使用DROP VIEW s3_stock将其删除。


### 幻灯片 15

3.5 视图
3.5.2 查询视图
从用户角度：
      －查询视图与查询基本表相同。
注：
 (一般情况下)视图可以像基本表那样使用；
 视图名可以出现在关系名可以出现的地方；
 DBMS将视图转换成对基本表的操作。
DBMS实现视图查询的方法：视图消解法（View Resolution）
1）进行有效性检查，检查查询的基本表、视图是否存在；
2）如果存在，从数据字典中取出视图的定义，把视图定义中的子查询与用户的查询结合起来，转换成等价的对基本表的查询；
3）执行修正后的查询。


### 幻灯片 16

3.5 视图
3.5.2 查询视图
【例3.83】 在供电局1#仓库的物资视图s1_stock中找出单价小于20的物资名称、规格和单价。
SELECT mat_name,speci, unit
FROM s1_stock
WHERE unit<20;
转换后的查询语句为：
   SELECT mat_name,speci, unit
   FROM  Stock
   WHERE warehouse ='供电局1#仓库' 
      AND    unit<20;


### 幻灯片 17

3.5 视图
3.5.2 查询视图
【例3.84】 查询使用了供电局1#仓库物资的抢修工程项目号。
SELECT distinct prj_num
FROM s1_stock, inner join Out_stock
on s1_stock.mat_num=Out_stock.mat_num;
转换后的查询语句为：
SELECT distinct prj_num 
FROM Stock inner join  Out_stock on Stock.mat_num=Out_stock.mat_num
WHERE warehouse =‘供电局1#仓库’


### 幻灯片 18

3.5 视图
3.5.2 查询视图
视图消解法的局限:有些情况下，视图消解法不能转换成正确查询，则查询时会出现问题。
【例3.85】 查询所存物资种类大于2的仓库名称。
SELECT warehouse
FROM s4_stock
WHERE counts>2;
转换后的查询语句为：
SELECT warehouse
FROM Stock
WHERE COUNT(mat_num) >2
GROUP BY warehouse;
正确：
SELECT warehouse
FROM Stock
GROUP BY warehouse 
HAVING COUNT(mat_num) >2;
错误！


### 幻灯片 19

3.5 视图
3.5.3 更新视图
受限更新

 DBMS实现视图更新的方法：
视图消解法（View Resolution）

指定WITH CHECK OPTION子句后
        DBMS在更新视图时会进行检查，防止用户通过视图对不属于视图范围内的基本表数据进行更新。


### 幻灯片 20

3.5 视图
3.5.3 更新视图
【例3.86】 将供电局1#仓库的物资视图s1_stock中编号为m001的物资库存量改为100。
UPDATE s1_stock
SET amount =100
WHERE mat_num = 'm001';
转换后的语句：
      UPDATE Stock
      SET amount =100
      WHERE warehouse ='供电局1#仓库' 
            AND mat_num = 'm001';


### 幻灯片 21

3.5 视图
3.5.3 更新视图
【例3.87】向供电局1#仓库的物资视图s1_stock中插入一个新的物资记录，其中物资编号为“m022”，物资名称为“护套绝缘电线”， 规格为“BVV-150”，数量为100，单价为14.5。
INSERT
INTO s1_stock
VALUES('m022', '护套绝缘电线', 'BVV-150', 100,14.5);


### 幻灯片 22

3.5 视图
3.5.3 更新视图
若向供电局1#仓库的物资视图s2_stock中插入一个新的物资记录，分析结果。
INSERT
INTO s2_stock
VALUES('m023', '护套绝缘电线', 'BVV-150', 100,13.5);


### 幻灯片 23

3.5 视图
3.5.3 更新视图
【例3.88】 删除供电局1#仓库的物资视图s1_stock中编号为m001的物资的记录。
DELETE 
  FROM s1_stock
  WHERE mat_num = 'm001';
转换后的语句：
  DELETE 
  FROM Stock
  WHERE warehouse ='供电局1#仓库' 
        AND mat_num = 'm001';


### 幻灯片 24

3.5 视图
3.5.3 更新视图
在关系数据库中，并不是所有视图都可用于更新操作，因为有些视图的更新操作不能唯一有意义地转换成为相对应基本表的更新操作。

SQL SERVER中规定以下视图无法更新：
 视图的字段来自聚集函数；
 视图定义中含有GROUP BY子句；
 视图定义中含有DISTINCT短语;
 一个不允许更新的视图上定义的视图也不允许更新。


### 幻灯片 25

3.5 视图
3.5.4 视图的作用
1. 能够简化用户的操作
当视图中的数据不是直接来自某个基本表，而是基于多张表的连接而形成的视图，定义视图能够简化用户的数据查询操作。
2. 能够使用户以多种角度看待同一数据
视图机制能使不同用户以不同方式看待同一数据，适应数据库共享的需要。
3. 能够对机密数据提供安全保护
对不同用户定义不同视图，使每个用户只能看到他有权看到的数据；
4. 对数据库的重构提供了一定程度的逻辑独立性


### 幻灯片 26

3.5 视图
3.5.4 视图的作用
例：配电物资库存记录表 Stock(mat_num,mat_name,speci,warehouse, amount,unit,total),“垂直”地分成两个基本表：
   s1(mat_num,mat_name,speci,warehouse)
   s2(mat_num,amount,unit, total )
通过建立一个视图Stock：
CREATE VIEW Stock(mat_num,mat_name,speci, warehouse, amount,unit,total)
  AS
SELECT s1.mat_num, s1.mat_name, s1.speci, s1.warehouse, s2.amount, s2.unit, s2.total
FROM s1, s2
WHERE s1.mat_num =s2. mat_num    
         
   使用户的外模式保持不变，从而对原Stock表的查询程序不必修改。


### 幻灯片 27

小结
视图的定义与删除
查询视图
更新视图
视图的作用
谢谢观看！

---

