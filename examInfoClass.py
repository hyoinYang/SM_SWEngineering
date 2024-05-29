import mysql.connector
from wordDB.db_connection import connect_to_database

class ExamDBModel:
    def __init__(self):
        self.mydb = connect_to_database()

    def get_exam_info(self):
        try:
            cursor = self.mydb.cursor(buffered=True)
            sql = "SELECT * FROM exam_info"
            cursor.execute(sql)
            results = cursor.fetchall()
            total = []
            if results is NotImplemented:
                return total
            else:
                for result in results:
                    v1= result[1]+'\n'+result[2]
                    v2 = result[3]+'\n'+'~'+result[4]
                    v3 = result[5]+'\n'+result[6]
                    total.append({
                        "일정:":v1,
                        "접수기간:":v2,
                        "성적발표:":v3
                    })
                return total
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
        self.model = ExamDBModel()
        self.view = ExamView()

    def get_and_display_exam_info(self):
        exam_info = self.model.get_exam_info()
        self.view.display_exam_info(exam_info)
def main():
    controller = ExamController()
    controller.get_and_display_exam_info()

if __name__ == "__main__":
    main()