# 【考场精简】第3章 SQL语言

## 一、SQL概述

**SQL的核心特点：** 综合统一（DDL+DML+DCL）、高度非过程化（只需说做什么）、面向集合操作、语言简洁易用。

**九个核心动词：** SELECT查询、CREATE/DROP/ALTER定义、INSERT/UPDATE/DELETE操纵、GRANT/REVOKE控制。

---

## 二、数据定义语句

### 2.1 数据库操作

创建数据库：CREATE DATABASE 数据库名;
删除数据库：DROP DATABASE 数据库名;

### 2.2 基本表定义

**创建表语法：** CREATE TABLE 表名 (列名 数据类型 [列级约束], ..., [表级约束]);

**六大完整性约束：**
- PRIMARY KEY主码约束
- UNIQUE唯一性约束
- NOT NULL非空约束
- FOREIGN KEY外键约束（REFERENCES 引用表(引用列)）
- CHECK检查约束（CHECK(条件表达式)）
- DEFAULT默认值约束

**例题1：** 创建抢修工程表，prj_num为主码
```sql
CREATE TABLE Salvaging (
    prj_num char(8) PRIMARY KEY,
    prj_name varchar(50),
    start_date datetime,
    end_date datetime,
    prj_status bit
);
```

**例题2：** 创建出库表，复合主码+外键
```sql
CREATE TABLE Out_stock (
    prj_num char(8),
    mat_num char(4),
    amount int,
    get_date datetime default NOW(),
    department char(20),
    PRIMARY KEY(prj_num, mat_num),
    FOREIGN KEY (prj_num) REFERENCES Salvaging(prj_num),
    FOREIGN KEY (mat_num) REFERENCES Stock(mat_num)
);
```

### 2.3 修改表结构

**添加列：** ALTER TABLE 表名 ADD 列名 数据类型 [约束];
**删除列：** ALTER TABLE 表名 DROP COLUMN 列名;
**修改列：** ALTER TABLE 表名 MODIFY COLUMN 列名 数据类型 [约束];

**注意：** 新增列初始为空值。若表中已有数据，新增列不能设NOT NULL（除非有DEFAULT）。

**例题3：** 向表中添加负责人列
```sql
ALTER TABLE Salvaging ADD prj_director VARCHAR(10);
```

### 2.4 约束的添加与删除

**添加约束：** ALTER TABLE 表名 ADD CONSTRAINT 约束名 约束表达式;
**删除约束：** ALTER TABLE 表名 DROP CONSTRAINT 约束名;

**例题4：** 后期添加外键约束
```sql
ALTER TABLE out_stock ADD CONSTRAINT FK_Salvaging_Out_stock 
    FOREIGN KEY (prj_num) REFERENCES salvaging(prj_num);
```

### 2.5 删除表

**语法：** DROP TABLE 表名;
**危险：** 删除表会同时删除数据、索引、视图，且被外键引用的表不能删除。

---

## 三、单表查询

### 3.1 基本查询结构

**SELECT语句格式：**
SELECT [DISTINCT] 目标列 FROM 表名 [WHERE 条件] [GROUP BY 列名 [HAVING 条件]] [ORDER BY 列名 [ASC|DESC]];

**执行顺序：** FROM→WHERE→GROUP BY→HAVING→SELECT→ORDER BY

### 3.2 选择列

**查询指定列：** SELECT mat_num, mat_name, speci FROM Stock;
**查询全部列：** SELECT * FROM Stock;
**计算列：** SELECT prj_name, datediff(end_date, start_date) 抢修天数 FROM Salvaging;
**列别名：** 列名 [AS] 别名 或 别名=列名

**常用时间函数：** NOW()当前时间、YEAR(d)年份、MONTH(d)月份、DATEDIFF(d1,d2)天数差、ADDDATE(d,n)加天数、SUBDATE(d,n)减天数

### 3.3 选择元组（WHERE条件）

**1) 比较运算：** =、>、<、>=、<=、!=或<>、NOT

