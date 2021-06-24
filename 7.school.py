import sqlite3



with sqlite3.connect("school.db") as connection:
	cursor = connection.cursor()


	cursor.execute("""CREATE TABLE IF NOT EXISTS teachers(
						name TEXT NOT NULL,
						lastname TEXT NOT NULL,
						gender TEXT NOT NULL,
						subject TEXT NOT NULL)""")

	cursor.execute("""CREATE TABLE IF NOT EXISTS pupils(
						name TEXT NOT NULL,
						lastname TEXT NOT NULL,
						gender TEXT NOT NULL,
						class INT NOT NULL)""")

	cursor.execute("""INSERT INTO teachers
				(name, lastname, gender, subject)
				VALUES
				('Dato', 'MenabdiShvili', 'Male', 'PE')""")
	
	cursor.execute("""INSERT INTO teachers
				(name, lastname, gender, subject)
				VALUES
				('Tsisana', 'Qebadze', 'Female', 'Georgian')""")

	cursor.execute("""INSERT INTO teachers
				(name, lastname, gender, subject)
				VALUES
				('Vaxtang', 'Kasoievi', 'Male', 'Spanish')""")
	
	cursor.execute("""INSERT INTO teachers
				(name, lastname, gender, subject)
				VALUES
				('Ineza', 'Gafrindashvili', 'Female', 'History')""")
	
	cursor.execute("""INSERT INTO teachers
				(name, lastname, gender, subject)
				VALUES
				('Nino', 'Nikatsadze', 'Female', 'Math')""")

	cursor.execute("""INSERT INTO pupils
				(name, lastname, gender, class)
				VALUES
				('Griorgi', 'Namoradze', 'Male', '8')""")
	
	cursor.execute("""INSERT INTO pupils
				(name, lastname, gender, class)
				VALUES
				('Vano', 'Aniashvili', 'Male', '7')""")
	
	cursor.execute("""INSERT INTO pupils
				(name, lastname, gender, class)
				VALUES
				('Nika', 'Gurgenidze', 'Male', '8')""")
	
	cursor.execute("""INSERT INTO pupils
				(name, lastname, gender, class)
				VALUES
				('Lamzira', 'Giorgadze', 'Female', '9')""")









