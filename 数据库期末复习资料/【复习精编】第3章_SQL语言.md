# 数据库第3章 - SQL语言 【复习精编】

> 整理自数据库期末复习PPT，精炼知识点

---

## 📚 章节概览

- **3.1 SQL概述**
- **3.2 数据定义语句（DDL）**
- **3.3 查询（DQL）**
- **3.4 数据更新（DML）**
- **3.5 视图（VIEW）**

---

## 3.1 SQL概述

### 🎯 SQL简介

**全称：** Structured Query Language（结构化查询语言）

**发展历史：**
- 1974年由Boyce和Chamberlin提出
- 首先在IBM的System R上实现
- 1986年成为ANSI和ISO标准
- 标准版本：SQL/86、SQL/89、SQL/92、SQL99、SQL2003、SQL2008、SQL2011、SQL2016

### ⭐ SQL语言的五大特点

#### 1. 综合统一
集DDL、DML、DCL于一体，语言风格统一

| 功能类型 | 操作内容 |
|---------|---------|
| 数据定义（DDL） | 定义、删除、修改关系模式；定义、删除视图、索引 |
| 数据操纵（DML） | 数据查询；数据增、删、改 |
| 数据控制（DCL） | 用户访问权限的授予、收回 |

#### 2. 高度非过程化
- 用户只需提出"做什么"
- "怎么做"由DBMS自动完成
- 无需了解存取路径

#### 3. 面向集合的操作方式
- 操作对象：一个或多个关系
- 操作结果：关系

#### 4. 两种使用方式
- **自主型**：独立使用
- **嵌入型**：嵌入到高级语言中

#### 5. 语言简洁、易学易用
**核心9个动词：**

| SQL功能 | 操作符 |
|---------|--------|
| 数据查询 | SELECT |
| 数据定义 | CREATE, DROP, ALTER |
| 数据操纵 | INSERT, UPDATE, DELETE |
| 数据控制 | GRANT, REVOKE |

---

## 3.2 数据定义语句（DDL）

### 📋 数据定义操作汇总

| 操作对象 | 创建 | 删除 | 修改 |
|---------|------|------|------|
| 数据库 | CREATE DATABASE | DROP DATABASE | - |
| 表 | CREATE TABLE | DROP TABLE | ALTER TABLE |
| 视图 | CREATE VIEW | DROP VIEW | - |
| 索引 | CREATE INDEX | DROP INDEX | - |

### 🗄️ 数据库操作

#### 创建数据库
```sql
CREATE DATABASE <数据库名>;
-- 示例
CREATE DATABASE SampleDB;
```

#### 删除数据库
```sql
DROP DATABASE <数据库名>;
-- 示例
DROP DATABASE SampleDB;
```

### 📊 表的定义

#### 1. 创建表（CREATE TABLE）

**语法格式：**
```sql
CREATE TABLE <表名>
(
  <列名> <数据类型> [列级完整性约束条件],
  <列名> <数据类型> [列级完整性约束条件],
  ...
  [表级完整性约束条件]
);
```

**完整性约束类型：**

| 约束类型 | 语法 | 说明 |
|---------|------|------|
| 主码约束 | PRIMARY KEY | 定义主键 |
| 唯一性约束 | UNIQUE | 列值唯一 |
| 非空约束 | NOT NULL | 不允许空值 |
| 外码约束 | FOREIGN KEY REFERENCES 表名(列名) | 定义外键 |
| 检查约束 | CHECK(表达式) | 自定义约束条件 |
| 默认值约束 | DEFAULT 默认值 | 指定默认值 |