**例题5：** 查询单价小于80的物资
```sql
SELECT mat_name, amount, unit FROM stock WHERE unit < 80;
```

**2) 范围查询：** BETWEEN...AND...（闭区间）

**例题6：** 查询单价在50到100之间
```sql
SELECT mat_name, amount, unit FROM stock WHERE unit BETWEEN 50 AND 100;
-- 等价于：WHERE unit >= 50 AND unit <= 100
```

**3) 集合查询：** IN、NOT IN

**例题7：** 查询指定仓库的物资
```sql
SELECT mat_name, speci, amount FROM stock 
WHERE warehouse IN('供电局1#仓库', '供电局2#仓库');
```

**4) 模糊查询：** LIKE、NOT LIKE
- **%代表任意长度字符串**（包括0个）
- **_代表单个字符**
- **ESCAPE定义换码字符**（如ESCAPE '/'使/_失去通配符含义）

**例题8：** 模糊查询示例
```sql
-- 查询所有绝缘电线
SELECT mat_num, mat_name, speci FROM stock WHERE mat_name LIKE '%绝缘电线';
-- 第三四个字为"绝缘"
SELECT mat_num, mat_name, speci FROM stock WHERE mat_name LIKE '__绝缘%';
-- 包含"户外_真空"（_作为普通字符）
SELECT * FROM Stock WHERE mat_name LIKE '%户外/_真空%' ESCAPE '/';
```

**5) 空值查询：** IS NULL、IS NOT NULL（**注意不能用=NULL**）

**例题9：** 查询无单价的物资
```sql
SELECT mat_num, mat_name FROM stock WHERE unit IS NULL;
```

**6) 多条件：** AND优先级高于OR，可用括号改变优先级

### 3.4 结果排序与限制（⭐必考重点）

**ORDER BY排序：**
- **ASC** - 升序（默认，可省略）
- **DESC** - 降序（必须写）
- **多列排序：** 先按第一列排，相同再按第二列排
- **空值规则：** 空值在排序中是最小的

**LIMIT限制结果数量（老师重点强调）：**
- **LIMIT n** - 显示前n条记录（从第1条开始）
- **LIMIT m, n** - 从第m+1条开始，显示n条记录（**m是偏移量，从0开始计数**）
- **LIMIT offset, count** 等价于 **LIMIT count OFFSET offset**

**LIMIT核心理解：**
- **LIMIT 2, 3** 表示：跳过前2条（第1、2条），从第3条开始取3条（取第3、4、5条）
- **LIMIT 0, 5** 等价于 **LIMIT 5**（从第1条开始取5条）
- **LIMIT 5, 10** 表示：跳过前5条，从第6条开始取10条

**例题10：** ORDER BY基础用法
```sql
-- 按库存量降序排列
SELECT * FROM Stock ORDER BY amount DESC;

-- 按仓库降序，同一仓库内按库存量升序
SELECT * FROM stock ORDER BY warehouse DESC, amount ASC;
-- 等价于（ASC可省略）
SELECT * FROM stock ORDER BY warehouse DESC, amount;
```

**例题11：** LIMIT基础用法
```sql
-- 查询库存量最大的两条记录
SELECT * FROM Stock ORDER BY amount DESC LIMIT 2;

-- 查询库存量最大的第3到第5条记录（跳过前2条，取3条）
SELECT * FROM Stock ORDER BY amount DESC LIMIT 2, 3;
```

**例题12：** LIMIT分页查询（实战常考）
```sql
-- 第1页：显示前10条（第1-10条）
SELECT * FROM Stock ORDER BY mat_num LIMIT 0, 10;  -- 或 LIMIT 10

-- 第2页：显示第11-20条
SELECT * FROM Stock ORDER BY mat_num LIMIT 10, 10;

-- 第3页：显示第21-30条
SELECT * FROM Stock ORDER BY mat_num LIMIT 20, 10;

-- 通用公式：第page页，每页size条
-- LIMIT (page-1)*size, size
```

