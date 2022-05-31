import pymysql
import settings

"""
学生管理系统v2
1、添加学生
2、删除学生
3、修改
4、查询(有条件的查询)
5、查询所有
6、退出系统
"""
TABLE_NAME = settings.TABLE_NAME
conn = pymysql.connect(**settings.MYSQL_CONFIG)
cursor = conn.cursor()


def create_table():
    sql = f"""
    create table if not exists {TABLE_NAME}
        (
            id          int         not null primary key auto_increment comment "id",
            name        varchar(32) not null comment "姓名",
            age         tinyint     not null default 17 comment "年龄",
            gender      tinyint     not null default 1 comment "性别：1男生，2女生",
            create_time datetime             default now() comment "创建时间",
            update_time datetime             default now() comment "更新时间"
        );
    """
    cursor.execute(sql)


def insert_s():
    name = input("请输入学生姓名：")
    age = input("请输入学生年龄：")
    gender = input("请输入学生性别：")
    if not name:
        print("有空数据，学生添加失败！")
        return

    # sql = f"""
    # insert into cz_s2(`name`, `age`, `gender`)
    # values ("{name}", {age}, {gender});
    # """

    # sql = """
    #     insert into cz_s2(`name`, `age`, `gender`)
    #     values ("{}", {}, {});
    #     """.format(name, age, gender)

    sql = """
            insert into %s (`name`, `age`, `gender`)
            values (%s, %s, %s);
            """

    cursor.execute(sql, (TABLE_NAME, name, age, gender))


def delete_s():
    id = input("请输入要删除学生的id：")
    if not query_s(id):
        print("没有此人，更新失败！")
        return

    sql = f"""
    delete from {TABLE_NAME} where id = %s;
    """
    cursor.execute(sql, [id])


def update_s():
    id = input("请输入要更新学生的id：")
    if not query_s(id):
        print("没有此人，更新失败！")
        return

    age = input("请输入更新后的年龄：")
    if not age:
        age = input("输入为空，请重新输入年龄：")

    sql = """
    update %s set age = %s where id = %s
    """ % (TABLE_NAME, age, id)
    cursor.execute(sql)


def query_s(id):
    sql = """
    select * from %s where id = %s
    """ % (TABLE_NAME, id)
    cursor.execute(sql)
    res = cursor.fetchall()
    if not res:
        print("未查询到数据")
        return
    return res[0]


def query_all():
    sql = """
    select * from %s;
    """ % TABLE_NAME
    cursor.execute(sql)
    res = cursor.fetchall()
    if not res:
        print("cz_s2表的数据为空")
        return
    for r in res:
        print(r)


def select(id):
    sql = """
    select * from cpvs1 where id = %s
    """ % id
    cursor.execute(sql)
    res = cursor.fetchall()
    print(res[0])


def main():
    input("---------- 欢迎来到学生管理系统，按Enter键继续 ------------")
    create_table()
    while True:
        print('--------------')
        print("1、添加学生")
        print("2、删除学生")
        print("3、修改")
        print("4、查询")
        print("5、查询所有")
        print("6、退出系统")
        print('--------------')

        num = input("请输入功能序号：")
        if num == "1":
            insert_s()
        elif num == "2":
            delete_s()
        elif num == "3":
            update_s()
        elif num == "4":
            id = input("请输入要查询学生的id:")
            query_s(id)
        elif num == "5":
            query_all()
        elif num == "6":
            break
        else:
            print("输入错误，请重新输入！！")


if __name__ == '__main__':
    # main()
    # create_table()
    insert_s()
    # delete_s()
    # update_s()
    # query_s()
    # query_all()
    # id = 1
    # id = "1;drop table cpvs1;"
    # select(id)