**示例：**
```sql
-- 例1：创建抢修工程表
CREATE TABLE Salvaging
(
  prj_num CHAR(8) PRIMARY KEY,  -- 列级主码约束
  prj_name VARCHAR(50),
  start_date DATETIME,
  end_date DATETIME,
  prj_status BIT
);

-- 例2：创建物资库存表（带CHECK约束）
CREATE TABLE Stock
(
  mat_num CHAR(4) PRIMARY KEY,
  mat_name VARCHAR(50) NOT NULL,
  speci VARCHAR(20) NOT NULL,
  warehouse CHAR(20) NULL,
  amount INT NULL CHECK(amount>0),  -- 列级CHECK
  unit DECIMAL(18,2),
  CHECK(mat_num LIKE '[m][0-9][0-9][0-9]')  -- 表级CHECK
);

-- 例3：创建出库表（复合主码、外码）
CREATE TABLE Out_stock
(
  prj_num CHAR(8),
  mat_num CHAR(4),
  amount INT,
  get_date DATETIME DEFAULT NOW(),  -- 默认值
  department CHAR(20),
  PRIMARY KEY(prj_num, mat_num),  -- 表级主码约束（复合主码）
  FOREIGN KEY (prj_num) REFERENCES Salvaging(prj_num),
  FOREIGN KEY (mat_num) REFERENCES Stock(mat_num)
);
```

#### 2. 修改表（ALTER TABLE）

**语法格式：**
```sql
ALTER TABLE <表名>
[ADD <新列名> <数据类型> [完整性约束]]        -- 增加列
[DROP COLUMN <列名> | <完整性约束名>]          -- 删除列/约束
[MODIFY COLUMN <列名> <数据类型> <完整性约束>] -- 修改列
```

**示例：**
```sql
-- 增加列
ALTER TABLE Salvaging ADD prj_director VARCHAR(10);

-- 增加列（带默认值）
ALTER TABLE Salvaging ADD prj_director VARCHAR(10) NOT NULL DEFAULT '张三';

-- 删除列
ALTER TABLE Salvaging DROP COLUMN prj_director;

-- 修改列
ALTER TABLE Out_stock MODIFY COLUMN department VARCHAR(20) NOT NULL;
```

#### 3. 删除表（DROP TABLE）

```sql
DROP TABLE <表名>;
-- 示例
DROP TABLE Out_stock;
```

**⚠️ 注意：**
- 表删除后，数据、索引、视图都将自动删除
- 被其他表外键引用的表不能删除

### 🔐 约束的添加与删除

```sql
-- 添加约束
ALTER TABLE <表名> 
ADD CONSTRAINT <约束名> <约束表达式>;

-- 删除约束
ALTER TABLE <表名> 
DROP CONSTRAINT <约束名>;

-- 示例：添加外键约束
ALTER TABLE out_stock 
ADD CONSTRAINT FK_Salvaging_Out_stock
FOREIGN KEY (prj_num) REFERENCES salvaging(prj_num);

-- 示例：删除外键约束
ALTER TABLE out_stock 
DROP CONSTRAINT FK_Salvaging_Out_stock;

-- 示例：添加CHECK约束
ALTER TABLE stock 
ADD CONSTRAINT CK_amount CHECK(amount>0);

-- 示例：添加唯一性约束
ALTER TABLE salvaging 
ADD CONSTRAINT un_prj_name UNIQUE(prj_name);
```

---

## 3.3 查询（SELECT语句）

### 📐 查询的一般格式

```sql
SELECT [ALL|DISTINCT] <目标列表达式>
FROM <表名或视图名>
[WHERE <条件表达式>]
[GROUP BY <列名1> [HAVING <条件表达式>]]
[ORDER BY <列名2> [ASC|DESC]];
```

### 🔄 SELECT语句的执行顺序

1. **FROM**：读取表数据，执行笛卡尔积
2. **WHERE**：选择满足条件的元组
3. **GROUP BY**：按列值分组
4. **HAVING**：选择满足条件的组
5. **SELECT**：投影，输出目标列
6. **ORDER BY**：排序

**等价于关系代数：** π属性列表(σ条件(R1 × R2 × ... × Rm))

---

### 3.3.1 单表查询

#### 1. 选择表中若干列（投影）

```sql
-- 查询指定列
SELECT mat_num, mat_name, speci FROM Stock;

-- 查询全部列
SELECT * FROM Stock;

-- 查询经过计算的值
SELECT prj_name, start_date, end_date, 
       DATEDIFF(end_date, start_date) AS 抢修天数
FROM Salvaging;

-- 使用别名
SELECT prj_name AS 项目名称, 
       DATEDIFF(end_date, start_date) 抢修天数
FROM Salvaging;
```