**例题13：** ORDER BY + LIMIT组合（必考题型）
```sql
-- 查询单价最低的3种物资
SELECT mat_name, unit FROM Stock ORDER BY unit ASC LIMIT 3;

-- 查询库存量第4-6名的物资（跳过前3名）
SELECT mat_name, amount FROM Stock ORDER BY amount DESC LIMIT 3, 3;

-- 查询每个仓库库存量最大的物资（需要用开窗函数或子查询）
SELECT * FROM (
    SELECT *, ROW_NUMBER() OVER(PARTITION BY warehouse ORDER BY amount DESC) as rn
    FROM Stock
) t WHERE rn = 1;
```

### 3.5 聚集函数（重点）

**五大聚集函数：**
- **COUNT(*)** 统计元组个数
- **COUNT(列名)** 统计列中非空值个数
- **SUM(列名)** 求和（数值型）
- **AVG(列名)** 平均值（数值型）
- **MAX(列名)/MIN(列名)** 最大/最小值

**DISTINCT关键字：** 计算时取消重复值，如COUNT(DISTINCT prj_num)

**注意事项：** 
- 除COUNT外其他函数忽略NULL值
- **WHERE子句中不能使用聚集函数**

**例题11：** 聚集函数应用
```sql
-- 统计领取物资的工程数
SELECT COUNT(DISTINCT prj_num) FROM out_stock;
-- 查询m001物资的最高、最低、平均领取量
SELECT MAX(amount), MIN(amount), AVG(amount) FROM out_stock WHERE mat_num = 'm001';
```

### 3.6 分组查询（GROUP BY + HAVING）

**GROUP BY作用：** 细化聚集函数作用对象，将结果按某列分组，每组一个函数值。

**HAVING作用：** 筛选分组，作用于组而非元组。

**WHERE vs HAVING：**
- WHERE作用于基本表，选择满足条件的元组
- HAVING作用于分组，选择满足条件的组
- **先WHERE后GROUP BY再HAVING**

**例题12：** 查询使用2种以上物资的工程
```sql
SELECT prj_num, COUNT(*) 物资种类 FROM out_stock 
GROUP BY prj_num HAVING COUNT(*) >= 2;
```

**例题13：** 多列分组
```sql
SELECT department, mat_num, count(distinct prj_num) 项目个数, sum(amount) 领取总量
FROM Out_stock GROUP BY department, mat_num;
```

**WITH ROLLUP：** 按分组顺序先对第一个字段分组并统计，最后给出总计。

### 3.7 开窗函数（数据分析）

**特点：** 每条记录都执行函数，有几条记录执行完还是几条（不像聚合函数合并为一条）。

**常用函数：** ROW_NUMBER()行号、RANK()排名（有间隙）、DENSE_RANK()密集排名、LAG()前一行、LEAD()后一行

**例题14：** 查询每种物资使用量前2的出库情况
```sql
select * from (
    select *, row_number() over(partition by mat_num order by amount desc) as row_num
    from out_stock
) as t where row_num <= 2;
```

### 3.8 正则表达式查询

**语法：** 列名 REGEXP '匹配方式'

**常用模式：** ^开头、$结尾、.任意字符、[字符集]、|或、*零或多次、+一或多次、{N}出现N次、{M,N}出现M到N次

**例题15：** 正则表达式示例
```sql
-- 包含"西丽"或"明珠"
SELECT * FROM Salvaging WHERE prj_name REGEXP '西丽|明珠';
-- 包含"2"至少1次最多2次
SELECT * FROM Salvaging WHERE prj_name REGEXP '2{1,2}';
```

---

## 四、连接查询

### 4.1 等值连接与自然连接

**连接条件格式：** [表名1.]列名1 比较运算符 [表名2.]列名2

**执行过程：** 表1每个元组与表2全部元组逐一匹配，满足连接条件的拼接成结果元组。

**例题16：** 查询每个工程及其出库情况
```sql
SELECT Salvaging.*, Out_stock.* FROM Salvaging, Out_stock 
WHERE Salvaging.prj_num = Out_stock.prj_num;
```

**自然连接：** 去掉重复列，同名属性必须加表名前缀。

