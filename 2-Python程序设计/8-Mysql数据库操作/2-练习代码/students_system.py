import settings
import pymysql

conn = pymysql.connect(**settings.MYSQL_CONFIG)
cursor = conn.cursor()


def create():
    sql = """
            create table if not exists cz_students(
                id          int         not null primary key auto_increment comment "id",
                name        varchar(32) not null comment "姓名",
                age         tinyint     not null default 17 comment "年龄",
                gender      tinyint     not null default 1 comment "性别：1男生，2女生",
                create_time datetime             default now() comment "创建时间",
                update_time datetime             default now() comment "更新时间"
            );
    """
    cursor.execute(sql)


def insert():
    name = input("请输入姓名：")
    age = input("请输入年龄：")
    gender = input("请输入性别：")
    if not name or not age or not gender:
        print("任何字段都不可为空！！添加失败!")
        return

    sql = """
    insert into cz_s(`name`, `age`, `gender`)
    values ("%s", %s, %s);
    """ % (name, age, gender)
    cursor.execute(sql)


def update():
    id = input("请输入要修改的学生的id：")
    age = input("请输入修改之后的学生年龄：")
    sql_query = "select * from cz_s where id=%s" % (id)
    cursor.execute(sql_query)
    if not cursor.fetchall():
        print("删除用户不存在")
        return

    sql_update = "update cz_s set age = %s where id = %s" % (age, id)
    cursor.execute(sql_update)


def delete():
    id = input("请输入要删除的学生的id：")
    sql_query = "select * from cz_s where id=%s" % (id)
    cursor.execute(sql_query)
    if not cursor.fetchall():
        print("删除用户不存在")
        return
    sql_del = "delete from cz_s where id = %s" % (id)
    cursor.execute(sql_del)


def query():
    id = input("请输入要查询的学生id：")
    sql_query = "select * from cz_s where id=%s" % (id)
    cursor.execute(sql_query)
    res = cursor.fetchall()
    if not res:
        print("删除用户不存在")
        return
    print(res[0])


def query_all():
    sql_query = "select * from cz_s"
    cursor.execute(sql_query)
    res = cursor.fetchall()
    for r in res:
        print(r)



def main():
    input("---------- 欢迎来到学生管理系统，按Enter键继续 ------------")

    create()

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
            insert()
        elif num == "2":
            delete()
        elif num == "3":
            update()
        elif num == "4":
            query()
        elif num == "5":
            query_all()
        elif num == "6":
            break
        else:
            print("输入错误，请重新输入！！")


if __name__ == '__main__':
    main()