**📅 MySQL常用时间函数：**

| 函数 | 功能 |
|------|------|
| NOW() | 返回当前日期和时间 |
| YEAR(d) | 返回日期d中的年份 |
| MONTH(d) | 返回日期d中的月份 |
| DAYOFMONTH(d) | 返回日期d是本月第几天 |
| DATEDIFF(d1,d2) | 返回d1和d2相隔天数 |
| ADDDATE(d,n) | 返回d加上n天的日期 |
| SUBDATE(d,n) | 返回d减去n天的日期 |

#### 2. 选择表中若干元组（选择）

##### A. 消除重复行（DISTINCT）
```sql
-- 去重
SELECT DISTINCT warehouse FROM Stock;

-- 默认保留重复行（ALL）
SELECT warehouse FROM Stock;
```

##### B. 查询满足条件的元组（WHERE）

**比较运算符：** =、>、<、>=、<=、!=（<>）、BETWEEN...AND、IN、LIKE

**逻辑运算符：** AND、OR、NOT

**(1) 比较大小**
```sql
-- 等于
SELECT mat_num, mat_name, speci, amount
FROM Stock
WHERE warehouse = '供电局1#仓库';

-- 小于
SELECT mat_name, amount, unit
FROM Stock
WHERE unit < 80;

-- 大于等于的否定形式
SELECT mat_name, amount, unit
FROM Stock
WHERE NOT unit >= 80;
```

**(2) 确定范围（BETWEEN...AND）**
```sql
-- 在范围内
SELECT mat_name, amount, unit
FROM Stock
WHERE unit BETWEEN 50 AND 100;

-- 等价于
WHERE unit >= 50 AND unit <= 100;

-- 不在范围内
SELECT mat_name, amount, unit
FROM Stock
WHERE unit NOT BETWEEN 50 AND 100;

-- 等价于
WHERE unit < 50 OR unit > 100;
```

**(3) 确定集合（IN）**
```sql
-- 在集合中
SELECT mat_name, speci, amount
FROM Stock
WHERE warehouse IN('供电局1#仓库', '供电局2#仓库');

-- 等价于
WHERE warehouse = '供电局1#仓库' 
   OR warehouse = '供电局2#仓库';

-- 不在集合中
SELECT mat_name, speci, amount
FROM Stock
WHERE warehouse NOT IN('供电局1#仓库', '供电局2#仓库');
```

**(4) 字符匹配（LIKE）**

**通配符：**
- `%`：任意长度（0个或多个）字符串
- `_`：任意单个字符
- `ESCAPE`：定义换码字符

```sql
-- 完全匹配（等价于=）
SELECT * FROM Stock
WHERE warehouse LIKE '供电局1#仓库';

-- 后缀匹配
SELECT mat_num, mat_name, speci
FROM Stock
WHERE mat_name LIKE '%绝缘电线';

-- 位置匹配
SELECT mat_num, mat_name, speci
FROM Stock
WHERE mat_name LIKE '__绝缘%';  -- 第3、4个字为"绝缘"

-- 不包含
SELECT mat_num, mat_name, speci
FROM Stock
WHERE mat_name NOT LIKE '%绝缘%';

-- 使用ESCAPE转义特殊字符
SELECT * FROM Stock
WHERE mat_name LIKE '%户外/_真空%' ESCAPE '/';
-- '/'是换码字符，'/_'表示普通字符'_'
```

**(5) 空值查询（IS NULL）**
```sql
-- 查询空值
SELECT mat_num, mat_name
FROM Stock
WHERE unit IS NULL;

-- 查询非空值
SELECT mat_num, mat_name
FROM Stock
WHERE unit IS NOT NULL;
```

**⚠️ 注意：** 不能用 `= NULL` 或 `!= NULL`

**(6) 多重条件查询（AND、OR）**
```sql
SELECT mat_num, warehouse, amount
FROM Stock
WHERE mat_name = '护套绝缘电线' 
  AND speci = 'BVV-120';
```

**优先级：** AND > OR（可用括号改变优先级）

#### 3. 对查询结果排序（ORDER BY）