### 4.2 内连接（显式连接）

**语法：** 表1 INNER JOIN 表2 ON 连接条件

**优势：** 显式连接在每次连接时通过ON过滤，效率高于隐式连接（先笛卡尔积再WHERE过滤）。

**例题17：** 内连接写法
```sql
SELECT salvaging.prj_num, prj_name, mat_num, amount 
FROM salvaging INNER JOIN out_stock ON salvaging.prj_num = out_stock.prj_num;
```

### 4.3 外连接

**三种外连接：**
- **LEFT OUTER JOIN** 保留左表所有元组，右表不匹配的填NULL
- **RIGHT OUTER JOIN** 保留右表所有元组
- **FULL OUTER JOIN** 保留两表所有元组

**例题18：** 左外连接（显示所有工程，包括未领料的）
```sql
SELECT Salvaging.prj_num, prj_name, mat_num, amount 
FROM Salvaging LEFT OUTER JOIN Out_stock ON Salvaging.prj_num = Out_stock.prj_num;
```

### 4.4 复合条件连接

WHERE子句中包含连接条件+其他限定条件。

**例题19：** 查询项目20100015使用的物资
```sql
SELECT Out_stock.mat_num, mat_name, speci, Out_stock.amount
FROM Stock JOIN Out_stock ON Stock.mat_num = Out_stock.mat_num
WHERE prj_num = '20100015';
```

### 4.5 自身连接

**关键：** 必须给表起别名，所有属性必须加前缀。

**例题20：** 查询同时使用m001和m002的工程
```sql
SELECT A.prj_num FROM Out_stock A, Out_stock B
WHERE A.prj_num = B.prj_num AND A.mat_num = 'm001' AND B.mat_num = 'm002';
```

---

## 五、嵌套查询

### 5.1 基本概念

**定义：** WHERE或HAVING中出现另一个SELECT语句。

**求解方法：**
- **不相关子查询：** 子查询条件不依赖父查询，由里向外逐层处理
- **相关子查询：** 子查询条件依赖父查询，取外层元组→传给内层→执行内层→判断WHERE→重复

**限制：** 子查询不能使用ORDER BY（只能对最终结果排序）。

### 5.2 带IN的嵌套查询

子查询结果是一个集合。

**例题21：** 查询与BVV-120护套绝缘电线同仓库的物资
```sql
SELECT mat_name, speci, amount FROM Stock
WHERE warehouse IN (
    SELECT warehouse FROM Stock 
    WHERE speci = 'BVV-120' AND mat_name = '护套绝缘电线'
);
```

**例题22：** 多层嵌套查询观澜站光缆抢修使用的物资
```sql
SELECT mat_num, mat_name FROM Stock
WHERE mat_num IN (
    SELECT mat_num FROM Out_stock WHERE prj_num IN (
        SELECT prj_num FROM Salvaging WHERE prj_name = '观澜站光缆抢修'
    )
);
```

### 5.3 带比较运算符的子查询

**要求：** 子查询返回单值。常用于相关子查询。

**例题23：** 查询库存量超过该仓库平均库存量的物资（相关子查询）
```sql
SELECT mat_num, mat_name, speci, amount FROM Stock s1
WHERE amount > (
    SELECT avg(amount) FROM Stock s2 WHERE s2.warehouse = s1.warehouse
);
```

### 5.4 带ANY或ALL的子查询

**必须同时使用比较运算符：**
- **>ANY** 大于某个值（等价于>MIN）
- **<ANY** 小于某个值（等价于<MAX）
- **>ALL** 大于所有值（等价于>MAX）
- **<ALL** 小于所有值（等价于<MIN）
- **=ANY** 等价于IN
- **!=ALL** 等价于NOT IN

**例题24：** 查询比供电局1#仓库某物资库存少的其他仓库物资
```sql
SELECT mat_name, speci, amount FROM Stock
WHERE warehouse <> '供电局1#仓库' AND amount < ANY (
    SELECT amount FROM Stock WHERE warehouse = '供电局1#仓库'
);
-- 等价于用MAX
WHERE warehouse <> '供电局1#仓库' AND amount < (
    SELECT MAX(amount) FROM Stock WHERE warehouse = '供电局1#仓库'
);
```

