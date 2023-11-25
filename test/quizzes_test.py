import unittest

from app.controllers.quizzes_controller import QuizzesController

class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Run tests on non-production data
        self.ctrl = QuizzesController('quizzes_test.py')
        
    def test_expose_failure_01(self):
        """
        Implement this function and two more that
        execute the code and make it fail.
        """
        #Clearing data if any present
        self.ctrl.clear_data()
        #Adding a quiz using add quiz method
        #Passing None as text which causes TypeError in line 63 of quizzer_controller.py
        #TypeError is cause by adding None and a string value
        quizId = self.ctrl.add_quiz(None, "This is a test quiz", "2023-11-07", "2023-11-14")
        quizzes = self.ctrl.get_quizzes()
        self.assertEquals(len(quizzes), 1, "There is exactly one quiz.")
        questionID  = self.ctrl.get_quiz_by_id(quizId)
        self.assertIsNotNone(questionID,"The quiz can be retrieved")
        

    def test_expose_failure_02(self):
        title='\ud861\udd37'
        #Clearing data if any present
        self.ctrl.clear_data()
        #Adding a quiz using add quiz method
        #Then Adding a question to the quiz using the quiz_id
        #While adding the question I am passing title as a string which cannot be encoded by UTF-8
        #Due to this UnicodeEncodeError is thrown by line 11 of utils.py which is popped up to line 78 of quizzes_controller.py
        quizId = self.ctrl.add_quiz("Quiz1", "This is a test quiz", "2023-11-07", "2023-11-14")
        quizzes = self.ctrl.get_quizzes()
        self.assertEquals(len(quizzes), 1, "There is exactly one quiz.")
        questionID = self.ctrl.add_question(quizId,title,"Question1")
        self.assertIsNotNone(questionID,"The question is added successfully")

    def test_expose_failure_03(self):
        #Adding a quiz using add quiz method
        #Then Adding a question to the quiz using the quiz_id
        #Then adding an answer to the question with the questionID
        #Passing the title as a large integer value which python failes to convert into string and throws exceed the limit for integer error
        self.ctrl.clear_data()
        quizId = self.ctrl.add_quiz("q", "This is a test quiz", "2023-11-07", "2023-11-14")
        quizzes= self.ctrl.get_quizzes()
        self.assertEquals(len(quizzes),1,"Quiz is generated as expected")
        questionID = self.ctrl.add_question(quizId,"Q1","2+2=")
        self.assertIsNotNone(questionID,"The question is added successfully")
        answerId =  self.ctrl.add_answer(questionID,987687745739**456766, True)
        self.assertIsNotNone(answerId,"Answer Added")
        

if __name__ == '__main__':
    unittest.main()