```sql
-- 单列排序（降序）
SELECT mat_name, unit
FROM Stock
WHERE mat_name = '护套绝缘电线'
ORDER BY unit DESC;

-- 多列排序
SELECT *
FROM Stock
ORDER BY warehouse DESC, amount ASC;  -- 先按仓库降序，再按数量升序
```

**说明：**
- `ASC`：升序（默认）
- `DESC`：降序
- 空值最小

#### 4. 限制查询结果数量（LIMIT）

```sql
-- 显示前N条
SELECT * FROM Stock
ORDER BY amount DESC
LIMIT 2;

-- 从指定位置开始显示N条
SELECT * FROM Stock
LIMIT 3, 5;  -- 从第3条开始显示5条（初始位置从0开始）
```

#### 5. 聚集函数（Aggregate Functions）

| 函数 | 功能 | 适用类型 |
|------|------|----------|
| COUNT(*) | 统计元组个数 | 任意 |
| COUNT([DISTINCT] 列名) | 统计列中值的个数 | 任意 |
| SUM([DISTINCT] 列名) | 计算列值总和 | 数值型 |
| AVG([DISTINCT] 列名) | 计算列值平均值 | 数值型 |
| MAX([DISTINCT] 列名) | 求列中最大值 | 数值型 |
| MIN([DISTINCT] 列名) | 求列中最小值 | 数值型 |

```sql
-- 统计项目数（去重）
SELECT COUNT(DISTINCT prj_num)
FROM out_stock;

-- 求最大、最小、平均值
SELECT MAX(amount) AS 最高数量, 
       MIN(amount) AS 最低数量, 
       AVG(amount) AS 平均数量
FROM out_stock
WHERE mat_num = 'm001';
```

**⚠️ 注意：**
- 除COUNT(*)外，其他函数忽略NULL值
- WHERE子句中不能使用聚集函数

#### 6. 分组查询（GROUP BY）

```sql
-- 基本分组
SELECT prj_num AS 项目号, COUNT(*) AS 物资种类
FROM out_stock
GROUP BY prj_num;

-- 带HAVING的分组（筛选组）
SELECT prj_num AS 项目号, COUNT(*) AS 物资种类
FROM out_stock
GROUP BY prj_num
HAVING COUNT(*) >= 2;  -- 只显示使用了2种以上物资的项目

-- 多列分组
SELECT department, mat_num, 
       COUNT(DISTINCT prj_num) AS 项目个数,
       SUM(amount) AS 领取总量
FROM Out_stock
GROUP BY department, mat_num;

-- 带ROLLUP的分组（分级汇总）
SELECT department, mat_num,
       COUNT(DISTINCT prj_num) AS 项目个数,
       SUM(amount) AS 领取总量
FROM Out_stock
GROUP BY department, mat_num
WITH ROLLUP;
```

**WHERE vs HAVING：**

| 对比项 | WHERE | HAVING |
|--------|-------|--------|
| 作用对象 | 基本表或视图 | 分组后的结果集 |
| 筛选单位 | 元组（行） | 组 |
| 执行时机 | 分组前 | 分组后 |
| 能否使用聚集函数 | 否 | 是 |

#### 7. 正则表达式查询（REGEXP）

**常用模式字符：**

| 模式字符 | 说明 |
|---------|------|
| ^ | 匹配字符串开始 |
| $ | 匹配字符串结束 |
| . | 任意单个字符 |
| [字符集合] | 匹配字符集合中的任意一个 |
| [^字符集合] | 不匹配字符集合中的任意一个 |
| S1\|S2\|S3 | 匹配S1、S2、S3中任意一个 |
| * | 匹配0个或多个前面的字符 |
| + | 匹配1个或多个前面的字符 |
| {N} | 出现N次 |
| {M,N} | 出现M到N次 |

```sql
-- 查询包含"西丽"或"明珠"的项目
SELECT * FROM Salvaging
WHERE prj_name REGEXP '西丽|明珠';

-- 查询包含"2"出现1到2次的项目
SELECT * FROM Salvaging
WHERE prj_name REGEXP '2{1,2}';
```

---

### 3.3.2 连接查询