**注意：** 使用聚集函数比ANY/ALL效率更高。

### 5.5 带EXISTS的嵌套查询（难点）

**EXISTS存在量词：** 子查询结果非空返回TRUE，为空返回FALSE，不返回数据。
**NOT EXISTS：** 子查询结果为空返回TRUE。

**目标列用*：** 因为EXISTS只关心有无结果，给出列名无意义。

**例题25：** 查询使用了m001物资的工程
```sql
SELECT prj_name FROM Salvaging
WHERE EXISTS (
    SELECT * FROM Out_stock 
    WHERE prj_num = Salvaging.prj_num AND mat_num = 'm001'
);
```

**例题26：** 查询没使用m001物资的工程
```sql
SELECT prj_num, prj_name FROM Salvaging
WHERE NOT EXISTS (
    SELECT * FROM Out_stock 
    WHERE prj_num = Salvaging.prj_num AND mat_num = 'm001'
);
```

### 5.6 用EXISTS实现全称量词

**转换公式：** ∀xP ≡ ¬∃x(¬P) 即"对所有x满足P" = "不存在x不满足P"

**例题27：** 查询被所有工程都使用的物资（双重NOT EXISTS）
```sql
SELECT mat_num, mat_name, speci FROM Stock
WHERE NOT EXISTS (
    SELECT * FROM Salvaging WHERE NOT EXISTS (
        SELECT * FROM Out_stock 
        WHERE mat_num = Stock.mat_num AND prj_num = Salvaging.prj_num
    )
);
```
**理解：** 不存在某个工程，不存在使用该物资的出库记录。

### 5.7 用EXISTS实现逻辑蕴涵

**转换公式：** p→q ≡ ¬p∨q ≡ ¬(p∧¬q)

**例题28：** 查询包含工程20100016所用物资的工程
```sql
SELECT DISTINCT prj_num FROM Out_stock sx
WHERE NOT EXISTS (
    SELECT * FROM Out_stock sy WHERE sy.prj_num = '20100016' AND NOT EXISTS (
        SELECT * FROM Out_stock sz 
        WHERE sz.mat_num = sy.mat_num AND sz.prj_num = sx.prj_num
    )
);
```
**理解：** 不存在这样的物资：20100016用了但x没用。

---

## 六、集合查询

### 6.1 集合操作

**三种操作：** UNION并、INTERSECT交、EXCEPT差

**相容要求：** 属性个数和数据类型必须一致，属性名无关（用第一个结果的属性名）。

**自动去重：** 默认去除重复元组，用ALL保留重复。

**例题29：** 并操作
```sql
SELECT * FROM Stock WHERE warehouse = '供电局1#仓库'
UNION
SELECT * FROM Stock WHERE unit <= 50;
-- UNION ALL保留重复
```

**例题30：** 查询使用m001或m002的工程
```sql
SELECT prj_num FROM Out_stock WHERE mat_num = 'm001'
UNION
SELECT prj_num FROM Out_stock WHERE mat_num = 'm002';
```

### 6.2 通过中间表查询

子查询作为FROM子句中的临时表。

**例题31：** 查询使用物资数量前3的工程
```sql
select prj_num from (
    select prj_num, sum(amount) as sum_amount from out_stock group by prj_num
) as S order by sum_amount DESC limit 3;
```

---

## 七、数据更新

### 7.1 插入数据

**1) 插入单个元组：** INSERT INTO 表名[(列名...)] VALUES (常量...);
- 未指定列名：插入完整元组，顺序与表定义一致
- 指定部分列：其余列取空值（非空列必须指定）

**例题32：** 插入新物资
```sql
INSERT INTO Stock(mat_num, mat_name, speci, warehouse, unit, amount)
VALUES ('m020', '架空绝缘导线', '10KV-100', '供电局1#仓库', 12.8, 50);
```

