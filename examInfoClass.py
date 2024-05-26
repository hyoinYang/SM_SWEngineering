import mysql.connector
from wordDB.db_connection import connect_to_database

class ExamModel:
    def __init__(self):
        self.mydb = connect_to_database()

    def get_exam_info(self):
        try:
            cursor = self.mydb.cursor(buffered=True)
            sql = "SELECT * FROM exam_info"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result
        except mysql.connector.Error as err:
            print("MySQL Error:", err)
        finally:
            cursor.close()
class ExamView:
    @staticmethod
    def display_exam_info(exam_info):
        if exam_info:
            print("Exam Information:", exam_info)
        else:
            print("No exam information found.")

class ExamController:
    def __init__(self):
        self.model = ExamModel()
        self.view = ExamView()

    def get_and_display_exam_info(self):
        exam_info = self.model.get_exam_info()
        self.view.display_exam_info(exam_info)
def main():
    controller = ExamController()
    controller.get_and_display_exam_info()

if __name__ == "__main__":
    main()