**定义：** 同时涉及两个或多个表的查询

**连接条件格式：**
```
[表名1.]列名1 <比较运算符> [表名2.]列名2
[表名1.]列名1 BETWEEN [表名2.]列名2 AND [表名2.]列名3
```

#### 1. 等值连接与非等值连接

**等值连接：** 连接运算符为 `=`

```sql
-- 等值连接
SELECT Salvaging.*, Out_stock.*
FROM Salvaging, Out_stock
WHERE Salvaging.prj_num = Out_stock.prj_num;

-- 自然连接（去除重复列）
SELECT Salvaging.prj_num, prj_name, start_date, end_date, prj_status,
       mat_num, amount, get_date, department
FROM Salvaging, Out_stock
WHERE Salvaging.prj_num = Out_stock.prj_num;
```

**⚠️ 注意：** 同名属性必须加表名前缀

#### 2. 内连接查询（INNER JOIN）

```sql
-- 显式内连接
SELECT salvaging.prj_num, prj_name, start_date, end_date, prj_status,
       mat_num, amount, get_date, department
FROM salvaging 
INNER JOIN out_stock ON salvaging.prj_num = out_stock.prj_num;
```

**隐式连接 vs 显式连接：**
- **隐式连接**：FROM中所有表笛卡尔积，WHERE过滤
- **显式连接**：每次连接时用ON过滤，效率更高 ✅

#### 3. 外连接查询（OUTER JOIN）

**与内连接的区别：**
- 内连接：只输出满足连接条件的元组
- 外连接：保留主体表中不满足条件的元组（其他列填NULL）

**三种类型：**

```sql
-- 左外连接（保留左表所有记录）
SELECT Salvaging.prj_num, prj_name, start_date, end_date, prj_status,
       mat_num, amount, get_date, department
FROM Salvaging 
LEFT OUTER JOIN Out_stock ON Salvaging.prj_num = Out_stock.prj_num;

-- 右外连接（保留右表所有记录）
SELECT ... 
FROM Salvaging 
RIGHT OUTER JOIN Out_stock ON ...;

-- 全外连接（保留两表所有记录）
SELECT ...
FROM Salvaging 
FULL OUTER JOIN Out_stock ON ...;
```

#### 4. 复合条件连接查询

WHERE子句中包含多个条件

```sql
SELECT Out_stock.mat_num, mat_name, speci, Out_stock.amount
FROM Stock 
JOIN Out_stock ON Stock.mat_num = Out_stock.mat_num
WHERE prj_num = '20100015';  -- 连接条件 + 其他条件
```

#### 5. 自身连接查询

同一个表的两个副本之间的连接

```sql
-- 查询同时使用了m001和m002的项目
SELECT A.prj_num
FROM Out_stock A, Out_stock B
WHERE A.prj_num = B.prj_num
  AND A.mat_num = 'm001'
  AND B.mat_num = 'm002';

-- 或使用INNER JOIN
SELECT A.prj_num
FROM Out_stock A 
INNER JOIN Out_stock B ON A.prj_num = B.prj_num
WHERE A.mat_num = 'm001' AND B.mat_num = 'm002';
```

**⚠️ 注意：** 必须给表起别名，所有属性都要加前缀

---

### 3.3.3 嵌套查询

**定义：** SELECT语句的WHERE或HAVING子句中嵌套另一个SELECT语句

```sql
SELECT prj_name
FROM Salvaging
WHERE prj_num IN
      (SELECT prj_num
       FROM Out_stock
       WHERE mat_num = 'm003');
```

#### 查询类型分类

**按相关性分类：**
- **不相关子查询**：子查询不依赖父查询，由里向外执行
- **相关子查询**：子查询依赖父查询，反复执行

#### 1. 带IN谓词的嵌套查询

```sql
-- 示例：查询与"BVV-120"护套绝缘电线在同一仓库的物资
SELECT mat_name, speci, amount
FROM Stock
WHERE warehouse IN
      (SELECT warehouse
       FROM Stock
       WHERE speci = 'BVV-120' 
         AND mat_name = '护套绝缘电线');

-- 多层嵌套
SELECT mat_num, mat_name
FROM Stock
WHERE mat_num IN
      (SELECT mat_num
       FROM Out_stock
       WHERE prj_num IN
             (SELECT prj_num
              FROM Salvaging
              WHERE prj_name = '观澜站光缆抢修'));
```