**2) 插入多行元组：** VALUES后用逗号分隔多组值
```sql
INSERT INTO Out_stock VALUES 
    ('20110006', 'm001', 2, '2011-3-9', '工程4部'),
    ('20110006', 'm002', 3, '2011-3-9', '工程4部');
```

**3) 插入子查询结果：** INSERT INTO 表名[(列名...)] 子查询;

**例题33：** 统计每个工程的物资总费用并存入新表
```sql
-- 先建表
CREATE TABLE Prj_cost (prj_num char(8) PRIMARY KEY, cost decimal(18, 2));
-- 插入统计结果
INSERT INTO Prj_cost
SELECT prj_num, SUM(out_stock.amount * unit) 
FROM Out_stock, Stock WHERE Out_stock.mat_num = Stock.mat_num GROUP BY prj_num;
```

### 7.2 修改数据

**语法：** UPDATE 表名 SET 列名=表达式[, 列名=表达式...] [WHERE 条件];

**省略WHERE：** 修改表中所有元组。

**例题34：** 修改单个元组
```sql
UPDATE Stock SET unit = 44.5 WHERE mat_num = 'm020';
```

**例题35：** 修改多个元组
```sql
UPDATE Stock SET unit = unit + 1;  -- 所有物资单价加1
```

**例题36：** 带子查询的修改
```sql
UPDATE Out_stock SET amount = 0
WHERE mat_num IN (SELECT mat_num FROM Stock WHERE warehouse = '供电局1#仓库');
```

### 7.3 删除数据

**语法：** DELETE FROM 表名 [WHERE 条件];

**省略WHERE：** 删除表中所有元组（但不删表定义）。

**例题37：** 删除单个元组
```sql
DELETE FROM Out_stock WHERE prj_num = '20110001' AND mat_num = 'm001';
```

**例题38：** 删除所有元组
```sql
DELETE FROM Out_stock;
```

**例题39：** 带子查询的删除
```sql
DELETE FROM Out_stock
WHERE prj_num IN (
    SELECT prj_num FROM Salvaging WHERE prj_name = '观澜站光缆抢修'
);
```

---

## 八、视图

### 8.1 视图定义

**语法：** CREATE VIEW 视图名[(列名...)] AS 子查询 [WITH CHECK OPTION];

**视图特点：** 虚表、只存定义不存数据、基表数据变化视图数据也变。

**必须明确指定列名的情况：**
1. 目标列是集函数或表达式
2. 多表连接有同名列
3. 需要为列启用新名字

**例题40：** 行列子集视图
```sql
CREATE VIEW s1_stock AS
SELECT mat_num, mat_name, speci, amount, unit FROM Stock 
WHERE warehouse = '供电局1#仓库';
```

**例题41：** 带WITH CHECK OPTION
```sql
CREATE VIEW s2_stock AS
SELECT mat_num, mat_name, speci, amount, unit FROM Stock 
WHERE warehouse = '供电局1#仓库' WITH CHECK OPTION;
-- 确保后续INSERT/UPDATE仍满足warehouse条件
```

**例题42：** 多表连接视图
```sql
CREATE VIEW s1_outstock AS
SELECT prj_name, mat_name, speci, out_stock.amount
FROM Stock INNER JOIN Out_stock ON Stock.mat_num = Out_stock.mat_num
INNER JOIN Salvaging ON Salvaging.prj_num = Out_stock.prj_num;
```

**例题43：** 带表达式的视图（必须指定列名）
```sql
CREATE VIEW s1_salvaging(prj_name, start_date, end_date, days) AS
SELECT prj_name, start_date, end_date, datediff(day, start_date, end_date)
FROM Salvaging;
```

**例题44：** 分组视图
```sql
CREATE VIEW s4_stock(warehouse, counts) AS
SELECT warehouse, COUNT(mat_num) FROM Stock GROUP BY warehouse;
```

**例题45：** 基于视图的视图
```sql
CREATE VIEW s3_stock AS
SELECT mat_num, mat_name, speci, amount FROM s1_stock WHERE amount >= 50;
```

