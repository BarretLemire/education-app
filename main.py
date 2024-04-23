from sqlalchemy import create_engine, text


engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)


create_students_table = """
    CREATE TABLE Students (
        StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
        First_Name TEXT,
        Last_Name TEXT,
        Email TEXT,
        EnrollmentYear INTEGER
);
"""

insert_student = """
    INSERT INTO Students 
    (First_name, Last_name, Email, EnrollmentYear)
    VALUES ('Barret', 'Lemire', 'barretlemire@gmail.com', 2024);
"""







with engine.connect() as conn:
    conn.execute(text(create_students_table))
    conn.execute(text(insert_student))
    conn.commit()
    result = conn.execute(text("SELECT * FROM students"))
    print(result.fetchall())