**可用连接查询替代：**
```sql
SELECT Stock.mat_num, mat_name
FROM Stock, Out_stock, Salvaging
WHERE Stock.mat_num = Out_stock.mat_num
  AND Out_stock.prj_num = Salvaging.prj_num
  AND prj_name = '观澜站光缆抢修';
```

#### 2. 带比较运算符的子查询

子查询必须返回**单值**

```sql
-- 相关子查询示例：查询库存量超过本仓库平均库存量的物资
SELECT mat_num, mat_name, speci, amount
FROM Stock s1
WHERE amount > 
      (SELECT AVG(amount)
       FROM Stock s2
       WHERE s2.warehouse = s1.warehouse);
```

**相关子查询执行过程：**
1. 从外层取一个元组
2. 将相关属性值传给内层
3. 执行内层查询
4. 用内层结果判断外层WHERE条件
5. 重复直到外层表全部处理完

#### 3. 带ANY或ALL谓词的子查询

必须与比较运算符配合使用

| 谓词 | 含义 | 等价函数 |
|------|------|----------|
| >ANY | 大于子查询结果中某个值 | >MIN |
| <ANY | 小于子查询结果中某个值 | <MAX |
| >ALL | 大于子查询结果中所有值 | >MAX |
| <ALL | 小于子查询结果中所有值 | <MIN |
| =ANY | 等于子查询结果中某个值 | IN |
| !=ALL | 不等于子查询结果中所有值 | NOT IN |

```sql
-- 比某一物资库存量少
SELECT mat_name, speci, amount
FROM Stock
WHERE warehouse <> '供电局1#仓库'
  AND amount < ANY
      (SELECT amount
       FROM Stock
       WHERE warehouse = '供电局1#仓库');

-- 等价于使用MAX
WHERE amount < (SELECT MAX(amount) FROM Stock WHERE warehouse = '供电局1#仓库');

-- 比所有物资库存量少
SELECT mat_name, speci, amount
FROM Stock
WHERE warehouse <> '供电局1#仓库'
  AND amount < ALL
      (SELECT amount
       FROM Stock
       WHERE warehouse = '供电局1#仓库');

-- 等价于使用MIN
WHERE amount < (SELECT MIN(amount) FROM Stock WHERE warehouse = '供电局1#仓库');
```

**💡 提示：** 使用聚集函数效率更高 ✅

#### 4. 带EXISTS谓词的子查询

**EXISTS**：存在量词，返回TRUE或FALSE

- 子查询结果非空 → TRUE
- 子查询结果为空 → FALSE

```sql
-- 查询使用了物资的项目
SELECT prj_num, prj_name
FROM Salvaging
WHERE EXISTS
      (SELECT *
       FROM Out_stock
       WHERE Out_stock.prj_num = Salvaging.prj_num);

-- NOT EXISTS：查询未使用物资的项目
SELECT prj_num, prj_name
FROM Salvaging
WHERE NOT EXISTS
      (SELECT *
       FROM Out_stock
       WHERE Out_stock.prj_num = Salvaging.prj_num);
```

**⚠️ 注意：** EXISTS子查询的目标列通常用 `*`，因为只返回逻辑值

**EXISTS实现全称量词（难点）：**

逻辑等价：
- `∀x P(x)` ≡ `¬∃x ¬P(x)`
- "所有"可以转换为"不存在...不..."

```sql
-- 查询使用了全部物资的项目
SELECT prj_num, prj_name
FROM Salvaging
WHERE NOT EXISTS
      (SELECT *
       FROM Stock
       WHERE NOT EXISTS
             (SELECT *
              FROM Out_stock
              WHERE Out_stock.prj_num = Salvaging.prj_num
                AND Out_stock.mat_num = Stock.mat_num));
```

理解：不存在（一种物资）不被（该项目）使用 = 该项目使用了所有物资

---

### 3.3.4 集合查询

对多个查询结果进行集合运算