### 8.2 删除视图

**语法：** DROP VIEW 视图名;

**注意：** 
1. 只删视图定义，不删基表数据
2. 该视图导出的其他视图定义仍在但不能用，需显式删除
3. 删除基表时，其导出的视图都不能用

### 8.3 查询视图

**视图消解法：** DBMS将视图查询转换为对基本表的查询。

**例题46：** 查询视图
```sql
SELECT mat_name, speci, unit FROM s1_stock WHERE unit < 20;
-- 转换为：
SELECT mat_name, speci, unit FROM Stock 
WHERE warehouse = '供电局1#仓库' AND unit < 20;
```

**局限性：** 某些情况视图消解法无法正确转换（如分组视图的WHERE条件应转为HAVING）。

### 8.4 更新视图

**受限更新：** 通过视图消解法将更新转换为对基表的更新。

**例题47：** 更新视图
```sql
UPDATE s1_stock SET amount = 100 WHERE mat_num = 'm001';
-- 转换为：
UPDATE Stock SET amount = 100 
WHERE warehouse = '供电局1#仓库' AND mat_num = 'm001';
```

**例题48：** 插入视图
```sql
INSERT INTO s1_stock VALUES('m022', '护套绝缘电线', 'BVV-150', 100, 14.5);
-- 转换为对Stock表的插入，warehouse列取NULL（若有WITH CHECK OPTION会报错）
```

**不可更新的视图：**
1. 字段来自聚集函数
2. 含GROUP BY子句
3. 含DISTINCT短语
4. 基于不可更新视图的视图

### 8.5 视图的作用

1. **简化操作：** 隐藏复杂的连接查询
2. **多角度看数据：** 不同用户定义不同视图
3. **安全保护：** 限制用户只能看到授权数据
4. **逻辑独立性：** 基表结构改变时，通过重建视图保持应用程序不变

**例题49：** 数据库重构的逻辑独立性
```sql
-- Stock表垂直分成s1和s2后，建视图保持外模式不变
CREATE VIEW Stock(mat_num, mat_name, speci, warehouse, amount, unit, total) AS
SELECT s1.mat_num, s1.mat_name, s1.speci, s1.warehouse, s2.amount, s2.unit, s2.total
FROM s1, s2 WHERE s1.mat_num = s2.mat_num;
-- 原有查询程序无需修改
```

---

## 九、考前快速记忆

**1. 约束类型：** 主码PRIMARY KEY、唯一UNIQUE、非空NOT NULL、外键FOREIGN KEY、检查CHECK、默认DEFAULT

**2. 聚集函数：** COUNT计数、SUM求和、AVG平均、MAX最大、MIN最小（除COUNT外都忽略NULL）

**3. 模糊查询：** %任意长度、_单个字符、ESCAPE换码字符

**4. 连接类型：** 内连接INNER JOIN、左外LEFT OUTER JOIN、右外RIGHT OUTER JOIN、自身连接需别名

**5. 子查询：** IN集合、比较运算符单值、ANY/ALL范围、EXISTS存在性

**6. EXISTS转换：** 全称量词∀xP≡¬∃x(¬P)、逻辑蕴涵p→q≡¬(p∧¬q)

**7. 执行顺序：** FROM→WHERE→GROUP BY→HAVING→SELECT→ORDER BY

**8. 视图限制：** 不能含ORDER BY、不能用DISTINCT、聚集函数/GROUP BY的视图不可更新

**9. 集合操作：** UNION并（自动去重）、UNION ALL（保留重复）

**10. 空值判断：** 只能用IS NULL或IS NOT NULL，不能用=NULL

---

**考场提示：** 
- WHERE用于元组筛选，HAVING用于分组筛选
- 显式连接（INNER JOIN ON）效率高于隐式连接
- 双重NOT EXISTS实现"所有"的语义
- 子查询不能在WHERE中使用聚集函数，要用HAVING
- 空值在排序中是最小的
- 视图WITH CHECK OPTION确保更新时满足视图定义条件