| 运算符 | 含义 | 说明 |
|--------|------|------|
| UNION | 并集 | 自动去重 |
| UNION ALL | 并集 | 保留重复 |
| INTERSECT | 交集 | 部分DBMS不支持 |
| EXCEPT / MINUS | 差集 | 部分DBMS不支持 |

```sql
-- 并集（去重）
SELECT mat_num FROM Stock WHERE warehouse = '供电局1#仓库'
UNION
SELECT mat_num FROM Out_stock WHERE prj_num = '20100015';

-- 并集（保留重复）
... UNION ALL ...

-- 交集（MySQL不直接支持，用IN代替）
SELECT mat_num FROM Stock WHERE warehouse = '供电局1#仓库'
  AND mat_num IN
      (SELECT mat_num FROM Out_stock WHERE prj_num = '20100015');
```

---

## 3.4 数据更新（DML）

### ➕ 插入数据（INSERT）

#### 1. 插入单个元组
```sql
-- 插入所有列
INSERT INTO Salvaging
VALUES ('20110011', '变压器抢修', '2011-03-15', '2011-03-16', 1);

-- 插入部分列
INSERT INTO Salvaging(prj_num, prj_name, start_date)
VALUES ('20110012', '电缆抢修', '2011-03-17');
```

#### 2. 插入查询结果
```sql
INSERT INTO 目标表(列1, 列2, ...)
SELECT 列1, 列2, ...
FROM 源表
WHERE 条件;
```

### 🔄 修改数据（UPDATE）

```sql
-- 修改单个元组
UPDATE Stock
SET amount = 100, unit = 50.00
WHERE mat_num = 'm001';

-- 修改多个元组
UPDATE Stock
SET unit = unit * 1.1
WHERE mat_name = '护套绝缘电线';

-- 使用子查询
UPDATE Out_stock
SET amount = amount + 10
WHERE mat_num IN
      (SELECT mat_num
       FROM Stock
       WHERE mat_name = '护套绝缘电线');
```

### ❌ 删除数据（DELETE）

```sql
-- 删除满足条件的元组
DELETE FROM Out_stock
WHERE prj_num = '20100015';

-- 删除所有元组（保留表结构）
DELETE FROM Out_stock;

-- 使用子查询
DELETE FROM Out_stock
WHERE mat_num IN
      (SELECT mat_num
       FROM Stock
       WHERE warehouse = '供电局1#仓库');
```

**⚠️ 注意：**
- DELETE删除元组，保留表结构
- DROP TABLE删除整个表
- TRUNCATE TABLE快速清空表

---

## 3.5 视图（VIEW）

### 🔍 视图的概念

**定义：** 从一个或多个基本表导出的虚表

**特点：**
- 视图只存储定义，不存储数据
- 数据仍存储在基本表中
- 对视图的操作最终转换为对基本表的操作

**优点：**
1. **简化操作**：隐藏复杂查询
2. **数据独立性**：基本表结构变化，视图不变
3. **安全性**：限制用户访问范围
4. **逻辑独立性**：同一数据的不同表现形式

### 📝 视图的定义

#### 创建视图（CREATE VIEW）

```sql
CREATE VIEW <视图名> [(<列名1>, <列名2>, ...)]
AS <子查询>
[WITH CHECK OPTION];
```

**示例：**
```sql
-- 基本视图
CREATE VIEW v_project_info
AS
SELECT prj_num, prj_name, start_date, end_date
FROM Salvaging
WHERE prj_status = 1;

-- 指定列名
CREATE VIEW v_stock_summary(物资名称, 总库存)
AS
SELECT mat_name, SUM(amount)
FROM Stock
GROUP BY mat_name;

-- 带WITH CHECK OPTION（插入/更新时检查条件）
CREATE VIEW v_warehouse1
AS
SELECT * FROM Stock
WHERE warehouse = '供电局1#仓库'
WITH CHECK OPTION;
```

**列名的指定规则：**
必须指定列名的情况：
1. 目标列包含聚集函数
2. 目标列包含表达式
3. 多表连接时有同名列
4. 需要在视图中为列取新名字

#### 删除视图（DROP VIEW）

```sql
DROP VIEW <视图名>;
-- 示例
DROP VIEW v_project_info;
```

### 🔎 视图的查询

**与基本表查询完全相同：**
```sql
SELECT * FROM v_project_info;

SELECT * FROM v_stock_summary
WHERE 总库存 > 100;
```

**执行过程（视图消解）：**
1. 从数据字典中取出视图定义
2. 将视图查询转换为等价的基本表查询
3. 执行修正后的查询

### ✏️ 视图的更新

**限制：** 并非所有视图都可更新

**可更新的视图：**
- 从单个基本表导出
- 包含基本表的主码
- 不包含聚集函数、GROUP BY、DISTINCT

```sql
-- 插入
INSERT INTO v_warehouse1
VALUES ('m015', '护套绝缘电线', 'BVV-200', '供电局1#仓库', 50, 100, 5000);

-- 更新
UPDATE v_warehouse1
SET amount = 60
WHERE mat_num = 'm001';

-- 删除
DELETE FROM v_warehouse1
WHERE mat_num = 'm015';
```

**WITH CHECK OPTION作用：**
- 插入/更新时，检查是否满足WHERE条件
- 防止插入视图范围外的数据

---

## 🎓 重点总结

### 必须掌握的内容

✅ **SQL语言特点**：综合统一、非过程化、面向集合、易学易用  
✅ **DDL操作**：CREATE、ALTER、DROP的语法和应用  
✅ **完整性约束**：PRIMARY KEY、FOREIGN KEY、UNIQUE、NOT NULL、CHECK、DEFAULT  
✅ **SELECT语句结构和执行顺序**  
✅ **单表查询**：WHERE条件、ORDER BY排序、GROUP BY分组、HAVING筛选  
✅ **聚集函数**：COUNT、SUM、AVG、MAX、MIN  
✅ **连接查询**：内连接、外连接、自身连接  
✅ **嵌套查询**：IN、比较运算符、ANY/ALL、EXISTS  
✅ **数据更新**：INSERT、UPDATE、DELETE  
✅ **视图**：创建、查询、更新限制  

### 常见考点

⭐ 编写CREATE TABLE语句，包含各种完整性约束  
⭐ 使用ALTER TABLE添加/删除/修改列和约束  
⭐ 编写各种SELECT查询语句（单表、连接、嵌套）  
⭐ HAVING与WHERE的区别和使用场景  
⭐ 内连接、左外连接、右外连接的区别  
⭐ EXISTS实现全称量词查询  
⭐ 视图的定义和可更新性判断  

### 易错点

⚠️ HAVING必须与GROUP BY配合使用  
⚠️ WHERE子句不能使用聚集函数  
⚠️ 空值判断用IS NULL，不能用= NULL  
⚠️ LIKE通配符：%（多个字符）、_（单个字符）  
⚠️ DISTINCT去重在SELECT后，作用于所有目标列  
⚠️ ORDER BY只能对最终结果排序，子查询中不能用  
⚠️ ANY和ALL必须与比较运算符配合使用  
⚠️ 自身连接必须给表起不同别名  
⚠️ 不是所有视图都可更新  

### SQL语句编写技巧

1. **复杂查询分步骤思考**：
   - 确定涉及的表
   - 确定连接条件
   - 确定筛选条件
   - 确定输出列

2. **嵌套查询 vs 连接查询**：
   - 嵌套查询更易理解，连接查询效率更高
   - 优先考虑连接查询

3. **EXISTS的使用场景**：
   - 判断存在性
   - 实现全称量词（双重否定）
   - 实现差集（NOT EXISTS）

4. **聚集函数使用注意**：
   - 与GROUP BY配合
   - 结果筛选用HAVING
   - WHERE中不能用聚集函数

---

## 📌 复习建议

1. **理解SQL执行流程**：FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY
2. **熟练掌握各种查询**：大量练习各类型查询语句
3. **理解完整性约束**：知道何时使用哪种约束
4. **掌握嵌套查询技巧**：特别是EXISTS的使用
5. **练习实际场景**：结合实际业务场景编写SQL

---

**祝复习顺利！🎉**

